#!/bin/bash

# Descobre o caminho da pasta onde o monitor.sh está e sobe um nível
BASE_DIR=$(dirname "$(dirname "$(readlink -f "$0")")")
cd "$BASE_DIR"

echo "--- Local do projeto: $BASE_DIR ---"

echo "--- Instalando dependências ---"
pip3 install -r requirements.txt

echo "--- Processando logs e treinando IA ---"
# Agora o caminho será relativo à raiz do projeto
python3 scripts/parser.py

echo "--- Iniciando Dashboard ---"
streamlit run app.py
