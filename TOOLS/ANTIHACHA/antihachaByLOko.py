"""
Este programa ha sido creado por felipedelosh

Se toman todos archivos de la carpeta <nombre_archivo_partX.csv> INPUT
Todos esos archivos se van a unificar en uno solo basado en estas reglas:

Solo se van a dejar los headers del primer archivo.
Se van a eliminar los headers de los siguientes archivos y el salto de linea
EL archivo va a tener el nombre output.csv y estara en la carpeta output

"""
from email import header
from tkinter import *
import os
from os import scandir

class Software:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="Programa para Unificar reportes de excel")
        self.lblLoadStatus = Label(self.canvas, text="Por favor cargue los archivos")
        self.btnLoadArchives = Button(self.canvas, text="Load Files", command=self.loadFiles)
        self.lblSaveArchives = Label(self.canvas, text="Guardar archivos en un excel")
        self.btnSaveArvhices = Button(self.canvas, text="Save archives", command=self.saveArchive)
        self.lblFooterProgram = Label(self.canvas, text="")
        self.txtMainFooter = "This is a main Footer"

        self.reloadMainFooterText()
        self.headers = ""
        self.outputDATA = ""
        self.temp = []


        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("Antihacha by loko")
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

    def reloadMainFooterText(self):
        self.lblFooterProgram['text'] = self.txtMainFooter

    def loadFiles(self):
        files = self.rtnFolderFilesNames()
        counter = 0
        for i in files:
            path = os.getcwd() + "/TOOLS/ANTIHACHA/INPUT"
            data_of_file = self.rtnFileInfo(path+"/"+i)
            # Catching first headers of first input file 
            if counter == 0:
                self.headers = data_of_file.split("\n")[0] + "\n"

            # Caching a rich information
            self.extractInformation(data_of_file)

            counter = counter + 1

            print("Se ha cargado: ", i)

    def rtnFolderFilesNames(self):
        try:
            path = os.getcwd() + "/TOOLS/ANTIHACHA/INPUT"       
            filesNames = []
            
            for i in scandir(path):
                if i.is_file():
                    if ".csv" in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return []

    def rtnFileInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info

    def extractInformation(self, i):
        data = i.split("\n")
        lenFile = len(data)
        data = data[1:lenFile-1]
        
        self.temp = self.temp + data

    def saveArchive(self):
        path = os.getcwd() + "/TOOLS/ANTIHACHA/OUTPUT/output.csv"      
        try:

            for i in self.temp:
                self.outputDATA = self.outputDATA + i + "\n"
            f = open(path, 'w', encoding="utf-8")
            f.write(self.headers + self.outputDATA)
            f.close()
        except:
            print("Error creando el archivo: output")
        

s = Software()