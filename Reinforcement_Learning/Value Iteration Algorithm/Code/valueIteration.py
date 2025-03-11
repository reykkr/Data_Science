import random

# The value iteration algorithme to calulate the value function for each state
def valueIteration(states, actions, transitions, rewards, epsilon, gamma):
    # delta to mesure the difference between state values in precedent and current function
    delta=1
    # initialise the value function to 0 for all states
    V = {s: 0.0 for s in states}
    i= 1
    # value iteration loop with stop condition  delta < epsilon
    while delta > epsilon:
        delta = 0
        for s in states:
            v = V[s]
            max_value = float('-inf')
            for a in actions:
                # Calculate the expected value for each action
                action_value = 0
                for s_prime, prob in transitions(s, a).items():
                    action_value += prob * (rewards(s, a) + gamma * V[s_prime])
                if action_value > max_value:
                    max_value = action_value
            V[s] = max_value
            delta = max(delta, abs(v - V[s]))
        print(f"Iteration {i} values: {V}")
        i += 1
    return V


# pi(s) = argmax V(s) for all a in A
# the policy for a given state returns the best action to perform in this state knowing V
def pi(V, state, actions, transitions, rewards, gamma):
    best_action = max(actions, key=lambda a: sum(transitions(state, a)[s_prime] * (rewards(state, a) + gamma * V.get(s_prime, 0)) for s_prime in transitions(state, a)))
    return best_action
    

# Run an episode of game from a given initial state to end state following the optimal policy pi
def playEpisode(s0, isEnd, V, actions, transitions, rewards, gamma):
    state = s0 #set cursor to initial state

    while not isEnd(state):
        action = pi(V, state, actions, transitions, rewards, gamma)
        transition_probs = transitions(state, action)
        next_state = max(transition_probs.keys(), key=lambda s_prime: transition_probs[s_prime])
        reward = rewards(state, action)  # Call rewards function with only two arguments
        print(f"State: {state}, Action: {action}, Next State: {next_state}, Reward: {reward}")
        state = next_state
    