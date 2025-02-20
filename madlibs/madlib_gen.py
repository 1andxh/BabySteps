from tkinter import *

Screen = Tk()
Screen.title('Mad Libs Generator')
Screen.geometry('400 x 400')
Screen.config(bg='grey')
Label (Screen, text='Mad libs Generator').place(x=100, y=20)

# create buttons
story1Button = Button(Screen, text='A memorable day', font=('Times New Roman', 13), command = lambda: story1(Screen),bg='Blue')
story1Button.place(x=140, y=90)
story2Button = Button(Screen, text='Ambitions', font=('Times New roman', 13), command=lambda: story2(Screen), bg='Blue') 
story2Button.place(x=150, y=150)

Screen.update()
Screen.mainloop()

def story1(win):
    def final(tl: Toplevel, name, sports, City, playername, drinkname, snacks):
        text = f'''
                One day me and my friends {name} decided to play a {sports} game in {City}
                We wanted to watch {playername}.
                We drank {drinkname} and also ate some {snacks}
                We really enjoyed! We are looking forward to go again and enjoy'''
        
        tl.geometry(newGeometry='500x500')

        Label(tl, text='Story:',
wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl,text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
        
        NewScreen = Toplevel(win,bg='yellow')
        NewScreen.title('A memorable day')
        NewScreen.geometry('500x500')
        Label(NewScreen, text='memorable day').place(x=100, y=0)
        Label(NewScreen, text='Name:').place(x=0, y=35)
        Label(NewScreen, text='Enter a game:').place(x=0, y=70)
        Label(NewScreen, text='Enter a city:').place(x=0, y=110)
        Label(NewScreen, text='Enter name a drink:').place(x=0, y=109)


def story2():
    pass