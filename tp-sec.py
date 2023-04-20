#fonction de generation de cle
def generer_cle(cle):
    # Appliquer la permutation P
    P = [6, 5, 2, 7, 4, 1, 3, 0]
    cle_permute = [cle[i] for i in P]
    
    # Diviser la clé en deux blocs de 4 bits
    k1_prime = cle_permute[:4]
    k2_prime = cle_permute[4:]
    
    # Calculer les sous-clés k1 et k2
    k1 = [k1_prime[i] ^ k2_prime[i] for i in range(4)]
    k2 = [k2_prime[i] & k1_prime[i] for i in range(4)]
    
    # Appliquer les décalages
    k1_decale = k1[2:] + k1[:2]
    k2_decale = k2[-1:] + k2[:-1]
    
    # Retourner les sous-clés
    return k1_decale, k2_decale


#fonction de chiffrement
def bloc_chiffrement(block, cle):
    # Appliquer la permutation π
    pi = [4, 6, 0, 2, 7, 3, 1, 5]
    block_permite = [block[i] for i in pi] 
    # Diviser le bloc en deux blocs de 4 bits
    left_half = block_permite[:4]
    right_half = block_permite[4:]
    # Générer les clés k1 et k2
    k1, k2 = generer_cle(cle)
    # Premier Round
    d1 = [left_half[i] ^ k1[i] for i in range(4)]
    g1 = [right_half[i] ^ (left_half[i] | k1[i]) for i in range(4)]
    
    # Deuxième Round
    d2 = [g1[i] ^ k2[i] for i in range(4)]
    g2 = [d1[i] ^ (g1[i] | k2[i]) for i in range(4)]
    
    # Concaténer les deux moitiés
    block_chiffre = g2 + d2
    
    # Appliquer l'inverse de la permutation π^-1
    pi_inv = [2, 6, 3, 1, 4, 7, 0, 5]
    block_final = [block_chiffre[i] for i in pi_inv]
    
    # Retourner le texte chiffré
    return block_final
    # fonction de dexhiffrement
def block_dechiffrement(block, cle):
    # Appliquer la permutation π
    pi = [4, 6, 0, 2, 7, 3, 1, 5]
    block_permite = [block[i] for i in pi]
    
    # Diviser le bloc en deux blocs de 4 bits
    partie_gauche = block_permite[:4]
    partie_droite = block_permite[4:]
    
    # Générer les sous-clés k1 et k2
    k1, k2 = generer_cle(cle)
    
    # Deuxième Round inverse
    g1 = [partie_gauche[i] ^ (partie_droite[i] | k2[i]) for i in range(4)]
    d1 = [partie_droite[i] ^ k2[i] for i in range(4)]
    
    # Premier Round inverse
    g0 = [g1[i] ^ (d1[i] | k1[i]) for i in range(4)]
    d0 = [partie_droite[i] ^ k1[i] for i in range(4)]
    
    # Concaténer les deux moitiés
    block_dechiffre = g0 + d0
    
    # Appliquer l'inverse de la permutation π^-1
    pi_inv = [2, 6, 3, 1, 4, 7, 0, 5]
    block_final = [block_dechiffre[i] for i in pi_inv]
    
    # Retourner le texte déchiffré
    return block_final


print("concepteur : NZALE MWEMBU ARISTOTE")
print("à partir d'une suite d'entrees de longueur 8, ce programme:")
print("1.genere une cle;")
print("2.fait le chiffrement;")
print("3.fait le déchiffrement/")


s='2'
l=len(str(s))
print(l)
while l!=8:
    print("entrez une cle de chiffres de longueur 8")
    s=(input())
    l=len(s)
kl=[int(s[0]),int(s[1]),int(s[2]),int(s[3]),int(s[4]),int(s[5]),int(s[6]),int(s[7])]
k1,k2=generer_cle(kl)
clef=k1+k2
print("______________suite de 8 bits inscrit___________")
print(kl)
print("__________generation de la cle____________")
print(clef)
ch=bloc_chiffrement(kl,clef)
print("______________chiffrement____________")
print(ch)
dch=block_dechiffrement(kl,clef)
print("______________dechiffrement____________")
print(dch)
    



 



   



