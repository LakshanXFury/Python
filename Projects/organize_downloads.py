import os
import shutil  # Library for copying files or folders

# Path to your downloads folder
DOWNLOADS = os.path.expanduser("~/Downloads")

# Define where to move files based on extension
FILE_TYPES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Programs": [".exe", ".msi", ".dmg"],
    "Scripts": [".py", ".js", ".sh"],
}


def organize_downloads():
    for filename in os.listdir(DOWNLOADS):  # → lists everything inside Downloads.
        file_path = os.path.join(DOWNLOADS, filename)  # → full path to the file.

        if os.path.isfile(file_path):
            """
            os.path.splitext(filename) → splits the file into (name, extension).
            Example: "report.pdf" → ("report", ".pdf").
            """
            _, ext = os.path.splitext(filename)
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    """
                    If file extension matches →
                    Make sure destination folder exists (os.makedirs(..., exist_ok=True)).
                    Move the file with shutil.move().
                    Print confirmation.
                    Mark as moved, then break (stop checking further).
                    """
                    dest_folder = os.path.join(DOWNLOADS, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} → {folder}")
                    moved = True
                    break

            if not moved:
                # Optional: put unknown file types in "Others"
                other_folder = os.path.join(DOWNLOADS, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved {filename} → Others")


if __name__ == "__main__":
    organize_downloads()
