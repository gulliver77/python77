import tkinter as tk
import random
import string
import os

# Fonction pour générer un mot de passe aléatoire
def generer_mot_de_passe(longueur=12):
    if longueur < 4:
        raise ValueError("La longueur du mot de passe doit être d'au moins 4 caractères.")

    # Définir les caractères de chaque catégorie
    majuscules = string.ascii_uppercase
    minuscules = string.ascii_lowercase
    chiffres = string.digits
    speciaux = '&#|@?%'

    # S'assurer d'avoir au moins un caractère de chaque catégorie
    mot_de_passe = [
        random.choice(majuscules),
        random.choice(minuscules),
        random.choice(chiffres),
        random.choice(speciaux)
    ]

    # Compléter le mot de passe avec des caractères aléatoires
    caracteres_restants = majuscules + minuscules + chiffres + speciaux
    mot_de_passe += random.choices(caracteres_restants, k=longueur - 4)

    # Mélanger les caractères pour plus de sécurité
    random.shuffle(mot_de_passe)

    return ''.join(mot_de_passe)
    
    
# Fonction pour ajouter les informations au fichier
def ajouter_infos():
    nom_du_site = entry_nom_site.get()
    url_du_site = entry_url_site.get()
    login_pour_le_site = "gerardzmoi@gmail.com"
    mdp_pour_le_site = generer_mot_de_passe()
    signature = entry_signature.get()

    # Vérifier si le fichier existe, sinon le créer
    if not os.path.exists("mdp-gulliver.txt"):
        with open("mdp-gulliver.txt", 'w') as f:
            pass

    # Vérifier si l'URL est déjà présente dans le fichier
    with open("mdp-gulliver.txt", 'r') as f:
        for ligne in f:
            if url_du_site in ligne:
                message_label.config(text="L'URL est déjà présente dans le fichier.", fg="red")
                return

    # Ajouter les informations au fichier
    with open("mdp-gulliver.txt", 'a') as f:
        f.write(f"{nom_du_site}\t{url_du_site}\t{login_pour_le_site}\t{mdp_pour_le_site}\t{signature}\n")
    
    message_label.config(text="Informations ajoutées avec succès.", fg="green")

    # Réinitialiser les zones de saisie
    entry_nom_site.delete(0, tk.END)
    entry_url_site.delete(0, tk.END)
    entry_signature.delete(0, tk.END)

# Fonction pour quitter l'application
def quitter():
    root.quit()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de mots de passe")
root.geometry("400x400")  # Agrandir la fenêtre

# Création des champs de saisie
label_nom_site = tk.Label(root, text="Nom du site :")
label_nom_site.pack(pady=5)
entry_nom_site = tk.Entry(root, width=50)
entry_nom_site.pack(pady=5)

label_url_site = tk.Label(root, text="URL du site :")
label_url_site.pack(pady=5)
entry_url_site = tk.Entry(root, width=50)
entry_url_site.pack(pady=5)

label_signature = tk.Label(root, text="Signature :")
label_signature.pack(pady=5)
entry_signature = tk.Entry(root, width=50)
entry_signature.pack(pady=5)

# Label pour afficher les messages
message_label = tk.Label(root, text="", fg="black")
message_label.pack(pady=10)

# Boutons
button_ajouter = tk.Button(root, text="Ajouter", command=ajouter_infos)
button_ajouter.pack(pady=5)

button_quitter = tk.Button(root, text="Quitter", command=quitter)
button_quitter.pack(pady=10)  # Ajout d'un espacement vertical

# Lancement de la boucle principale
root.mainloop()
