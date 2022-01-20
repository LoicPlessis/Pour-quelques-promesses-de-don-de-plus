import mysql.connector as msql

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = msql.connect(user='root', password='root', host='localhost', port="8081", database='promesse_de_don')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def get_users() : # récupère les informations inscrites  de la table dans la BDD
    global cursor

    connexion()
    query = "SELECT * FROM utilisateurs"
    cursor.execute(query)
    utilisateurs = []

    for enregistrement in cursor :
        utilisateur = {}
        utilisateur['id_Utilisateur'] = enregistrement[0]
        utilisateur['Nom'] = enregistrement[1]
        utilisateur['Prenom'] = enregistrement[2]
        utilisateur['Age'] = enregistrement[3]
        utilisateur['Genre'] = enregistrement[4]
        utilisateur['Email'] = enregistrement[5]
        utilisateur['Numero_tel'] = enregistrement[6]
        utilisateur['Montant'] = enregistrement[7]


        utilisateurs.append(utilisateur) # Ajoute  le dictionnaire de l'utilisateur a la liste des utilisateurs totaux
    
    print(utilisateurs)
    deconnexion()
    return utilisateurs


def somme():
    connexion()
    total=0
    query="SELECT * FROM utilisateurs"
    cursor.execute(query)
    for enregistrement in cursor:
        total +=enregistrement[7]
    deconnexion()
    return (total)

def set_utilisateur(Nom,Prenom,Age,Genre,Email,Numero_tel,Montant): # récupère les infos du formulaire qui vont s'inscrire dans la bdd
    global bdd
    global cursor

    connexion()

    query="INSERT INTO utilisateurs(Nom,Prenom,Age,Genre,Email,Numero_tel,Montant) VALUES ('"+Nom+"','"+Prenom+"','"+Age+"','"+Genre+"','"+Email+"','"+Numero_tel+"','"+Montant+"')"
    cursor.execute(query)
    bdd.commit()
    #inscrits les infos utilisateurs dans bdd



    deconnexion()


