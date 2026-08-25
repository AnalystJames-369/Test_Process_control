import subprocess
import os
from datetime import datetime

# 1. Garante a criação da pasta de relatórios
os.makedirs("reports", exist_ok=True)

# 2. Carimbo de data/hora único
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# 3. Definição exata conforme a matriz do README.md
cenarios = [
    {
        "nome": "Carga_Nominal",
        "users": 50,
        "spawn_rate": 5,
        "run_time": "2m",
        "html_report": f"reports/relatorio_carga_nominal_{timestamp}.html"
    },
    {
        "nome": "Estresse",
        "users": 500,
        "spawn_rate": 25,
        "run_time": "3m",
        "html_report": f"reports/relatorio_estresse_{timestamp}.html"
    },
    {
        "nome": "Pico",
        "users": 5000,
        "spawn_rate": 100,
        "run_time": "1m",
        "html_report": f"reports/relatorio_pico_{timestamp}.html"
    },
    {
        "nome": "Endurance_Soak",
        "users": 500,
        "spawn_rate": 20,
        "run_time": "10m",
        "html_report": f"reports/relatorio_endurance_{timestamp}.html"
    }
]

print("🚀 Iniciando Suíte Automatizada de Testes de Performance (Locust)...\n")

for cenario in cenarios:
    print(f"▶️ Executando Cenário: {cenario['nome']}")
    print(f"   • Usuários Virtuais: {cenario['users']}")
    print(f"   • Taxa de Ramp-up: {cenario['spawn_rate']} VUs/seg")
    print(f"   • Duração: {cenario['run_time']}\n")

    comando = [
        "locust",
        "-f", "locustfile.py",
        "--headless",
        "--host", "http://localhost:8000",
        "--users", str(cenario["users"]),
        "--spawn-rate", str(cenario["spawn_rate"]),
        "--run-time", cenario["run_time"],
        "--html", cenario["html_report"]
    ]

    subprocess.run(comando)
    print(f"✅ Cenário {cenario['nome']} concluído! Relatório salvo em: {cenario['html_report']}\n")

print("🎉 Todos os cenários de testes foram executados com sucesso!")