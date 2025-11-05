import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import os

def load_image(path):
    img = Image.open(path).convert('RGB')
    data = np.array(img)
    return data, img.size

def save_image(data, size, path):
    img = Image.fromarray(data.astype('uint8'))
    img.save(path)

def xor_operation(data, key):
    return data ^ key

def swap_pixels(data):
    swapped = data.copy()
    h, w, _ = swapped.shape
    for i in range(0, h, 2):
        for j in range(0, w, 2):
            if i+1 < h and j+1 < w:
                swapped[i, j], swapped[i+1, j+1] = swapped[i+1, j+1], swapped[i, j]
    return swapped

def process_image(path, output_path, key, method, mode):
    data, size = load_image(path)
    if method == 'xor':
        result = xor_operation(data, key)
    elif method == 'swap':
        result = swap_pixels(data)
    else:
        raise ValueError("Unsupported method")
    save_image(result, size, output_path)
    messagebox.showinfo("Success", f"Image {mode}ed using {method} method and saved to:\n{output_path}")

def browse_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.bmp")]))

def run_process(mode):
    path = file_path.get()
    if not path:
        messagebox.showerror("Error", "Please select an image file.")
        return
    method = method_var.get()
    key = int(key_entry.get()) if method == 'xor' else 0
    output = os.path.splitext(path)[0] + f"_{mode}.png"
    process_image(path, output, key, method, mode)

# GUI setup
root = tk.Tk()
root.title("Image Encryption Tool")

file_path = tk.StringVar()
method_var = tk.StringVar(value='xor')

tk.Label(root, text="Select Image:").grid(row=0, column=0, sticky='e')
tk.Entry(root, textvariable=file_path, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

tk.Label(root, text="Method:").grid(row=1, column=0, sticky='e')
tk.OptionMenu(root, method_var, 'xor', 'swap').grid(row=1, column=1, sticky='w')

tk.Label(root, text="Key (for XOR):").grid(row=2, column=0, sticky='e')
key_entry = tk.Entry(root)
key_entry.insert(0, "123")
key_entry.grid(row=2, column=1, sticky='w')

tk.Button(root, text="Encrypt", command=lambda: run_process('encrypt')).grid(row=3, column=0, pady=10)
tk.Button(root, text="Decrypt", command=lambda: run_process('decrypt')).grid(row=3, column=1, pady=10)

root.mainloop()
