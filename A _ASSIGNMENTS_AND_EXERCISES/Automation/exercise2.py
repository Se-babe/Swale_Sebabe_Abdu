# exercise1 create an automatic script that backs up files from a folder within 3minutes of modification to a backup folder.
import os
import shutil
import time
# Define the source and backup directories
source_folder = 'C:\\Users\\SEBABE\\Desktop\\Downloads'
backup_folder = 'C:\\Users\\SEBABE\\Desktop\\Backup'
# Create the backup folder if it doesn't exist
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)
# Function to check for modified files and back them up
def backup_modified_files():
    while True:
        # Get the current time
        current_time = time.time()
        # Loop through files in the source folder
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            # Check if it's a file and not a directory
            if os.path.isfile(file_path):
                # Get the last modified time of the file
                last_modified_time = os.path.getmtime(file_path)
                # Check if the file was modified within the last 3 minutes (180 seconds)
                if current_time - last_modified_time < 60:
                    # Copy the file to the backup folder
                    shutil.copy2(file_path, backup_folder)
                    print(f'Backed up: {filename}')
        # Wait for a minute before checking again
        time.sleep(60)
# Start the backup process
backup_modified_files()
# This script will continuously monitor the specified source folder and back up any files that have been modified within the last 3 minutes to the backup folder. It checks for modifications every minute. Make sure to adjust the paths according to your system.
# Note: This script runs indefinitely. You can stop it by interrupting the execution (e
#e.g., pressing Ctrl+C in the terminal).