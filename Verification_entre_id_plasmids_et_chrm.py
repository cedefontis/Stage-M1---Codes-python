import sys
#On parcout le fichier .predicted_plamids.id et on fait une liste avec tous les identifiants des plasmides 
fichier1=sys.argv[1]        #Attention pas [0] car sys.argv [0] = nom du script
id_plasmid=[]
with open(fichier1, "r") as fichier :
        for ligne in fichier :
                id_plasmid.append(ligne)

#On parcourt le fichier des chromosomes de .all_chrm_identification.id et on verifie si les id plasmides sont present dans le fichier des chrm
compteur=0
fichier2=sys.argv[2]

with open(fichier2, "r") as fichier :
        for ligne in fichier :
                for element in id_plasmid :

                        if ligne == element :

                                compteur+=1

#si oui = intru - si non = RAS
if compteur > 0 :
        print("INTRU : Il y a ", compteur, "id plasmidiques et chromosomiques en commun")
else :
        print("RAS")

#commande pour effectuer le script de verif
#Se mettre dans le chemin /data/debroas/Plasmidome/FW_plasmidome/sample/PlasPredict/*/
#time for D in /data/debroas/Plasmidome/FW_plasmidome/sample/PlasPredict/*/ ; do (cd "$D" && python /databis/defontis/verification_entre_id_plasmid_et_id_chrm.py *.predicted_plasmids.id *.all_chrm_identification.id) ; done

