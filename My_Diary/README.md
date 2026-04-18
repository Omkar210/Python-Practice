# My Diary

A simple Python diary application that lets users write and read encrypted notes with password protection. This project demonstrates file handling, basic XOR encryption, command-line interaction, and secure password input.

## Features

- Password-protected diary access
- Write encrypted diary entries
- Read and decrypt stored diary notes
- Simple menu-driven interface
- File error handling for missing diary files

## Files

- `my_diary.py` — main diary application script

## Run

```bash
cd My_Diary
python my_diary.py
```

## Notes

- Enter your username and password to access the diary.
- The current script checks for a valid username/password combination before allowing diary actions.
- Diary entries are stored in a file named `<username>_diary.txt`.
