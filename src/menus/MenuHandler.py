# TODO: I want to convert these functions to a class in the future, seems that grouping similar functions together is a perfect use for a class.

from rich.console import Console
from beaupy import select
import os

console = Console()
terminal_width = console.width
content_width = terminal_width - 2

# Generates the logo for the program
def logo(logo_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    centered_logo = f"{logo_name:^{content_width}}"
    
    console.print("+" + "-" * content_width + "+")
    console.print(f"|{centered_logo}|")
    console.print("+" + "-" * content_width + "+")


    
# Generates the menu with a customizable list of options and menu name. menu_handler returns the option that user chose so main.py can call that module
def menu_handler(menu_options: list, menu_name: str):
    console.print(f"[bold]{menu_name}[/bold]")
    user_selection = select(menu_options, cursor="🡆")
    
    return user_selection
