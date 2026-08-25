import random
from locust import HttpUser, task, between

class UsuarioAPI(HttpUser):
    # Think Time: Tempo de espera entre 1 e 5 segundos
    wait_time = between(1, 5)

    def on_start(self):
        """Executado 1x na criação do usuário virtual"""
        self.login()

    def login(self):
        """Autenticação inicial"""
        with self.client.post(
            "/api/login",
            json={"username": "usuario_teste", "password": "senha_teste"},
            name="POST /api/login",
            catch_response=True
        ) as resposta:
            if resposta.status_code != 200:
                resposta.failure(f"Falha na autenticacao: HTTP {resposta.status_code}")
            else:
                resposta.success()

    @task(5)
    def consultar_usuarios(self):
        """Peso 5 (50% do tráfego) - Rota de alta demanda com SLA de 500ms"""
        with self.client.get("/api/usuarios", name="GET /api/usuarios", catch_response=True) as resposta:
            if resposta.status_code != 200:
                resposta.failure(f"Erro no servidor: HTTP {resposta.status_code}")
            elif resposta.elapsed.total_seconds() > 0.5:
                resposta.failure(f"SLA Violado: Tempo de resposta {resposta.elapsed.total_seconds():.2f}s (Limite: 0.5s)")
            else:
                resposta.success()

    @task(3)
    def consultar_perfil(self):
        """Peso 3 (30% do tráfego) - Consulta de perfil"""
        with self.client.get("/api/perfil", name="GET /api/perfil", catch_response=True) as resposta:
            if resposta.status_code != 200:
                resposta.failure(f"Erro ao consultar perfil: HTTP {resposta.status_code}")
            else:
                resposta.success()

    @task(2)
    def consultar_dashboard(self):
        """Peso 2 (20% do tráfego) - Consulta de dashboard"""
        with self.client.get("/api/dashboard", name="GET /api/dashboard", catch_response=True) as resposta:
            if resposta.status_code != 200:
                resposta.failure(f"Erro ao consultar dashboard: HTTP {resposta.status_code}")
            else:
                resposta.success()