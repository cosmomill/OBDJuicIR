# OBD-JuicIR: OBD Daten zur Widerstands- und SoH-Schätzung


## Installationsvoraussetzungen

1. Installiere Git: `apt-get install git`
2. Installiere pip für Python: `apt-get install python3-pip`
3. [Installiere virtualenv:](https://virtualenv.pypa.io/en/latest/) `apt-get install virtualenv`
4. Installiere libxcb-cursor `apt-get install libxcb-cursor-dev`

Dieses Projekt nutzt OBD-Daten, um den Widerstand und den State of Health (SoH) von Fahrzeugbatterien zu schätzen. Es besteht aus zwei Hauptskripten: `ir.py` und `soh.py`.

### Repository klonen

```shell
git clone https://github.com/cosmomill/OBDJuicIR.git
```


## Python Virtuelle Umgebung

Python unterstützt virtuelle Umgebungen (venv), somit müssen entsprechenden Abhängigkeiten nicht global installiert werden. Im Hauptverzeichnis wird Umgebung mit dem Befehl

```shell
cd OBDJuicIR
python3 -m venv venv
```

angelegt.

Möchte man diese Umgebung anschliessend verwenden, so muss diese aktiviert werden.

### Linux (Bash)

```shell
source ./venv/bin/activate
```


## Abhängigkeiten

Alle Abhängigkeiten lassen sich mit `pip` installieren, dazu muss nachfolgender Befehl ausgeführt werden.

```shell
pip install -r requirements.txt
```


## Dateien

### prepare_data.py

Dieses Skript verarbeitet CSV-Rohdaten aus Car Scanner. Filtern von Außreißern, Spaltenauswahl, zeilenbasierte Format -> spaltenbasiert umwandeln

```shell
python3 .\prepare_data.py --input_path="ioniq_vfl.csv" --output_path="test_data.csv"
```

Hilfe: `python3 .\iprepare_data.py --help`

### ir.py

Dieses Skript ist für die Berechnung des Innenwiderstands (IR) der Batterie zuständig. Es verwendet OBD-Daten zur Durchführung der Berechnungen und gibt den geschätzten Innenwiderstand aus.

```shell
python3 .\ir.py --data_path="test_data.csv" --threshold=0.99 --cells=96
```

Hilfe: `python3 .\ir.py --help`

### soh.py

Dieses Skript berechnet den State of Health (SoH) der Batterie basierend auf den OBD-Daten. Der SoH gibt Auskunft über die verbleibende Kapazität der Batterie im Vergleich zu ihrem Neuzustand.

```shell
python3 .\soh.py --data_path="test_data.csv"
```

Hilfe: `python3 .\soh.py --help`


## Support und Fragen

Im Akkudoktor Forum bitte -> forum.akkudoktor.net

Beschwerden: In den Spiegel bitte! Oder noch besser: Machs besser und lade es hoch!

Autor: Dr. Andreas Schmitz
