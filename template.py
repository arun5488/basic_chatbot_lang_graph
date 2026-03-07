import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name="basic_chatbot_lang_graph"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/graph/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/llm/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/state/__init__.py",
    f"src/{project_name}/tools/__init__.py",
    f"src/{project_name}/ui/__init__.py",
    f"src/{project_name}/ui/streamlitui/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "data/.keep",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "research.ipynb",
    "schema.yaml",
    "params.yaml",
    ".env"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename}  already exists")