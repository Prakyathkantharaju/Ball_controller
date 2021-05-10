import cv2
import numpy as np


class ball_position(object):
    """
    ball_position class:
    1. Get the center from the ball.
    2. Update the frame.
    """
    def __init__(self, lower_bounds = [110,50,50], upper_bounds = [130, 255, 255]):
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.frame = None
        self._center = np.zeros((1,2))
        self._ball_present = False

    # update center location (hidden method)
    def _update_center(self, wall_boundaries):
        if self.frame is not None:
            # convert rgb to hsv
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

            # frame matrix shape
            shape_frame = [0,0, 500, 500]
            shape_frame[0] = int(np.min(wall_boundaries[:,0]))
            shape_frame[1] = int(np.min(wall_boundaries[:,1]))
            shape_frame[2] = int(np.max(wall_boundaries[:,0]))
            shape_frame[3] = int(np.max(wall_boundaries[:,1]))
            # performing erosion
            kernel = np.ones((5,5),np.uint8)
            gray = cv2.erode(gray, kernel, iterations = 3)
            # breaking and getting the boundaries
            test_mask = gray[shape_frame[0]:shape_frame[2],
                             shape_frame[1]:shape_frame[3]]
            ret,test_mask = cv2.threshold(test_mask,180,255,cv2.THRESH_BINARY)
            self.test_mask = test_mask
            ball = np.where(200 < test_mask)
            if len(ball[1]) > 25:
                center_quad_ball = np.mean(ball, axis = 1).reshape(1,2)
                self._center = center_quad_ball
                self._ball_present = True
            else:
                self._center = np.array([[0,0]])
                self._ball_present = False
                # print('$' * 50 + '\n' + 'ball '+' center not found')
            # offset boundaries.
            self._center[0,0] += shape_frame[0]
            self._center[0,1] += shape_frame[1]
            


    # update frame (public method)
    def set_frame(self, frame, wall_boundaries):
        """ 
        update the frame (BGR)
        """
        self.frame = frame
        self._update_center(wall_boundaries)

    # get  boundaries (public method)
    def get_boundaries(self):
        return None

    # get center (public method)
    def get_center(self):
        return self._ball_present,self._center[0,:]

    # visualize 
    def vis(self, ball = False):
        if self.frame is not None:
            if ball:
                cv2.imshow('ball', self.test_mask)
            
            cv2.imshow('frame', self.frame)
        else:
            print('frame not found!!!')


if __name__ == '__main__':
    print('debugging')
    from boundary import boundary
    bond = boundary()
    ball = ball_position()
    cap = cv2.VideoCapture(0)
    while(1):
        _, frame = cap.read()
        print('done reading')
        bond.set_frame(frame)
        wall_boundaries = bond.get_boundaries()
        ball.set_frame(frame, wall_boundaries)
        print(bond.get_center())
        print(ball.get_center())
        ball.vis(ball =True)
        k = cv2.waitKey(5) & 0xFF == ord('q')
        if k:
            break