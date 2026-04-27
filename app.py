import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SecDataOps Dashboard", layout="wide")
st.title("🛡️ Sistema de Monitoramento SSH")

# Caminhos absolutos para evitar erro de "Arquivo não encontrado"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_DATA = os.path.join(BASE_DIR, 'data', 'processed_logs.csv')
BLOCKED_FILE = os.path.join(BASE_DIR, 'blocked_ips.txt')

try:
    # 1. Carregamento dos dados processados
    if os.path.exists(PROCESSED_DATA):
        df = pd.read_csv(PROCESSED_DATA)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🌐 Tentativas por País")
            st.bar_chart(df['country'].value_counts())
        
        with col2:
            st.subheader("👤 Usuários Mais Visados")
            st.table(df['user'].value_counts().head(5))
            
        # 2. Exibição dos IPs Bloqueados
        st.subheader("🚫 IPs Bloqueados pela IA (Anomalias)")
        
        if os.path.exists(BLOCKED_FILE):
            with open(BLOCKED_FILE, "r") as f:
                # Usamos set() para não repetir o mesmo IP várias vezes na tela
                conteudo = f.read().splitlines()
                ips_unicos = sorted(list(set(conteudo))) 
                
                if ips_unicos:
                    # Cria uma caixa de texto formatada com os IPs
                    st.text_area(label="Lista de IPs no Firewall", value="\n".join(ips_unicos), height=200)
                else:
                    st.warning("O arquivo de bloqueio está vazio.")
        else:
            st.info("Nenhum IP foi bloqueado pelo modelo de IA ainda.")
    else:
        st.error("Arquivo 'processed_logs.csv' não encontrado em data/. Execute o monitor.sh.")

except Exception as e:
    st.error(f"Erro ao carregar o dashboard: {e}")
