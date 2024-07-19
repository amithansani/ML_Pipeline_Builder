import os
import sys
from dataclasses import dataclass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logger import logging
from src.exception import CustomException

# @dataclass
# class ProjectPath:
#     project_path:str = 

class DevelopNewProject:
    def __init__(self,project_name,description,problem_statement,environment,version,project_path):
        
        self.project_name=project_name
        self.description = description
        self.problem_statement = problem_statement
        self.environment = environment
        self.version = version
        self.project_path = project_path

    def validate_inputs(self):
        pass

    def insert_project_db(self):
        pass
    
    def create_structure(self):
        pass

    
    



