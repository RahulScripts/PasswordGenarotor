# Password Generator

## Overview
The Password Generator is a user-friendly desktop application built with Python and Tkinter. It allows users to generate secure and customizable passwords based on their preferences, ensuring a balance of security and convenience.

## Features
- **Password Length:** Adjustable password length (minimum 8 characters, maximum 32 characters).
- **Character Options:** Includes options to toggle:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Numbers (0-9)
  - Special characters (@#$%&_=*)
- **Generated Password Display:** Displays the generated password with an option to copy it to the clipboard.
- **Validation:** Ensures the user selects at least one character type and warns if the password length is too short.

## Requirements
- Python 3.x
- Required Python modules:
  - `tkinter`
  - `pyperclip`

To install the required modules, use the `requirements.txt` file:

1. Open a terminal and navigate to the directory containing `requirements.txt`.
2. Run the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Installation
1. Clone the repository or download the source code.
2. Ensure Python 3.x is installed on your system.
3. Install the required Python module using pip:
   ```bash
   pip install pyperclip
   ```
4. Ensure the `icon.ico` file is located at the specified path or update the path in the code.

## Usage
1. Run the script:
   ```bash
   python app.py
   ```
2. Use the sliders and checkboxes to configure the password settings:
   - Set the desired password length using the entry field or slider.
   - Toggle the character sets (lowercase, uppercase, numbers, special characters).
3. Click the **Generate Password** button to create a password.
4. The generated password will be displayed in the "Generated Password" field.
5. Click the **Copy** button to copy the password to your clipboard.

**NOTE: You can you use the executable file directly from the foldere "Executable File"**

## Screenshot
![Screenshot](image.png)

## Known Issues
- The application does not ensure equal distribution of character types in the generated password.

## Future Enhancements
- Add an option to ensure at least one character from each selected character set.
- Enhance the user interface with more customization options.
- Save settings for reuse.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

## Author
- Rahul Halli
- Contact: hallirahul777@gmail.com

## Acknowledgments
- Python for the programming language.
- Tkinter for GUI development.
- Pyperclip for clipboard functionality.

