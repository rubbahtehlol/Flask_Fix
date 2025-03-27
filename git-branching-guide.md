# Git-branching Guide for Feilsøkingsoppgaver

Dette dokumentet gir en oversikt over foreslåtte Git-brancher for feilsøkingsoppgaver i denne Flask-applikasjonen. Hver branch fokuserer på en spesifikk type feil for organisert og strukturert læring.

## Oppstart av Git-repositoriet

```bash
# Initialisere Git-repositoriet
git init

# Legge til alle filer
git add .

# Første commit med den feilaktige kodebasen
git commit -m "Initial commit med feil for feilsøkingsoppgaver"
```

## Foreslåtte Brancher

### 1. `fix/database-errors`
Fokus på feil relatert til JSON-databasen og databehandling.

```bash
git checkout -b fix/database-errors
```

Feil som skal fikses:
- Returnerer `None` i stedet for tom liste i `get_users()`
- Mangler mappestruktursjekk for datafilens plassering
- Mangler `indent` parameter i `json.dump()`
- Mangler null-sjekk før man itererer gjennom brukerliste

### 2. `fix/login-authentication`
Fokus på feil relatert til innlogging og autentisering.

```bash
git checkout -b fix/login-authentication
```

Feil som skal fikses:
- Feil variabelnavn (`passord` vs `password`)
- Feil håndtering av passordsjekkingen
- Syntaksfeil i `match-case` strukturen

### 3. `fix/template-rendering`
Fokus på feil relatert til rendering av templates.

```bash
git checkout -b fix/template-rendering
```

Feil som skal fikses:
- Skrivefeil i template-navn (`brukerr.html` vs `bruker.html`)
- Mangler å sende `users` til admin-template
- Feil sti til CSS i admin.html
- Feil nøkkelnavn i admin.html (`userRole` vs `role`)

### 4. `fix/crud-operations`
Fokus på feil relatert til CRUD-operasjoner.

```bash
git checkout -b fix/crud-operations
```

Feil som skal fikses:
- Feil action-path i admin-skjema
- Manglende formdata for `role` i update-funksjonen
- Udefinert variabel (`role`) i update-funksjonen
- Logisk feil i filtreringen ved sletting av bruker

### 5. `fix/ui-issues`
Fokus på feil relatert til brukergrensesnittet.

```bash
git checkout -b fix/ui-issues
```

Feil som skal fikses:
- Syntaksfeil i onclick JavaScript (manglende } i tekststrengen)
- Manglende sjekk om `users` er definert i template
- Feil i CSS-stier og statiske filer

### 6. `feature/error-handling`
Legge til bedre feilhåndtering i applikasjonen.

```bash
git checkout -b feature/error-handling
```

Funksjoner som skal implementeres:
- Legge til spesifikke feilmeldinger til brukeren
- Implementere Flask flash-meldinger
- Legge til loggingssystem
- Forbedre try-except blokkene

### 7. `feature/security-improvements`
Forbedre sikkerheten i applikasjonen.

```bash
git checkout -b feature/security-improvements
```

Funksjoner som skal implementeres:
- Passordhashing
- CSRF-beskyttelse
- Input-validering
- Sesjonshåndtering

## Arbeidsflyt for å Løse Oppgaver

1. Sjekk ut releveant branch (f.eks. `git checkout fix/database-errors`)
2. Identifiser og fiks feilene i den aktuelle kategorien
3. Test applikasjonen for å sikre at feilene er løst
4. Commit endringene (`git commit -m "Fikset database-feil"`)
5. Gå tilbake til main branch (`git checkout main`)
6. Merge inn den fiksede branchen (`git merge fix/database-errors`)

Denne arbeidsmetoden simulerer en realistisk arbeidsprosess i et prosjekt og gir god praksis i både feilsøking og Git-branching.
