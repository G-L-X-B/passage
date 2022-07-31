import tkinter as tk
from tkinter import ttk

from generator import get_pin_code


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.master.title('passage')

        ttk.Label(self, text='Number of digits: ').grid(column=0, row=0)
        self.pin_len = ttk.Spinbox(self, from_=4, to=16, increment=1, width=3, validate='all', validatecommand=self.validate_pin_len)
        self.pin_len.set('8')
        self.pin_len.grid(column=1, row=0)
        self.pin = tk.StringVar()
        ttk.Label(self, textvariable=self.pin).grid(column=0, row=1)
        ttk.Button(self, text='Copy', command=self.copy_pin_code).grid(column=1, row=1)
        ttk.Button(self, text='Generate', command=self.generate_pin_code).grid(column=1, row=2)

    def validate_pin_len(self):
        return 4 > int(self.pin_len.get()) < 16

    def generate_pin_code(self):
        self.pin.set(get_pin_code(int(self.pin_len.get())))
    
    def copy_pin_code(self):
        if len(self.pin.get()) != 0:
            self.clipboard_clear()
            self.clipboard_append(self.pin.get())


if __name__ == '__main__':
    app = Application()
    app.mainloop()