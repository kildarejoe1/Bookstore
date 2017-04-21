#This will be the python flask script -> to create the front end of the bookstore app

#Import the Twkinter library - to create the frontend application

from Tkinter import *


window=Tk()
window.wm_title("BookStore Application")

l1=Label(window,text="Title")
l1.grid(row=0, column=0)

l2=Label(window,text="Author")
l2.grid(row=0, column=2)

l1=Label(window,text="Name")
l1.grid(row=1, column=0)

l1=Label(window,text="ISBN")
l1.grid(row=1, column=2)
#Now create texts boxes

title_var=StringVar()
E1=Entry(window,textvariable=title_var)
E1.grid(row=0, column=1)

Author_var=StringVar()
E2=Entry(window,textvariable=Author_var)
E2.grid(row=0, column=3)

Name_var=StringVar()
E3=Entry(window,textvariable=Name_var)
E3.grid(row=1, column=1)

ISBN_var=StringVar()
E4=Entry(window,textvariable=ISBN_var)
E4.grid(row=1, column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All",width=12)
b1.grid(row=2,column=3)

b2=Button(window,text="Search",width=12)
b2.grid(row=3,column=3)

b3=Button(window,text="Add",width=12)
b3.grid(row=4,column=3)

b4=Button(window,text="Delete",width=12)
b4.grid(row=5,column=3)

b5=Button(window,text="Close",width=12)
b5.grid(row=6,column=3)


window.mainloop()
