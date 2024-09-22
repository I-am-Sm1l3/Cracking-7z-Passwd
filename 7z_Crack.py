import py7zr
import argparse
import sys
import lzma

def crack_7z(file_path, password_list):
    # Read the passwords from the password list file
    with open(password_list, 'r') as f:
        passwords = f.read().splitlines()

    # Try each password from the list
    for password in passwords:
        try:
            with py7zr.SevenZipFile(file_path, mode='r', password=password) as archive:
                archive.extractall()
                print(f"\nPassword found: {password}")
                return
        except py7zr.exceptions.Bad7zFile:
            print("Invalid 7z file. Please check the file path and try again.")
            sys.exit(1)
        except (py7zr.exceptions.PasswordRequired, lzma.LZMAError):
            print(f"Trying password: {password}")
        except Exception as e:
            print(f"Error: {e}")

    # If no password works, let the user know
    print("\nPassword not found in the list.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="7z Password Cracker")
    parser.add_argument('-f', '--file', required=True, help="Path to the .7z file")
    parser.add_argument('-p', '--passwords', required=True, help="Path to the password list file (.txt)")

    # Parse the arguments
    args = parser.parse_args()

    # Print instructions
    print("=== 7z Password Cracker ===\n ===By 01smile10===")
    print("\nThis script attempts to crack the password of a .7z file using a list of passwords.")
    print("\nUsage example:")
    print("  python crack_7z.py -f /path/to/file.7z -p /path/to/passwords.txt")
    print("\nStarting password cracking...\n")

    # Call the function with the provided file paths
    crack_7z(args.file, args.passwords)
