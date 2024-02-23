import xml.etree.ElementTree as ET
import hashlib
import pandas as pd

# Function to read the Alteryx workflow XML content
def read_workflow_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf8').decode('utf8')

# Function to hash the XML content
def hash_content(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

# Functions to save and read the latest hash to/from a file
def save_hash_to_file(hash_value, file_path='latest_hash.txt'):
    with open(file_path, 'w') as file:
        file.write(hash_value)

def read_hash_from_file(file_path='latest_hash.txt'):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

# Function to detect changes and log them
def detect_and_log_changes(new_content, log_file='change_log.txt'):
    new_hash = hash_content(new_content)
    old_hash = read_hash_from_file()
    
    if new_hash != old_hash:
        with open(log_file, 'a') as log:
            log.write(f"Change detected at {pd.Timestamp.now()}: Old Hash: {old_hash}, New Hash: {new_hash}\n")
        save_hash_to_file(new_hash)
        print("Change detected and logged.")
    else:
        print("No changes detected.")

# Main execution flow
if __name__ == "__main__":
    workflow_path = 'path_to_your_workflow.yxmd'  # Update this path to your actual Alteryx workflow file path
    workflow_content = read_workflow_xml(workflow_path)
    detect_and_log_changes(workflow_content)
