# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

# Diccionario para almacenar las combinaciones de las jugadas previas
play_order = [{
    "RR": 0,
    "RP": 0,
    "RS": 0,
    "PR": 0,
    "PP": 0,
    "PS": 0,
    "SR": 0,
    "SP": 0,
    "SS": 0,
}]

# Diccionario de respuestas ideales
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

# Función para jugar, ahora con secuencias de 2 a 5 jugadas
def player(prev_play, opponent_history=[], epsilon=0.07):
    if not prev_play:
        prev_play = 'R'  # Si no hay jugada previa, comenzar con 'R'
    
    # Guardar la jugada previa del oponente
    opponent_history.append(prev_play)

    # Ajustar epsilon para disminuir la exploración conforme se avanza
    if len(opponent_history) > 50:
        epsilon = max(0.1, epsilon - 0.001)  # Reducir gradualmente epsilon
    
    # Predecir basándonos en secuencias de 2 a 5 jugadas
    best_move = None
    for seq_len in range(2, 6):  # Ahora cubrimos secuencias de 2, 3, 4 y 5 jugadas
        if len(opponent_history) >= seq_len:
            sequence = "".join(opponent_history[-seq_len:])

            # Registrar la combinación de jugadas
            if len(sequence) == seq_len:
                if sequence not in play_order[0]:
                    play_order[0][sequence] = 0
                play_order[0][sequence] += 1

            # Filtrar las jugadas posibles y contar su frecuencia
            potential_plays = [
                sequence + "R", sequence + "P", sequence + "S"
            ]
            sub_order = {k: play_order[0][k] for k in potential_plays if k in play_order[0]}

            # Si hay jugadas posibles, elegir la más frecuente
            if sub_order:
                prediction = max(sub_order, key=sub_order.get)[-1:]
                best_move = ideal_response[prediction]
    
    # Si no se encuentra ninguna predicción (es posible al principio), elegir aleatoriamente
    if best_move is None:
        best_move = random.choice(["R", "P", "S"])

    # Introducir la aleatoriedad con probabilidad epsilon
    if random.random() < epsilon:
        guess = random.choice(["R", "P", "S"])
    else:
        guess = best_move

    return guess
