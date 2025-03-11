import random
import qlearning
import matplotlib.pyplot as plt
#from gille4_oracle import next_state, reward, isEnd, states, actions
#from gille4_prob_oracle import next_state, reward, isEnd, states, actions
#from gille6_oracle import next_state, reward, isEnd, states, actions
from gille6_prob_oracle import next_state, reward, isEnd, states, actions


def transitions(state, action):
    return next_state(state, action)

def simulate(state, action):
    return next_state(state, action)

initial_state = "s0"

n_episodes = 100
actions_per_episode = []  
reward_per_episode = [] 

Q = {}  
for i in range(n_episodes):
    Q, trace = qlearning.playEpisode(Q, next_state, reward, initial_state, isEnd, actions)
    
    actions_per_episode.append(len(trace))  
    total_reward = sum(step[2] for step in trace) 
    reward_per_episode.append(total_reward)  
    
    qlearning.printTrace("Episode-"+str(i), trace)
    qlearning.printStat(Q, trace)
    qlearning.printQ("Result: ", Q)


plt.plot(range(n_episodes), actions_per_episode)
plt.xlabel('Episode')
plt.ylabel('Actions')
plt.title('Evolution of actions by episode')
plt.show()

plt.plot(range(n_episodes), reward_per_episode)
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Evolution of rewards by episode')
plt.show()
