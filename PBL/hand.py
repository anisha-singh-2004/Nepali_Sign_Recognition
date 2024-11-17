import cv2
import mediapipe as mp
import os
import numpy as np

# Initialize MediaPipe hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2)

# Load images from folder
folder_path = r'C:\DHA bright'
image_files = os.listdir(folder_path)

# Output folder for cropped hand images
output_folder = r'C:\Users\anish\Desktop\hand'
os.makedirs(output_folder, exist_ok=True)

for image_file in image_files:
    # Read image
    image = cv2.imread(os.path.join(folder_path, image_file))
    
    # Detect hands in the image
    results = hands.process(image)
    
    if results.multi_hand_landmarks:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Extract bounding box of hand region
            bounding_box = cv2.boundingRect(
                np.array([(landmark.x * image.shape[1], landmark.y * image.shape[0]) for landmark in hand_landmarks.landmark]))
            
            # Crop hand region from the image
            hand_cropped = image[bounding_box[1]:bounding_box[1]+bounding_box[3],
                                 bounding_box[0]:bounding_box[0]+bounding_box[2]]
            
            # Generate filename based on image name and hand index
            output_filename = f"{os.path.splitext(image_file)[0]}_hand_{i}.jpg"
            
            # Save cropped hand image to output folder
            cv2.imwrite(os.path.join(output_folder, output_filename), hand_cropped)
