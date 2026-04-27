# Limpeza e ML

import os
import re
import pandas as pd
from geolite2 import geolite2
from sklearn.ensemble import IsolationForest

# Adicione estas linhas logo no início do parser.py para achar a pasta correta
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, 'data', 'auth_sample.log')
SAVE_FILE = os.path.join(BASE_DIR, 'data', 'processed_logs.csv')
BLOCKED_FILE = os.path.join(BASE_DIR, 'blocked_ips.txt')

def block_ip(ip):
    # Simulação de firewall para segurança do portfólio
    with open("blocked_ips.txt", "a") as f:
        f.write(f"{ip}\n")
    # Comando real (comentado): os.system(f"sudo ufw deny from {ip}")

def parse_logs():
    pattern = r"(?P<date>\w+ \d+ \d+:\d+:\d+) .* Failed password for (?P<user>.*) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
    reader = geolite2.reader()
    data = []

    # Lê o log da pasta data/
    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                match = re.search(pattern, line)
                if match:
                    d = match.groupdict()
                    # Adiciona Geolocation
                    loc = reader.get(d['ip'])
                    d['country'] = loc['country']['names']['en'] if loc and 'country' in loc else "Unknown"
                    data.append(d)
    except FileNotFoundError:
        return pd.DataFrame()

    df = pd.DataFrame(data)
    if not df.empty:
        # ML: Detecção de anomalia baseada na frequência de tentativas
        df['attempts'] = df.groupby('ip')['ip'].transform('count')
        model = IsolationForest(contamination=0.3, random_state=42)
        df['is_attack'] = model.fit_predict(df[['attempts']])
        
        # Bloqueia se is_attack == -1
        for ip in df[df['is_attack'] == -1]['ip'].unique():
            block_ip(ip)
            
        df.to_csv(SAVE_FILE, index=False)
    return df

if __name__ == "__main__":
    parse_logs()
    print("Logs processados e firewall atualizado.")
