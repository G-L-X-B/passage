import tkinter as tk
from tkinter import ttk

from generator import get_pin_code


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.master.title('passage')

        ttk.Label(self, text='Press button to create a pin code').grid(column=0, row=0)
        self.pin = tk.StringVar()
        self.pin_label = ttk.Label(self, textvariable=self.pin).grid(column=0, row=1)
        ttk.Button(self, text='Get', command=self.generate_pin_code).grid(column=0, row=2)

    def generate_pin_code(self):
        self.pin.set(get_pin_code(8))


if __name__ == '__main__':
    app = Application()
    app.mainloop()