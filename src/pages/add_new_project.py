import flet as ft
import os

def open_new_project_page(page: ft.Page):
    # Clean the existing page content
    page.clean()

    # Create new project page title
    title = ft.Text("Create New Project", style="headline4", text_align=ft.TextAlign.CENTER)

    # Create form fields
    project_name = ft.TextField(label="Project Name")
    project_description = ft.TextField(label="Project Description")
    problem_statement = ft.TextField(label="Problem Statement", multiline=True, min_lines=3)
    environment = ft.TextField(label="Environment")
    version = ft.TextField(label="Version")
    
    # Create a browse button for project path
    project_path = ft.TextField(label="Project Path", read_only=True)

    # Define the callback function for file picker
    def on_file_picker_result(e):
        if e.files:
            # Extract folder path from the selected file's path
            folder_path = os.path.dirname(e.files[0].path)
            project_path.value = folder_path
        else:
            project_path.value = ""

    # Create the file picker instance
    file_picker = ft.FilePicker(on_result=on_file_picker_result)
    
    # Add the file picker to the page (as overlay)
    page.overlay.append(file_picker)

    # Add elements to the new project page
    page.add(
        title,
        project_name,
        project_description,
        problem_statement,
        environment,
        version,
        ft.Row([project_path, ft.ElevatedButton("Browse", on_click=lambda e: file_picker.pick_files())], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.ElevatedButton("Submit", on_click=lambda e: print("Project Created"))  # Add your submit logic here
    )
    page.update()

    # Clean the existing page content
    page.clean()

    # Create new project page title
    title = ft.Text("Create New Project", style="headline4", text_align=ft.TextAlign.CENTER)

    # Create form fields
    project_name = ft.TextField(label="Project Name")
    project_description = ft.TextField(label="Project Description")
    problem_statement = ft.TextField(label="Problem Statement", multiline=True, min_lines=3)
    environment = ft.TextField(label="Environment")
    version = ft.TextField(label="Version")
    
    # Create a browse button for project path
    project_path = ft.TextField(label="Project Path", read_only=True)

    # Define the callback function for file picker
    def on_file_picker_result(e):
        if e.files:
            project_path.value = e.files[0].path
        else:
            project_path.value = ""

    # Create the file picker instance
    file_picker = ft.FilePicker(on_result=on_file_picker_result)
    
    # Add the file picker to the page (as overlay)
    page.overlay.append(file_picker)

    # Add elements to the new project page
    page.add(
        title,
        project_name,
        project_description,
        problem_statement,
        environment,
        version,
        # ft.Row([project_path, ft.ElevatedButton("Browse", on_click=lambda e: file_picker.pick_files())], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.ElevatedButton("Submit", on_click=lambda e: print("Project Created"))  # Add your submit logic here
    )
    page.update()




ft.app(target=open_new_project_page)