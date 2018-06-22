
from tkinter import *

#key down function
def click():
    entered_text=textentry.get() #this will collect the text from the text entry box
    output.delete(0.0, END)
    try:
        Definition = my_compdictn[entered_text]
    except:
        Definition = 'Sorry there is no word like that, please try another word'
    output.insert(END, Definition)

#Main workings :
window = Tk()
window.title('My Words glossory')
window.configure(background= "black")


## My photo
photo1 = PhotoImage(file = 'glosorry.gif')
Label (window, image=photo1, bg = 'black') .grid(row=0, column=0, sticky=E)

#Create label
Label (window, text= 'Enter the word you would like a definition for:', bg='black', fg='yellow', font='none 12 bold') .grid(row=1, column=0, sticky=W)

#create a text entry box
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2,column=0, sticky=W)

#creat a submit button
Button(window, text='SUBMIT', width=6, command=click) .grid(row=3, column=0, sticky=W)

#create another label
Label (window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold') .grid(row=4, column=0, sticky=W)


#create a text box
output = Text(window, width=75, height=6, wrap=WORD, background= 'white')
output.grid(row=5, column=0, sticky=W)

#the dictionary
my_compdictn = {'algorithm':'step by step instructions to complete a task', 'bug': 'piece of code that cause a program to fail',\
            'school': 'A place where students go for learning', 'church': ' A place believers for for worship of God, especially christians',\
            'house': 'A building where a family or group of people stay',\
            'food': 'A meal eaten by people for nurishment'}

#Exit label
Label(window, text='click to exit:', bg='black', fg='white', font='none 12 bold') .grid(row=6, column=0, sticky=W)

#Exit function
def close_window():
    window.destroy()
    exit()


#Exit button
Button(window, text='EXIT', width=14, command=close_window) .grid(row=7, column=0, sticky=W)

#return main loop


window.mainloop()
