import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def create_folders(base_path):
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files(base_path):
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    dest = os.path.join(base_path, folder, file)
                    shutil.move(file_path, dest)
                    print(f"Moved: {file} -> {folder}")
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(base_path, "Others")
                if not os.path.exists(other_path):
                    os.makedirs(other_path)
                shutil.move(file_path, os.path.join(other_path, file))
                print(f"Moved: {file} -> Others")

def main():
    path = input("Enter folder path to organize: ")

    if not os.path.exists(path):
        print("Invalid path ❌")
        return

    create_folders(path)
    move_files(path)
    print("✨ Files organized successfully!")

if __name__ == "__main__": 
    main()
