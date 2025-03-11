import gymnasium as gym
import random
import numpy as np

# Mohamad Ali GHADDAR
# Ali ABDALLAH

# priciser l'environnement que vous souhaitez etudier parmi la liste :
# - CliffWalking-v0 : https://gymnasium.farama.org/environments/toy_text/cliff_walking/
# - Blackjack-v1 : https://gymnasium.farama.org/environments/toy_text/blackjack/
# - Taxi-v3 : https://gymnasium.farama.org/environments/toy_text/taxi/
# - FrozenLake-v1 : https://gymnasium.farama.org/environments/toy_text/frozen_lake/
# - one of the minigrid environemnts like MiniGrid-Fetch-8x8-N3-v0
      # liste des environnement mini grid https://minigrid.farama.org/environments/minigrid/


# Avec affichage
# env = gym.make("CliffWalking-v0", render_mode="human")
# Sans  affichage
env = gym.make("CliffWalking-v0")
observation, info = env.reset()
observation = str(observation)
num_states = env.observation_space.n

Q = { observation : np.zeros(env.action_space.n)}
print(Q)

# Create a mapping from numerical states to string states
state_map = {i: f's{i}' for i in range(48)}
reverse_state_map = {v: k for k, v in state_map.items()}

# Create a mapping from action numbers to action names
action_map = {0: "up", 1: "right", 2: "down", 3: "left"}
reverse_action_map = {v: k for k, v in action_map.items()}

# Define the action space
actions = [0, 1, 2, 3]

# Define the starting state
s0 = "s36"

# Function to observe the next state
def observe_next_state(state, action):
    state_int = reverse_state_map[state]
    row = state_int // 12
    col = state_int % 12
    if action == 0: 
        row = max(0, row - 1)
    elif action == 1:  
        col = min(11, col + 1)
    elif action == 2:  
        row = min(3, row + 1)
    elif action == 3: 
        col = max(0, col - 1)
    next_state_int = row * 12 + col

    # Handle cliff locations
    if row == 3 and 1 <= col <= 10:
        next_state_int = 36  # Return to start location

    return state_map[next_state_int]

# Function to observe the reward based on state and action
def observe_reward(state, action):
    next_state = observe_next_state(state, action)
    next_state_int = reverse_state_map[next_state]  
    if next_state_int == 36: 
        return -100
    elif next_state_int == 47:  
        return 50
    else:
        return -1

# Check if the state is the terminal state
def isEnd(state):
    state_int = reverse_state_map[state]
    return state_int == 47

def policy(observation, epsilon=0.9):
   # if random > 0.9 then explore (10% chance)
   # if random < 0.9 then exploit (90% chance) = 90% greedy
   if random.random() > epsilon :
      return random.randint(0,env.action_space.n -1)
   else :
      # return the action key with the higest associated value
      return np.argmax(Q[observation])

def updateQ(observation, action, reward, next_observation, alpha= 0.1, gamma=0.9):  
   if next_observation not in Q :
      Q[next_observation]= np.zeros(env.action_space.n)     
   # update rule for Q-learning
   Q[observation][action] = ( ( 1-alpha ) * Q[observation][action] ) + ( alpha * ( reward + (gamma* np.max(Q[next_observation]  ) ) ))
        


for _ in range(10000):
   # ici vous devez appeler votre politique
   action = policy(observation)  # User-defined policy function 
   next_observation, reward, terminated, truncated, info = env.step(action)
   next_observation = str(next_observation)
   updateQ(observation, action, reward, next_observation)
   observation = next_observation

   if terminated or truncated:
      observation, info = env.reset()
      observation = str(observation)
      if observation not in Q:
                      Q = {observation : np.zeros(env.action_space.n)}
env.close()
