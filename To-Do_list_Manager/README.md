# To-Do List Manager

A simple Python command-line utility for writing and reading an encrypted diary-style to-do list. This project demonstrates basic file I/O, password-protected access, and simple XOR encryption.

## Overview

This application allows users to:
- Enter a username and password
- Write encrypted diary entries or to-do notes to a file
- Read and decrypt existing diary content
- Use a password-based verification mechanism for access control

## Key Features

- **Secure access** with password verification
- **Encrypted storage** using XOR encryption
- **Read and write diary entries** in a text file
- **Simple menu interface** for ease of use
- **File handling** with error detection and reporting

## Python Concepts Demonstrated

### File Input/Output

This project shows how to read from and write to text files in Python using `open()` and file modes such as `a+` and `r`.

### Password Input

The `getpass` module is used to securely collect password input without showing it on the terminal.

### Basic Encryption

A simple XOR-based encryption is used to transform text before writing it to the file. The same key is used to decrypt entries when reading them back.

## Usage

1. Run the application:
   ```bash
   python to-do_list.py
   ```
2. Enter your username and password when prompted.
3. Use the menu to choose between writing a diary entry or reading saved entries.
4. Select `3` to exit.

## Example Interaction

```
Enter username: Omkar
Enter password: 
****************************************
1. Write to Diary
2. Read Diary
3. Exit
****************************************
Enter your choice: 1
Write a message in Omkar_diary.txt: Buy milk and finish homework
Message written successfully.
```

## Project Structure

- `to-do_list.py`: Main application file containing the menu, encryption logic, and file handling.

## Learning Outcomes

- Understanding text file read/write operations in Python
- Working with user input and hidden password input
- Implementing simple encryption/decryption logic
- Building a basic command-line menu-driven application
- Handling missing file and access errors gracefully

## Requirements

- Python 3.x
- No external dependencies (uses only built-in Python modules)
