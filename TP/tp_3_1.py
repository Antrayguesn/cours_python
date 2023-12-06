DEBUT_MAJUSCULE = 65
DEBUT_MINUSCULE = 97

FIN_MAJUSCULE = DEBUT_MAJUSCULE + 25
FIN_MINUSCULE = DEBUT_MINUSCULE + 25

MAJUSCULE = 1
MINUSCULE = -1

class Cesar:

  def __init__(self, clef: int):
    self.clef = clef

  @property
  def clef(self):
    return self._clef

  @clef.setter
  def clef(self, clef: int):
    self._clef = clef

  def _est_majuscule(self, lettre: str) -> int:
    return MAJUSCULE if lettre.isupper() else MINUSCULE

  def _est_lettre(self, lettre: str) -> bool:
    return lettre.isalpha()
  
  def ascii_to_alphabet(self, lettre: str) -> (str, int):
    position_lettre = ord(lettre)

    if not self._est_lettre(lettre):
      return (None, None)
  
    return (ord(lettre.lower()) - ord('a'), self._est_majuscule(lettre))
  
  def decaler_lettre(self, lettre: str, decalage: int) -> str:
    pos_alphabet, typeLettre = self.ascii_to_alphabet(lettre)
    if pos_alphabet is not None :
      pos_chiffre = (pos_alphabet + decalage) % 26
      pos_ascii = self.alphabet_to_ascii(pos_chiffre, typeLettre)
      return chr(pos_ascii)
    return lettre
  
  def alphabet_to_ascii(self, position_lettre: int, typeLettre: int) -> str:
    if typeLettre == MAJUSCULE:
      return position_lettre + DEBUT_MAJUSCULE
    elif typeLettre == MINUSCULE:
      return position_lettre + DEBUT_MINUSCULE
    return None

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

class CesarBinaire:
  def __init__(self, clef: int):
    self.clef = clef

  @property
  def clef(self):
    return self._clef

  @clef.setter
  def clef(self, clef: int):
    self._clef = clef

  def decaler_lettre(self, lettre: bytes, decalage: int) -> str:
    return lettre ^ decalage

  def chiffrer(self, message: str) -> str:
    message_chiffre = bytearray()
    for lettre in message.encode():
      message_chiffre.append(self.decaler_lettre(lettre, self.clef))
    return str(bytes(message_chiffre).decode())

  def dechiffrer(self, message: str) -> str:
    message_chiffre = bytearray()
    for lettre in message.encode():
      message_chiffre.append(self.decaler_lettre(lettre, self.clef))
    return str(bytes(message_chiffre).decode())

  


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

import time

c = CesarBinaire(5)
c2 = Cesar(5)
m = Message(lire_message("message.txt"), c)
m2 = Message(lire_message("message.txt"), c2)

start = time.time()
me = m.chiffrer()
test_time = (time.time() - start) * 1000
print(f"Le test à pris {test_time:.1f} ms")

start = time.time()
me = m2.chiffrer()
test_time = (time.time() - start) * 1000
print(f"Le test à pris {test_time:.1f} ms")

m = Message(me, c)

m.dechiffrer()










