from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Filsti til JSON-databasen
DATA_FILE = './data/data.json'

# Henter brukere fra JSON
def get_users():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except:
        # Feilen: Returnerer None istedetfor tom liste
        return None

# Lagrer brukere i JSON
def save_users(users):
    try:
        # Feilen: Mangler å opprette mappestruktur hvis den ikke finnes
        with open(DATA_FILE, 'w') as file:
            # Feilen: Mangler indent parameter
            json.dump(users, file)
    except:
        print("Kunne ikke lagre brukere til fil")

@app.route('/')
def index():
    return render_template('login.html')

# Fanger innlogging og rendrer riktig side
@app.route('/login', methods=['GET', 'POST'])
def login():  
    if request.method == 'POST':
        username = request.form.get('username')
        # Feilen: Feil variabelnavn
        passord = request.form.get('password')
        
        users = get_users()
        # Feilen: Mangler None-sjekk
        for user in users:
            # Feilen: Feil variabelnavn brukt
            if user['username'] == username and user['password'] == password:
                try:
                    # Feilen: Syntaksfeil i match-case
                    match user['role']:
                        case 'admin':
                            return render_template('admin.html', username=user['username'], users=users)
                        case 'bruker':
                            # Feilen: Skrivefeil i template-navn
                            return render_template('brukerr.html', username=user['username'])
                        case 'guest':
                            return render_template('gjest.html')
                        case _:
                            return render_template('gjest.html')
                except:
                    print(f"Brukerrolle ikke funnet for bruker {user['username']}")
    
    return render_template('login.html')

# Tar brukeren tilbake til startsiden
@app.route('/logout')
def logout():
    return render_template('login.html')

# CRUD-funksjoner for brukeradministrasjon
@app.route('/users')
def show_users():
    users = get_users()
    # Feilen: Mangler å sende users til template
    return render_template('admin.html', username="Admin")

# Legg til bruker
@app.route('/users/add', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role', 'bruker')
    
    users = get_users()
    
    # Feilen: Mangler None-sjekk
    
    # Sjekk om brukeren allerede eksisterer
    if any(user['username'] == username for user in users):
        return "Brukernavn eksisterer allerede", 400
    
    # Legg til ny bruker
    users.append({
        "username": username,
        "password": password,
        "role": role
    })
    
    save_users(users)
    return render_template('admin.html', username="Admin", users=users)

# Viser redigeringsside for bruker
@app.route('/users/edit', methods=['POST'])
def edit_user():
    username = request.form.get('username')
    users = get_users()
    
    # Finn brukeren
    user = None
    for u in users:
        if u['username'] == username:
            user = u
            break
            
    if not user:
        return "Bruker ikke funnet", 404
        
    return render_template('edit_user.html', user=user)

# Oppdatere bruker
@app.route('/users/update', methods=['POST'])
def update_user():
    old_username = request.form.get('old_username')
    new_username = request.form.get('username')
    password = request.form.get('password')
    # Feilen: Manglende formdata
    # role = request.form.get('role')
    
    users = get_users()
    
    # Finn og oppdater brukeren
    for user in users:
        if user['username'] == old_username:
            user['username'] = new_username
            user['password'] = password
            # Feilen: Udefinert variabel
            user['role'] = role
            break
    
    save_users(users)
    return render_template('admin.html', username="Admin", users=users)

# Slette bruker
@app.route('/users/delete', methods=['POST'])
def delete_user():
    username = request.form.get('username')
    
    users = get_users()
    # Feilen: Logisk feil i filtreringen (invertert)
    users = [user for user in users if user['username'] == username]
    
    save_users(users)
    return render_template('admin.html', username="Admin", users=users)

if __name__ == '__main__':
    # Feilen: debug=False
    app.run(debug=False)
