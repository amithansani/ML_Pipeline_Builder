import flet as ft
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.pipelines.create_new_project import create_new_project_pipeline
from src.logger import logging

def open_new_project_page(page: ft.Page):
    # # Clean the existing page content
    # page.clean()

    # # Create new project page title
    # title = ft.Text("Create New Project", style="headline4", text_align=ft.TextAlign.CENTER)

    # # Create form fields
    # project_name = ft.TextField(label="Project Name")
    # project_description = ft.TextField(label="Project Description")
    # problem_type_list = [
    #     ft.dropdown.Option("ML Classifier"),
    #     ft.dropdown.Option ("ML Regression"),
    #     ft.dropdown.Option("NLP"),
    #     ft.dropdown.Option("Gen AI"),
    #     ft.dropdown.Option("Computer Vision"),
    # ]
    # # problem_statement = ft.TextField(label="Problem Statement", multiline=True, min_lines=3)
    # def on_select(e):
    #     selected_value = e.control.value
    #     # Display the selected value on the page
    #     page.controls.append(ft.Text(f"Selected: {selected_value}"))
    #     problem_statement=selected_value
    #     page.update()

    # problem_type_combo_box = ft.Dropdown(
    #     hint_text="Select Problem Type", 
    #     options=problem_type_list,
    #     on_change=on_select,
    # )


    # environment = ft.TextField(label="Environment")
    # version = ft.TextField(label="Version")
    
    # # Create a browse button for project path
    # project_path = ft.TextField(label="Project Path", read_only=True)
    
    # # Define the callback function for file picker
    # def on_file_picker_result(e):
    #     if e.files:
    #         # Extract folder path from the selected file's path
    #         folder_path = os.path.dirname(e.files[0].path)
    #         project_path.value = folder_path
    #     else:
    #         project_path.value = ""

    # # Create the file picker instance
    # file_picker = ft.FilePicker(on_result=on_file_picker_result)
    
    # # Add the file picker to the page (as overlay)
    # page.overlay.append(file_picker)

    # # Add elements to the new project page
    # page.add(
    #     title,
    #     project_name,
    #     project_description,
    #     problem_type_combo_box,
    #     environment,
    #     version,
    #     ft.Row([project_path, ft.ElevatedButton("Browse", on_click=lambda e: file_picker.pick_files())], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
    #     ft.ElevatedButton("Submit", on_click=lambda e: print("Project Created"))  # Add your submit logic here
    # )
    # page.update()

    # Clean the existing page content
    page.clean()

    # Create new project page title
    title = ft.Text("Create New Project", style="headline4", text_align=ft.TextAlign.CENTER)

    # Create form fields
    project_name = ft.TextField(label="Project Name")
    project_description = ft.TextField(label="Project Description")
    # problem_statement = ft.TextField(label="Problem Statement", multiline=True, min_lines=3)
    problem_type_list = [
        ft.dropdown.Option("ML Classifier"),
        ft.dropdown.Option ("ML Regression"),
        ft.dropdown.Option("NLP"),
        ft.dropdown.Option("Gen AI"),
        ft.dropdown.Option("Computer Vision"),
    ]
    # problem_statement = ft.TextField(label="Problem Statement", multiline=True, min_lines=3)
    problem_statement=""
    def on_select(e):
        global ploblem_statement
        selected_value = e.control.value
        
        # Display the selected value on the page
        page.controls.append(ft.Text(f"Selected: {selected_value}"))
        problem_statement=selected_value
        print("problem_statement",problem_statement)
        page.update()

    problem_type_combo_box = ft.Dropdown(
        hint_text="Select Problem Type", 
        options=problem_type_list,
        on_change=on_select,
    )

    environment = ft.TextField(label="Environment")
    version = ft.TextField(label="Version")
    
    # Create a browse button for project path
    project_path = ft.TextField(label="Project Path", read_only=True)

    # Define the callback function for file picker
    def on_dialog_result(e: ft.FilePickerResultEvent):
        # print("Selected files:", e.files)
        print("Selected file or directory:", e.path)
        if e.path:
            project_path.value=e.path
            page.update()
        else:
            project_path.value=""
            page.update()
            
    def save_project(e):
        logging.info("In Save project")
        global problem_statement
        create_new_project_pipeline(project_name.value,project_description.value,problem_statement,environment.value,version.value,project_path.value)
        
    # Create the file picker instance
    
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    # Add the file picker to the page (as overlay)
    page.overlay.append(file_picker)

    # Add elements to the new project page
    page.add(
        title,
        project_name,
        project_description,
        problem_type_combo_box,
        environment,
        version,
        ft.Row([project_path, ft.ElevatedButton("Choose Folder",        on_click=lambda _: file_picker.get_directory_path())], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.ElevatedButton("Submit", on_click=save_project)  # Add your submit logic here
    )
    page.update()


 

ft.app(target=open_new_project_page)