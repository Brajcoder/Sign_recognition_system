import cv2
import mediapipe as mp
import csv
import os

LABEL = "A"
CSV_FILE = "dataset.csv"

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

sample_count = 0

if os.path.exists(CSV_FILE):
    with open(CSV_FILE, "r") as file:
        sample_count = sum(1 for _ in file) - 1
        if sample_count < 0:
            sample_count = 0

file_exists = os.path.isfile(CSV_FILE)

with open(CSV_FILE, "a", newline="") as file:

    writer = csv.writer(file)

    if not file_exists:

        header = []

        for i in range(21):
            header.extend([
                f"x{i}",
                f"y{i}",
                f"z{i}"
            ])

        header.append("label")

        writer.writerow(header)

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        row = []

        if results.multi_hand_landmarks:

            hand_landmarks = results.multi_hand_landmarks[0]

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            for lm in hand_landmarks.landmark:

                row.extend([
                    lm.x,
                    lm.y,
                    lm.z
                ])

        cv2.putText(
            frame,
            f"Label : {LABEL}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Samples : {sample_count}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            "Press S to Save",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.imshow("Dataset Collector", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s"):

            if len(row) == 63:

                row.append(LABEL)

                writer.writerow(row)

                sample_count += 1

                print(f"Sample {sample_count} Saved")

        elif key == 27:
            break

cap.release()
cv2.destroyAllWindows()