import random

states = ["s"+str(i) for i in range(4)]
actions = ["right", "down", "left", "up"]

transition_probabilities = {
    "s0": {"down": {"s1": 1.0}},
    "s1": {"right": {"s2": 1.0}, "up": {"s0": 1.0}},
    "s2": {"left": {"s1": 1.0}, "up": {"s3": 1.0}},
    "s3": {"up": {"s3": 1.0}}  
}

def next_state(state, action):
    if state in transition_probabilities and action in transition_probabilities[state]:
        possible_transitions = transition_probabilities[state][action]
        next_state = random.choices(list(possible_transitions.keys()), weights=possible_transitions.values())[0]
        return next_state
    else:
        return state

def reward(state, action):
    if state == "s2" and action == "up":
        return 10
    elif state == "s3":
        return 0
    else:
        return -1

def isEnd(state):
    return state == "s3"
