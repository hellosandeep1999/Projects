# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:08:28 2020

@author: user
"""
import random
import time
import datetime
import tkinter.messagebox
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management Systems")
root.configure(background = "Cadet Blue")

Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief = RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial',59,'bold'), text="Restaurant Management Systems",
                 bd=21, bg='Cadet Blue', fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0)

ReceiptCal_F = Frame(root, bg='Powder Blue', bd=10,relief = RIDGE)
ReceiptCal_F.pack(side=RIGHT)
Buttons_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=3,relief = RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=6,relief = RIDGE)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief = RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='Cadet Blue', bd=10,relief = RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F = Frame(MenuFrame, bg='Powder Blue', bd=4, relief = RIDGE)
Cost_F.pack(side=BOTTOM)
Drinks_F = Frame(MenuFrame, bg='Powder Blue', bd=10, relief = RIDGE)
Drinks_F.pack(side=TOP)

Drinks_F = Frame(MenuFrame, bg='Powder Blue', bd=10, relief = RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F = Frame(MenuFrame, bg='Powder Blue', bd=10, relief = RIDGE)
Cake_F.pack(side=RIGHT)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

#==========================================Drinks============================================================================

Latta = Checkbutton(Drinks_F, text="Latta", variable=var1, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=0, sticky=W)
Espresso = Checkbutton(Drinks_F, text="Espresso", variable=var2, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=1, sticky=W)
Iced_Latta = Checkbutton(Drinks_F, text="Iced_Latta", variable=var3, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=2, sticky=W)
Vale_Coffee = Checkbutton(Drinks_F, text="Vale_Coffee", variable=var4, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=3, sticky=W)
Cappuccino = Checkbutton(Drinks_F, text="Cappuccino", variable=var5, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=4, sticky=W)
African_Coffee = Checkbutton(Drinks_F, text="African_Coffee", variable=var6, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=5, sticky=W)
American_Coffee = Checkbutton(Drinks_F, text="American_Coffee", variable=var7, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=6, sticky=W)
Iced_Cappuccino = Checkbutton(Drinks_F, text="Iced_Cappuccino\t", variable=var8, onvalue=1, offvalue=0,font=('arial',18,'bold'),
                    bg='Powder Blue').grid(row=7, sticky=W)

#==========================================Entry Box for Drinks============================================================================
txtLatta = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtLatta.grid(row=0, column=1)

txtEspresso = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtEspresso.grid(row=1, column=1)

txtIced_Latta = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtIced_Latta.grid(row=2, column=1)

txtVale_Coffee = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtVale_Coffee.grid(row=3, column=1)

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtCappuccino.grid(row=4, column=1)

txtAfrican_Coffee = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtAfrican_Coffee.grid(row=5, column=1)

txtAmerican_Coffee = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtAmerican_Coffee.grid(row=6, column=1)

txtIced_Cappuccino = Entry(Drinks_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtIced_Cappuccino.grid(row=7, column=1)


#==========================================Cakes============================================================================

SchoolCake = Checkbutton(Cake_F, text="School Cake\t\t\t", variable=var9, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=0, sticky=W)
Sunny_Ao_Cake = Checkbutton(Cake_F, text="Sunny O Cake", variable=var10, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=1, sticky=W)
Jonathan_Yo_Cake = Checkbutton(Cake_F, text="Jonathan O Cake", variable=var11, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=2, sticky=W)
West_African_Cake = Checkbutton(Cake_F, text="West African Cake", variable=var12, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=3, sticky=W)
Lagos_Chocolate_Cake = Checkbutton(Cake_F, text="Lagos Chocolate Cake", variable=var13, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=4, sticky=W)
Kilburn_Chocolate_Cake = Checkbutton(Cake_F, text="Kilburn Chocolate Cake", variable=var14, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=5, sticky=W)
Cariton_Hill_Cake = Checkbutton(Cake_F, text="Cariton Hill Chocolate Cake", variable=var15, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=6, sticky=W)
Queen_Park_Cake = Checkbutton(Cake_F, text="Queen Park Chocolate Cake", variable=var16, onvalue=1, offvalue=0,font=('arial',16,'bold'),
                    bg='Powder Blue').grid(row=7, sticky=W)

#==========================================Entry Box for Cakes============================================================================
txtSchoolCake = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtSchoolCake.grid(row=0, column=1)

txtSunny_Ao_Cake = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtSunny_Ao_Cake.grid(row=1, column=1)

txtJonathan_Yo_Cake = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtJonathan_Yo_Cake.grid(row=2, column=1)

txtWest_African_Cake = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtWest_African_Cake.grid(row=3, column=1)

txtLagos_Chocolate_Cake = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtLagos_Chocolate_Cake.grid(row=4, column=1)

txtKilburn_Chocolate_Cake = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtKilburn_Chocolate_Cake.grid(row=5, column=1)

txtCariton_Hill_Cake  = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtCariton_Hill_Cake .grid(row=6, column=1)

txtQueen_Park_Cake = Entry(Cake_F,font=('arial',16,'bold'), bd=8, width=6, justify='left', state=DISABLED)
txtQueen_Park_Cake.grid(row=7, column=1)

#===========================================Receipt================================================================

txtReceipt = Text(Receipt_F, width=46, height=12, bg="white", bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)

#===========================================Receipt================================================================
btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black",font=('arial',16,'bold'),width=4, text="Total",
                  bg='Powder Blue').grid(row=0,column=0)
btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black",font=('arial',16,'bold'),width=4, text="Receipt",
                  bg='Powder Blue').grid(row=0,column=1)
btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black",font=('arial',16,'bold'),width=4, text="Reset",
                  bg='Powder Blue').grid(row=0,column=2)
btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, fg="black",font=('arial',16,'bold'),width=4, text="Exit",
                  bg='Powder Blue').grid(row=0,column=3)



root.mainloop()














