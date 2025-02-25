import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk 

def generate_qr():
    data = entry.get()
    if not data:
        status_label.config(text="Please enter data!", fg="red")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png"), 
                                                        ("All Files", "*.*")])
    if file_path:
        img.save(file_path)
        status_label.config(text="QR Code saved!", fg="green")

        img = img.resize((200, 200))  
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk  
    
#GUI setup
root = tk.Tk()
root.geometry("500x500")
root.title("QR Code Generator")
root.configure(bg='white', highlightthickness=20, highlightcolor="pink")


tk.Label(root, text="Enter the data(text or url): ", font=("Cambria", 16, "bold italic"), bg="white" ).pack(pady=15)
entry = tk.Entry(root, width=35, font= ("Cambria",15), borderwidth=5, bg='white')
entry.pack(pady=10)

#Generate button
generate_button = tk.Button(root, text=" Generate QR ",font=("Cambria",13), bg='pink',relief='ridge', command=generate_qr)

generate_button.pack(pady=10)

# QR Code Display
qr_label = tk.Label(root, bg="white")
qr_label.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Cambria", 12), bg="white")
status_label.pack(pady=10)

root.mainloop()

