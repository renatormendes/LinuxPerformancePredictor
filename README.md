<img width="1368" height="749" alt="Captura de tela" src="https://github.com/user-attachments/assets/2a428443-ab21-4067-ac9d-3b4d912a1606" />
# 🛡️ Linux SecDataOps: Detecção de Intrusão com IA

Este projeto demonstra uma pipeline completa de Ciência de Dados aplicada à Segurança de Sistemas Linux. Ele monitora tentativas de invasão via SSH, utiliza Machine Learning para identificar comportamentos anômalos e automatiza o bloqueio de IPs maliciosos.

## 🚀 Funcionalidades
- **Parser de Logs:** Extração de dados brutos do `/var/log/auth.log` usando Regex.
- **Enriquecimento:** Geolocalização de IPs em tempo real com GeoLite2.
- **Inteligência Artificial:** Detecção de ataques de força bruta usando o algoritmo *Isolation Forest*.
- **Automação de Segurança:** Sistema de bloqueio automático de IPs (Simulação de Firewall).
- **Dashboard Interativo:** Visualização de métricas e ataques com Streamlit.

## 🛠️ Tecnologias
- **Linguagem:** Python 3.x
- **Bibliotecas:** Pandas, Scikit-Learn, Streamlit, Geolite2
- **Infraestrutura:** Bash Script, Linux (Ubuntu/Debian)

## 📁 Estrutura do Projeto
- `scripts/parser.py`: O "cérebro" que limpa os dados e aplica a IA.
- `app.py`: Interface visual do dashboard.
- `scripts/monitor.sh`: Automação que instala dependências e roda a pipeline.
- `data/`: Armazenamento de logs brutos e processados.

## ⚡ Como Executar
1. Clone o repositório.
2. Dê permissão ao script: `chmod +x scripts/monitor.sh`
3. Execute: `./scripts/monitor.sh`
