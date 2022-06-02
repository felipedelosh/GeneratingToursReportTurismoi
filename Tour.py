class Tour:
    def __init__(self) -> None:
        self.tour_info = "" # This is a general information of tour: id, name, slug....
        self.name_tour_operator = ""
        self.is_turismoi = ""
        self.is_e_comerce = ""
        self.sing_to_tour_distribution_separator = " "
        self.pago_nulo = -1
        self.pago_aprobado = 0
        self.pago_expirado = 0
        self.pago_extornado = 0
        self.pago_no_procesado = 0
        self.pago_pendiente = 0
        self.por_pagar = 0
        # Added
        self.add_tour_city = "NULL"


    def toString(self):
        return self.tour_info + self.add_tour_city + " |" + self.name_tour_operator + " |" + self.is_turismoi + self.sing_to_tour_distribution_separator + self.is_e_comerce + " |" + str(self.pago_nulo) + " |" + str(self.pago_aprobado) + " |" + str(self.pago_expirado) + " |" + str(self.pago_extornado) + " |" + str(self.pago_no_procesado) + " |" + str(self.pago_pendiente) + " |" + str(self.por_pagar)