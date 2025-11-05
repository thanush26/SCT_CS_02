# SCT_CS_02
Image Encryption Tool

A beginner-friendly Python GUI application for encrypting and decrypting images using simple techniques like XOR and pixel swapping. Built with Tkinter, Pillow, and NumPy, this tool is perfect for exploring basic image obfuscation methods.

Features

Load `.jpg`, `.png`, `.bmp` images
Encrypt/Decrypt using:
**XOR**: Bitwise XOR with a user-defined key
**Swap**: 2×2 pixel grid swapping
Save processed images automatically
Simple GUI with file browser and method selector
Success/error pop-ups for user feedback

How It Works

1. Launch the app.
2. Select an image file.
3. Choose encryption method (`xor` or `swap`).
4. Enter a key (only for XOR).
5. Click **Encrypt** or **Decrypt**.
6. The output image is saved with `_encrypt.png` or `_decrypt.png` suffix.

 Methods Explained

| Method | Description | Reversible |
|--------|-------------|------------|
| XOR    | Applies bitwise XOR with a key to each pixel | Yes, with same key |
| Swap   | Swaps pixels in a 2×2 grid pattern | Yes, symmetric |

File Overview

- `load_image(path)`: Loads image as NumPy array
- `save_image(data, size, path)`: Saves processed image
- `xor_operation(data, key)`: XOR encryption logic
- `swap_pixels(data)`: Pixel swapping logic
- `process_image(...)`: Main processing function
- `run_process(mode)`: Handles GUI input and triggers processing

 Educational Use

This tool is designed for learning and experimentation. It does not implement secure encryption protocols and should not be used for protecting sensitive data.

 Author

Made with  by Thanush  
Cybersecurity Engineering Student @ Coorg Institute of Technology
