import tkinter as tk
from PIL import ImageTk, Image
import os
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.path = os.getcwd()


    def create_widgets(self):
        self.cat = tk.Button(self)
        self.cat['text'] = 'Cat pics'
        self.cat['command'] = self.cat_gen
        self.cat.pack(fill = 'x',side = 'left')

        self.dog = tk.Button(self)
        self.dog['text'] = 'Dog pics'
        self.dog['command'] = self.dog_gen
        self.dog.pack(fill = 'x',side = 'left')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def create_window(self, img):
        print(img)
        t = tk.Toplevel(self)
        t.wm_title("Happiness here")
        print(self.path +'/'+ str(img))
        
        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img_temp = ImageTk.PhotoImage(Image.open(self.path + str(img)).resize((300,300)))
        print(img_temp)
        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(t, image = img_temp)
        panel.image = img_temp
        panel.place(x=0, y=0)

        t.after(3000, lambda: t.destroy())


    def dog_gen(self):
        os.system('python dog.py')
        for dog in os.listdir(self.path + '/dogs'):
            self.create_window('/dogs/' + dog)
            time.sleep(1)



    def cat_gen(self):
        os.system('python cat.py')
        for cat in os.listdir(self.path + '/cats'):
            self.create_window('/cats/' + cat)
            time.sleep(1)



root = tk.Tk()
root.geometry('500x500')
app = Application(master=root)
app.mainloop()