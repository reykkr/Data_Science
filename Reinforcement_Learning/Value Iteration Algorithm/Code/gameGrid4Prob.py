#GRID 4 probabilistic MDP model:

# set of states S
states= ["s"+str(i) for i in range(4) ]
# set of actions A
actions= ["down", "left", "up", "right"]

# transition function T
def transitions(state, action):
    # Calculate next state (according to simple grid with wall)
    # 20% chance of error in calibration
    next_states = {}
   
    if (state == "s0" and action == "down") :
        next_states["s1"] = 0.8
        next_states["s2"] = 0.2
    elif (state == "s1" and action == "up") :
        next_states["s0"] = 0.8
        next_states["s3"] = 0.2
    elif (state == "s1" and action == "right") :
        next_states["s2"] = 0.9
        next_states["s3"] = 0.1
    elif (state == "s2" and action == "left") :
        next_states["s1"] = 0.9
        next_states["s0"] = 0.1
    elif (state == "s2" and action == "up") :
        next_states["s3"] = 0.9
        next_states["s0"] = 0.1
    else :
        # Default: remain in a state if action tries to leave grid
        next_states[state] = 1.0

    return next_states


# Reward function R
def rewards(state, action):
    # Calculate reward
    if (state == "s2" and action == "up") :
        return 10
    elif (state == "s3"):
        return 0
    else:
        return -1

# final state 
def isEnd(state):
    return (state == "s3")

