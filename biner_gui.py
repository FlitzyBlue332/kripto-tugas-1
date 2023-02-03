from pathlib import Path
import control.controlOneTimePad as onetimepad
import control.controlPlayFair as playfair
import control.controlVignere as vigenere
import control.controlVignereExt as vigenereExt

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage, messagebox, Text
from tkinter.filedialog import asksaveasfile, askopenfile, askopenfilename

def encProcess():
    '''
    file biner only
    '''
    ptext = entry_ptext.get()
    key = entry_key.get()
    cipher = cipher_label.cget("text")
    if(len(ptext)>0):
        if(cipher == "Vigenere" and len(key)>0):
            set_entry_cptext(vigenere.vignereChiperEncrypt(ptext, key))
        elif(cipher == "Vigenere Ext." and len(key)>0):
            set_entry_cptext(vigenereExt.vignereExtEncrypt(ptext, key))
        elif(cipher == "Playfair" and len(key)>0):
            set_entry_cptext(playfair.playfairEnc(ptext, key))
        elif(cipher == "One Time Pad"):
            key = onetimepad.keyGenerator()
            set_entry_key(key)
            savefiletxt(key, 'Save Key As', "my-one-time-pad-key")
            set_entry_cptext(onetimepad.oneTimePadEncrypt(ptext, key))
        elif(len(key) <= 0):
            messagebox.showerror("Key Empty!!!", "There is no text in the key box nyaa!!!\n This cipher need key nyaa!!")
        else:
            messagebox.showerror("No Cipher Selected!!!", "No Cipher selecter nyaa!!\n Select cipher to start encrypt or decrypt nyaa!!")
    else:
        messagebox.showerror("Plaintext Empty!!!", "There is no text in the plaintext box nyaa!!!")

def decProcess():
    cptext = entry_cptext.get()
    key = entry_key.get()
    cipher = cipher_label.cget("text")
    if(len(cptext)>0):
        if(cipher == "Vigenere" and len(key)>0):
            set_entry_ptext(vigenere.vignereChiperDecrypt(cptext, key))
        elif(cipher == "Vigenere Ext." and len(key)>0):
            set_entry_ptext(vigenereExt.vignereExtDecrypt(cptext, key))
        elif(cipher == "Playfair" and len(key)>0):
            set_entry_ptext(playfair.playfairDec(cptext, key))
        elif(cipher == "One Time Pad"):
            key = loadfiletxt()
            
            set_entry_ptext(onetimepad.oneTimePadDecrypt(cptext, key))
        elif(len(key) <= 0):
            messagebox.showerror("Key Empty!!!", "There's no text in the key box nyaa!!!\n This cipher need key nyaa!!")
        else:
            messagebox.showerror("No Cipher Selected!!!", "No Cipher selecter nyaa!!\n Select cipher to start encrypt or decrypt nyaa!!")
    else:
        messagebox.showerror("Plaintext Empty!!!", "There's no text in the plaintext box nyaa!!!")

# file manage
## save file
# def saveButtonFunc():
    
def savefiletxt(content, title_name:str, default_name:str):
    f = asksaveasfile(mode='w', title=title_name, defaultextension=".txt", initialfile=default_name)
    if(f is not None):
        f.write(content)
        f.close()
    

def savefilebytes(content, title_name:str, default_name:str, extention:str):
    f = asksaveasfile(mode='wb', title=title_name, defaultextension= extention, initialfile=default_name)
    if(f is not None):
        f.write(content)
        f.close()

## load file
def loadfiletxt():
    f = askopenfile(mode='r', filetypes=[('Text documents', '.txt')])
    if(f is not None):
        content = f.read()
        return content
    return

def loadfilebytes():
    filename = askopenfilename(filetypes=[('All files', '*')])
    if(f is not None):
        f = open(filename, 'rb')
        content = f.read()
        extention = (filename.split('.'))[1]
    return content, extention

# GUI
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\COODING\Kripto\kripto-tugas-1\build\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# func set chiper
def change_cipher(changed_to:str):
    cipher = changed_to
    cipher_label.config(text=cipher)

# func untuk set entry
def set_entry_ptext(input:str):
    last = len(entry_ptext.get())
    entry_ptext.delete(0, last)
    entry_ptext.insert(0, input)
    return

def set_entry_file_ptext(input:str):
    last = len(entry_file_ptext.get())
    entry_file_ptext.delete(0, last)
    entry_file_ptext.insert(0, input)
    return

def set_entry_cptext(input:str):
    last = len(entry_cptext.get())
    entry_cptext.delete(0, last)
    entry_cptext.insert(0, input)
    return

def set_entry_file_cptext(input:str):
    last = len(entry_file_cptext.get())
    entry_file_cptext.delete(0, last)
    entry_file_cptext.insert(0, input)
    return

def set_entry_key(input:str):
    last = len(entry_key.get())
    entry_key.delete(0, last)
    entry_key.insert(0, input)
    return

window = Tk()

window.geometry("900x600")
window.configure(bg = "#7D20C5")
window.title("Chiper Enc/Dec")

canvas = Canvas(
    window,
    bg = "#440982",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
# gambar sugar
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    727.0,
    310.0,
    image=image_image_1
)

# label
cipher_label = Label(
    text="Cipher", 
    font=("Heebo Regular", 15 * -1),
)
cipher_label.place(
    x=785.0,
    y=57.0,
    width=100.0,
    height=34.0
)

# cipher
button_vigenere = Button(
    text="Vigenere",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_cipher('Vigenere'),
    relief="flat"
)
button_vigenereExt = Button(
    text="Vigenere Ext.",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_cipher('Vigenere Ext.'),
    relief="flat"
)
button_playfair = Button(
    text="Playfair",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_cipher('Playfair'),
    relief="flat"
)
button_onetimepad = Button(
    text="One Time Pad",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_cipher('One Time Pad'),
    relief="flat"
)
button_vigenere.place(
    x=785.0,
    y=116.0,
    width=100.0,
    height=30.0
)
button_vigenereExt.place(
    x=785.0,
    y=164.0,
    width=100.0,
    height=30.0
)
button_playfair.place(
    x=785.0,
    y=212.0,
    width=100.0,
    height=30.0
)
button_onetimepad.place(
    x=785.0,
    y=260.0,
    width=100.0,
    height=30.0
)

# encrypt button & decrypt button
button_encrypt_text = Button(
    text="Encrypt Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: encProcess(),
    relief="flat"
)
button_encrypt_file = Button(
    text="Encrypt File",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: encProcess(),
    relief="flat"
)
button_decrypt_file = Button(
    text="Decrypt File",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: decProcess(),
    relief="flat"
)
button_decrypt_text = Button(
    text="Decrypt Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: decProcess(),
    relief="flat"
)
button_encrypt_text.place(
    x=482.0,
    y=122.0,
    width=100.0,
    height=30.0
)
button_decrypt_file.place(
    x=482.0,
    y=475.0,
    width=100.0,
    height=30.0
)
# ptext load and save button
button_ptext_open = Button(
    text="Load Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_ptext_save = Button(
    text="Save Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_ptext_open.place(
    x=231.0,
    y=62.0,
    width=100.0,
    height=30.0
)
button_ptext_save.place(
    x=350.0,
    y=62.0,
    width=100.0,
    height=30.0
)
# cptext load and save button
button_cptext_open = Button(
    text="Load Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_cptext_save = Button(
    text="Save Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_cptext_open.place(
    x=231.0,
    y=352.0,
    width=100.0,
    height=30.0
)
button_cptext_save.place(
    x=350.0,
    y=352.0,
    width=100.0,
    height=30.0
)

# Entry
entry_ptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_file_ptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_file_cptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_cptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_key = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_ptext.place(
    x=53.0,
    y=100.0,
    width=397.0,
    height=78.0
)
entry_file_ptext.place(
    x=105.0,
    y=181.0,
    width=345.0,
    height=39.0
)
entry_cptext.place(
    x=53.0,
    y=390.0,
    width=397.0,
    height=78.0
)
entry_file_cptext.place(
    x=105.0,
    y=471.0,
    width=345.0,
    height=39.0
)
entry_key.place(
    x=141.0,
    y=285.0,
    width=309.0,
    height=48.0
)

canvas.create_text(
    53.0,
    58.0,
    anchor="nw",
    text="Plaintext:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)
canvas.create_text(
    53.0,
    181.0,
    anchor="nw",
    text="File:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)
canvas.create_text(
    53.0,
    471.0,
    anchor="nw",
    text="File:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)
canvas.create_text(
    50.0,
    348.0,
    anchor="nw",
    text="Chipertext:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)
canvas.create_text(
    70.0,
    293.0,
    anchor="nw",
    text="Key:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)
window.resizable(False, False)
window.mainloop()