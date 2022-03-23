#PARTIE Fonctions:
#PARTIE OOP
class achat:
    def __init__(self,name,quantite):
        self.name=name
        self.quantite=quantite


class Produit:
    def __init__ (self,code,name):
        self.stock=0
        self.prix=-1
        self.name=name
        self.code=code

    def ajout(self=None):
        donner_le_prix=int(input("donner le prix du produit"))
        self.prix=donner_le_prix
        quantite_a_ajouter = int(input("donne la quantite a ajouter"))
        self.stock += quantite_a_ajouter
    def modifier_prix(self):
        self.prix = int(input("saisie le nouveau prix du produit"))
    def modifier_stock(self):
        self.stock = int(input("modifier la quantite du stock"))
    def consulter(self=None):
        print(f"le code de produit {self.name} est {self.code}")
        print(f"la quantite restante de produit {self.name} est   {self.stock}")
        print(f"le prix du produit {self.name}est  {self.prix}")
        print("\n\n")
#grand surface A
class grand_surfaceA(Produit):
    pass
#grand surface B
class grand_surfaceB(Produit):
    pass
#liste de produit pour la magasin A
a=[]
Oeufs=grand_surfaceA(2,"Oeufs")
a.append(Oeufs)
Huile=grand_surfaceA(8,"Huile")
a.append(Huile)
Beurre=grand_surfaceA(10,"Beurre")
a.append(Beurre)
Pâtes=grand_surfaceA(12,"Pâtes")
a.append(Pâtes)
Sucres=grand_surfaceA(15,"Sucres")
a.append(Sucres)
Farine=grand_surfaceA(20,"Farine")
a.append(Farine)
Légumes=grand_surfaceA(31,"Légumes")
a.append(Légumes)
Fruits=grand_surfaceA(43,"Fruits")
a.append(Fruits)
Viandes=grand_surfaceA(59,"Viandes")
a.append(Viandes)
Produit_de_nettoyage=grand_surfaceA(67,"Produit_de_nettoyage")
a.append(Produit_de_nettoyage)
#liste de produit pour la magasin B
b=[]
Oeufs=grand_surfaceB(2,"Oeufs")
b.append(Oeufs)
Huile=grand_surfaceB(8,"Huile")
b.append(Huile)
Beurre=grand_surfaceB(10,"Beurre")
b.append(Beurre)
Pâtes=grand_surfaceB(12,"Pâtes")
b.append(Pâtes)
Sucres=grand_surfaceB(15,"Sucres")
b.append(Sucres)
Farine=grand_surfaceB(20,"Farine")
b.append(Farine)
Légumes=grand_surfaceB(31,"Légumes")
b.append(Légumes)
Fruits=grand_surfaceB(43,"Fruits")
b.append(Fruits)
Viandes=grand_surfaceB(59,"Viandes")
b.append(Viandes)
Produit_de_nettoyage=grand_surfaceB(67,"Produit_de_nettoyage")
b.append(Produit_de_nettoyage)
#Programme principal

#partie 1
choix=0
while (True):
    while True:
        z=input("veuillez choisir quelle magasin vous aimez modifier A ou B \n")
        if z in ["A","a"]:
            L=a
            break
        elif z in ["B","b"]:
            L=b
            break
    print("Merci de saisir votre choix : ")
    print("1- Ajouter les produits ainsi que les quantités dans le stock")
    print("2- Modifier les produits ainsi que les quantités dans le stock ")
    print("3- Consulter la liste des produits ")
    print("4- Quitter ")
    choix = int(input(""))
    if (choix==1):
        for j in L:
            print(f'le produit est {j.name} qui porte le code {j.code}')
            x=input("veuillez donner le prix et la quantite dans la stock taper y/Y si non taper n/N")
            if x in["y","Y"]:
                j.ajout()
            elif x in ["N","n"]:
                continue
            else:
                print("error,on va passer aux produit suivent")
    elif choix==2:
        x=int(input("saisir le code de produit"))
        for j in L:

            if int(j.code)==x:
                j.modifier_prix()
                j.modifier_stock()
                break
    elif (choix==3):
        for j in L:
            j.consulter()
    elif (choix==4):
        break
    else:
        print('veuillez saisir une valeur entre 1 et 4')
#partie 2
#liste_prod est la liste de produit a acheter(c est le panier)
ach=[]
while(True):
    print("Merci de saisir votre choix : ")
    print("1- Consulter la liste des produits ")
    print("2- Saisir les produits à acheter ")
    print("3- Modifier la liste des achats ")
    print("4- Guide ")
    print("5- Quitter ")
    choix = int(input(""))
    if choix==1:
        for j in range(10):
            print(f"{a[j].name} \t prix dans A: {a[j].prix}\t prix dans B: {b[j].prix} \n")
    elif choix ==2:
        nbr=int(input("saisir le nombre des articles"))
        for nb in range(nbr):
            az=input("saisir le nom du produit a achete")
            ab=int(input("saisir la quantite de ce produit"))
            m=achat(az,ab)
            ach.append(m)

    elif choix ==3:
        comp=0
        mod=input("saisir le nom du produit a modifier")
        nov_qu=int(input("saisir la nouvelle quantite si vous aimer annuler la commande taper 0"))
        if nov_qu==0:
            for j in ach:
                if j.name==mod:
                    del ach[comp]
                comp+=1
        else:
            for j in ach:
                if j.name==mod:
                    j.quantite=nov_qu
    elif choix ==4:
        score_a=0
        score_b=0
        for j in ach:
            for z1 in a:
                if z1.name==j.name:
                    r1=z1.prix
                    r2=z1.stock
            for z2 in b:
                if z2.name==j.name:
                    r3=z2.prix
                    r4=z2.prix
            score_a+=1/r1*(r2-j.quantite)
            score_b+=1/r3*(r4-j.quantite)
        if score_b>score_a:
            print("vous devez acheter de la magasin B\n")
        elif score_b==score_a:
            print("les deux magasin ont le meme score\n")
        else:
            print("vous devez acheter de la magasin A\n")

    elif choix ==5:
        break
    else:
        print('veuillez saisir une valeur entre 1 et 5 \n')

