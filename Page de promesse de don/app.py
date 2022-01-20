from flask import Flask, render_template, request #SQL requete
import data

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/afficher', methods=['GET'])
def ajouter():
    Nom = request.values.get('Nom')
    Prenom = request.values.get('Prenom')
    Age=request.values.get('Age')
    Genre=request.values.get('Genre')
    Email=request.values.get('Email')
    Numero_tel=request.values.get('Numero_tel')
    Montant=request.values.get('Montant')

    data.set_utilisateur(Nom,Prenom,Age,Genre,Email,Numero_tel,Montant)

    donnees = data.get_users()

# pour afficher les dons
    total=data.somme()
    
    
    return render_template('afficher.html', utilisateurs = donnees, total=total)

if __name__== "__main__" :
    app.run(debug=True, port=5001)