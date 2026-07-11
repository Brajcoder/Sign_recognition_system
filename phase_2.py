import cv2
import mediapipe as mp 
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils
tip_ids = [4, 8, 12, 16, 20]


cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

  
    frame = cv2.flip(frame, 2)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    total_fingers = 0

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

           
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = []

            h, w, c = frame.shape

            
            for lm in hand_landmarks.landmark:
                cx = int(lm.x * w)
                cy = int(lm.y * h)
                landmarks.append((cx, cy))

            if len(landmarks) != 0:

                fingers = []

                
                if landmarks[4][0] > landmarks[3][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                
                for i in range(1, 5):

                    if landmarks[tip_ids[i]][1] <= landmarks[tip_ids[i] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = sum(fingers)

    cv2.putText(
        frame,
        f"Fingers: {total_fingers}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    cv2.imshow("Finger Counter", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()