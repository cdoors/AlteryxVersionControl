# Alteryx Workflow Version Control

## Overview

This Python script provides a simple version control system for Alteryx Designer workflows. Since Alteryx workflows (.yxmd files) are essentially XML documents, this tool tracks changes between versions by comparing the XML content, logging differences, and maintaining a history of modifications.

## Features

- **Change Detection**: Automatically detects changes between the current workflow and its previous version
- **Diff Generation**: Creates detailed diffs showing exactly what changed in the XML structure
- **Change Logging**: Maintains a running log of all changes made to the workflow over time
- **Version Tracking**: Saves snapshots of workflow versions for comparison

## Requirements

- Python 3.x
- Alteryx Designer (to create and modify workflows)
- Standard Python libraries:
  - xml.etree.ElementTree
  - difflib
  - os

## Installation

1. Download the script to your local machine
2. Update the following variables in the script to match your environment:
   - `workflow_path`: Path to your Alteryx workflow file (.yxmd)
   - `version_file_path`: Path where you want to save the current version snapshot
   - `change_log_path`: Path where you want to save the change log

## Usage

1. Run the script after making changes to your Alteryx workflow:

```bash
python alteryx_version_control.py
```

2. The script will:
   - Read your current workflow XML
   - Compare it to the previous version (if available)
   - Log any differences to the change log file
   - Save the current version for future comparisons

3. Review the change log to see what modifications were made between versions

## How It Works

1. The script reads the XML content of the specified Alteryx workflow file
2. It compares this content with the previously saved version
3. If differences are found, it generates a unified diff output showing additions, deletions, and changes
4. The diff is appended to the change log file with appropriate timestamps
5. The current version is saved as a reference for future comparisons

## Benefits

- **Tracking Changes**: See what changed between workflow versions
- **Collaboration**: Better understand modifications made by team members
- **Auditing**: Maintain a historical record of all workflow changes
- **Recovery**: Reference previous versions when troubleshooting

## Limitations

- This is a basic version control solution and doesn't provide all the features of a dedicated VCS like Git
- Large workflows may produce extensive diff outputs that can be difficult to interpret
- The script must be manually run after each workflow modification

