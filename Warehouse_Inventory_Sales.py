# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:11:17 2020

@author: user
"""

#import modules
from tkinter import * 
import tkinter.messagebox
import sqlite3


#class for Front end of Warehouse Inventory UI(user interface)
class Product:
    def __init__(self,root):
        
        self.root = root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1290x690")
        self.root.config(bg="yellow")
        
        
        pId = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany =StringVar()
        pContact = StringVar()
        
        
        """ Create the frame """
        MainFrame = Frame(self.root,bg="red")
        MainFrame.grid()
        
        HeadFrame = Frame(MainFrame, bd=1, padx=50, pady=10, bg='white', relief=RIDGE)
        HeadFrame.pack(side=TOP)
        
        self.ITitle = Label(HeadFrame, font=('arial',50,'bold'), fg='red',
                            text="Warehouse Inventory Sales Purchase", bg='white')
        self.ITitle.grid()
        
        OperationFrame = Frame(MainFrame,bd=4,width=1300,height = 60,padx=50,
                               pady=20,bg="white",relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)
        
        BodyFrame = Frame(MainFrame,bd=2,width=1290,height = 400,padx=30,
                          pady=20,bg="white",relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)
        
        
        LeftBodyFrame = LabelFrame(BodyFrame,bd=5,width=600,height = 380,
                        padx=20,pady=10,bg="yellow",relief=RIDGE,font=('arial',15,'bold'),
                        text='Product Item Details: ')
        LeftBodyFrame.pack(side=LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd=5,width=400,height = 380,
                        padx=20,pady=10,bg="yellow",relief=RIDGE,font=('arial',15,'bold'),
                        text='Product Item Information: ')
        RightBodyFrame.pack(side=RIGHT)
        
        """ Add the Widgets to LeftBodyFrame """
        
        #For Product ID
        self.labelpID = Label(LeftBodyFrame, font=('arial',15,'bold'),
                              text = "Product Id :", padx=2,pady=2, bg='yellow',fg='blue')
        self.labelpID.grid(row=0,column=0,sticky=W)
        self.txtpID = Entry(LeftBodyFrame, font=('arial',20,'bold'),
                            textvariable = pId, width=35)
        self.txtpID.grid(row=0,column=1,sticky=W)
        
        
         #For Product Name
        self.labelpName = Label(LeftBodyFrame, font=('arial',15,'bold'),
                              text = "Product Name :", padx=2,pady=2, bg='yellow',fg='blue')
        self.labelpName.grid(row=1,column=0,sticky=W)
        self.txtpName = Entry(LeftBodyFrame, font=('arial',20,'bold'),
                            textvariable = pName, width=35)
        self.txtpName.grid(row=1,column=1,sticky=W)
        
        
         #For Product Price
        self.labelpPrice = Label(LeftBodyFrame, font=('arial',15,'bold'),
                              text = "Product Price :", padx=2,pady=2, bg='yellow',fg='blue')
        self.labelpPrice.grid(row=2,column=0,sticky=W)
        self.txtpPrice = Entry(LeftBodyFrame, font=('arial',20,'bold'),
                            textvariable = pPrice, width=35)
        self.txtpPrice.grid(row=2,column=1,sticky=W)
        
        
         #For Product Quantity
        self.labelpQty = Label(LeftBodyFrame, font=('arial',15,'bold'),
                              text = "Product Quantity :", padx=2,pady=2, bg='yellow',fg='blue')
        self.labelpQty.grid(row=3,column=0,sticky=W)
        self.txtpQty = Entry(LeftBodyFrame, font=('arial',20,'bold'),
                            textvariable = pQty, width=35)
        self.txtpQty.grid(row=3,column=1,sticky=W)
        
        
         #For Product Company
        self.labelpCompany = Label(LeftBodyFrame, font=('arial',15,'bold'),
                              text = "Mfg. Company :", padx=2, pady=2,bg='yellow',fg='blue')
        self.labelpCompany.grid(row=4,column=0,sticky=W)
        self.txtpCompany = Entry(LeftBodyFrame, font=('arial',20,'bold'),
                            textvariable = pCompany, width=35)
        self.txtpCompany.grid(row=4,column=1,sticky=W)
        
        
         #For Product Contact
        self.labelpContact = Label(LeftBodyFrame, font=('arial',15,'bold'),
                              text = "Company Contact :", padx=2,pady=2, bg='yellow',fg='blue')
        self.labelpContact.grid(row=5,column=0,sticky=W)
        self.txtpContact = Entry(LeftBodyFrame, font=('arial',20,'bold'),
                            textvariable = pContact, width=35)
        self.txtpContact.grid(row=5,column=1,sticky=W)
        
        
        self.labelpC1 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC1.grid(row=6,column=0,sticky=W)
        
        self.labelpC2 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC2.grid(row=7,column=0,sticky=W)
        
        self.labelpC3 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC3.grid(row=8,column=0,sticky=W)
        
        self.labelpC4 = Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC4.grid(row=9,column=0,sticky=W)
        
        """  Add Scroll bar  """
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0, column = 1, sticky='ns')
        
        productList = Listbox(RightBodyFrame, width=40, height=16, font=('arial',12,'bold'),
                yscrollcommand=scroll.set)
        
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)
        
        ''' Add the buttons to operation frame '''
        
        self.buttonSaveData = Button(OperationFrame, text='Save',
                            font=('arial',18,'bold'),height=1,width='10',bd=4 )
        self.buttonSaveData.grid(row = 0, column = 0)
        
        self.buttonShowData = Button(OperationFrame, text='Show Data',
                            font=('arial',18,'bold'),height=1,width='10',bd=4 )
        self.buttonShowData.grid(row = 0, column = 1)
        
        self.buttonClear = Button(OperationFrame, text='Reset',
                            font=('arial',18,'bold'),height=1,width='10',bd=4 )
        self.buttonClear.grid(row = 0, column = 2)
        
        self.buttonDelete = Button(OperationFrame, text='Delete',
                            font=('arial',18,'bold'),height=1,width='10',bd=4 )
        self.buttonDelete.grid(row = 0, column = 3)
        
        self.buttonSearch = Button(OperationFrame, text='Search',
                            font=('arial',18,'bold'),height=1,width='10',bd=4 )
        self.buttonSearch.grid(row = 0, column = 4)
        
        self.buttonUpdate = Button(OperationFrame, text='Search',
                            font=('arial',18,'bold'),height=1,width='10',bd=4 )
        self.buttonUpdate.grid(row = 0, column = 5)
        
        self.buttonClose = Button(OperationFrame, text='Close',
                            font=('arial',18,'bold'),height=1,width='10',bd=4 )
        self.buttonClose.grid(row = 0, column = 6)
        
# Back End Database operations
class Database:
    def conn(self):
        print("Database : connection method called\n")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "create table if not exists product(pid integer primary key,\
                 pname text,price text,qty text,company text,contact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print('Database : connection method finished\n')
        
    def insert(self,pid,name,price,qty,company,contact):
        print("Database : insert method called\n")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.close()
        print('Database : insert method finished\n')
        
    def show(self):
        print("Database : show method called\n")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "select * from product"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : show method finished\n")
        
        
        
        
if __name__ == '__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    