# Importer la classe  Etudiant
from Etudiant import *

# Importer le fichier de l'interface graphique qu'on a créé
import interface_graphique_classe

# Impprter le module sys qui nous permet de lancer une application
import sys

# Importer la librairie QtWidget et QtDesigner
from PyQt5 import QtWidgets

from PyQt5.QtCore import pyqtSlot

class MaFenetre(QtWidgets.QMainWindow,interface_graphique_classe.Ui_MainWindow):

    def __init__(self, parent = None):
        super(MaFenetre,self).__init__(parent) # Appeler les constructeurs des classes mères
        self.setupUi(self) # Préparer l'interface utilisateur

        # Gestionnaire d'événement du bouton Button_Etudiant
    @pyqtSlot()
    def on_Button_Ajouter_clicked(self):
        mat = self.Edit_Numero_etudiant.text()
        nom = self.Edit_Nom_etudiant.text()
        prenom = self.Edit_Prenom_etudiant.text()
        prgm = self.Button_Ajouter.text()

        Etud = Etudiant(mat, nom, prenom, prgm)
        self.label_affichage.setText(Etud.__str__())


def main():
    mon_app = QtWidgets.QApplication(sys.argv)
    mon_formulaire = MaFenetre()
    mon_formulaire.show()
    mon_app.exec()


if __name__=="__main__":
    main()
