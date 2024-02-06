import Read_Data
from tkinter import *
from  read_images import Read_Images
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"


class Game():
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50,pady=50 ,bg=BACKGROUND_COLOR)
        self.canvas=Canvas(width=800,height=526)
        self.read_csv()
        self.build_the_canvas()
    def read_csv(self):
        self.rd=Read_Data.read_file("1000_words.csv")
        self.rd.condition()
        self.to_learn=self.rd.to_learn
        #print(len(self.rd.df))
    def read_images(self):
        card_front_img=Read_Images.convert("card_front.png")
        card_back_img=Read_Images.convert("card_back.png")
        card_right_img=Read_Images.convert("right.png")
        card_wrong_img=Read_Images.convert("wrong.png")
        return card_front_img,card_back_img,card_right_img,card_wrong_img
    def flip_the_card(self):
        self.canvas.itemconfig(self.language,text="Türkçe",fill="white")
        self.canvas.itemconfig(self.card_word,text=self.curr["Turkish"],fill="white")
        self.canvas.itemconfig(self.card_background,image=self.card_back)

    def next_card(self):
        self.curr=random.choice(self.to_learn)
        self.window.after_cancel(self.flip_timer)

        self.canvas.itemconfig(self.language,text="English",fill="black")
        self.canvas.itemconfig(self.card_word,text=self.curr["English"],fill="black")
        self.canvas.itemconfig(self.card_background,image=self.card_front)
        self.flip_timer=self.window.after(3000,self.flip_the_card)

    def is_known(self): 
        self.to_learn.remove(self.curr)
        self.next_card()
        data=pd.DataFrame(self.to_learn)
        self.rd.data_to_csv(data)
        #print(len(data))
    def build_the_canvas(self):
        self.flip_timer=self.window.after(3000,self.flip_the_card)
        self.card_front,self.card_back,self.right,self.wrong=self.read_images()
        self.canvas.grid(row=0,column=0,columnspan=2)
        self.canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
        self.card_background=self.canvas.create_image(400,263,image=self.card_front)
        self.language=self.canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
        self.card_word=self.canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
        self.unknown_button = Button(image=self.wrong,command=self.next_card)
        self.unknown_button.grid(column=0,row=1)
        self.unknown_button.config(highlightthickness=0)
        self.check_button = Button(image=self.right,command=self.is_known)
        self.check_button.config(highlightthickness=0)
        self.check_button.grid(column=1,row=1)
        self.next_card()



    def __main__(self):
        self.window.mainloop()
    def destroy(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        self.window.destroy() 
