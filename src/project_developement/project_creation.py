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
        try:
            print("insert project")
            db=DatabaseExecutions() 
            print("db connected")
            logging.info("DB Connection Successful")   
            query=f'''
                insert into PROJECT(proj_name,description,problem_statement,environment,version,project_path) VALUES('{self.project_name}','{self.description}','{self.problem_statement}','{self.environment}','{self.version}','{self.project_path}')
            '''
            print(type(db))
            db.execute_ddl_dml(query)
            # print("query executed")
            logging.info("Query Execution Successful")
            db.close_connection
            logging.info("DB Connection Closed")
        except Exception as e:
            print(e)
            logging.ERROR(e)
    
    def create_structure(self):
        #create project structure
        project_dir=os.path(self.project_path,self.project_name)
        

    
    



