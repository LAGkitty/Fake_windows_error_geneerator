# Fake Windows Error Generator

This Python application allows you to create and display highly realistic, native Windows error dialogs. Leveraging the Windows API, it generates error messages that are indistinguishable from genuine system alerts, making it a powerful tool for pranks, demonstrations, or testing user reactions.

## ✨ Features

-   **Native Windows Dialogs**: Spawns actual `MessageBoxW` dialogs using the Windows API (`ctypes`), ensuring an authentic look and feel.
-   **Customizable Title**: Set the title of the error window.
-   **Customizable Message**: Craft detailed error messages with line breaks.
-   **Authentic Icons**: Choose from standard Windows error icons: Error, Warning, Information, and Question.
-   **Standard Button Sets**: Select from common button combinations like "OK", "OK, Cancel", "Yes, No", and "Abort, Retry, Ignore".
-   **Always On Top**: Generated dialogs appear as topmost windows, mimicking critical system alerts.
-   **Cross-Platform Fallback**: On non-Windows operating systems, the application provides a simulated preview using `tkinter` to demonstrate the intended native dialog.

## 🚀 Installation

1.  **Python**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2.  **Clone the Repository (or download the script)**:
    ```bash
    git clone https://github.com/your-username/fake-windows-error-generator.git
    cd fake-windows-error-generator
    ```
    *(Note: Replace `your-username/fake-windows-error-generator.git` with the actual repository URL once it's hosted.)*

3.  **No External Libraries Required for Native Dialogs**: The core functionality for spawning native Windows errors relies only on built-in Python modules (`tkinter`, `ctypes`, `platform`).

## 💡 Usage

1.  **Run the application**:
    ```bash
    python fake_error_generator.py
    ```

2.  **Customize Your Error**: Use the intuitive Tkinter interface to set the window title, error message, icon type, and button configuration.

3.  **Spawn Native Error**: Click the "SPAWN NATIVE ERROR" button. If you are on a Windows machine, a real system error dialog will appear. On other operating systems, a `tkinter` based informational message will be displayed, simulating the native dialog.

## ⚠️ Disclaimer

This tool is intended for educational, demonstrative, or entertainment purposes only. Please use it responsibly and ethically. Do not use this tool to cause distress, panic, or for any malicious activities. The author is not responsible for any misuse of this software.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
