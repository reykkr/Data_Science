import random
from gille4_oracle import next_state, reward, isEnd

def qlearning(states, actions, transitions, reward, epsilon, gamma):
    Q = {s: {a: 0 for a in actions} for s in states}
    for _ in range(1000):  #
        state = random.choice(states)  
        while not isEnd(state):  
            if random.random() < epsilon:
                action = random.choice(actions)  
            else:
                action = max(Q[state], key=Q[state].get)  
            next_state = transitions(state, action)  
            r = reward(state, action)  
            Q[state][action] += epsilon * (r + gamma * max(Q[next_state].values()) - Q[state][action])
            state = next_state 
    return Q

def pi(Q, state, actions, simulate, transitions, reward, gamma):
    best_action = max(actions, key=lambda a: sum(transitions(state, a)[s_prime] * (reward(state, a) + gamma * Q.get((s_prime, a), 0)) for s_prime in transitions(state, a)))
    return best_action


def playEpisode(Q, next_state, reward, s0, isEnd, actions, epsilon=0.9, alpha=0.1, horizon=1000, gamma=0.9):
    state = s0
    trace = []
    if state not in Q:
        Q[state] = {a: 0 for a in actions}
    
    while not isEnd(state) and horizon > 0:
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(actions, key=lambda a: Q[state].get(a, 0))
        next_state_val = next_state(state, action)
        r = reward(state, action)
        trace.append((state, action, r, next_state_val))
        if (next_state_val not in Q):
            Q[next_state_val] = {a: 0 for a in actions}
        Q[state][action] = Q[state].get(action, 0) + alpha * (r + gamma * max(Q[next_state_val].values(), default=0) - Q[state].get(action, 0))
        state = next_state_val
        horizon -= 1
    return Q, trace


def printTrace(episode_name, trace):
    print(f"Episode: {episode_name}")
    for i, step in enumerate(trace):
        state, action, reward, next_state = step
        print(f"Step {i}: State={state}, Action={action}, Reward={reward}, Next State={next_state}")

def printStat(Q, trace):
    total_reward = sum(step[2] for step in trace)
    print(f"Total reward: {total_reward}")
    print("Q-values:")
    for state_action, value in Q.items():
        state, action = state_action
        print(f"State={state}, Action={action}, Q-value={value}")

def printQ(header, Q):
    print(header)
    for state_action, value in Q.items():
        state, action = state_action
        print(f"State={state}, Action={action}, Q-value={value}")


