# template.py
import os

# ------------------------
# DEFINE YOUR FOLDER/FILE STRUCTURE HERE
# ------------------------
# Use nested dictionaries for folders, and list of files inside each folder
project_structure = {
    "my_project": {  # root folder
        "src": ["__init__.py", "main.py"],
        "src/tests": ["__init__.py","test_main.py"],
        "data": [],
        "notebooks": ["analysis.ipynb"],
        "src/config": ["__init__.py","config.yaml"],
        "docs": [],
        "src/utils":["__init__.py","customLogger.py","customException.py"],
        "src/modules":["__init__.py"],
        "src/modules/testReply":["__init__.py", "testRequest.py", "testReplyFinal.py"],
        "src/modules/testReply/testByDifficulty":["__init__.py"],
        "src/modules/testReply/testByCompanies":["__init__.py"],
        "src/modules/testReply/testByGenAI":["__init__.py"],
        "src/modules/testReply/testReply":["__init__.py"],
        "src/modules/scoreReply":["__init__.py", "scoreRequest.py", "scoreReplyFinal.py"],
        "src/modules/scoreReply/scoreByDifficulty":["__init__.py"],
        "src/modules/scoreReply/scoreByCompanies":["__init__.py"],
        "src/modules/scoreReply/scoreByGenAI":["__init__.py"],
        "src/modules/scoreReply/scoreReply":["__init__.py"],

    }
}

# ------------------------
# FUNCTION TO CREATE FOLDERS & FILES
# ------------------------
def create_structure(base_path, structure):
    """
    Recursively creates folder and file structure.
    
    Args:
        base_path (str): Path where to create structure
        structure (dict): Nested dict of folders and list of files
    """
    for folder, contents in structure.items():
        folder_path = os.path.join(base_path, folder)
        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")

        # Process contents
        if isinstance(contents, dict):
            # Nested folders
            create_structure(folder_path, contents)
        elif isinstance(contents, list):
            # Create files inside this folder
            for file_name in contents:
                file_path = os.path.join(folder_path, file_name)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        pass  # create empty file
                    print(f"Created file: {file_path}")
                else:
                    print(f"File already exists: {file_path}")

# ------------------------
# RUN SCRIPT
# ------------------------
if __name__ == "__main__":
    base_path = "."  # current directory
    create_structure(base_path, project_structure)
