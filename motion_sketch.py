import cv2
import mediapipe as mp
import numpy as np

cam = cv2.VideoCapture(0)
draw = mp.solutions.drawing_utils
hands = mp.solutions.hands.Hands()

success, frame = cam.read()
pre_x = None
pre_y = None

if success:
    h,w,_ = frame.shape
    blank_canvas  = np.zeros((h,w,3))


while True:

    success, frame = cam.read()
    

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand_landmark in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand_landmark, mp.solutions.hands.HAND_CONNECTIONS)

            index_tip = hand_landmark.landmark[8]
            h,w,_ = frame.shape
            x = index_tip.x * w
            y = index_tip.y * h

            index_pip = hand_landmark.landmark[6]
            x1 = index_pip.x 
            y1 = index_pip.y
            
     
            cv2.imshow("Blank canvas", blank_canvas)


            if index_tip.y < index_pip.y - 0.05:                        
                if pre_x is not None and pre_y is not None:
                    cv2.line(blank_canvas, (int(pre_x), int(pre_y)), (int(x), int(y)), (255, 0, 255), 5)
                
                # Only save the current position as 'previous' while actively drawing
                pre_x, pre_y = x, y 
            else:
                # Clear the previous position when you lift your finger so it doesn't cross-connect lines
                pre_x, pre_y = None, None

            cv2.circle(frame, (int(x), int(y)),4, (255, 0, 255), 8)
            cv2.circle(frame, (int(x1), int(y1)),4, (255, 0, 255), 8)
            

            

    if not success:
        print ("Camera not opened")
        break

    cv2.imshow("Video cam", frame)
    
    key = cv2.waitKey(1)

    if key == ord('q') or key == ord('Q'):
        break
    if key == ord('r'):
        blank_canvas  = np.zeros((h,w,3))
        pre_x = None
        pre_y = None


cam.release()


