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
#print(compter_occurences('o','bonjour'))

#Question 2
def compter_mots(chaine):
    compteur = 1
    
    for i in range(len(chaine)):
        if chaine[i] == " ":
            compteur += 1
    return compteur

#print(compter_mots("salut a a tous aa"))
    




##############################################
##############################################
    




""""""
a =ord('a')
z = ord('z')

with open('message3.txt', 'r', encoding = 'utf8') as f:
   message = f.read()
   
with open('message2.txt', 'r', encoding = 'utf8') as f:
   message1 = f.read()
    
with open('message4.txt', 'r', encoding = 'utf8') as f:
   message2 = f.read()   
    
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




######### DECHIFFREMENT CESAR (FONCTIONS) ############
    
def cesar(mot):  #Dechiffrement césar pour un mot chiffré, test toute les 26 clés possibles et les print
    mot=''
    for k in range(26):
        
        print(chiff_cesar(mot,-k))
        
    return None




    
def frequence(texte): # fonction qui met dans un dictionnaire le nombre de lettre dans un mot
    mon_dico = {}
    for i in range(len(texte)):
        if texte[i] in mon_dico :
            mon_dico[texte[i]]+=1
        else:
            mon_dico[texte[i]]= 1
    return mon_dico




def plusFrequent(texte):
    plusFrequent = ' '
    initial = 0
    mon_dico = frequence(texte)
    for i in mon_dico :
        if mon_dico[i] >= initial :
            initial = mon_dico[i]
            plusFrequent = i
    return plusFrequent




def definir_la_cle(texte):  #l'occurence la plus frequente dans un texte est normalment l'espace donc por determiner la clé on prend ' '  comme repère
    
    x = plusFrequent(texte)
    cle = ord(' ')- ord(x)
    
    return cle

def décalement(lettre_crypter, decalage) : #retrouve le caractere décalé
    
    nb = ord(lettre_crypter)
    lettre_cherchee = chr(nb + decalage)
    
    return lettre_cherchee
    

######### CHIFFREMENT CESAR ############    
def chiff_cesar(texte,k):
    # 
    message_crypté = ''
    definir_la_cle = k
    
    for char in texte :
        lettreX = décalement(char, definir_la_cle)
        message_crypté = message_crypté + lettreX
        
    return message_crypté
        
"""
        nb= ord(lettre) - a
        nb_crypter = cesar_chiffre_nb(nb,k)
        lettre_crypter = chr(nb_crypter + a)
        message.append(lettre_crypter)
       # if lettre == ' ':
           # lettre = 'n'             
    message = ''.join(message)
    return (message)
        """

############ DECHIFFREMENT CESAR MESSAGE 2 ET 3
def dechiffrement_cesar(chaine) : 
    
    cesar_key = definir_la_cle(chaine)
    texte = chiff_cesar(chaine,cesar_key)
    
    return texte
    
print(dechiffrement_cesar(message))
print(dechiffrement_cesar(message1))       

###################################
###################################




"""
def decryptage_cesar(mot,k):
    
    message =[]
    for lettre in mot:
        nb= ord(lettre) - a
        nb_crypter = cesar_chiffre_nb(nb,-k)
        lettre_crypter = chr(nb_crypter + a)
        message.append(lettre_crypter)
    message = ''.join(message)
    return (message)




def dechiffrement_cesar(chaine,cle):
    message=''
    for c in chaine:
        k=chiff_cesar(c,cle)-(2*cle)
        message+=k
    return message

print(dechiffrement_cesar('a',))

"""
##############################
###############################


def separation(chaine) :    #decrypatage message 4.
   
    chaine1 = ''
    chaine2 = ''
    chaine_final = ''
   
    
    for i in range(len(chaine)) :
        
        if i%2 == 0:
            chaine1 += chaine[i]
        else : 
            chaine2 += chaine[i]
            
 
    chaine1_dech = dechiffrement_cesar(chaine1)
    chaine2_dech = dechiffrement_cesar(chaine2)
    
    
    for i in range(len(chaine1_dech)):
        chaine_final += chaine1_dech[i] + chaine2_dech[i]
    return chaine_final
        
print(separation(message2))

##################################
##################################



