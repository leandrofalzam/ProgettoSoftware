import unittest

from gestione.amministrazione.GestioneDipendenti.controller_GestioneDipendenti.Controller_GestioneDipendenti import \
    Controller_GestioneDipendenti
from gestione.amministrazione.GestioneDipendenti.model_GestioneDipendenti.model_GestioneDipendenti import \
    GestioniDipendente
from gestione.amministrazione.dipendenti.controller_dipendenti.controller_dipendenti import Controller_Dipendenti


class Test(unittest.TestCase):
    def setUp(self):
        self.controller_listadipendenti = Controller_Dipendenti()
        self.dipendente = GestioniDipendente("Filippo", "Caterbetti","Macerata", "13/04/2000", "1234567891234567","indeterminato", "addetto alle pulizie","99999", "1500")
        self.model_lista_dipendenti = self.controller_listadipendenti.get_lista_dipendenti()
        self.controller_listadipendenti.aggiungi_dipendente(self.dipendente)

    def test_aggiungi_dipendente(self):
        self.assertIsNotNone(self.dipendente.id)
        self.controller_listadipendenti.aggiungi_dipendente(self.dipendente)
        self.assertTrue(self.dipendente in self.model_lista_dipendenti)

    def test_elimina_dipendente_by_id(self):
        self.assertIsNotNone(self.model_lista_dipendenti)
        self.controller_listadipendenti.elimina_dipendente_by_id(self.dipendente.id)
        self.assertTrue(self.dipendente not in self.model_lista_dipendenti)

    def test_get_dipendente_by_id(self):
        self.assertIsNone(self.controller_listadipendenti.get_dipendente_by_id("33333"))
        self.assertIsNotNone(self.controller_listadipendenti.get_dipendente_by_id("99999"))

    def test_get_lista_dipendenti(self):
        self.assertNotEqual(self.controller_listadipendenti.get_lista_dipendenti(),[])