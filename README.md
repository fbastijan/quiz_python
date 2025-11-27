

# KVIZ APLIKACIJA za RS

## Opis
Kviz aplikacija napisana u pythonu, koja  se pokreće u CLi-u

## Funkcionalnosti
-  Započni kviz sa pitanjima iz baze
-  Prikaži scoreboard sa rangiranjem igrača
-  Dodaj nova pitanja u bazu
-  Spremi rezultate igrača


## Instalacija

### 1. Kloniraj/preuzmi projekt
```bash
git clone https://github.com/fbastijan/quiz_python
```

### 2. Kreiraj virtualno okruženje
```bash
conda create -n quiz_py
```

### 3. Aktiviraj virtualno okruženje


```bash
conda activate quiz_py
```


### 4. Instaliraj ovisnosti
```bash
pip install -r requirements.txt
```

## Pokretanje

### Kao Python skriptu:
```bash
python main.py
```

### Kao standalone executable (Windows):
```bash
pyinstaller main.spec
.\dist\main.exe
```

## Datoteke podataka

### questions.json
Sadrži pitanja sa opcijama i odgovorima.

### players.json
Sprema rezultate igrača i njihove bodove.

## Korištenje

1. **Započni kviz** - Unesi svoje ime i odgovori na pitanja
2. **Pokaži scoreboard** - Vidi rang za sve igrače
3. **Dodaj pitanje** - Kreiraj novo pitanje za bazu
4. **Exit** - Izlaz iz aplikacije


