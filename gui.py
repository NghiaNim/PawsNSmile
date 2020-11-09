import tkinter as tk
from PIL import ImageTk, Image
import os
import time
import random
path = os.getcwd()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.dog_list = []
        self.cat_list = []
        self.all = []



    def create_widgets(self):
        self.cat = tk.Button(self)
        self.cat['text'] = 'Generate cats'
        self.cat['command'] = self.cat_gen
        self.cat.pack(fill = 'x',side = 'left')

        self.dog = tk.Button(self)
        self.dog['text'] = 'Generate dogs'
        self.dog['command'] = self.dog_gen
        self.dog.pack(fill = 'x',side = 'left')

        self.dog_pics = tk.Button(self, text = 'sample dog', command = lambda: self.create_window(self.dog_list[-1]))

        self.dog_pics.pack(fill = 'x',side = 'right')

        self.cat_pics = tk.Button(self, text = 'sample cat', command = lambda: self.create_window(self.cat_list[-1]))

        self.cat_pics.pack(fill = 'x',side = 'right')

        self.allbut = tk.Button(self, text = 'random cat/dog', command = lambda: self.create_window(self.all[-1]))

        self.allbut.pack(fill = 'x',side = 'right')

        self.timer = tk.Button(self, text = 'Set timer', command = self.timing)

        self.timer.pack(fill ='x', side = 'bottom')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        

    def timing(self):

        self.t = tk.Toplevel(self)
        self.butt1 =tk.Button(self.t, text = '5 minutes', command = lambda: self.set_time(300))
        self.butt1.pack(fill = 'x',side = 'right')
        self.butt2 =tk.Button(self.t, text = '10 minutes', command = lambda: self.set_time(600))
        self.butt2.pack(fill = 'x',side = 'right')
        self.butt3 =tk.Button(self.t, text = '15 minutes', command = lambda: self.set_time(900))
        self.butt3.pack(fill = 'x',side = 'right')
        self.butt4 =tk.Button(self.t, text = '20 minutes', command = lambda: self.set_time(1200))
        self.butt4.pack(fill = 'x',side = 'right')
        self.butt5 =tk.Button(self.t, text = 'custom', command = lambda: self.set_time(int(input('What time do you want?'))))
        self.butt5.pack(fill = 'x',side = 'right')     

        
        
    def set_time(self,time):
        self.after(time*1000, lambda: self.allbut.invoke())


    
    def create_window(self, img):
        t = tk.Toplevel(self)
        t.wm_title("Happiness here")
        print(path +'/'+ str(img))
        
        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img_temp = ImageTk.PhotoImage(Image.open(path + str(img)).resize((300,300)))
        # print(img_temp)
        # #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        # panel = tk.Label(t, image = img_temp)
        # panel.image = img_temp
        # panel.place(x=0, y=0)

        
        label = tk.Label(t,image=img_temp)
        label.image = img_temp # keep a reference!
        label.pack()
        t.after(3000, lambda: t.destroy())


        if len(self.dog_list) > 0 and len(self.cat_list) == 0:
            self.dog_list.pop()
        elif len(self.cat_list) > 0 and len(self.dog_list) == 0:
            self.cat_list.pop()
        else:
            self.all.pop()



    def dog_gen(self):
        os.system('python dog.py')

        for dog in os.listdir(path + '/dogs'):
            self.dog_list.append('/dogs/' + dog)
            self.all.append('/dogs/' + dog)

        random.shuffle(self.all)
        
    



    def cat_gen(self):
        os.system('python cat.py')

        for cat in os.listdir(path + '/cats'):
            self.cat_list.append('/cats/' + cat)
            self.all.append('/cats/' + cat)

        random.shuffle(self.all)



root = tk.Tk()
root.geometry('500x500')
app = Application(master=root)
app.mainloop()