from tkinter import *
from tkinter import ttk 
from tkinter import filedialog

window = Tk()
window.title('Music Window')
window.geometry("300*300")
window.configure(bg = 'LightSkyBlue')

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
     MusicWindow()
setup()

def MusicWindow():
    selectlabel = label(window, text = "Select Song", bg="LightSkyBlue",font = ("Calibri",8))
    selectlabel.place(x=2,y=1)

    listbox = listbox(window,height = 10,width = 38, activestyle = 'dotbox',bg = 'LightSkyBlue', font=("calibri",10),borderwidth=2)
    listbox.place(x=10,y=10)

    scrollbar = ScrollBar(listbox)
    scrollbar.place(relheight = 1,relx =1)
    scrollbar.config(command= list.yview)

    Playbutton = Button(window,text="Play",width = 10,bd=1,bg ='skyblue',font=("Calibri",10))
    Playbutton.place(x=30,y=200)

    Stop = Button(window,text = 'Stop',bd = 1,width = 10,bg = 'SkyBlue',font=("Calibri",10))
    Stop.place(x=200,y=200)

    Upload = Button(window,text = 'Upload',width = 10,bd=1,bg='skyblue',font=("Calibri",10))
    Upload.place(x=30,y=250)

    Download = Button(window,text='Download',width=10,bd=1,bg='skyblue',font('calibri',10))
    Download.place(x=200,y=250)

    infoLabel = Label(window,text="",fg='Blue',font=("Calibri",8))
    infoLabel.place(x=4,y=200)

    window.mainloop()
