import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"  # Valor predeterminado

    # Convertir el historial del oponente en una cadena para buscar subcadenas
    history_str = "".join(opponent_history)

    # Intentar encontrar patrones en las últimas jugadas (ventana adaptable de 3 a 5)
    if len(opponent_history) >= 5:
        for window in range(5, 2, -1):  # Intentar con ventanas de 5 a 3
            sequence = history_str[-window:]  # Últimas jugadas como cadena
            if sequence in history_str[:-window]:
                next_index = history_str[:-window].index(sequence) + window
                if next_index < len(opponent_history):
                    predicted_move = opponent_history[next_index]
                    if predicted_move == "R":
                        guess = "P"
                    elif predicted_move == "P":
                        guess = "S"
                    else:
                        guess = "R"
                    break
    else:
        # Respaldo a probabilidad basada en frecuencia
        counts = {"R": opponent_history.count("R"),
                  "P": opponent_history.count("P"),
                  "S": opponent_history.count("S")}

        # Probabilidad ponderada según frecuencia
        total = sum(counts.values())
        if total > 0:
            weighted_choice = random.choices(["P", "S", "R"], 
                                             weights=[counts["R"], counts["P"], counts["S"]])[0]
            guess = {"R": "P", "P": "S", "S": "R"}[weighted_choice]

    return guess
