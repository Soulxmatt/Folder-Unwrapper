import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
#util
from shutil import move as shmove
from os import getcwd, listdir,remove

WIDTH=800
HEIGHT=180
TITLE="Folder Unwrapper"
class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        botton_colors=[
            {
                "bg":"#ede2e1",
                "fg":"#000000"
            },
            {
                "bg":"#fa0000",
                "fg":"#ffffff"
            },
            {
                "bg":"#0000fa",
                "fg":"#ffffff"
            },
            {
                "bg":"#00ff00",
                "fg":"#ffffff"
            }
            ]
        self.srcbox=ttk.Entry(width=100)
        self.dstbox=ttk.Entry(width=97)

        self.srcbotton=tkinter.Button(self,text="examinate",width=13,height=1,bg=botton_colors[0]["bg"],fg=botton_colors[0]["fg"],command=self.get_src)
        self.dstbotton=tkinter.Button(self,text="examinate",width=13,height=1,bg=botton_colors[0]["bg"],fg=botton_colors[0]["fg"],command=self.get_dst)

        self.unwrappbutton=tkinter.Button(self,text="unwrap",width=13,height=1,bg=botton_colors[0]["bg"],fg=botton_colors[0]["fg"],command=self.unwrapp)

        self.src_label=tkinter.Label(self,text="Source:")
        self.dst_label=tkinter.Label(self,text="Destination:")

        self.srcbox.place(x=60, y=10)
        self.dstbox.place(x=80,y=50)

        self.srcbotton.place(x=677,y=10)
        self.dstbotton.place(x=677, y=50)
        self.unwrappbutton.place(x=600,y=100)

        self.src_label.place(x=2,y=10)
        self.dst_label.place(x=2,y=50)

#       TEST
#       self.srcbox.insert(0,r"C:\Users\Soulx\Desktop\Codigos Propios\Python Projects\Folder Unwrapper\Nueva carpeta")
#       self.dstbox.insert(0,r"C:\Users\Soulx\Desktop\Codigos Propios\Python Projects\Folder Unwrapper")
        
#       configuraciones de la GUI
        self.title(TITLE)
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)
        #self.iconbitmap("Source/icon.ico
    def get_src(self):
        dir_path=filedialog.askdirectory(initialdir=getcwd(),title="Select Directory")
        self.srcbox.delete(0, tkinter.END)
        self.srcbox.insert(0,dir_path)
    def get_dst(self):
        dir_path=filedialog.askdirectory(initialdir=getcwd(),title="Select Directory")
        self.dstbox.delete(0, tkinter.END)
        self.dstbox.insert(0,dir_path)
    def unwrapp(self):
        src=self.srcbox.get()
        dst=self.dstbox.get()
        unwrapp(src,dst)
        messagebox.showerror(title="Unwrapping Finished Succesfully",message=f"All files has been unwrapped sucessfully")
def unwrapp(src,dst):
    folder_list=[i for i in listdir(src) if "." not in i]
    file_list=[i for i in listdir(src) if "." in i]
    for i in file_list:
        shmove(f"{src}/{i}",f"{dst}/{i}")
    for i in folder_list:
        try:
            unwrapp(f"{src}/{i}",dst)
        except:
            pass

if __name__=="__main__":
    window=App()
    #window.state('zoomed')
    window.mainloop()