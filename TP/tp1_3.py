DEBUT_MAJUSCULE = 65
DEBUT_MINUSCULE = 97

FIN_MAJUSCULE = DEBUT_MAJUSCULE + 26
FIN_MINUSCULE = DEBUT_MINUSCULE + 26

MAJUSCULE = 1
MINUSCULE = -1

print("Saisir le message à chiffrer : ")
message_saisi = input()

print("Saisir la clé : ")
clef_str = input()

clef = int(clef_str)

def est_majuscule(lettre: str):
  """ Retourne :
    1 si majuscule
     -1 si minuscule
     0 si aucun des deux """
  position_lettre = ord(lettre)
  if (position_lettre >= DEBUT_MAJUSCULE and position_lettre <= FIN_MAJUSCULE):
    return MAJUSCULE
  elif (position_lettre >= DEBUT_MINUSCULE and position_lettre <= FIN_MINUSCULE):
    return MINUSCULE
  return 0

def ascii_to_alphabet(lettre: str) -> (str, int):
  position_lettre = ord(lettre)

  if est_majuscule(lettre) == MAJUSCULE:
    return (position_lettre - DEBUT_MAJUSCULE, MAJUSCULE)
  elif est_majuscule(lettre) == MINUSCULE:
    return (position_lettre - DEBUT_MINUSCULE, MINUSCULE)
  return (None, None)

def alphabet_to_ascii(position_lettre: int, typeLettre: int) -> str:
  if typeLettre == MAJUSCULE:
    return position_lettre + DEBUT_MAJUSCULE
  elif typeLettre == MINUSCULE:
    return position_lettre + DEBUT_MINUSCULE
  return None

def chiffrer_cesar(message: str, clef: int):
  message_chiffre = ""
  for lettre in message:
    pos_alphabet, typeLettre = ascii_to_alphabet(lettre)
    if pos_alphabet is not None :
      pos_chiffre = (pos_alphabet + clef) % 26
      pos_ascii = alphabet_to_ascii(pos_chiffre, typeLettre)
      message_chiffre += chr(pos_ascii)
    else:
      message_chiffre += lettre

  return message_chiffre

def dechiffrer_cesar(message: str, clef: int):
  message_chiffre = ""
  for lettre in message:
    pos_alphabet, typeLettre = ascii_to_alphabet(lettre)
    if pos_alphabet is not None:
      pos_chiffre = (pos_alphabet - clef) % 26
      pos_ascii = alphabet_to_ascii(pos_chiffre, typeLettre)
      message_chiffre += chr(pos_ascii)
    else:
      message_chiffre += lettre

  return message_chiffre

c = chiffrer_cesar(message_saisi, clef)
print(c)
print(dechiffrer_cesar(c, clef))