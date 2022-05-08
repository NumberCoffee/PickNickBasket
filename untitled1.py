from tkinter import *
import random

root=Tk()

root.title("Picknick Basket")
root.geometry("500x500")


list1 = ["Food" , "Friends" , "Phone" , "Id Card" , "Toaster"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_gift = list1[random_no]
    print("your gift is: " + random_gift)
    
    btn1 = Button(root)
    btn1 = Button(root, text="GIFT FROM BASKET ", command = random_number)
    btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )
    
    root.mainloop()