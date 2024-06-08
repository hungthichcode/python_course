import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re

class LibraryCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Checking Library v1.2.0 by Developers Official")
        self.root.geometry("500x250")  # Set the initial size of the window

        self.create_widgets()

    def create_widgets(self):
        # Create and place the Select Python File button
        self.select_button = tk.Button(self.root, text="Select Python File", command=self.select_file)
        self.select_button.pack(pady=10)

        # Create and place the input field to display selected file path
        self.file_path_entry = tk.Entry(self.root, width=50)
        self.file_path_entry.pack(pady=10)

        # Create and place the Checking Library button
        self.check_button = tk.Button(self.root, text="Checking Library", command=self.check_libraries)
        self.check_button.pack(pady=10)

    def select_file(self):
        # Open a file dialog to select a Python file
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py *.pyw")])
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

    def check_libraries(self):
        file_path = self.file_path_entry.get()
        if not file_path:
            messagebox.showerror("Error", "No file selected!")
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Regex to find import statements
            libraries = re.findall(r'^\s*(?:import|from)\s+(\w+)', content, re.MULTILINE)
            libraries = sorted(set(libraries))

            if libraries:
                # Extract the base name of the selected file
                base_name = os.path.basename(file_path)
                name, _ = os.path.splitext(base_name)
                output_file_name = f"{name}_Library.txt"

                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                output_file_path = os.path.join(desktop_path, output_file_name)
                
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for lib in libraries:
                        output_file.write(f"pip install {lib}\n")
                    output_file.write("\n*Lưu ý: Hãy sao chép từng thư viện vào Command Prompt (Chạy bằng quyền Run as Administrator) và bấm Enter")

                messagebox.showinfo("Checking Library", f"Successfully... Library đã lưu thành công ở Desktop với tên {output_file_name}")
            else:
                messagebox.showwarning("Checking Library", "Error... Trong File không sử dụng Library nào !")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryCheckerApp(root)
    root.mainloop()