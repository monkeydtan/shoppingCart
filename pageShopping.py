import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Shopping Mall")
window.geometry("500x400")
font1 = ['Arial',14,'bold']
font2 = ['Arial',10,'normal']

#เพิ่มค่า
def increase():
    global count
    count += 1
    label_qty.config(text=f"{count}")
    #update_label()
    
#ลดค่า
def decrease():
    global count
    if count > 0:
        count -= 1
        label_qty.config(text=f"{count}")
    else:
        messagebox.showwarning("Warning","ไม่สามารถลดค่าได้มากกว่านี้แล้ว !")

# # แสดงค่า
# def update_label():
#     result.config(text=f"ปริมาณ : {count}")

# ค่าเริ่มต้น
count = 0

header = tk.Label(window,text="Shopping Cart",font=font1)
header.pack(pady=(20,0))

frame_product1 = tk.Frame(window,background='sky blue',width=200, height=200)
frame_product1.pack(side='left',padx=(10,10))

# ป้องกันไม่ให้กรอบปรับขนาดตามเนื้อหา
frame_product1.pack_propagate(False)

product1_name = tk.Label(frame_product1,text="Snack",font=font2,bg='sky blue')
product1_name.pack(side='top',pady=(5,0))

# โหลดรูปภาพ
img1 = Image.open("pic/snack.jpg")
img1_resize = img1.resize((130,130),Image.LANCZOS)
photo1 = ImageTk.PhotoImage(img1_resize)

# สร้าง label สำหรับรูปภาพ
product1_img = tk.Label(frame_product1,image=photo1,bg='sky blue')
product1_img.pack(side='top',pady=5)

# กรอบปุ่มเพิ่มลด frame_product1,background='white'width=50, height=2
frame_btn = tk.Frame(frame_product1,bg='sky blue',width=130,height=30)
frame_btn.pack(side='bottom',pady=(5,10))

frame_btn.grid_rowconfigure(0, weight=1)  # ทำให้แถวที่ 0 ขยายได้
frame_btn.grid_columnconfigure(0, weight=1)  # ทำให้คอลัมน์ที่ 0 ขยายได้
frame_btn.grid_columnconfigure(1, weight=1)  # ทำให้คอลัมน์ที่ 1 ขยายได้
frame_btn.grid_columnconfigure(2, weight=1)  # ทำให้คอลัมน์ที่ 2 ขยายได้

# ปุ่มลด
btn_down = tk.Button(frame_btn,text="-",font=15,command=decrease)
btn_down.grid(row=0,column=0,sticky='nsew', padx=(5, 5))

# label จำนวนสินค้าที่จะเอา
label_qty = tk.Label(frame_btn,text=f"{count}",bg='sky blue')
label_qty.grid(row=0,column=1,sticky='nsew', padx=(10, 10))

# ปุ่มเพิ่ม
btn_up = tk.Button(frame_btn,text="+",font=15,command=increase)
btn_up.grid(row=0,column=2,sticky='nsew', padx=(5, 5))


window.mainloop()