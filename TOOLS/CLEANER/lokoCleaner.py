"""
Programa creado por felipedelosh

ingresa un texto y le quita todas las etiquetas html (trash.txt)
y las cambia por un espacio en blanco

programar proximamente...
"""
import os
from os import scandir
from tkinter import *

class Software:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem)
        self.lblBannerProgram = Label(self.canvas, text="This is a program to clean archive")
        self.lblLOADFILE    = Label(self.canvas, text="LOAD FILE")
        self.btnLoadFile = Button(self.canvas, text="LOAD", command=self.loadFiles)
        self.lblChargeFiles = Label(self.canvas, text=".")
        self.lblFooterProgram = Label(self.canvas, text="This is a main Footer")
        self.lblCleanInfo = Label(self.canvas, text="Clean data")
        self.btnCleanData = Button(self.canvas, text="clean DATA", command=self.cleanData)
        self.filesINFO = {}

        # Charge a trash
        self.trash = self.loadTrash()
        print("Se limpiara la siguiente basura: \n")    
        print(self.trash)

        self.vizualizedAndRun()


    def vizualizedAndRun(self):
        self.screem.title("Program Title")
        self.screem.geometry("720x480")
        self.canvas['width'] = 720
        self.canvas['height'] = 480
        self.canvas['bg'] = "snow"
        self.canvas.place(x=0, y=0)
        self.lblBannerProgram.place(x=20, y=20)
        self.lblFooterProgram.place(x=200, y=450)
        self.lblLOADFILE.place(x=100, y=80)
        self.btnLoadFile.place(x=100, y=120)
        self.lblChargeFiles.place(x=300, y=10)
        self.lblCleanInfo.place(x=100, y=200)
        self.btnCleanData.place(x=100, y=220)

        self.screem.mainloop()

    def loadTrash(self):
        try:
            trash = []
            f = open("trash.txt", 'r', encoding="utf-8")
            for i in f.read().split("\n"):
                if str(i).strip != "":
                    trash.append(i)

            return trash
        except:
            return ["\"", "<hr>", "<br>", "&nbsp;", "<ol>", "<ul>", "<li>", "<u>", "<b>", "<p>", "<a>", "</ol>", "</ul>", "</li>", "</u>", "</b>", "</p>", "</a>"]

    def loadFiles(self):
        files = self.rtnFilesNames()
        if len(files) > 0:
            # Put labels
            outputText = ""
            for i in files:
                outputText = outputText + i
            self.lblChargeFiles['text'] = outputText

            # Save info
            for i in files:
                data = self.rtnArcheveInfo("data/"+i)
                # save in dictionary
                self.filesINFO[str(i)] = data

        print("Cargada la siguinte info...\n", outputText)


    def cleanData(self):
        for i in self.filesINFO:
            print("limpiando...", i)

            for j in self.trash:
                self.filesINFO[i] = str(self.filesINFO[i]).replace(j, ' ')

            print("Limpiado el archivo: ", i)

        self.saveAllFiles()
        


    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info


    def rtnFilesNames(self):
        """
        Return all files names of data folder
        """
        try:
            path = os.getcwd() + "/data/"
            
            filesNames = []
            
            for i in scandir(path):
                if i.is_file():
                    if ".csv" in i.name:
                        filesNames.append(i.name)

            return filesNames
        except:
            return []

    def saveAllFiles(self):
        for i in self.filesINFO:
            try:
                f = open("output/"+i, 'w', encoding="utf-8")
                f.write(self.filesINFO[i])
                f.close()
            except:
                print("Error Guardando...", i)





s = Software()
