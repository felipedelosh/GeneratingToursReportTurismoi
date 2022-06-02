"""
FelipedelosH

"""
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.controller.loadHeaders()
        self.controller.loadCities()
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Programa para generar los reportes de excel tours por ventas")
        self.lblLoadStatus = Label(self.canvas, text="Por favor cargue los archivos")
        self.btnLoadArchives = Button(self.canvas, text="Load Files", command=self.controller.loadToursFiles)
        self.lblSaveArchives = Label(self.canvas, text="Guardar archivos en un excel")
        self.btnSaveArvhices = Button(self.canvas, text="Save archives", command=self.controller.generateExcel)
        self.lblFooterProgram = Label(self.canvas, text="This is a main Footer")



        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("Program Title")
        self.screem.geometry("720x480")
        self.canvas['width'] = 720
        self.canvas['height'] = 480
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=20, y=20)
        self.lblLoadStatus.place(x=20, y=100)
        self.btnLoadArchives.place(x=20, y=120)
        self.lblSaveArchives.place(x=20, y=200)
        self.btnSaveArvhices.place(x=20, y=220)

        self.lblFooterProgram.place(x=200, y=300)

        self.screem.mainloop()




s = Software()