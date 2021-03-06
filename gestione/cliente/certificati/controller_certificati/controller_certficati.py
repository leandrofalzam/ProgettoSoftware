from gestione.cliente.certificati.model_certificati.model_certificati import model_certificati


class controller_certificati():

    def __init__(self):
        super(controller_certificati, self).__init__()
        self.model = model_certificati()

    def aggiungi_certificato(self, certificato):
        self.model.aggiungi_certificato(certificato)

    def get_lista_certificati(self):
        return self.model.get_lista_certificati()

    def get_certificato_by_codicefiscale(self, codicefiscale):
        return self.model.get_certificato_by_codicefiscale(codicefiscale)

    def elimina_certificato_by_codicefiscale(self, codicefiscale):
        self.model.elimina_certificato_by_codicefiscale(codicefiscale)

    def save_data(self):
        self.model.save_data()

