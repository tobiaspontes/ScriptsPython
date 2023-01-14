from tkinter import *
from PIL import Image, ImageTk
import os

caminho = os.path.dirname(__file__)

root = Tk()
root.geometry("400x400")

# Create a photoimage object of the image in the path
image1 = Image.open(caminho + "\\ficha_livro.png")
teste = ImageTk.PhotoImage(image1)

label1 = Label(image=teste)
# label1.image = teste

# Position image
label1.place(relx=0.2, rely=0.2)
root.mainloop()