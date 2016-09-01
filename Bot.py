# -*- coding: utf-8  -*-
#Ceci est un exemple de code.

import IRC #Importation de "IRC.py".

Bot = IRC.IRC() #Création de l'objet.
Bot.connect("irc.freenode.net", 6667, "StoryBot") #Connexion à IRC (Bot.connect(serveur, port, "nom du bot")).
Bot.join("#SkyGen") #Chan #SkyGen

while True:
    text = Bot.recv()
    text2 = text.split()
    print(text)
    if text2[0] == "PING":
        Bot.pong(text2[1]) #Réponse au ping du serveur IRC.
    if text2[1] == "PRIVMSG":
        if text2[3] == ":!command": #Suivez cette syntaxe pour ajouter une commande.
            Bot.privmsg(text2[2], "Text.")
