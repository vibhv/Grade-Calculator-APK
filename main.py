import tkinter
from tkinter import *
from tkinter import font

root = Tk()
root.title("GRADE CALCULATOR")
root.geometry("500x400")

def marks_calculate():
    physics = int(physics_value.get())
    chemistry = int(chemistry_value.get())
    maths = int(maths_value.get())
    final =(physics+chemistry+maths)
    Label(text=f"{final}",font="arial 20 bold").place(x=250,y=170)

    percentage = float((final/300)*100)
    Label(text=f"{percentage}",font="arial 20 bold").place(x=250,y=220)
    
    if(percentage>36):
        grade_scored ="PASS"
    else:
        grade_scored="FAIL"

    Label(text=f"{grade_scored}",font="arial 20 bold").place(x=250,y=270)

sub_1 =Label(root,text="Physics",font="arial 20")
sub_1.place(x=50,y=20)

sub_2 =Label(root,text="Chemistry",font="arial 20")
sub_2.place(x=50,y=70)

sub_3 =Label(root,text="Maths",font="arial 20")
sub_3.place(x=50,y=120)

total_marks =Label(root,text="Total",font="arial 20")
total_marks.place(x=50,y=170)

percentage_marks =Label(root,text="Percentage",font="arial 20")
percentage_marks.place(x=50,y=220)

grade_scored =Label(root,text="Grades",font="arial 20")
grade_scored.place(x=50,y=270)

physics_marks = StringVar()
chemistry_marks = StringVar()
maths_marks = StringVar()

physics_value = Entry(root,textvariable =physics_marks ,font="arial 20",width=50)
physics_value.place(x=250,y=20)

chemistry_value = Entry(root,textvariable =chemistry_marks ,font="arial 20",width=50)
chemistry_value.place(x=250,y=70)

maths_value = Entry(root,textvariable =maths_marks ,font="arial 20",width=50)
maths_value.place(x=250,y=120)

Button(text="calculate",font="arial 15",bg="green",bd=5,command=marks_calculate).place(x=50,y=330)

Button(text="Exit",font="arial 15",bg="red",bd=5,width=8,command=lambda: exit()).place(x=350,y=330)


root.mainloop()
