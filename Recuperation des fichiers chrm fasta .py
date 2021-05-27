import sys

#On parcourt le fichier .all_chrm_identification.id et on fait une liste avec tous les identifiants des chrm
fichier1=sys.argv[1]
with open (fichier1, "r") as fichier :
        id_chrm=[]
        for ligne in fichier :
                ligne=ligne.rstrip("\n")
                id_chrm.append(">"+ligne)

#On parcourt chaque fichier dans le dossier d'assemblage et on repere si on trouve les id de la liste id_chrm 
compteur=0
fichier2=sys.argv[2]
with open (fichier2, "r")  as fichier :
        for ligne in fichier :
                ligne=ligne.rstrip("\n")
                if ligne.startswith(">") :
                        ligne2=ligne.split(" ")
                        for chrm in id_chrm :
                                if ligne2[0] == chrm :
                                        print(ligne)
                                        compteur +=1
                else :
                        print(ligne)

if compteur > 0 :
        print("Il y a", compteur, "chrm de PlasPredict qui avait un fichier fasta dans assembling")







