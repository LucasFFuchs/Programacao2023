#A solução está na linha 86
#Chat GPT pode ter deixado passar batido esse erro, não sei exatamente o que fez com que ele errasse isso.

import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ['pedra', 'papel', 'tesoura']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "Empate!"
    elif (
        (user_choice == 'pedra' and opponent_choice == 'tesoura') or
        (user_choice == 'papel' and opponent_choice == 'pedra') or
        (user_choice == 'tesoura' and opponent_choice == 'papel')
    ):
        return "Jogador 1 venceu!"
    else:
        return "Jogador 2 venceu!"

def play_computer_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Resultado", f"Você escolheu: {user_choice}\nO computador escolheu: {computer_choice}\n\n{result}")

def play_2player_game(player1_choice, player2_choice):
    result = determine_winner(player1_choice, player2_choice)
    messagebox.showinfo("Resultado", f"Jogador 1 escolheu: {player1_choice}\nJogador 2 escolheu: {player2_choice}\n\n{result}")

def create_gui():
    window = tk.Tk()
    window.title("Pedra, Papel e Tesoura")

    def handle_computer_button_click():
        window.destroy()
        create_computer_gui()

    def handle_2player_button_click():
        window.destroy()
        create_2player_gui()

    computer_button = tk.Button(window, text="Contra Computador", font=("Arial", 16), width=20, height=3, command=handle_computer_button_click)
    computer_button.pack(pady=20)

    player_button = tk.Button(window, text="Dois Jogadores", font=("Arial", 16), width=20, height=3, command=handle_2player_button_click)
    player_button.pack()

    window.mainloop()

def create_computer_gui():
    window = tk.Tk()
    window.title("Pedra, Papel e Tesoura - Contra Computador")

    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)

    def handle_button_click(user_choice):
        play_computer_game(user_choice)

    rock_button = tk.Button(button_frame, text="Pedra", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click("pedra"))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = tk.Button(button_frame, text="Papel", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click("papel"))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = tk.Button(button_frame, text="Tesoura", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click("tesoura"))
    scissors_button.grid(row=0, column=2, padx=10)

    window.mainloop()



def create_2player_gui():
    window = tk.Tk()
    window.title("Pedra, Papel e Tesoura - Dois Jogadores")

    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)

    def handle_button_click(player, user_choice):

        #SOLUÇÃO: 
        global player1_choice #Definir essa variável como global

        if player == 1:
            player1_choice = user_choice 
            player_label.config(text="Jogador 2, faça sua escolha.")
        else:
            play_2player_game(player1_choice, user_choice) 
            window.destroy()

    player1_choice = ""

    rock_button = tk.Button(button_frame, text="Pedra", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click(1, "pedra"))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = tk.Button(button_frame, text="Papel", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click(1, "papel"))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = tk.Button(button_frame, text="Tesoura", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click(1, "tesoura"))
    scissors_button.grid(row=0, column=2, padx=10)

    player_label = tk.Label(window, text="Jogador 1, faça sua escolha.", font=("Arial", 14))
    player_label.pack(pady=20)

    rock_button2 = tk.Button(button_frame, text="Pedra", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click(2, "pedra"))
    rock_button2.grid(row=2, column=0, padx=10)

    paper_button2 = tk.Button(button_frame, text="Papel", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click(2, "papel"))
    paper_button2.grid(row=2, column=1, padx=10)

    scissors_button2 = tk.Button(button_frame, text="Tesoura", font=("Arial", 16), width=10, height=3, command=lambda: handle_button_click(2, "tesoura"))
    scissors_button2.grid(row=2, column=2, padx=10)

    window.mainloop()

create_gui()
