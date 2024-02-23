import xml.etree.ElementTree as ET
import difflib
import os

# Function to read the Alteryx workflow XML content
def read_workflow_xml(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to save the current version of the workflow
def save_current_version(content, version_file_path):
    with open(version_file_path, 'w') as file:
        file.write(content)

# Function to get the previous version of the workflow if it exists
def get_previous_version(version_file_path):
    if os.path.exists(version_file_path):
        with open(version_file_path, 'r') as file:
            return file.read()
    return None

# Function to log differences between the current and previous versions
def log_differences(current_content, previous_content, log_file):
    diff = difflib.unified_diff(
        previous_content.splitlines(keepends=True),
        current_content.splitlines(keepends=True),
        fromfile='previous_version',
        tofile='current_version',
    )
    with open(log_file, 'a') as log:
        log.writelines(diff)

# Main execution flow
if __name__ == "__main__":
    workflow_path = 'path_to_your_workflow.yxmd'  # Update this path to your actual Alteryx workflow file path
    version_file_path = 'path_to_your_version_file.txt'  # Path where the current version of the workflow is saved
    change_log_path = 'path_to_your_change_log.txt'  # Path to the change log file

    current_content = read_workflow_xml(workflow_path)
    previous_content = get_previous_version(version_file_path)

    if current_content != previous_content:
        if previous_content is not None:  # If it's not the first run
            log_differences(current_content, previous_content, change_log_path)
            print("Changes detected and logged.")
        save_current_version(current_content, version_file_path)
    else:
        print("No changes detected.")
