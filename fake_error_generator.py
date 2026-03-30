import tkinter as tk
from tkinter import ttk, messagebox
import ctypes
import platform

# Windows API constants for MessageBoxW
MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001
MB_ABORTRETRYIGNORE = 0x00000002
MB_YESNOCANCEL = 0x00000003
MB_YESNO = 0x00000004
MB_RETRYCANCEL = 0x00000005

MB_ICONERROR = 0x00000010
MB_ICONQUESTION = 0x00000020
MB_ICONWARNING = 0x00000030
MB_ICONINFORMATION = 0x00000040

MB_TOPMOST = 0x00040000

class FakeErrorGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Native Windows Error Generator")
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        
        # Variables
        self.title_var = tk.StringVar(value="System Error")
        self.icon_type = tk.StringVar(value="Error")
        self.button_type = tk.StringVar(value="OK")
        
        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="25")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        ttk.Label(main_frame, text="Windows Native Error Customizer", font=("Segoe UI", 14, "bold")).pack(pady=(0, 20))

        # Title Input
        ttk.Label(main_frame, text="Window Title:", font=("Segoe UI", 10)).pack(anchor=tk.W)
        ttk.Entry(main_frame, textvariable=self.title_var, width=60).pack(fill=tk.X, pady=(5, 15))

        # Message Input
        ttk.Label(main_frame, text="Error Message:", font=("Segoe UI", 10)).pack(anchor=tk.W)
        self.message_text = tk.Text(main_frame, height=4, width=60, font=("Segoe UI", 9))
        self.message_text.insert(tk.END, "The instruction at 0x00007FF7B3E54A8B referenced memory at 0x0000000000000000. The memory could not be read.")
        self.message_text.pack(fill=tk.X, pady=(5, 15))

        # Icon Selection
        ttk.Label(main_frame, text="Select Icon:", font=("Segoe UI", 10)).pack(anchor=tk.W)
        icons_frame = ttk.Frame(main_frame)
        icons_frame.pack(fill=tk.X, pady=(5, 15))
        
        for icon in ["Error", "Warning", "Information", "Question"]:
            ttk.Radiobutton(icons_frame, text=icon, variable=self.icon_type, value=icon).pack(side=tk.LEFT, padx=10)

        # Button Selection
        ttk.Label(main_frame, text="Select Buttons:", font=("Segoe UI", 10)).pack(anchor=tk.W)
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=(5, 20))
        
        btn_options = ["OK", "OK, Cancel", "Yes, No", "Abort, Retry, Ignore"]
        for btn in btn_options:
            ttk.Radiobutton(buttons_frame, text=btn, variable=self.button_type, value=btn).pack(side=tk.LEFT, padx=10)

        # Action Button
        style = ttk.Style()
        style.configure("Action.TButton", font=("Segoe UI", 10, "bold"))
        
        ttk.Button(main_frame, text="SPAWN NATIVE ERROR", command=self.spawn_error, style="Action.TButton").pack(fill=tk.X, ipady=10)
        
        ttk.Label(main_frame, text="Note: This will spawn a real Windows system dialog.", foreground="gray", font=("Segoe UI", 8)).pack(pady=(10, 0))

    def spawn_error(self):
        title = self.title_var.get()
        message = self.message_text.get("1.0", tk.END).strip()
        
        # Map Icons
        icon_map = {
            "Error": MB_ICONERROR,
            "Warning": MB_ICONWARNING,
            "Information": MB_ICONINFORMATION,
            "Question": MB_ICONQUESTION
        }
        
        # Map Buttons
        button_map = {
            "OK": MB_OK,
            "OK, Cancel": MB_OKCANCEL,
            "Yes, No": MB_YESNO,
            "Abort, Retry, Ignore": MB_ABORTRETRYIGNORE
        }
        
        flags = icon_map.get(self.icon_type.get(), MB_ICONERROR) | \
                button_map.get(self.button_type.get(), MB_OK) | \
                MB_TOPMOST

        if platform.system() == "Windows":
            # Call the real Windows API
            ctypes.windll.user32.MessageBoxW(0, message, title, flags)
        else:
            # Fallback for non-Windows (like this sandbox)
            messagebox.showinfo("System Simulation", f"On Windows, this would spawn a native {self.icon_type.get()} dialog with title '{title}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeErrorGenerator(root)
    root.mainloop()
