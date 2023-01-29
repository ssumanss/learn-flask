import time
from locust import HttpUser, task, between

class AuthenticateUser(HttpUser):
    timer = between(1, 10)

    @task
    def authenticate_task(self):
        self.client.get("/login")



    def on_start(self):
        self.client.post("/login", json={"username":"testuser",
                                            "password":"testpass"})