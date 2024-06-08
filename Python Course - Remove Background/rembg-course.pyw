import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import rembg

# Tạo một cửa sổ Tkinter
root = tk.Tk()
root.title("Remove Background Tools by NGuyen MAnh HUng")

# Các biến để lưu trữ đường dẫn ảnh, đường dẫn xuất ảnh, và tên tệp xuất ra
selected_image_path = tk.StringVar()
output_image_path = tk.StringVar()
output_filename = tk.StringVar()

# Hàm để chọn ảnh
def choose_image():
    file_path = filedialog.askopenfilename(
        title="Chọn ảnh",
        filetypes=[("Tất cả các tệp", "*.*"), ("Ảnh JPG", "*.jpg"), ("Ảnh PNG", "*.png")],
    )
    if file_path:
        selected_image_path.set(file_path)

# Hàm để chọn đường dẫn xuất ảnh
def choose_output_path():
    folder_path = filedialog.askdirectory(
        title="Chọn thư mục xuất ảnh"
    )
    if folder_path:
        output_image_path.set(folder_path)

# Hàm để loại bỏ nền của ảnh và xuất ra tệp
def remove_background():
    input_path = selected_image_path.get()
    output_path = output_image_path.get()
    custom_filename = output_filename.get()
    
    if not input_path or not output_path:
        messagebox.showerror("Lỗi", "Vui lòng chọn ảnh và đường dẫn xuất ảnh!")
        return
    
    try:
        # Mở ảnh gốc và loại bỏ nền
        with open(input_path, "rb") as img_file:
            img_data = img_file.read()
        img_no_bg = rembg.remove(img_data)
        
        # Tạo tên tệp cho ảnh xuất ra, sử dụng tên tùy chỉnh hoặc mặc định
        if custom_filename:
            filename = custom_filename + "_no_bg.png"
        else:
            filename = os.path.basename(input_path).replace(" ", "_").split('.')[0] + "_no_bg.png"
        
        output_full_path = os.path.join(output_path, filename)
        
        # Lưu ảnh đã loại bỏ nền
        with open(output_full_path, "wb") as out_file:
            out_file.write(img_no_bg)
        
        messagebox.showinfo("Thành công", f"Đã loại bỏ nền và xuất ảnh tại: {output_full_path}")
    
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Tạo giao diện
frame = tk.Frame(root)
frame.pack(pady=20)

# Nút chọn ảnh
btn_choose_image = tk.Button(frame, text="Chọn ảnh", command=choose_image)
btn_choose_image.grid(row=0, column=0, padx=10)

# Nút chọn đường dẫn xuất ảnh
btn_choose_output = tk.Button(frame, text="Chọn đường dẫn xuất ảnh", command=choose_output_path)
btn_choose_output.grid(row=0, column=1, padx=10)

# Hộp nhập liệu để đặt tên tệp xuất ra
tk.Label(frame, text="Tên tệp xuất ra (không cần phần mở rộng)").grid(row=1, column=0, padx=10, pady=10)
entry_output_filename = tk.Entry(frame, textvariable=output_filename)
entry_output_filename.grid(row=1, column=1, columnspan=2, padx=10)

# Nút xác nhận để loại bỏ nền
btn_remove_bg = tk.Button(frame, text="Loại bỏ nền", command=remove_background)
btn_remove_bg.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
