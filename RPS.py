# Diccionario para almacenar las combinaciones de las jugadas previas
play_order = {}

# Diccionario de respuestas ideales
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

def player(prev_play, opponent_history=[]):
    # Si no hay jugada previa, iniciar con 'P'
    if not prev_play:
        prev_play = 'P'
    
    # Agregar la jugada previa al historial
    opponent_history.append(prev_play)
    
    # Configurar la longitud de la secuencia
    seq_len = 4  # Probar con longitud 4
    
    if len(opponent_history) >= seq_len:
        # Extraer los últimos movimientos
        sequence = "".join(opponent_history[-seq_len:])
        
        # Registrar la secuencia en el diccionario
        if sequence not in play_order:
            play_order[sequence] = 0
        play_order[sequence] += 1

        # Buscar patrones que coincidan con los últimos movimientos
        potential_plays = {
            seq[-1]: play_order[seq]
            for seq in play_order if seq.startswith(sequence[1:])
        }

        if potential_plays:
            # Predecir el movimiento más probable
            prediction = max(potential_plays, key=potential_plays.get)
            # Responder con el movimiento que lo derrota
            return ideal_response[prediction]

    # Respaldo dinámico: alternar entre 'P', 'R', y 'S'
    fallback = ["P", "R", "S"]
    return fallback[len(opponent_history) % 3]

