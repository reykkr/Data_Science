states= ["s"+str(i) for i in range(4) ]
actions= ["right", "down", "left", "up" ]


def next_state(state, action):
    next_state = state
    if state == "s0" and action == "down":
        next_state = "s1"
    elif state == "s1" and action == "right":
        next_state = "s2"
    elif state == "s1" and action == "up":
        next_state = "s0"
    elif state == "s2" and action == "left":
        next_state = "s1"
    elif state == "s2" and action == "up":
        next_state = "s3"
    return next_state

def reward(state, action):
    if (state == "s2" and action == "up"):
        return 10
    elif (state == "s3"):
        return 0
    else:
        return -1

    
def isEnd(state) :
    return state == "s3"