class Etudiant :
    """
    Classe Etudiant
    """
    def __init__(self, p_numero : str = "", p_nom : str = "", p_prenom : str = "", p_prgm : str = ""):
        self.Numero = p_numero
        self.Nom = p_nom
        self.Prenom = p_prenom
        self.Prgm = p_prgm

    def __str__(self):
        chaine = "Numero d'étudiant : "+ self.Numero + "\n"
        chaine += "Nom de l'étudiant : "+ self.Nom+"\n"
        chaine += "Prénom de l'étudiant : "+ self.Prenom + "\n"
        chaine += "Programme d'études : " + self.Prgm
        return chaine

