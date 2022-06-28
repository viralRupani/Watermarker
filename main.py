import tkinter.colorchooser
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import messagebox

window = Tk()
window.title("Watermarker")
window.minsize(width=600, height=400)


def select_image():
    global canvas, img, file_path
    file_path = filedialog.askopenfilename(title="Select a Picture")
    img = ImageTk.PhotoImage(Image.open(file_path).resize((300, 300)))
    canvas.create_image(0, 0, anchor=NW, image=img)


def add_watermark():
    try:
        global file_path, img, canvas
        watermark = watermark_text.get()
        img = Image.open(file_path).convert("RGBA")
        d = ImageDraw.Draw(img)
        print(watermark)
        fnt = ImageFont.truetype("arial.ttf", int(font_size.get()))
        d.text((int(x_entry.get()), int(y_entry.get())), watermark, font=fnt, fill=(color_picker[0][0], color_picker[0][1], color_picker[0][2], int(alpha_input.get())))
        img.save(f"watermarked.png", quality=95)
        img = ImageTk.PhotoImage(Image.open('watermarked.png').convert("RGBA").resize((300, 300)))
        canvas.create_image(0, 0, anchor=NW, image=img)
    except:
        messagebox.showerror("Error", "Something Went Wrong")

def color_picker_():
    global color_picker
    color_picker = tkinter.colorchooser.askcolor(title="choose a color for watermark")


select_image_button = Button(text="Select Image", command=select_image, width=40)
select_image_button.grid(row=7, column=0, columnspan=2, pady=3)

canvas = Canvas(width=300, height=300)
canvas.grid(row=0, column=0, rowspan=6, columnspan=2)
img = ImageTk.PhotoImage(Image.open("noimage.png").resize((300, 300)))
canvas.create_image(0, 0, anchor=NW, image=img)

font_label = Label(text="Font Size:")
font_label.grid(row=0, column=2)
font_size = Entry(width=3)
font_size.insert(0, "14")
font_size.grid(row=0, column=3)

x_label = Label(text="X co-ordinate:")
x_entry = Entry(width=4)
x_entry.insert(0, "0")
y_label = Label(text="Y Co-ordinate:")
y_entry = Entry(width=4)
y_entry.insert(0, "0")
x_label.grid(row=1, column=2)
x_entry.grid(row=1, column=3)
y_label.grid(row=2, column=2)
y_entry.grid(row=2, column=3)

watermark_label = Label(text="Watermark Text:")
watermark_label.grid(row=3, column=2)
watermark_text = Entry(window)
watermark_text.grid(row=3, column=3)

submit_text = Button(text='Add Watermark', command=add_watermark)
submit_text.grid(row=5, column=3, padx=5)

label_alpha = Label(text="Set Alpha:")
label_alpha.grid(row=4, column=2)
alpha_input = Entry()
alpha_input.insert(0, "250")
alpha_input.grid(row=4, column=3)

color_picker = [(255, 255, 255)]
color_picker_button = Button(text="Choose color", command=color_picker_)
color_picker_button.grid(row=5, column=2)

window.mainloop()
