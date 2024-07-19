import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.pages.add_new_project import open_new_project_page

def main(page: ft.Page):
    # Set the title of the web page
    page.title = "ML Pipeline Builder"

    # Create buttons
    btn_create_new_project = ft.ElevatedButton("Create New Project", on_click=lambda e: open_new_project_page(page))
    btn_update_existing_project = ft.ElevatedButton("Update an Existing Project", on_click=lambda e: print("Update an Existing Project Clicked"))
    btn_project_dashboards = ft.ElevatedButton("Project Dashboards", on_click=lambda e: print("Project Dashboards Clicked"))

    # Add widgets to the main page
    page.add(
        ft.Text("ML Pipeline Builder", style="headline4", text_align=ft.TextAlign.CENTER),
        ft.Row([btn_create_new_project], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn_update_existing_project], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btn_project_dashboards], alignment=ft.MainAxisAlignment.CENTER)
    )

# Run the app
ft.app(target=main)
