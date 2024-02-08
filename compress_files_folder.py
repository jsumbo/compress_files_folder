import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, archive_type):
    """
    Compresses the specified folder into the specified archive type.
    
    :param folder_path: Path to the folder to be compressed.
    :param archive_type: Type of archive to create (.zip, .tar, .tgz, etc.).
    """
    try:
        if not os.path.isdir(folder_path):
            print("The specified path does not exist or is not a directory.")
            return

        base_name = os.path.basename(folder_path.rstrip("/\\"))
        if archive_type == ".tgz":
            date_str = datetime.now().strftime("%Y_%m_%d")
            archive_name = f"{base_name}_{date_str}.tgz"
            with tarfile.open(archive_name, "w:gz") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif archive_type == ".tar":
            archive_name = f"{base_name}.tar"
            with tarfile.open(archive_name, "w") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif archive_type == ".zip":
            archive_name = f"{base_name}.zip"
            with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), 
                                   os.path.relpath(os.path.join(root, file), 
                                   os.path.join(folder_path, '..')))
        else:
            print("Unsupported archive type.")
            return
        print(f"Folder '{folder_path}' successfully compressed to '{archive_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    print("Select the type of compressed file:")
    print("1. Zip (.zip)")
    print("2. Tar (.tar)")
    print("3. Tar Gz (.tgz)")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        compress_folder(folder_path, ".zip")
    elif choice == '2':
        compress_folder(folder_path, ".tar")
    elif choice == '3':
        compress_folder(folder_path, ".tgz")
    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
