import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from captcha.image import ImageCaptcha
from tkinter import messagebox
import os

x = True
exit_ = False

class MathCaptcha:
    def __init__(self):
        root = Tk() #root Tkinter

        self.actual = str(random.randint(1, 9)) + \
            self.randOps()+str(random.randint(1, 9))
        print(self.actual) #For generating random string of mathmatical expression
        image = ImageCaptcha(fonts=['captcha.ttf']) #Font for captcha
        data = image.generate(self.actual)
        image.write(self.actual, "out.png") #Output image of captcha
        photo = PhotoImage(file=r"out.png")
        Button(root, text="Submit", image=photo).pack(side=TOP) #Putting image of captcha in tkinter
        Label(root, text="Enter the captcha:").pack(side=TOP)
        self.captchaInput = Entry(root)
        self.captchaInput.pack(side=TOP)
        Button(root, text="Submit", command=self.submit).pack(side=TOP)
        Button(root, text="Refresh", command=self.refresh).pack(side=TOP)

        mainloop()

    def refresh(self):
        r = tk.Tk()
        r.destroy()
        os.popen("main.py")

    def randOps(self):
        ops = ('+', '-', '*', '/')
        return random.choice(ops) #For choosingrandom operator the list as String

    def submit(self):
        cha_verify = False
        if(int(self.captchaInput.get()) == eval(self.actual)): #eval() converts returns the output of mathematical expression
            print("Captcha Verified")
            cha_verify = True
        else:
            print("Incorrect Captcha")
        if cha_verify:
            messagebox.showinfo("Captcha_LPU", "Congratulation Captcha Verified")
        else:
            messagebox.showinfo("Captcha_LPU", "Congratulation you failed")

c= MathCaptcha()