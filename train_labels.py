import cv2
import os
import numpy as np

# Set paths
train_path = '/home/dipshikha/Music/sign lanuagage/dataset/train'
output_path = '/home/dipshikha/Music/sign lanuagage/dataset/train'  # Change this to train path for labels

# Loop through each class directory
for class_dir in os.listdir(train_path):
    class_path = os.path.join(train_path, class_dir)
    if os.path.isdir(class_path):  # Ensure it's a directory
        # Loop through each image in the class directory
        for image_name in os.listdir(class_path):
            if image_name.endswith(('.jpg', '.png', '.jpeg')):  # Add more formats if needed
                image_path = os.path.join(class_path, image_name)
                img = cv2.imread(image_path)

                # Convert to grayscale and apply binary thresholding
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY_INV)

                # Find contours
                contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Create a .txt annotation file in the class directory
                annotation_file = os.path.join(class_path, f"{os.path.splitext(image_name)[0]}.txt")
                with open(annotation_file, 'w') as f:
                    for contour in contours:
                        x, y, w, h = cv2.boundingRect(contour)

                        # Normalize coordinates
                        x_center = (x + w / 2) / img.shape[1]
                        y_center = (y + h / 2) / img.shape[0]
                        width = w / img.shape[1]
                        height = h / img.shape[0]
                        # Get the class ID (you can modify this to map your classes accordingly)
                        class_id = class_dir  # Assuming class_dir is the class name
                        # Write to the file (use the index of the class)
                        f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

print("Annotations and labels created successfully.")
