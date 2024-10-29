import os
import shutil

# Set paths
train_path = '/home/dipshikha/Music/sign lanuagage/dataset/train'
annotations_path = '/home/dipshikha/Music/sign lanuagage/dataset/annotations'

# Loop through each class directory
for class_dir in os.listdir(train_path):
    class_path = os.path.join(train_path, class_dir)
    
    if os.path.isdir(class_path):  # Ensure it's a directory
        # Loop through each image in the class directory
        for image_name in os.listdir(class_path):
            if image_name.endswith(('.jpg', '.png', '.jpeg')):  # Check for image formats
                # Generate label file name
                label_name = os.path.splitext(image_name)[0] + '.txt'
                label_path = os.path.join(annotations_path, label_name)
                
                # Check if the label file exists
                if os.path.exists(label_path):
                    # Move the label file to the class directory
                    shutil.move(label_path, os.path.join(class_path, label_name))

print("Labels have been organized into class folders.")
