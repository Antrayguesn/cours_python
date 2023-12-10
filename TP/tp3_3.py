import os
import random

DEBUT_MAJUSCULE = ord('a')
DEBUT_MINUSCULE = ord('A')

FIN_MAJUSCULE = ord('Z')
FIN_MINUSCULE = ord('z')

MAJUSCULE = 1
MINUSCULE = -1

class Chiffrement: 
  def chiffrer(message: str):
    pass

  def dechiffrer(message: str):
    pass

class ChiffrementDecalage(Chiffrement): 
  def decaler_lettre(self, lettre: str, decalage: int) -> str:
    return chr((ord(lettre) + decalage) % 26)


class Cesar(ChiffrementDecalage):
  _clef = None
  def __init__(self, clef: int):
    self.clef = clef

  @property
  def clef(self):
    return self._clef

  @clef.setter
  def clef(self, clef: int):
    self._clef = clef

  def chiffrer(self, message: str) -> str:
    message_chiffre = ""
    for lettre in message:
      message_chiffre += self.decaler_lettre(lettre, self.clef)
    return message_chiffre

  def dechiffrer(self, message: str) -> str:
    message_chiffre = ""
    for lettre in message:
      message_chiffre += self.decaler_lettre(lettre, -self.clef)
    return message_chiffre

class PasBibliothequeError(Exception):
  pass

class ClefError(Exception):
  pass

class Vernam(ChiffrementDecalage):
  def __init__(self, bibliotheque: str):
    self.human_cle = None
    self.bibliotheque = bibliotheque

  @property
  def clef(self):
    return self._clef
  
  def generer_clef(self):
    if not self.bibliotheque:
      raise PasBibliothequeError("Pas de bibliotèque définit")

    files = os.listdir(self.bibliotheque)
    livre_clef_finename = self.bibliotheque + "/" + files[random.randint(0, len(files) - 1)]

    contenu_fichier = None
    with open(livre_clef_finename, "r") as livre_clef:
      contenu_fichier = livre_clef.read()

    if self.taille_message > len(contenu_fichier):
      raise ClefError("La taille du message est suppérieur à celle du livre")

    debut_clef = random.randint(0, len(contenu_fichier))
    fin_clef   = debut_clef + self.taille_message
    
    cle = contenu_fichier[debut_clef: fin_clef]
    self.human_cle = livre_clef_finename, debut_clef

    self._clef = cle

    return cle

  @clef.setter
  def clef(self, livre: str, debut_cle: int):
    with open(self.bibliotheque + "/" + livre, "r") as fichier_livre:
      self._clef = fichier_livre.seek(debut_cle).read(self.taille_message)

  def chiffrer(self, message: str) -> str:
    message_chiffre = ""
    self.taille_message = len(message)
    clef = self.clef
    for i in range(self.taille_message):
      message_chiffre += self.decaler_lettre(message[i], ord(clef[i]))
    return message_chiffre

  def dechiffrer(self, message: str) -> str:
    message_chiffre = ""
    self.taille_message = len(message)
    clef = self.clef
    for i in range(self.taille_message):
      message_chiffre += self.decaler_lettre(message[i], -ord(clef[i]))
    return message_chiffre
  


class Message:

  _algorithme_chiffrement = None
  _message = ""

  def __init__(self, message: str, algo: Cesar = None):
    self.algorithme_chiffrement = algo
    self.message = message
  
  @property
  def algorithme_chiffrement(self):
    return self._algorithme_chiffrement

  @algorithme_chiffrement.setter
  def algorithme_chiffrement(self, algo: Cesar):
    self._algorithme_chiffrement = algo

  @property
  def message(self):
    return self._message

  @message.setter
  def message(self, message: str):
    self._message = message

  def chiffrer(self):
    if self.algorithme_chiffrement is not None:
      return self.algorithme_chiffrement.chiffrer(self.message)
    return self.message

  def dechiffrer(self):
    if self.algorithme_chiffrement is not None:
      return self.algorithme_chiffrement.dechiffrer(self.message)
    return self.message


def lire_message(cheminMessage: str) -> str:
  with open(cheminMessage, "r") as fichierMessage:
    return fichierMessage.read()

def ecrire_message(message: str) -> str:
  with open("message_chiffre.txt", "w") as fichierMessage:
    fichierMessage.write(message)
