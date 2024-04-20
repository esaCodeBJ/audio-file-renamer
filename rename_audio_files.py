import os
import re
import shutil
import unicodedata

def nettoyer_noms_fichiers(dossier_source, dossier_destination, fichier_txt):
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    with open(fichier_txt, 'w', encoding='utf-8') as f_txt:
        for fichier in os.listdir(dossier_source):
            if os.path.isfile(os.path.join(dossier_source, fichier)):
                # Transformer les caractères spéciaux comme les accents
                nom_sans_extension, extension = os.path.splitext(fichier)
                nom_sans_accents = unicodedata.normalize('NFKD', nom_sans_extension).encode('ascii', 'ignore').decode('utf-8')
                nouveau_nom = re.sub(r'[^\w\s-]', '', nom_sans_accents).replace(' ', '-').lower() + extension

                # Renommer le fichier avec le nouveau nom
                ancien_chemin = os.path.join(dossier_source, fichier)
                nouveau_chemin = os.path.join(dossier_destination, nouveau_nom)
                shutil.move(ancien_chemin, nouveau_chemin)

                # Écrire le nouveau nom dans le fichier txt
                f_txt.write(f'{nouveau_nom}\n')
                print(f'Fichier renommé: {nouveau_nom}')

# Chemin du dossier source contenant les fichiers audio
dossier_source = '/chemin/vers/le/dossier/source'

# Chemin du dossier où les fichiers renommés seront déplacés
dossier_destination = '/chemin/vers/le/dossier/destination'

# Chemin du fichier txt pour enregistrer les nouveaux noms
fichier_txt = '/chemin/vers/le/fichier.txt'

nettoyer_noms_fichiers(dossier_source, dossier_destination, fichier_txt)
