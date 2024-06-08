import tkinter as tk
from tkinter import scrolledtext, colorchooser, messagebox
import subprocess
import requests
import shutil
from elevate import elevate

class CmdGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CMD and POWerShElL TOols PYthOn")

        # Menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        # Add "File" menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Check Update", command=self.check_update)
        self.file_menu.add_command(label="Exit", command=root.quit)

        # Add "Help" menu
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

        # Entry widget to accept user commands
        self.command_entry = tk.Entry(root, width=80)
        self.command_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # OptionMenu to choose between cmd and PowerShell
        self.shell_var = tk.StringVar(value='cmd')
        self.shell_menu = tk.OptionMenu(root, self.shell_var, 'cmd', 'powershell')
        self.shell_menu.grid(row=0, column=3, padx=10, pady=10)

        # Button to run the command
        self.run_button = tk.Button(root, text="Run", command=self.run_command)
        self.run_button.grid(row=0, column=4, padx=10, pady=10)

        # Button to run the command as administrator
        self.run_as_admin_button = tk.Button(root, text="Run as Admin", command=self.run_command_as_admin)
        self.run_as_admin_button.grid(row=1, column=4, padx=10, pady=10)

        # Button to change text color
        self.text_color_button = tk.Button(root, text="Text Color", command=self.change_text_color)
        self.text_color_button.grid(row=1, column=0, padx=10, pady=10)

        # Button to change background color
        self.bg_color_button = tk.Button(root, text="Background Color", command=self.change_bg_color)
        self.bg_color_button.grid(row=1, column=1, padx=10, pady=10)

        # ScrolledText widget to display command output
        self.output_text = scrolledtext.ScrolledText(root, width=100, height=30)
        self.output_text.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

    def run_command(self):
        command = self.command_entry.get()
        shell = self.shell_var.get()
        if command.strip():
            try:
                if shell == 'cmd':
                    result = subprocess.run(command, shell=True, text=True, capture_output=True)
                elif shell == 'powershell':
                    result = subprocess.run(['powershell', '-Command', command], text=True, capture_output=True)
                
                output = result.stdout if result.stdout else result.stderr
                self.output_text.insert(tk.END, f"Command: {command}\n{output}\n{'-'*80}\n")
                self.output_text.see(tk.END)  # Scroll to the end
            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {str(e)}\n{'-'*80}\n")
                self.output_text.see(tk.END)

    def run_command_as_admin(self):
        command = self.command_entry.get()
        shell = self.shell_var.get()
        if command.strip():
            try:
                elevate()
                if shell == 'cmd':
                    result = subprocess.run(command, shell=True, text=True, capture_output=True)
                elif shell == 'powershell':
                    result = subprocess.run(['powershell', '-Command', command], text=True, capture_output=True)
                
                output = result.stdout if result.stdout else result.stderr
                self.output_text.insert(tk.END, f"Command (as Admin): {command}\n{output}\n{'-'*80}\n")
                self.output_text.see(tk.END)  # Scroll to the end
            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {str(e)}\n{'-'*80}\n")
                self.output_text.see(tk.END)

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.output_text.config(fg=color)

    def change_bg_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.output_text.config(bg=color)

    def show_about(self):
        messagebox.showinfo("About", "Cmd and PowerShell GUI\nVersion 1.0\nAuthor: Your Name")

    def check_update(self):
        try:
            update_url = "https://example.com/your_script.py"  # URL của file cập nhật
            response = requests.get(update_url, stream=True)
            if response.status_code == 200:
                with open("cmd_gui.py", "wb") as f:
                    shutil.copyfileobj(response.raw, f)
                messagebox.showinfo("Update", "The application has been updated. Please restart the application.")
            else:
                messagebox.showwarning("Update", "Failed to download the update. Please try again later.")
        except Exception as e:
            messagebox.showerror("Update", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = CmdGUI(root)
    root.mainloop()