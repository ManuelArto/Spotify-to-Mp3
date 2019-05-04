import tkinter as tk
from PIL import Image
from PIL import ImageTk

HEIGHT = 500
WIDTH = 1000


class View:

    def __init__(self, start):
        root = tk.Tk()
        # root.attributes("-fullscreen", True)

        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        background = tk.Label(root, bg='black')
        background.place(relheight=1, relwidth=1)

        img = Image.open("./IMG/spotify_icon.png")
        img = img.resize((int(WIDTH/6), int(WIDTH/6)), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(img)
        background_image = ImageTk.PhotoImage(img)
        background_label = tk.Label(root, image=background_image, bg='black')
        background_label.place(anchor='nw')

        frame1 = tk.Frame(root, bg='black', bd=3)
        frame1.place(relx=0.58, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        entry = tk.Entry(frame1, font=40)
        entry.place(relwidth=0.65, relheight=1)

        button = tk.Button(frame1, text="Start", font=40, command=lambda: start(entry.get()))
        button.place(relx=0.7, relheight=1, relwidth=0.3)

        lower_frame = tk.Frame(root, bg='#05B039', bd=3)
        lower_frame.place(relx=0.58, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        self.songs = tk.Label(lower_frame)
        self.songs.place(relwidth=0.33, relheight=1)
        self.links = tk.Label(lower_frame)
        self.links.place(relx=0.34, relwidth=0.33, relheight=1)
        self.download = tk.Label(lower_frame)
        self.download.place(relx=0.68, relwidth=0.32, relheight=1)

        root.mainloop()

