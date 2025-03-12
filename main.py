import random
import matplotlib.pyplot as plt

class GameAgent:
    def __init__(self, secret_number, difficulty):
        self.secret_number = secret_number
        self.difficulty = difficulty
        self.max_attempts = {'facil': 9, 'medio': 6, 'dificil': 3}[difficulty]
        self.attempts = 0
        self.state = "Esperando tentativa."
        self.history = []

    def make_guess(self, guess):
        self.attempts += 1
        self.history.append(guess)

        if guess == self.secret_number:
            self.state = "Acertou!"
            return "Parabéns! Você acertou o número."

        elif self.attempts >= self.max_attempts:
            self.state = "Fim do jogo."
            return f"Game over! O número era {self.secret_number}."

        difference = abs(guess - self.secret_number)
        
        if self.difficulty == 'facil':
            if difference > 25:
                return "O número é bem maior." if guess < self.secret_number else "O número é bem menor."
            elif difference <= 10:
                return "O número é um pouco maior." if guess < self.secret_number else "O número é um pouco menor."
            else:
                return "O número é maior." if guess < self.secret_number else "O número é menor."
        
        elif self.difficulty == 'medio':
            if difference <= 10:
                return "O número é um pouco maior." if guess < self.secret_number else "O número é um pouco menor."
            else:
                return "O número é maior." if guess < self.secret_number else "O número é menor."
        
        else:  
            return "O número é maior." if guess < self.secret_number else "O número é menor."
difficulty = ""
while difficulty not in ["facil", "medio", "dificil"]:
    difficulty = input("Escolha a dificuldade (facil, medio, dificil): ").strip().lower()


agent = GameAgent(secret_number=random.randint(1, 100), difficulty=difficulty)

while agent.attempts < agent.max_attempts and agent.state != "Acertou!":
    try:
        guess = int(input("Digite um número: "))
        print(agent.make_guess(guess))
    except ValueError:
        print("Por favor, insira um número válido.")



def plot_attempts(agent):
    plt.figure(figsize=(8,5))
    plt.plot(range(1, len(agent.history) + 1), agent.history, marker='o', linestyle='-')
    plt.axhline(y=agent.secret_number, color= 'r', linestyle='--', label="Número Secreto")
    plt.xlabel("Tentativas")
    plt.ylabel("Valor do palpite")
    plt.title("Evolução das tentativas do jogador")
    plt.legend()
    plt.show()


plot_attempts(agent)

