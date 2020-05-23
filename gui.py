#Tkinter GUI Challenge

#Setup window and import module
import tkinter as tk
root = tk.Tk()
root.geometry("565x440")
root.resizable(0, 0)
root.title("TkInter GUI Challenge - Peter Wetherall")

#Title and description
tk.Label(root, text="Gamer’s Website", fg="#388E9A", anchor="w", width=30, font="Times 20 italic bold").place(x=10, y=10)
tk.Label(root, text="Welcome to our website. In order to play our games you need to", anchor="w").place(x=10, y=60)
tk.Label(root, text="complete the registration form below.", anchor="w").place(x=10, y=80)

#Image
img = tk.PhotoImage(file="gui-image.gif")
tk.Label(root, image=img, width=100, height=100).place(x=450, y=10)

#Name inputs
tk.Label(root, text="First Name", borderwidth=1, anchor="w", relief="solid", width=15).place(x=10, y=120)
firstname = tk.Entry(root, borderwidth=1, relief="solid", width=30)
firstname.place(x=120, y=120)
tk.Label(root, text="Last Name", borderwidth=1, anchor="w", relief="solid", width=15).place(x=10, y=145)
lastname = tk.Entry(root, borderwidth=1, relief="solid", width=30)
lastname.place(x=120, y=145)

#For extracting gender values
gender = "Prefer not to say"
def male():
    global gender
    gender = "Male"
def female():
    global gender
    gender = "Female"
def neuter():
    global gender
    gender = "Prefer not to say"
    
#Radio buttons
tk.Label(root, text="Gender?").place(x=10, y=180)
male = tk.Radiobutton(root, text="Male", value=1, command=male)
female = tk.Radiobutton(root, text="Female", value=2, command=female)
neuter = tk.Radiobutton(root, text="Prefer not to say", value=3, command=neuter)
male.place(x=10, y=210)
male.deselect()
female.place(x=10, y=230)
female.deselect()
neuter.place(x=10, y=250)
neuter.select()

#For extracting games values
quizzes, dice, cards, other = False, False, False, False
def cb1():
    global quizzes
    quizzes = not quizzes
def cb2():
    global dice
    dice = not dice
def cb3():
    global cards
    cards = not cards
def cb4():
    global other
    other = not other
    
#Checkboxes
tk.Label(root, text="Which games do you like to play?").place(x=250, y=180)
tk.Checkbutton(root, text="Quizzes", command=cb1).place(x=250, y=210)
tk.Checkbutton(root, text="Dice", command=cb2).place(x=250, y=230)
tk.Checkbutton(root, text="Cards", command=cb3).place(x=250, y=250)
tk.Checkbutton(root, text="Other", command=cb4).place(x=250, y=270)

#Age slider
tk.Label(root, text="Age? (If over 30 then please choose 30)").place(x=10, y=300)
age = tk.Scale(root, from_=5, to=30, orient="horizontal", tickinterval=1, length=500)
age.place(x=10, y=320)

#On quit function
def leave():
    root.destroy()

#Compiles checkbox values into one string
def getGames():
    games = []
    if quizzes:
        games.append("Quizzes")
    if dice:
        games.append("Dice")
    if cards:
        games.append("Cards")
    if other:
        games.append("Other")
    return str(games)

#On submit function
def submit():
    print("\nForm submitted!\n")
    #Print out form values
    print("First Name: " + str(firstname.get()))
    print("Last Name: " + str(lastname.get()))
    print("Gender: " + str(gender))
    print("Games: " + getGames())
    print("Age: " + str(age.get()))
    root.destroy()

#Quit and submit buttons
tk.Button(root, text="QUIT", borderwidth=1, relief="solid", command=leave, height=2, width=12).place(x=358, y=390)
tk.Button(root, text="SUBMIT", borderwidth=1, relief="solid", command=submit, height=2, width=12).place(x=458, y=390)

#Mainloop (creates window)
root.mainloop()
