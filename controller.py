"""
FelipedelosH



"""
import os
from os import scandir
from Tour import *

class Controller:
    def __init__(self) -> None:
        self.countryINFO = {}  # {nameOfCountry : data, nameOfCountry : data ...}
        # This is a specifed header i need calculate
        self._peruCitiesNames = {}
        self.generalHeaders = ""
        self.generalHeadersOthers = ""
        self.specifed_headers = "name of tour operator|tour_distribution|pago nulo|pago aprobado|pago expirado|pago extornado|pago no procesado|pago pendiente|por pagar\n" 
        self.county_host_names = {} # To save a <ISO country>, <Name country>
        self.temporalSaveTours = {}

        

    def rtnArcheveInfo(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info


    def rtnArchieveFilesNames(self):
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

    def loadHeaders(self):
        info = self.rtnArcheveInfo("resources/headers.txt")
        for i in info.split("\n"):
            self.generalHeaders = self.generalHeaders + i + "|"
        info = self.rtnArcheveInfo("resources/headers_others.txt")
        for i in info.split("\n"):
            self.generalHeadersOthers = self.generalHeadersOthers + i + "|"

    def loadCities(self):
        info = self.rtnArcheveInfo("resources/cities_packages_peru.csv")
        info = info.split("\n")
        info = info[1:len(info)-2]
        # Save in peru cities
        for i in info:
            data = i.split("|")
            id_tour = data[0]
            id_tour = id_tour.lstrip()
            id_tour = id_tour.rstrip()
            city_of_tour = data[1]
            city_of_tour = city_of_tour.lstrip()
            city_of_tour = city_of_tour.rstrip()
            self._peruCitiesNames[id_tour] = city_of_tour

    def loadHostCountriesNames(self):
        info = self.rtnArcheveInfo("resources/paises_host.txt")
        for i in info.split("\n"):
            data = i.split("|")
            self.county_host_names[data[2]] = data[3]

    def loadToursFiles(self):
        # Load Excel info
        for i in self.rtnArchieveFilesNames():
            try:
                if i != "otros.csv":
                    print("cargando info de ...", i)

                    # Load tour information
                    info = self.rtnArcheveInfo("data/"+i)
                    # This is a calculate information
                    tourInformation = info.split("\n")
                    tourInformation = tourInformation[1:len(tourInformation)-1] # Becos .csv end to newline and not need read headers
                    for t in tourInformation:
                        # Se captura el ID
                        data = t.split("|")
                        id = data[0]
                        id = id.lstrip()
                        id = id.rstrip()

                        #Save in diccionary
                        if id not in self.temporalSaveTours.keys():
                            self.temporalSaveTours[id] = Tour()


                        # Save a general data
                        if self.temporalSaveTours[id].tour_info == "":
                            tour_data = ""
                            for x in data[0:len(data)-5]:
                                x_copy = x
                                x_copy = x_copy.lstrip()
                                x_copy = x_copy.rstrip()
                                tour_data = tour_data + x_copy + " |"
                            self.temporalSaveTours[id].tour_info = tour_data

                        #Add city info
                        if 'peru' in str(i).lower() or 'perú' in str(i).lower():
                            try:
                                self.temporalSaveTours[id].add_tour_city = self._peruCitiesNames[id]
                            except:
                                self.temporalSaveTours[id].add_tour_city = "perú"
                                print("Error en :", i, ">>", id, "No se encontro CIty... Reload info plz")

                        # Caching name of tour operator
                        name_of_tour_op = data[-3]
                        name_of_tour_op = name_of_tour_op.lstrip()
                        name_of_tour_op = name_of_tour_op.rstrip()
                        self.temporalSaveTours[id].name_tour_operator = name_of_tour_op

                        # Caching a tipe of distribution channel
                        control_is_turismoi = data[-5]
                        control_is_turismoi = control_is_turismoi.lstrip()
                        control_is_turismoi = control_is_turismoi.rstrip()
                        if control_is_turismoi == "1":
                            self.temporalSaveTours[id].is_turismoi = "Turismoi"

                        control_is_e_comerce = data[-4]
                        control_is_e_comerce = control_is_e_comerce.lstrip()
                        control_is_e_comerce = control_is_e_comerce.rstrip()
                        if control_is_e_comerce == "1":
                            self.temporalSaveTours[id].is_e_comerce = "E-Comerce" 

                        if self.temporalSaveTours[id].is_turismoi == "":
                            self.temporalSaveTours[id].sing_to_tour_distribution_separator = ""

                        if self.temporalSaveTours[id].is_turismoi == "Turismoi" and self.temporalSaveTours[id].is_e_comerce == "E-Comerce":
                            self.temporalSaveTours[id].sing_to_tour_distribution_separator = " - "


                        # Cathcing a tipe of payment
                        payment_state = data[-2]
                        payment_state = payment_state.lstrip()
                        payment_state = payment_state.rstrip()

                        if payment_state == "NULL":
                            self.temporalSaveTours[id].pago_nulo = self.temporalSaveTours[id].pago_nulo + 1

                        if payment_state == "pago aprobado":
                            self.temporalSaveTours[id].pago_aprobado = self.temporalSaveTours[id].pago_aprobado + 1

                        if payment_state == "pago expirado":
                            self.temporalSaveTours[id].pago_expirado = self.temporalSaveTours[id].pago_expirado + 1

                        if payment_state == "pago extornado":
                            self.temporalSaveTours[id].pago_extornado = self.temporalSaveTours[id].pago_extornado + 1

                        if payment_state == "pago no procesado":
                            self.temporalSaveTours[id].pago_no_procesado = self.temporalSaveTours[id].pago_no_procesado + 1

                        if payment_state == "pago pendiente":
                            self.temporalSaveTours[id].pago_pendiente = self.temporalSaveTours[id].pago_pendiente + 1

                        if payment_state == "por pagar":
                            self.temporalSaveTours[id].por_pagar = self.temporalSaveTours[id].por_pagar + 1


                    self.saveTourDataInCountry(i, self.temporalSaveTours)
                    self.temporalSaveTours = {} # ReStart


                else:
                    print("Estoy en otros")
                    # This is a calculate information
                    self.loadHostCountriesNames()

                    info = self.rtnArcheveInfo("data/"+i)
                    
                    self.loadHostCountriesNames()

                    tourInformation = info.split("\n")
                    tourInformation = tourInformation[1:len(tourInformation)-1]

                    for t in tourInformation:
                        # Se captura el ID
                        data = t.split("|")
                        id = data[0]
                        # Se captura el pais
                        pais = data[3]
                        pais = pais.lstrip()
                        pais = pais.rstrip()

                        # Se captura el pais
                        pais = self.county_host_names[pais]


                        #Save in diccionary
                        if pais not in self.temporalSaveTours.keys():
                            self.temporalSaveTours[pais] = {}
                            self.temporalSaveTours[pais][id] = Tour()
                        else:
                            self.temporalSaveTours[pais][id] = Tour()

                        # Save a general data
                        if self.temporalSaveTours[pais][id].tour_info == "":
                            tour_data = ""
                            for x in data[0:len(data)-5]:
                                x_copy = x
                                x_copy = x_copy.lstrip()
                                x_copy = x_copy.rstrip()
                                tour_data = tour_data + x_copy + "|"
                            self.temporalSaveTours[pais][id].tour_info = tour_data

                        # Caching name of tour operator
                        name_of_tour_op = data[-3]
                        name_of_tour_op = name_of_tour_op.lstrip()
                        name_of_tour_op = name_of_tour_op.rstrip()

                        self.temporalSaveTours[pais][id].name_tour_operator = name_of_tour_op

                        # Caching a tipe of distribution channel        
                        is_turismoi = data[-5]
                        is_turismoi = is_turismoi.lstrip()
                        is_turismoi = is_turismoi.rstrip()
                        if is_turismoi == "1":
                            self.temporalSaveTours[pais][id].is_turismoi = "Turismoi"

                        is_e_comerce = data[-4]
                        is_e_comerce = is_e_comerce.lstrip()
                        is_e_comerce = is_e_comerce.rstrip()
                        if is_e_comerce  == "1":
                            self.temporalSaveTours[pais][id].is_e_comerce = "E-Comerce" 

                        if self.temporalSaveTours[pais][id].is_turismoi == "":
                            self.temporalSaveTours[pais][id].sing_to_tour_distribution_separator = ""

                        if self.temporalSaveTours[pais][id].is_turismoi == "Turismoi" and self.temporalSaveTours[pais][id].is_e_comerce == "E-Comerce":
                            self.temporalSaveTours[pais][id].sing_to_tour_distribution_separator = " - "

                        # Cathcing a tipe of payment
                        payment_state = data[-2]
                        payment_state = payment_state.lstrip()
                        payment_state = payment_state.rstrip()

                        if payment_state == "NULL":
                            self.temporalSaveTours[pais][id].pago_nulo = self.temporalSaveTours[pais][id].pago_nulo + 1

                        if payment_state == "pago aprobado":
                            self.temporalSaveTours[pais][id].pago_aprobado = self.temporalSaveTours[pais][id].pago_aprobado + 1

                        if payment_state == "pago expirado":
                            self.temporalSaveTours[pais][id].pago_expirado = self.temporalSaveTours[pais][id].pago_expirado + 1

                        if payment_state == "pago extornado":
                            self.temporalSaveTours[pais][id].pago_extornado = self.temporalSaveTours[pais][id].pago_extornado + 1

                        if payment_state == "pago no procesado":
                            self.temporalSaveTours[pais][id].pago_no_procesado = self.temporalSaveTours[pais][id].pago_no_procesado + 1

                        if payment_state == "pago pendiente":
                            self.temporalSaveTours[pais][id].pago_pendiente = self.temporalSaveTours[pais][id].pago_pendiente + 1

                        if payment_state == "por pagar":
                            self.temporalSaveTours[pais][id].por_pagar = self.temporalSaveTours[pais][id].por_pagar + 1
                        
                        
                
                    self.saveTourDataInCountryOfOthers(self.temporalSaveTours)
                    self.temporalSaveTours = {} # ReStart

            except:
                print("Error en el archivo: ", i)

    def saveTourDataInCountry(self, country, data):
        key = country.replace(".csv", "")
        info = self.generalHeaders + self.specifed_headers
        
        for w in data:
            info = info + data[w].toString() + "\n"

        if key not in self.countryINFO.keys():
            self.countryINFO[key] = info

    def saveTourDataInCountryOfOthers(self,data):
        for w in data:
            for y in data[w]:
                if w not in self.countryINFO:
                    temp = self.generalHeadersOthers + self.specifed_headers
                    temp = temp + data[w][y].toString() + "\n"
                    self.countryINFO[w] = temp
                else:
                    temp = self.countryINFO[w]
                    temp = temp + data[w][y].toString() + "\n"
                    self.countryINFO[w] = temp


        
    

    def generateExcel(self):
        for i in self.countryINFO.keys():
            try:
                f = open("output/"+i+".csv", 'w', encoding="utf-8")
                f.write(self.countryINFO[i])
                f.close()
            except:
                print("Error creando el archivo: "+i)
