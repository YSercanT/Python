from tkinter import *
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class Timer():
    def __init__(self):
        self.window = Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.reps = 0
        self.timer = None
        self.init_body()

    def init_body(self):
        self.title_label = Label(text="Timer", fg=GREEN, bg=YELLOW)
        self.title_label.config(font=(FONT_NAME, 50, "bold"))
        self.title_label.grid(column=1, row=0)

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        self.start_button = Button(text="Start", background="white", highlightthickness=0, command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(text="Reset", background="white", highlightthickness=0, command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        self.check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
        self.check_marks.grid(column=1, row=3)

    def start_timer(self):
        self.reps += 1
        work_sec = int(WORK_MIN * 60)
        short_break_sec = int(SHORT_BREAK_MIN * 60)
        long_break_sec = int(LONG_BREAK_MIN * 60)

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.title_label.config(text="Break", fg=RED)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.title_label.config(text="Break", fg=PINK)
        else:
            self.count_down(work_sec)
            self.title_label.config(text="Work", fg=GREEN)

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.title_label.config(text="Timer", fg=GREEN)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.check_marks.config(text="")
        self.reps = 0

    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        if count_min < 10:
            count_min = f"0{count_min}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            mark = "✓" * math.floor(self.reps / 2)
            self.check_marks.config(text=mark)

    def __main__(self):
        self.count_down(0)
        self.window.mainloop()

timer_ = Timer()
timer_.__main__()
