# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 17:00:04 2020

@author: etudiant
"""

#Question 1 


def compter_occurences(caractere, chaine): 
    
    compteur = 0
    
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            compteur += 1
    return compteur
print(compter_occurences('o','bonjour'))

#Question 2
def compter_mots(chaine):
    compteur = 1
    
    for i in range(len(chaine)):
        if chaine[i] == " ":
            compteur += 1
    return compteur

print(compter_mots("salut a a tous aa"))

""""""
a =ord('a')
z = ord('z')


def cesar_chiffre_nb(x,k):
    """
    chiffre uncaractèreaveclaclék
    entrées :
        x : caractère
        k : cléentière
    sortie:
        y : caractèrechiffré
    """
    return(x+k)%(z-a)
"""   
def cesar_chiffre_nb2(x,k):
    return(x-k)%26
"""""

    
def chiff_cesar(mot,k):
    # 
    message =[]
    for lettre in mot:
        nb= ord(lettre) - a
        nb_crypter = cesar_chiffre_nb(nb,k)
        lettre_crypter = chr(nb_crypter + a)
        message.append(lettre_crypter)
        if lettre == ' ':
            lettre = 'n'             
    message = ''.join(message)
    return (message)


def decryptage_cesar(mot,k):
    
    message =[]
    for lettre in mot:
        nb= ord(lettre) - a
        nb_crypter = cesar_chiffre_nb(nb,-k)
        lettre_crypter = chr(nb_crypter + a)
        message.append(lettre_crypter)
    message = ''.join(message)
    return (message)