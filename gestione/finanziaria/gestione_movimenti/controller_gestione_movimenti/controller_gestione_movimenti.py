class Controller_GestioneMovimenti():


    def __init__(self, movimenti):
        self.model = movimenti

    def get_importo_movimenti(self):
        return self.model.nome

    def get_data_movimenti(self):
        return self.model.data

    def get_causale_movimenti(self):
        return self.model.movimenti

    def set_importo_movimenti(self, importo):
        self.model.importo = importo

    def set_data_movimenti(self, data):
        self.model.data = data

    def set_causale_movimenti(self, causale):
        self.model.causale = causale