import pandas as pd
import argparse

# Argumentparser für Shell-Parameter
parser = argparse.ArgumentParser(description='This script processes raw CSV data from Car Scanner. It filters out outliers, selects columns, and converts the data from row-based to column-based format.')
parser.add_argument('--input_path', type=str, required=True, help='Car Scanner CSV-Datei Dateiname')
parser.add_argument('--output_path', type=str, required=True, help='Bereinigte CSV-Datei Dateiname')

args = parser.parse_args()

# Lade die ursprüngliche Datei
input_path = args.input_path
data = pd.read_csv(input_path, delimiter=';')

# Entferne die überflüssige Spalte
data_clean = data.drop(columns=['Unnamed: 4'])

# Definiere die gewünschten PIDs
selected_pids = [
    '[BMS] Battery DC Voltage', '[BMS] Battery Current', '[BMS] State of Health', '[BMS] Battery Power', 
    '[BMS] Battery Max Temperature', '[BMS] Battery Min Temperature', '[BMS] State of Charge BMS'
]

# Filtere die gewünschten PIDs
data_filtered = data_clean[data_clean['PID'].isin(selected_pids)]

# Wandle die Daten in ein breites Format um
data_wide = data_filtered.pivot_table(index='SECONDS', columns='PID', values='VALUE', aggfunc='first')

# Konvertiere den Index zurück in eine Spalte
data_wide.reset_index(inplace=True)

# Konvertiere die SECONDS-Spalte zu numerischen Werten
data_wide['SECONDS'] = pd.to_numeric(data_wide['SECONDS'], errors='coerce')

# Filtere die Daten ab Sekunde 58.500
data_wide_filtered = data_wide[data_wide['SECONDS'] >= 58800]

# Interpoliere die Daten
data_interpolated = data_wide_filtered.interpolate(method='linear', limit_direction='both')

# Berechne die mittlere Temperatur
data_interpolated['Average temperature'] = data_interpolated[['[BMS] Battery Max Temperature', '[BMS] Battery Min Temperature']].mean(axis=1)

# Speichere die bereinigten Daten im breiten Format
output_path = args.output_path
data_interpolated.to_csv(output_path, index=False)

# Ausgabe des Speicherpfads (optional)
print(f'Die bereinigte CSV-Datei wurde gespeichert unter: {output_path}')
