from src.menus.MenuHandler import logo, menu_handler

if __name__ == "__main__":
    logo("Workout Tracker V2")
    menu_handler(["Add workout", "Run Reports"], "Main Menu")