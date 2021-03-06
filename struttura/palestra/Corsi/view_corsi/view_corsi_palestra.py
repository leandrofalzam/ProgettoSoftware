
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtWidgets import QGridLayout, QCalendarWidget


from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont
from datetime import datetime

from PyQt5 import QtGui, QtCore

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from struttura.palestra.Corsi.corsiPalestra.view_corsi_palestra.view_mostra_tutti_corsi_palestra import \
    view_mostra_tutti_corsi_palestra
from struttura.palestra.Corsi.view_corsi.view_day_corsi_palestra import view_day_corsi_palestra


class view_corsi_palestra(QWidget):

    def __init__(self, parent=None):
        super(view_corsi_palestra, self).__init__(parent)

        self.g_layout = QGridLayout()

        self.label_prenotazioni_by_data = QLabel("\nSeleziona una data per visualizzare i dettagli di quel giorno, cliccando Mostra giorno,\nAltrimenti clicca Mostra tutte per visualizzare tutti i corsi di oggi e futuri: \n")
        self.label_prenotazioni_by_data.setFont(QFont("Yu Gothic UI Light", 12))
        self.g_layout.addWidget(self.label_prenotazioni_by_data, 0, 0)

        self.calendario = QCalendarWidget()
        self.calendario.setGridVisible(True)
        self.calendario.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendario.setMinimumDate(QDate(2021, 5, 1))


        data_di_oggi = QTextCharFormat()
        data_di_oggi.setBackground(QColor("red"))
        self.calendario.setDateTextFormat(QDate(datetime.now()),data_di_oggi )
        self.g_layout.addWidget(self.calendario, 1, 0)

        self.h_layout = QHBoxLayout()

        #tasto indietro
        self.crea_pulsante("⬅️", self.mostra_indietro_palestra)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.mostra_indietro_palestra)

        #tasto mostra giorno
        self.crea_pulsante("Mostra giorno", self.mostra_view_day_palestra)
        self.shortcut_mostra_giorno = QShortcut(QKeySequence('Return'), self)
        self.shortcut_mostra_giorno.activated.connect(self.mostra_view_day_palestra)

        #tasto mostra tutte
        self.crea_pulsante("Mostra tutte", self.mostra_tutte_prenotazioni_palestra)

        self.g_layout.addLayout(self.h_layout, 2, 0)

        self.setLayout(self.g_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco Corsi Palestra")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

    #funzione per creare i pulsanti
    def crea_pulsante(self, titolo, funzione):
        pulsante = QPushButton(titolo)
        pulsante.setFont(QFont("Yu Gothic UI Light", 12))
        pulsante.clicked.connect(funzione)
        self.h_layout.addWidget(pulsante)
        pulsante.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    #funzione per chiudere la pagina
    def mostra_indietro_palestra(self):
        self.close()

    #funzione per mostrare il giorno selezionato
    def mostra_view_day_palestra(self):
        dataq = self.calendario.selectedDate()
        self.datai = datetime(dataq.year(), dataq.month(), dataq.day())
        self.lista_prenotazioni_day = view_day_corsi_palestra(self.datai)
        self.lista_prenotazioni_day.show()

    #funzione per mostare tutti i corsi
    def mostra_tutte_prenotazioni_palestra(self):
        self.lista_prenotazioni = view_mostra_tutti_corsi_palestra()
        self.lista_prenotazioni.show()
