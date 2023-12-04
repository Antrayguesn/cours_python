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

message_chiffre = ""

for lettre in message_saisi:
  typeLettre = None
  pos_lettre_alphabet = ""

  position_lettre = ord(lettre)

  if (position_lettre >= DEBUT_MAJUSCULE and position_lettre <= FIN_MAJUSCULE):
    typeLettre = MAJUSCULE
    pos_lettre_alphabet = position_lettre - DEBUT_MAJUSCULE
  elif (position_lettre >= DEBUT_MINUSCULE and position_lettre <= FIN_MINUSCULE):
    typeLettre = MINUSCULE
    pos_lettre_alphabet = position_lettre - DEBUT_MINUSCULE
  else:
    typeLettre = None

  if typeLettre:
    pos_lettre_alphabet = (pos_lettre_alphabet + clef) % 26
  
  if typeLettre == MAJUSCULE:
    position_lettre = pos_lettre_alphabet + DEBUT_MAJUSCULE
  elif typeLettre == MINUSCULE:
    position_lettre = pos_lettre_alphabet + DEBUT_MINUSCULE

  message_chiffre += chr(position_lettre)
    
 
print(message_chiffre)
