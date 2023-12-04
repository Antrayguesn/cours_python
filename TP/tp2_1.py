from collections import Counter

DEBUT_MAJUSCULE = 65
DEBUT_MINUSCULE = 97

FIN_MAJUSCULE = DEBUT_MAJUSCULE + 26
FIN_MINUSCULE = DEBUT_MINUSCULE + 26

MAJUSCULE = 1
MINUSCULE = -1

OFFSET_TYPE = {MAJUSCULE: DEBUT_MAJUSCULE, MINUSCULE: DEBUT_MINUSCULE}


def lire_message(cheminMessage: str) -> str:
  with open(cheminMessage, "r") as fichierMessage:
    return fichierMessage.read()

def ecrire_message(message: str) -> str:
  with open("message_chiffre.txt", "w") as fichierMessage:
    fichierMessage.write(message)



def est_majuscule(lettre: str) -> int:
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

def est_lettre(lettre: str) -> bool:
  return est_majuscule(lettre) != 0

def ascii_to_alphabet(lettre: str) -> (str, int):
  position_lettre = ord(lettre)

  typeLettre = est_majuscule(lettre)
  
  if typeLettre:
    return (position_lettre - OFFSET_TYPE[typeLettre], typeLettre)

  return (None, None)
    

def alphabet_to_ascii(position_lettre: int, typeLettre: int) -> str:
  if typeLettre == MAJUSCULE:
    return position_lettre + DEBUT_MAJUSCULE
  elif typeLettre == MINUSCULE:
    return position_lettre + DEBUT_MINUSCULE
  return None

def decaler_lettre(lettre: str, decalage: int) -> str:
  pos_alphabet, typeLettre = ascii_to_alphabet(lettre)
  if pos_alphabet is not None :
    pos_chiffre = (pos_alphabet + decalage) % 26
    pos_ascii = alphabet_to_ascii(pos_chiffre, typeLettre)
    return chr(pos_ascii)
  return lettre


def chiffrer_cesar(message: str, clef: int):
  message_chiffre = ""
  for lettre in message:
    message_chiffre += decaler_lettre(lettre, clef)
  return message_chiffre

def dechiffrer_cesar(message: str, clef: int):
  message_chiffre = ""
  for lettre in message:
    message_chiffre += decaler_lettre(lettre, -clef)
  return message_chiffre


def dechiffrer_cesar(message: str, clef: int):
  message_chiffre = ""
  for lettre in message:
    message_chiffre += decaler_lettre(lettre, -clef)
  return message_chiffre

def counter_lettre(occurences: Counter) -> Counter:
  for occurence in occurences:
    if not est_lettre(occurence):
      occurences[occurence] = 0
  
  return +occurences

def occurence_lettre_livre(cheminLivre: str) -> Counter:
  """ Prend le chemin d'un livre format plain text et 
  retourne le nombre d'occurence de chaue lettre
  """
  with open(cheminLivre, "r") as livre:
    frequence_lettre_livre = Counter(livre.read().lower())

  return counter_lettre(frequence_lettre_livre)

def decrypter_cesar(message: str, frequence_lettre_langue: Counter) -> str:

  freq_chiffre = Counter(message.lower())
  freq_chiffre = counter_lettre(freq_chiffre)
  
  range_ = len(freq_chiffre)
  
  most_common_freq_chiffre = freq_chiffre.most_common()[:range_]
  most_common_freq_langue = frequence_lettre_langue.most_common()[:range_]

  score_cle_probable = {}

  for i in range(range_):
    pos_caratere_chiffre = ord(most_common_freq_chiffre[i][0]) 
    pos_caractere_langue = ord(most_common_freq_langue[i][0])

    cle_probable = pos_caratere_chiffre - pos_caractere_langue
    if cle_probable < 0:
      cle_probable += 26

    try:
      score_cle_probable[cle_probable] += len(freq_chiffre) - i
    except KeyError:
      score_cle_probable[cle_probable] = len(freq_chiffre) - i
    
  sorted_clef = sorted(score_cle_probable.items(), key=lambda x: x[1], reverse=True)[:3]
  return [s[0] for s in sorted_clef]

print(occurence_lettre_livre("livres/livre1.txt"))


message = lire_message("message_chiffre.txt")

cles = decrypter_cesar(message, occurence_lettre_livre("livres/livre1.txt"))

for c in cles:
  print(dechiffrer_cesar(message, c))


  


