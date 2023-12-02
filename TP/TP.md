= Boite mail chiffrée 

== Serveur REST

=== v1 sans JSON v2 retour en JSON et UUID

* Expose un /v1/login en POST pour vérifier une connexion
* Expose un /v1/envoyerMessage en POST
* Expose un /v1/recevoirMessage en GET
* Expose en CRUD /v1/user

== Client

* v1 Stocke son nom en constante v2 Stocke un `UUID` en constante

* Peut s'enregistrer avec /v1/user en passant son v1 `UUID` v2 nom
* Peut récuperer les users avec /v1/user GET
* Peut envoyer un message avec /v1/envoyerMessage en passant 
* Peut récuperer des messgaes avec /v1/recupererMessage

= Script de chiffrement de message



class Message
class AlgoChiffrmeent
class Cesar(AlgoChiffrmeent)
class Vernam(AlgoChiffrmeent)


Opération arithmetique et sur les chaines de caractère :
  Ecriture d'une fonction de chiffrement/dechiffrement de César

Type de données complexes (dictionnaire, list, date):
  Analyse de fréquence pour casser le chiffrement de César

Orienté objet :
  Représentation objet d'un message (Chiffrable)

Héritage / Interface
  Réprésentatin objet d'un algo de chiffrement 
  Implémentation du chiffre de Cesar

Polymorphisme
  Orienté objet avec l'implémentation d'un pseudo chiffre de Vernam avec comme clé un fichier (livre) et un offset


