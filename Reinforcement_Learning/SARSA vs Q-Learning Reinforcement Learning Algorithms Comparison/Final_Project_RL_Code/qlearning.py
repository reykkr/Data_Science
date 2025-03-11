import random;

# Mohamad Ali GHADDAR
# Ali ABDALLAH

def playEpisode(Q, s0, actions, observe_next_state, observe_reward, isEnd, epsilon= 0.9, alpha= 0.1, horizon= 1000, gamma=0.9):
    # set cursor to initial state
    state = s0 
    h = 0
    rewards = 0

    # step when end state reached or if more than "horizon" number of actions 
    while not isEnd(state) and h < horizon :
        # register type of action "exploration" or "exploitation" for printing reasons
        typeAction = ""
        # if random > 0.9 then explore (10% chance)
        # if random < 0.9 then exploit (90% chance) = 90% greedy
        if random.random() > epsilon :
            action= random.choice( actions )
            typeAction = "explore"
        else :
            # return the action key with the higest associated value
            action= max( Q[state], key= Q[state].get )
            typeAction = "exploit"
        next_state = observe_next_state(state, action)    
        reward = observe_reward(state, action)
        rewards += reward
        h+= 1
        
        # initialize new state in Q matrix if not yet exists
        if next_state not in Q :
            Q[next_state]= { a : 0.0 for a in actions }

        # update rule for Q-learning
        Q[state][action] = ( ( 1-alpha ) * Q[state][action] ) + ( alpha * ( reward + (gamma * max( Q[next_state].values() ) ) ) )
        
        # print trace : state, action, next_state, reward 
        print("trace " + str(h) + "; state : " + state + "; action : " + str(action) + " (" + typeAction + "); next state : " + next_state + "; reward : " + str(reward))

        # move to next state
        state= next_state

    return Q, rewards


def printQ(Q) :
    print( "\nQ_TABLE")
    print("\n".join([state + ": " + ", ".join([str(action) + ": " + str(round(Q[state][action], 2))for action in range(len(Q[state]))])for state in Q]))
    print( "\nBEST ACTIONS")
    print( str({ state: max(Q[state], key= Q[state].get) for state in Q }) )


