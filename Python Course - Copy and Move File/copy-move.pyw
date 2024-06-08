import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os

# Hàm để chọn nhiều thư mục nguồn
def chon_thu_muc_nguon():
    folders = []
    while True:
        folder = filedialog.askdirectory(title="Chọn thư mục nguồn")
        if folder:
            folders.append(folder)
        else:
            break
    if folders:
        text_thu_muc_nguon.delete("1.0", tk.END)
        for folder in folders:
            text_thu_muc_nguon.insert(tk.END, folder + "\n")

# Hàm để chọn thư mục đích
def chon_thu_muc_dich():
    folder_path = filedialog.askdirectory(title="Chọn thư mục đích")
    if folder_path:
        entry_thu_muc_dich.delete(0, tk.END)
        entry_thu_muc_dich.insert(0, folder_path)

# Hàm để di chuyển tệp từ thư mục nguồn sang thư mục đích
def di_chuyen_tep():
    thu_muc_nguon = text_thu_muc_nguon.get("1.0", tk.END).strip().split("\n")
    thu_muc_dich = entry_thu_muc_dich.get()

    if not thu_muc_nguon or not thu_muc_dich:
        messagebox.showerror("Lỗi", "Vui lòng chọn cả thư mục nguồn và thư mục đích.")
        return

    for folder_path in thu_muc_nguon:
        try:
            folder_name = os.path.basename(folder_path)
            destination = os.path.join(thu_muc_dich, folder_name)
            shutil.move(folder_path, destination)
        except Exception as e:
            messagebox.showerror("Lỗi", f'Lỗi không xác định: {e}')

    messagebox.showinfo("Thành công", "Các thư mục đã được di chuyển thành công.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Copy and Move Tools DEvelopMenT by NGuyen MAnh HUng")

# Tạo các thành phần GUI
label_thu_muc_nguon = tk.Label(root, text="Thư mục nguồn hoặc các thư mục:")
label_thu_muc_nguon.grid(row=0, column=0, padx=10, pady=10)

text_thu_muc_nguon = tk.Text(root, height=5, width=50)
text_thu_muc_nguon.grid(row=0, column=1, padx=10, pady=10)

button_chon_thu_muc_nguon = tk.Button(root, text="Chọn thư mục", command=chon_thu_muc_nguon)
button_chon_thu_muc_nguon.grid(row=0, column=2, padx=10, pady=10)

label_thu_muc_dich = tk.Label(root, text="Thư mục đích:")
label_thu_muc_dich.grid(row=1, column=0, padx=10, pady=10)

entry_thu_muc_dich = tk.Entry(root, width=50)
entry_thu_muc_dich.grid(row=1, column=1, padx=10, pady=10)

button_chon_thu_muc_dich = tk.Button(root, text="Chọn thư mục", command=chon_thu_muc_dich)
button_chon_thu_muc_dich.grid(row=1, column=2, padx=10, pady=10)

button_di_chuyen = tk.Button(root, text="Di chuyển thư mục", command=di_chuyen_tep)
button_di_chuyen.grid(row=2, column=1, padx=10, pady=10)

# Khởi chạy giao diện
root.mainloop()
