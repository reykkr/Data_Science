import random

states = ["s"+str(i) for i in range(6)]
actions = ["right", "down", "left", "up"]


transition_probabilities = {
    "s0": {"down": {"s4": 1.0}},
    "s4": {"up": {"s0": 0.8, "s3": 0.2}, "down": {"s5": 0.7, "s4": 0.3}, "right": {"s3": 0.6, "s4": 0.4}},
    "s3": {"left": {"s4": 0.9, "s3": 0.1}, "right": {"s2": 0.7, "s3": 0.3}, "up": {"s1": 0.8, "s3": 0.2}},
    "s2": {"left": {"s3": 1.0}},
    "s1": {"down": {"s3": 0.9, "s5": 0.1}, "up": {"s0": 0.5, "s5": 0.5}}
}

def next_state(state, action):
    if state in transition_probabilities and action in transition_probabilities[state]:
        possible_transitions = transition_probabilities[state][action]
        next_state = random.choices(list(possible_transitions.keys()), weights=possible_transitions.values())[0]
        return next_state
    else:
        return state

def reward(state, action):
    if state == "s1" and action == "up":
        return 100
    elif state == "s4" and action == "down":
        return 10
    else:
        return -1

def isEnd(state):
    return state == "s5"
