import sqlite3 as sq
import tkinter as tk
from tkinter import ttk
from datetime import date

db = sq.connect("employee_data.db")
cursor = db.cursor()
cmd1 = ('''CREATE TABLE IF NOT EXISTS EMPLOYEE
(ID,NAME,DOB,GENDER,CITY)
''')

cursor.execute(cmd1)

#cursor.execute('''INSERT INTO EMPLOYEE (ID,NAME,DOB,GENDER,CITY) VALUES("1","Prem","16/04/1995","Male","Hyderabad")''')
#j = cursor.execute('SELECT ID,NAME,DOB,GENDER,CITY FROM EMPLOYEE').fetchall()
k = cursor.execute('SELECT CITY FROM EMPLOYEE').fetchall()
#cursor.execute('''DELETE FROM EMPLOYEE WHERE ID='1' ''')
#cursor.execute('''UPDATE EMPLOYEE SET DOB = '18/03/1991' WHERE ID='8' ''')
db.commit()
k = set(k)
a = []

for i in k:
    k = cursor.execute(f'SELECT DOB FROM EMPLOYEE WHERE CITY=?',(i)).fetchall()
    p = 0
    for p in range(len(k)):
        h = k[p][0]
        p = p+1
        d = int(h[0:2])
        m = int(h[3:5])
        y = int(h[6:10])
        today = date.today()
        age = today.year - y -((today.month, today.day) <(m, d))
        a.append([i,age])
b = []
i = 0
h = []
for i in range(len(a)):
    y = a[i]
    count = a.count(y)
    b.append([y,count])
for i in range(len(a)):
    y = b[i][0][0][0]
    j = b[i][0][1]
    k = b[i][1]
    l = [y,j,k]
    h.append(l)
print(h)
b = []
for i in h:
    if i not in b:
        b.append(i)
    else:
        pass
print(b)

# root = tk.Tk() 
# root.title("Event Remainder App")
# root.geometry("800x400+50+50")

# tree = ttk.Treeview(column=("c1", "c2", "c3"), show='headings')

# tree.column("#1", anchor=tk.CENTER)

# tree.heading("#1", text="CITY")

# tree.column("#2", anchor=tk.CENTER)

# tree.heading("#2", text="AGE")

# tree.column("#3", anchor=tk.CENTER)

# tree.heading("#3", text="Num of Employees")

# tree.place(x=0,y=0,height=350,width=800)

# style = ttk.Style(root)
# # set ttk theme to "clam" which support the fieldbackground option
# style.theme_use("clam")
# style.configure("Treeview", font =("arial",15,"bold") )


# root.mainloop()