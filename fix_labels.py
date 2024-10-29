import os

# Set paths
train_path = '/home/dipshikha/Music/sign lanuagage/dataset/train'
labels_path = '/home/dipshikha/Music/sign lanuagage/dataset/labels'

# Loop through each image file in the training directory
for image_name in os.listdir(train_path):
    if image_name.endswith(('.jpg', '.png', '.jpeg')):  # Add more formats if needed
        # Get the name without extension
        base_name = os.path.splitext(image_name)[0]
        
        # Create expected label file name
        expected_label_file = os.path.join(labels_path, f"{base_name}.txt")
        
        # Check if the label file exists
        if os.path.exists(expected_label_file):
            print(f"Found matching label for {image_name}: {expected_label_file}")
        else:
            print(f"Warning: No matching label found for {image_name}")

# If you want to rename mismatched labels
for label_name in os.listdir(labels_path):
    if label_name.endswith('.txt'):
        # Extract the base name without extension
        base_name = os.path.splitext(label_name)[0]
        
        # Check if there's a corresponding image file
        corresponding_image = f"{base_name}.jpg"  # Adjust this if your images have different extensions
        if corresponding_image not in os.listdir(train_path):
            # Find the corresponding image file if it has a different naming convention
            for img in os.listdir(train_path):
                if img.startswith(base_name):  # You can change this condition based on your naming scheme
                    new_label_name = f"{img}.txt"
                    old_label_path = os.path.join(labels_path, label_name)
                    new_label_path = os.path.join(labels_path, new_label_name)
                    print(f"Renaming {label_name} to {new_label_name}")
                    os.rename(old_label_path, new_label_path)
                    break
