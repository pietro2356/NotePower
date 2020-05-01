import tkinter as tk
# min: 12:17

# Classe controller
class NotePower:

    def __init__(self, master):
        master.title("Untitle - NotePower")
        master.geometry("1200x700")

        self.master = master

        self.txtArea = tk.Text(master)
        self.scroll = tk.Scrollbar(master, command=self.txtArea.yview)
        self.txtArea.configure(yscrollcommand=self.scroll.set)
        self.txtArea.pack(side=tk.LEFT)
        self.scroll.pack(side=tk.RIGHT)


if __name__ == "__main__":
    master = tk.Tk()
    pt = NotePower(master)
    master.mainloop()
