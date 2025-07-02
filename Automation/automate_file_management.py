# python scripts to automate file management tasks such as organizing files, renaming files, and moving files based on certain criteria.
import os
import shutil

#define a path to the download directory
downloads_folder = 'C:\Users\SEBABE\Desktop\Downloads'

#define the target folders for different file types
folders = {
    'images': ['jpg', 'jpeg', 'png', 'gif'],
    'documents': ['pdf', 'docx', 'txt', 'xlsx'],
    'videos': ['mp4', 'mkv', 'avi', 'mov'],
    'audio': ['mp3', 'wav', 'aac', 'flac'],
    'archives': ['zip', 'rar', 'tar', 'gz'],
    'scripts': ['py', 'js', 'sh', 'bat'],
    'installers': ['exe', 'msi'],
    'others': []
}
#creating folders if they do not exist
for folder in folders.keys():
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
#loop through files in the downloads folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    if os.path.isfile(file_path):
        #skip directories 
        if os.path.isdir(file_path):
            continue
        
        #check for extension and move to the app
        for folder, extensions in folders.items():
            if filename.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(downloads_folder, folder, filename))
                break
            
        