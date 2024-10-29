import os
import random
import shutil

# Set paths
dataset_path = '/home/dipshikha/Music/sign lanuagage/Indian'  # Change this to your dataset path
train_path = 'dataset/train/'
val_path = 'dataset/val/'

# Create train and val directories
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)

# Iterate through each class directory
for class_dir in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_dir)
    if os.path.isdir(class_path):  # Ensure it's a directory
        # List all images in the class directory
        images = [f for f in os.listdir(class_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        
        if not images:  # Skip if the class directory is empty
            print(f"No images found in class directory: {class_dir}")
            continue
        
        random.shuffle(images)  # Shuffle images for randomness

        # Split the dataset
        split_ratio = 0.8  # 80% training, 20% validation
        split_index = int(len(images) * split_ratio)

        # Create class-specific directories
        train_class_path = os.path.join(train_path, class_dir)
        val_class_path = os.path.join(val_path, class_dir)
        os.makedirs(train_class_path, exist_ok=True)
        os.makedirs(val_class_path, exist_ok=True)

        # Copy images to train and validation folders
        for image in images[:split_index]:
            shutil.copy(os.path.join(class_path, image), os.path.join(train_class_path, image))

        for image in images[split_index:]:
            shutil.copy(os.path.join(class_path, image), os.path.join(val_class_path, image))

print("Dataset split completed without deleting original images.")
