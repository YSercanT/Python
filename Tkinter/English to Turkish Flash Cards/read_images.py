from tkinter import PhotoImage
import os

class Read_Images():
    @staticmethod
    def convert( file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(current_dir, "images", file)
        card_img = PhotoImage(file=filename)
        print(filename)
        return card_img