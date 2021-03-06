from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gestione.amministrazione.GestioneInventario.controller_gestione_articolo.controller_gestione_articolo import \
    controller_gestione_articolo
from gestione.amministrazione.GestioneInventario.view_modifica_articolo.view_modifica_articolo import \
    view_modifica_articolo
from gestione.amministrazione.inventario.controller_inventario.controller_inventario import controller_inventario
from gestione.amministrazione.inventario.view_inventario.view_inserisci_articolo import view_inserisci_articolo


class view_inventario(QWidget):

    #view di inventario con diversi bottoni che servono all'utente per gestire l'inventario
    def __init__(self, parent=None):
        super(view_inventario, self).__init__(parent)

        self.controller = controller_inventario()

        self.v_layout = QVBoxLayout()

        self.list_view = QListView()
        self.list_view.setGeometry(40, 60, 500, 401)

        self.aggiorna_dati()
        self.v_layout.addWidget(self.list_view)

        self.h_layout = QHBoxLayout()

        self.font_bottoni = QFont("Yu Gothic UI Light", 12)

        self.indietro = QPushButton("⬅️")
        self.indietro.setIconSize(QtCore.QSize(40, 40))
        self.indietro.setDefault(False)
        self.indietro.setFont(self.font_bottoni)
        self.shortcut_indietro = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_indietro.activated.connect(self.chiudi_schermata)

        self.h_layout.addWidget(self.indietro)
        self.indietro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.indietro.setIconSize(QtCore.QSize(40, 40))
        self.indietro.clicked.connect(self.chiudi_schermata)

        self.inserisci_inventario = QPushButton("Inserisci articolo")
        self.inserisci_inventario.clicked.connect(self.mostra_inserisci_inventario)
        self.inserisci_inventario.setFont(self.font_bottoni)
        self.h_layout.addWidget(self.inserisci_inventario)
        self.inserisci_inventario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.elimina_inventario = QPushButton("Elimina articolo")
        self.elimina_inventario.setFont(self.font_bottoni)
        self.elimina_inventario.clicked.connect(self.mostra_elimina_inventario)
        self.h_layout.addWidget(self.elimina_inventario)
        self.elimina_inventario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.modifica_inventario = QPushButton("Modifica articolo")
        self.modifica_inventario.setFont(self.font_bottoni)
        self.modifica_inventario.clicked.connect(self.mostra_modifica_inventario)
        self.h_layout.addWidget(self.modifica_inventario)
        self.modifica_inventario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.setMinimumSize(781, 500)
        self.setMaximumSize(781, 500)
        self.setWindowTitle("Elenco inventario")
        self.setWindowIcon(QtGui.QIcon("images/immaginelogo1.png"))

        # per lo sfondo
        oImage = QImage("images/immaginepesisfocata.jpeg")
        sImage = oImage.scaled(QSize(791, 501))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.show()

    #funzione che chiude la finestra
    def chiudi_schermata(self):
        self.close()

    # funzione che mostra all'utente gli articoli inseriti attraverso una list view
    def aggiorna_dati(self):

        self.list_view_model = QStandardItemModel(self.list_view)

        self.font_item = QFont("Yu Gothic UI Light", 12)

        for inventario in self.controller.get_lista_inventario():
            item = QStandardItem()
            item.setText(inventario.articolo + " " + (str(inventario.quantita)))
            item.setEditable(False)
            item.setFont(self.font_item)
            self.list_view_model.appendRow(item)
        self.list_view.setModel(self.list_view_model)

    # funzione che richiama la view di insersci articolo per l'inserimento di un articolo
    def mostra_inserisci_inventario(self):

        self.inserisci_inventario = view_inserisci_articolo(self.controller, self.aggiorna_dati)
        self.inserisci_inventario.show()

    def closeEvent(self, event):
        self.controller.save_data()

    # elimina dalla lista l'articolo selezionato
    def mostra_elimina_inventario(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_eliminare = self.controller.get_lista_inventario()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un articolo da eliminare", QMessageBox.Ok, QMessageBox.Ok)
            return
        risposta = QMessageBox.question(self, "Conferma", "Vuoi eliminare l'articolo?", QMessageBox.Yes,
                                        QMessageBox.No)

        if risposta == QMessageBox.Yes:

            self.controller.elimina_inventario_by_codice(da_eliminare.codice)
            QMessageBox.about(self, "Eliminato", "L'articolo è stato eliminato")
            self.aggiorna_dati()
        else:
            return

    #richiama la view di modifica inventario per modificare inventario
    def mostra_modifica_inventario(self):

        try:
            index = self.list_view.selectedIndexes()[0].row()
            da_visualizzare = self.controller.get_lista_inventario()[index]

        except:
            QMessageBox.critical(self, "Errore", "Seleziona un articolo da visualizzare", QMessageBox.Ok,
                                 QMessageBox.Ok)
            return

        self.modifica_inventario = view_modifica_articolo(controller_gestione_articolo(da_visualizzare),
                                                           self.aggiorna_dati, self.controller.get_lista_inventario())
        self.modifica_inventario.show()
