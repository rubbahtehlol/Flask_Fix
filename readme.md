# Flask Brukeradministrasjon - Feilsøkingsoppgaver

Dette prosjektet inneholder en Flask-applikasjon for brukeradministrasjon med innlagte feil som er designet for å brukes i feilsøkingsoppgaver. Applikasjonen er også satt opp for å gi praksis med Git-branching.

## Oversikt

Applikasjonen er en enkel brukeradministrasjonssystem med:
- Innloggingssystem
- Forskjellige brukerroller (admin, bruker, gjest)
- CRUD-operasjoner for brukeradministrasjon
- JSON-basert "database" for lagring av brukere

## Installasjon

```bash
# Klon repositoriet
git clone https://github.com/rubbahtehlol/Flask_Fix.git
cd Flask_Fix

# Opprett et virtuelt miljø
python -m venv venv

# Aktiver miljøet
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# Installer avhengigheter
pip install flask

# Kjør applikasjonen
python app.py
```

## Oppgaver

Applikasjonen inneholder bevisst innlagte feil av forskjellige typer:
- Syntaksfeil
- Logiske feil
- Navnefeil
- Manglende sjekker
- Feil i templates
- Problemer med databehandling

Din oppgave er å identifisere og fikse disse feilene. Se [Git-branching Guide](GIT-BRANCHING-GUIDE.md) for strukturert tilnærming til feilsøking med Git-brancher.

## Brukerinformasjon

For testing (når feilene er fikset) finnes det tre brukere:
- **Admin**: Brukernavn: admin1, Passord: admin123
- **Bruker**: Brukernavn: user1, Passord: user123
- **Gjest**: Brukernavn: gjest, Passord: gjest

## Filstruktur

```
Flask_Fix/
├── app.py                 # Hovedapplikasjonsfil (med feil)
├── Flask_JSON/
│   └── data.json          # JSON-"database"
├── templates/
│   ├── admin.html         # Admin-panel
│   ├── bruker.html        # Brukerside
│   ├── edit_user.html     # Redigeringsside
│   ├── gjest.html         # Gjesteside
│   └── login.html         # Innloggingsside
├── static/
│   ├── admin.css          # CSS for admin-siden
│   ├── bruker.css         # CSS for brukersiden
│   ├── edit_user.css      # CSS for redigeringssiden
│   ├── gjest.css          # CSS for gjestesiden
│   └── login.css          # CSS for innloggingssiden
├── .gitignore             # Git-ignore fil
├── README.md              # Denne filen
└── GIT-BRANCHING.md       # Guide for Git-branching
```

## Læringsmål

- Feilsøking i Flask-applikasjoner
- Forståelse av vanlige feil i webapplikasjoner
- Praksis med Git og branching-strategier
- Debugging-teknikker
- Håndtering av brukerdata og autentisering
