import cv2
import numpy as np


class boundary(object):
    """
    boundary class:
    1. Get the blue boundary.
    2. Get the center from the boundary.
    3. Update the frame. [ boundary and center location]
    """
    def __init__(self, lower_bounds = [110,50,50] , upper_bounds = [130, 255, 255]):
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.frame = None
        self._boundaries = np.zeros((4,2))
        self._center = []

    # update boundaried location (hidden method)
    def _update_boundary(self):
        if self.frame is not None:
            # convert rgb to hsv
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower_blue = np.array(self.lower_bounds)
            upper_blue = np.array(self.upper_bounds)

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue) 

            # frame matrix shape
            shape_frame = np.shape(mask)
            # performing erosion
            kernel = np.ones((5,5),np.uint8)
            mask = cv2.erode(mask, kernel, iterations = 1)
            # breaking and getting the boundaries
            test_mask = []
            test_mask.append(mask[0:int(shape_frame[0]/2),0:int(shape_frame[1]/2)])
            test_mask.append(mask[int(shape_frame[0]/2):int(shape_frame[0]),0:int(shape_frame[1]/2)])
            test_mask.append(mask[0:int(shape_frame[0]/2),int(shape_frame[1]/2):int(shape_frame[1])])
            test_mask.append(mask[int(shape_frame[0]/2):int(shape_frame[0]),int(shape_frame[1]/2):int(shape_frame[1])])
            self.test_mask = test_mask
            for i, ind_mask in enumerate(test_mask):
                box = np.where(200 < ind_mask)
                if len(box[1]) > 50:
                    center_quad_box = np.mean(box, axis = 1).reshape(1,2)
                    self._boundaries[i] = center_quad_box
                else:
                    self._boundaries = np.zeros((4,2))
                    print('$' * 50 + '\n' + 'quad' + str(i) +' center not found')
            # offset boundaries.
            self._boundaries[1][0] += int(shape_frame[0]/2)
            self._boundaries[2][1] += int(shape_frame[1]/2)
            self._boundaries[3][0] += int(shape_frame[0]/2)
            self._boundaries[3][1] += int(shape_frame[1]/2)
            

    # update the center location (hidden method)
    def _update_center(self):
        self._center = np.mean(self._boundaries, axis = 0)

    # update frame (public method)
    def set_frame(self, frame):
        """ 
        update the frame (BGR)
        """
        self.frame = frame
        self._update_boundary()
        self._update_center()

    # get  boundaries (public method)
    def get_boundaries(self):
        return self._boundaries

    # get center (public method)
    def get_center(self):
        return self._center

    # visualize 
    def vis(self, quad = False):
        if self.frame is not None:
            if quad:
                for i,quad_mask in enumerate(self.test_mask):
                    cv2.imshow('quad ' + str(i), quad_mask)
            
            cv2.imshow('frame', self.frame)
        else:
            print('frame not found!!!')




if __name__ == '__main__':
    print('debugging')
    bond = boundary()
    cap = cv2.VideoCapture(0)
    while(1):

        _, frame = cap.read()
        print('done reading')
        bond.set_frame(frame)
        print(bond.get_boundaries())
        print(bond.get_center())
        bond.vis(quad = True)
        k = cv2.waitKey(5) & 0xFF == ord('q')
        if k:
            break
    







