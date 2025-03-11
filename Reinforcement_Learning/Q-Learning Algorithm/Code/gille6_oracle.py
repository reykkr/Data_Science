states= ["s"+str(i) for i in range(6) ]
actions= ["right", "down", "left", "up" ]


def next_state(state, action):
    next_state = state
    if state == "s0" and action == "down":
        next_state = "s4"
    elif state == "s4" and action == "up":
        next_state = "s0"
    elif state == "s4" and action == "down":
        next_state = "s5"
    elif state == "s4" and action == "right":
        next_state = "s3"
    elif state == "s3" and action == "left":
        next_state = "s4"
    elif state == "s3" and action == "right":
        next_state = "s2"
    elif state == "s3" and action == "up":
        next_state = "s1"
    elif state == "s2" and action == "left":
        next_state = "s3"
    elif state == "s1" and action == "down":
        next_state = "s3"
    elif state == "s1" and action == "up":
        next_state = "s5"
    return next_state

def reward(state, action):
    if (state == "s1" and action == "up") :
        return 100
    elif (state == "s4" and action == "down"):
        return 10
    else:
        return -1

    
def isEnd(state) :
    return state == "s5"