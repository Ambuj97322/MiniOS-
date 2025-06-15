import os 
from users import get_current_user

def clear_screen():
    os.system("clear")

def show_help():
    print("""
Available Commands:
 - help: Show this help 
 - clear: Clear Screen
 - about: Info about MiniOS
 - user: Show current User
 - exit: Quit the shell
 """)
def shell_loop():
  user = get_current_user()
  while True:
    command = input(f"{user}@MiniOS $")
    if command =="exit":
        print("Shutting Down")
        break
    elif command =="clear":
        clear_screen()
    elif command =="help":
        show_help()
    elif command =="about":
        print("MiniOS v0.1 - Built by Asur")
    elif command =="user":
        print(f"Current User: {user}")
    else:
        print(f"Command notfound :{Command}")

print(show_help())