import numpy as np
import random
import matplotlib.pyplot as plt
from morpion1 import QLearningAgent  

class QLearningAgent2:
    def __init__(self, epsilon=0.1, alpha=0.5, gamma=1):
        self.epsilon = epsilon  
        self.alpha = alpha  
        self.gamma = gamma  
        self.q_values = {}  
        self.total_reward = 0  
        self.rewards_history = [] 

    def get_action(self, state, possible_actions):
        if random.uniform(0, 1) < self.epsilon:
            action = random.choice(possible_actions)
        else:
            max_q_value = -float('inf')
            best_actions = []
            for a in possible_actions:
                q_value = self.q_values.get((state, a), 0)
                if q_value > max_q_value:
                    max_q_value = q_value
                    best_actions = [a]
                elif q_value == max_q_value:
                    best_actions.append(a)
            action = random.choice(best_actions)
        return action

    def learn(self, state, action, reward, next_state, possible_next_actions):
        old_q_value = self.q_values.get((state, action), 0)
        if len(possible_next_actions) == 0:
            target = reward
        else:
            max_next_q_value = max(self.q_values.get((next_state, a), 0) for a in possible_next_actions)
            target = reward + self.gamma * max_next_q_value
        new_q_value = old_q_value + self.alpha * (target - old_q_value)
        self.q_values[(state, action)] = new_q_value

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != ' ':
            return board[0][col]
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != ' ':
        return board[0][0]
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != ' ':
        return board[0][2]
    return None

def print_board(board):
    for row in board:
        print('|'.join(row))
    print()

def next_state(board, action, player):
    row, col = action
    board[row][col] = player
    winner = check_winner(board)
    if winner:
        if winner == 'O':
            reward = 1
        else:
            reward = 0
        return board, reward, True
    elif ' ' not in np.array(board).flatten():
        reward = 0  
        return board, reward, True
    else:
        reward = 0
        return board, reward, False

def play_game(morpion1, morpion2):
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:

        # Player 1 (Morpion1)
        state = tuple(map(tuple, board))
        possible_actions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        action = morpion1.get_action(state, possible_actions)
        board, reward, done = next_state(board, action, 'X')
        if done:
            break

        # Player 2 (Morpion2)
        state = tuple(map(tuple, board))
        possible_actions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
        action = morpion2.get_action(state, possible_actions)
        board, reward, done = next_state(board, action, 'O')
        morpion2.learn(state, action, reward, tuple(map(tuple, board)), possible_actions)
    
    
    morpion2.rewards_history.append(morpion2.total_reward)
    if reward == 1:
        morpion2.total_reward += 1

    print("Final board:")
    print_board(board)
    if reward == 1:
        print("Morpion2 wins!")
    elif reward == 0:
        print("It's a tie!")
    else:
        print("Morpion1 wins!")

def main(num_games):
    morpion2 = QLearningAgent2()  
    morpion1 = QLearningAgent()  

    rewards_morpion2 = []
    rewards_morpion1 = []

    for i in range(num_games):
        print(f"Game {i+1}:")
        if i % 2 == 0:
            play_game(morpion2, morpion1)
        else:
            play_game(morpion1, morpion2)
        rewards_morpion2.append(morpion2.total_reward)
        rewards_morpion1.append(morpion1.total_reward)

    plt.plot(range(1, num_games+1), rewards_morpion2, label='Morpion2')
    plt.plot(range(1, num_games+1), rewards_morpion1, label='Morpion1')
    plt.xlabel('Game')
    plt.ylabel('Cumulative Reward')
    plt.title('Learning Curve - Morpion2 vs Morpion1')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    num_games = int(input("Enter the number of games to simulate: "))
    main(num_games)
