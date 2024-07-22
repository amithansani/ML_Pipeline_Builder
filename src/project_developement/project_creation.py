import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.logger import logging
from src.exception import CustomException
from src.utils import DatabaseExecutions
# @dataclass
# class ProjectPath:
#     project_path:str = 

class DevelopNewProject:
    def __init__(self,project_name,description,problem_statement,environment,version,project_path):
        
        logging.info("Project Class initiated")
        self.project_name=project_name
        self.description = description
        self.problem_statement = problem_statement
        self.environment = environment
        self.version = version
        self.project_path = project_path

    def validate_inputs(self):
        pass
        

    def insert_project_db(self):
        db=DatabaseExecutions()
        
        query=f'''
            insert into PROJECT(proj_name,description,problem_statement,environment,version,project_path) VALUES('{self.project_name}','{self.description}','{self.problem_statement}','{self.environment}','{self.version}','{self.project_path}')
        '''
        print(query)
        print(db.execute_ddl_dml(query=query))
        db.close_connection
    
    def create_structure(self):
        #create project structure
        project_dir=os.path(self.project_path,self.project_name)
        

    
    



