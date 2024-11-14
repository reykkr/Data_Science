def player(prev_play, opponent_history=[]):
    # Add previous play to the history list if it's not the first play
    if prev_play:
        opponent_history.append(prev_play)
    
    # Initialize a default guess
    guess = "R"

    # If there's enough history, look for patterns
    if len(opponent_history) > 2:
        # Track the opponent's last 3 moves as a pattern key
        last_three = ''.join(opponent_history[-3:])
        
        # Dictionary to count occurrences of the sequence following each pattern
        pattern_counts = {'RR': 0, 'RP': 0, 'RS': 0, 'PR': 0, 'PP': 0, 'PS': 0, 'SR': 0, 'SP': 0, 'SS': 0}
        
        # Populate the pattern counts
        for i in range(len(opponent_history) - 3):
            pattern = ''.join(opponent_history[i:i+2])
            next_move = opponent_history[i+2]
            pattern_counts[pattern] += 1
        
        # Most common pattern
        most_likely_pattern = max(pattern_counts, key=pattern_counts.get)
        
        # Guess the counter move
        if most_likely_pattern[-1] == "R":
            guess = "P"  # Paper beats Rock
        elif most_likely_pattern[-1] == "P":
            guess = "S"  # Scissors beat Paper
        elif most_likely_pattern[-1] == "S":
            guess = "R"  # Rock beats Scissors
    
    # Return the counter move guess
    return guess
