import tkinter as tk
from tkinter import*
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import Saves
import Sortear

root = tk.Tk()
root.title("Sorteador")
root.iconbitmap('Times/champions.ico')
width=750
height=500
root.geometry(str(width) + "x" + str(height))

teamsDic = {}
teamsDic = Saves.TeamsDic
teamsList = []
teamsList = Saves.TeamsList

gframes = []
grupos = []

letras=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
images = []

sorteio_frame = tk.Frame(root, bg='gray96')

def ShowGrupos():
    for i in range(8):
        gruponome = tk.Label(gframes[i], text=str("Grupo "+ str(letras[i])), bg="gray10", fg="white",
                            font=("Helvetica", 10, 'bold'), anchor='center', pady=1)
        gruponome.grid(row=0, column=0, columnspan=2, sticky='w'+'e'+'n')
        for j in range(4):
            timenome = tk.Label(gframes[i], text=str(grupos[i][j]), bg="gray97",
            font=("Helvetica", 10, 'bold'), anchor='w', pady=10)
            timenome.grid(row=j+1, column=0, sticky='w')

            escudooriginal = Image.open(teamsDic[grupos[i][j]].escudo).resize((40, 40), Image.ANTIALIAS)
            escudo = ImageTk.PhotoImage(escudooriginal)
            images.append(escudo)
            timeescudo = tk.Label(gframes[i], image=escudo, bg='gray97')
            timeescudo.grid(row=j+1, column=1, sticky='e')
    for f in gframes:
        f.grid_propagate(False)
        f.grid_columnconfigure(0, weight=1)
        f.grid_columnconfigure(1, weight=1)
        for i in range(4): f.grid_rowconfigure(i+1, weight=1)

    for i in range(4): tk.Grid.columnconfigure(sorteio_frame, index=i, weight=1)
    for i in range(2): tk.Grid.rowconfigure(sorteio_frame, index=i+1, weight=1)
    sorteio_frame.mainloop()
padx = 5
pady = 10
def MakeFrames():
    for x in range(8):
        if x <= 3:
            gframe = tk.Frame(sorteio_frame, bg = 'gray97', height=(height/2 - 2*pady), width=(width/4 - 2*padx)
                              , relief='solid', borderwidth=2)
            gframe.grid(row=1, column=x, padx=padx, pady=pady, sticky='nsew')
            gframes.append(gframe)

        else:
             gframe = tk.Frame(sorteio_frame, bg = 'gray97', height=(height/2 - 2*pady), width=(width/4 - 2*padx)
                               , relief='solid', borderwidth=2)
             gframe.grid(row=2, column=(x-4), padx=padx, pady=5, sticky='nsew')
             gframes.append(gframe)

def Draw():
    try:
        Sortear.Sortear()
    except:Sortear.Sortear()
    sorteio_frame.pack(fill='both', expand=1)
    global grupos
    grupos = Sortear.grupos
    gframes.clear()
    MakeFrames()
    ShowGrupos()

DrawAgain = tk.Button(sorteio_frame, padx=30, pady=10, text="Sortear novamente", border=1,command=Draw, relief='solid', borderwidth=3)
DrawAgain.grid(row=0, column=0, columnspan=4)

Draw()