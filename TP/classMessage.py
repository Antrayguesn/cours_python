#!/bin/python3

class AlgoChiffrement():
  DEBUT_MINUSCULE = 97
  FIN_MINUSCULE   = DEBUT_MINUSCULE + 26

  DEBUT_MAJUSCULE = 65
  FIN_MAJUSCULE   = DEBUT_MAJUSCULE + 26
  
  offset = {"maj": DEBUT_MAJUSCULE, "min": DEBUT_MINUSCULE}

  _clef = None

  def is_caractere_chiffrable(self, caractere: str):
    posCaractere = ord(caractere)
    if (posCaractere >= self.DEBUT_MAJUSCULE and posCaractere <= self.FIN_MAJUSCULE) or (posCaractere >= self.DEBUT_MINUSCULE and posCaractere <= self.FIN_MINUSCULE):
      return True
    return False
  
  def __init__(self, clef):
    self.clef = clef
  
  @property
  def clef(self):
    return self._clef
  
  @clef.setter
  def clef(self, clef: int):
    self._clef = clef

  def chiffrer(self, message):
    pass

  def dechiffrer(self, message):
    pass

class ChiffrementCesar(AlgoChiffrement):
  
  @property
  def clef(self):
    return self._clef
  
  @clef.setter
  def clef(self, clef: int):
    if clef > 26:
      print("La clef doit être inférieur à 26")
    self._clef = clef

  def _decaler_caractere(self, caractere: str, sens: int = 1):
    if not self.is_caractere_chiffrable(caractere):
      return caractere

    posCaractere = ord(caractere)
    type = "maj" if posCaractere < self.DEBUT_MINUSCULE else "min"
    
    alphabetCaratere = posCaractere - self.offset[type]
    if sens == 1:
      caratereChiffre = (alphabetCaratere + self._clef) % 26
    else:
      caratereChiffre = (alphabetCaratere - self._clef) % 26
    
    caractereFinal = caratereChiffre + self.offset[type]

    return chr(caractereFinal)
  

  def chiffrer(self, message : str):
    nouveauMessage = ""

    for c in message:
      nouveauMessage += self._decaler_caractere(c, 1)

    return nouveauMessage
      
      
  def dechiffrer(self, message : str):
    nouveauMessage = ""

    for c in message:
      nouveauMessage += self._decaler_caractere(c, 0)

    return nouveauMessage


class Message:
  _message = None
  _algoChiffrement = None

  def __init__(self, message: str = None, algoChiffrement: AlgoChiffrement = None):
    self.message = message
    self.algoChiffrement = algoChiffrement

  @property
  def message(self):
    return self._message
  
  @property
  def algoChiffrement(self):
    return self._algoChiffrement

  @algoChiffrement.setter
  def algoChiffrement(self, algo):
    self._algoChiffrement = algo

  @message.setter
  def message(self, message: str):
    if not isinstance(message, str):
      print("Le message n'est pas une chaine de caratère, le message n'a pas pu être enreigstré")
      return
    self._message = message
  
  def chiffrer(self):
    if self.algoChiffrement is None:
      print("Pas d'algorithme de chiffrement definit")
      return
    
    return self.algoChiffrement.chiffrer(self.message)
  
from collections import Counter

def decrypter_cesar(cle):
  cc = ChiffrementCesar(cle)
  with open("livres/livre1.txt") as f:
    freq = Counter(f.read().lower())
  
  with open("test.txt") as f:
    msgChiffre = Message(f.read(), cc)
  
  freqChiffrer = Counter(msgChiffre.chiffrer().lower())
  
  for c in freq:
    if not cc.is_caractere_chiffrable(c):
      freq[c] = 0
  
  for c in freqChiffrer:
    if not cc.is_caractere_chiffrable(c):
      freqChiffrer[c] = 0
  
  freq = +freq
  freqChiffrer = +freqChiffrer

  range_ = len(freqChiffrer)
  most_common_freq = freq.most_common()[:range_]
  most_common_freq_chiffrer = freqChiffrer.most_common()[:range_]

  score_cle_probable = {}

  for i in range(range_):
    posCaratereChiffrer = ord(most_common_freq_chiffrer[i][0]) 
    posCaractereFreq = ord(most_common_freq[i][0])

    cle_probable = posCaratereChiffrer - posCaractereFreq
    if cle_probable < 0:
      cle_probable += 26


    try:
      score_cle_probable[cle_probable] += len(freqChiffrer) - i
    except KeyError:
      score_cle_probable[cle_probable] = len(freqChiffrer) - i

  return sorted(score_cle_probable.items(), key=lambda x: x[1], reverse=True)[0][0]

for i in range(26):
  cle = decrypter_cesar(i)
  print (cle, i, cle == i)
  


