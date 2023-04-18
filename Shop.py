import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

Shop = Tk()
Shop.title('Shop program')
Shop.geometry('600x600')
title_font = ("Angsana New", 30)
text_font = ("Angsana New", 20)

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        content = f.read()
        tex.insert(END, content)

def Button_save():
    text = "บันทึกเสร็จเรียบร้อยแล้ว"
    messagebox.showinfo("บันทึกเสร็จสิ้น", text)



label_title = tk.Label(Shop, text="โปรแกรมบันทึกรายการสินค้า(Consumer Order)", anchor="center", font=title_font, fg="white", bg="brown")
label_title.pack()


label_name = tk.Label(Shop, text="ชื่อผู้รับ", font=text_font)
label_name.pack()
input_name = tk.Entry(Shop, width=30, font=text_font)
input_name.pack()


label_name_address = tk.Label(Shop, text="ที่อยู่ผู้รับ", font=text_font)
label_name_address.pack()
input_name_address = tk.Entry(Shop, width=50, font=text_font)
input_name_address.pack()

label_cellphone = tk.Label(Shop, text="เบอร์โทรศัพท์", font=text_font)
label_cellphone.pack()
input_cellphone = tk.Entry(Shop, width=20, font=text_font)
input_cellphone.pack()

label_order = tk.Label(Shop, text="รายการสินค้าที่สั่งชื้อ(Sales order)", font=text_font)
label_order.pack()
list_order = ttk.Combobox(Shop, font=text_font, values=["Shoes", "Pants", "T-shirt", "Hat", "Sock",])
list_order.pack()

payment = tk.Label(Shop, text="ใบเสร็จรับเงิน,หลักฐานการรับเงิน", font=text_font)
payment.pack()
button_payment = Button(Shop, text="เปิดไฟล์", font=text_font, command=open_file)
button_payment.pack()

button_complete = Button(Shop, text="เสร็จสิ้น", font=title_font, command=Button_save )
button_complete.pack()

Shop.mainloop()
