from tkinter import *
from PIL import ImageTk,Image
import pyqrcode

root=Tk()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"

    url = pyqrcode.create(link)
    url.png(file_name,scale=5)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,350,window=image_label)

canvas = Canvas(root,width=400,height=500)
canvas.pack()

app_label = Label(root,text="QR Code Generator",fg="blue",font=("ProductSans",30))
canvas.create_window(200,100,window=app_label)

name_label=Label(root,text="Link Name",font=("ariel",12))
link_label=Label(root,text="Link",font=("ariel",12))
canvas.create_window(200,150,window=name_label)
canvas.create_window(200,200,window=link_label)

name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,175,window=name_entry)
canvas.create_window(200,225,window=link_entry)

button=Button(text="Generate QRCode",command=generate)
canvas.create_window(200,250,window=button)



root.mainloop()
