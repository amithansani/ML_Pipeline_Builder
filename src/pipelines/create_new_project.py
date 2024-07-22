import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.project_developement.project_creation import DevelopNewProject
from src.logger import logging
from src.exception import CustomException

def create_new_project_pipeline(project_name,description,problem_statement,environment,version,project_path):
    try:

        logging.info("Starting Create Project Pipeline")
        prj=DevelopNewProject(project_name,description,problem_statement,environment,version,project_path)
        
        # prj.validate_inputs()
        # logging.info("Project Validated")
        
        prj.insert_project_db()
        logging.info("Project insterted in DB")
        
        prj.create_structure()
        logging.info("Structure Created")

    except Exception as e:
        CustomException(e,sys)




