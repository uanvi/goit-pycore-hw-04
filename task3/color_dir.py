import sys
from pathlib import Path
from colorama import Fore, Style

def display_directory_structure(directory_path):
    """Directory structure with colorama"""
    try:
        directory = Path(directory_path)
        if not directory.is_dir():
            print(f"{Fore.RED}Error: {directory_path} is not a directory.{Style.RESET_ALL}")
            return

        for item in directory.iterdir():
            if item.is_dir():
                print(f"{Fore.BLUE}[Directory] {item.name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[File] {item.name}{Style.RESET_ALL}")

    except Exception as e:
        print("Unexpected error" + e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Correct usage: python {sys.argv[0]} <directory_path>")
        sys.exit(1)

    display_directory_structure(sys.argv[1])
