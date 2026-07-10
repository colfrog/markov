import random

class Markov:
    def __init__(self):
        self.historique = {} # Clé: tuple de 2 mots, Valeur: liste des mots pouvant suivre ces deux mots
        self.ignorer = '.,:;\r\n'

    def ajouter_a_historique(self, mots, mot_a_ajouter):
        if mots in self.historique:
            self.historique[mots].append(mot_a_ajouter)
        else:
            self.historique[mots] = [mot_a_ajouter]

    def retirer_mot(self, mots):
        return random.choice(self.historique[mots])

    def lire_fichier(self, chemin):
        with open(chemin, 'r', encoding='utf8') as f:
            texte = f.read()
            self.lire(texte)

    def lire(self, texte):
        texte = texte.replace('\n', ' ')
        texte = texte.replace('\r', ' ')
        texte = texte.lower()

        mots = ('', '')
        for mot in texte.split(' '):
            mot_propre = mot.strip(self.ignorer)
            self.ajouter_a_historique(mots, mot_propre)

            mots = (mots[1], mot_propre)

            if '.' in mot:
                self.ajouter_a_historique(mots, '.')
                mots = ('', '')

    def generer_phrase(self, debut=None):
        mots = ['', ''] if debut is None else ['', debut]
        arreter = False
        while not arreter:
            mot = self.retirer_mot((mots[-2], mots[-1]))
            if mot == '.':
                arreter = True
            else:
                mots.append(mot)

        return ' '.join([mot for mot in mots if mot != ''])