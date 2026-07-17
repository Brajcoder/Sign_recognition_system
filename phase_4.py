import os
import csv
import cv2
import mediapipe as mp
from tqdm import tqdm

DATASET_PATH = "asl_alphabet_train"
OUTPUT_FILE = "dataset.csv"

MAX_IMAGES_PER_CLASS = 500

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
)

header = []

for i in range(21):
    header.extend([f"x{i}", f"y{i}", f"z{i}"])

header.append("label")

with open(OUTPUT_FILE, "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(header)

    classes = sorted(os.listdir(DATASET_PATH))

    for label in classes:

        class_path = os.path.join(DATASET_PATH, label)

        if not os.path.isdir(class_path):
            continue

        images = os.listdir(class_path)

        print(f"\nProcessing {label} ({len(images)} images)")

        count = 0

        for image_name in tqdm(images):

            if count >= MAX_IMAGES_PER_CLASS:
                break

            image_path = os.path.join(class_path, image_name)

            image = cv2.imread(image_path)

            if image is None:
                continue

            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            results = hands.process(rgb)

            if not results.multi_hand_landmarks:
                continue

            hand_landmarks = results.multi_hand_landmarks[0]

            row = []

            for lm in hand_landmarks.landmark:

                row.extend([
                    lm.x,
                    lm.y,
                    lm.z
                ])

            row.append(label)

            writer.writerow(row)

            count += 1

print("\nDataset Created Successfully!")
print(f"Saved as {OUTPUT_FILE}")