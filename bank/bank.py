class compteBancaire:
    def __init__(self, numeros, mot_de_passe, solde=0):
        self._numeros = numeros
        self._solde = solde
        self.__mot_de_passe = mot_de_passe
    
    def deposer(self, montant):
        if montant > 0:
            self._solde += montant
            print(f"{montant} a été déposé sur le compte de {self._numeros}")
        else:
            print("Le montant doit être positif.")
    
    def retirer(self, montant):
        mdp = input("Entrez le mot de passe: ")
        if mdp != self.__mot_de_passe:
            print("Mot de passe incorrect.")
            return
        if montant > 0 and montant <= self._solde:
            self._solde -= montant
            print(f"{montant} a été retiré du compte de {self._numeros}")
        else:
            print("Montant invalide ou solde insuffisant.")
    
    def afficher_solde(self):
        return self._solde
    
    def afficher_numeros(self):
        return self._numeros

    def change_mot_de_passe(self, ancien_mot_de_passe, nouveau_mot_de_passe):
        if ancien_mot_de_passe == self.__mot_de_passe:
            self.__mot_de_passe = nouveau_mot_de_passe
            print("Mot de passe changé avec succès.")
        else:
            print("Ancien mot de passe incorrect.")
    

class compteEpargne(compteBancaire):
    def __init__(self, numeros, mot_de_passe, solde=0, taux_interet=0.02):
        super().__init__(numeros , mot_de_passe, solde)
        self.__taux_interet = taux_interet
    
    def modifier_interet(self, nouveau_taux):
        if 0 <= nouveau_taux <= 1:
            self.__taux_interet = nouveau_taux
            print(f"Taux d'intérêt modifié à {nouveau_taux}")
        else:
            print("Taux d'intérêt invalide. Il doit être entre 0 et 1.")
    
    def appliquer_interet(self):
        interet = self._solde * self.__taux_interet
        self.deposer(interet)
        print(f"Intérêt de {interet} appliqué au compte de {self._numeros}")

    def afficher_taux_interet(self):
        return self.__taux_interet
    
class compteCourant(compteBancaire):
    def __init__(self, numeros, mot_de_passe, plafond_decouvert, solde=0):
        super().__init__(numeros, mot_de_passe, solde)
        self.__plafond_decouvert = plafond_decouvert
    
    def retirer(self, montant):
        if montant <= self._solde + self.__plafond_decouvert:
            return super().retirer(montant)
        else:
            print("Le montant dépasse le plafond de découvert.")

    def epargner(self, montant, numeros_compte_epargne):
        if montant <= self._solde:
            self.retirer(montant)
            numeros_compte_epargne.deposer(montant)
            print(f"{montant} a été transféré vers le compte d'épargne.")
        else:
            print("Solde insuffisant pour transférer vers le compte d'épargne.")
    def afficher_plafond_decouvert(self):
        return self.__plafond_decouvert
    
class client:
    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.__comptes = []
    
    def afficher_informations(self):
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Âge: {self.age}")
        print(f"Adresse: {self.adresse}")
    
    def ajouter_compte(self, numeros):
        self.__comptes.append(numeros)
    
    def afficher_comptes(self):
        self.afficher_informations()
        for compte in self.__comptes:
            print("_________________________________________________________________")
            print(f"Numéro de compte: {compte.afficher_numeros()}")
            print(f"Solde: {compte.afficher_solde()}")
            if isinstance(compte, compteEpargne):
                print(f"Taux d'intérêt: {compte.afficher_taux_interet()}")
            elif isinstance(compte, compteCourant):
                print(f"Plafond de découvert: {compte.afficher_plafond_decouvert()}")
            else:
                print("Type de compte inconnu.")
            print("_________________________________________________________________")


Nicolas = client("Nicolas", "Dupont", 30, "123 rue de Paris")

Nicolas_comptes_courant = compteCourant("100001", "mdp", 1000, 500)
Nicolas_comptes_epargne = compteEpargne("200001", "mdp", 1000, 0.05)

Nicolas.ajouter_compte(Nicolas_comptes_courant)
Nicolas.ajouter_compte(Nicolas_comptes_epargne)
Nicolas.afficher_comptes()

Nicolas_comptes_courant.deposer(500)
Nicolas_comptes_courant.epargner(200, Nicolas_comptes_epargne)
Nicolas_comptes_courant.retirer(100)
Nicolas_comptes_epargne.appliquer_interet()
Nicolas.afficher_comptes()




