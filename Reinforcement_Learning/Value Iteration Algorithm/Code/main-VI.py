import valueIteration
import gameGrid4 as game
# gameGrid4Prob gameGrid4 gameGrid6 gameGrid6Prob

epsilon = 0.1
gamma = 0.99

# Evaluate if the simulation reached an end state.
print("\n----------------------------")
print("Simple MDP")
print("----------------------------\n")

# print the MDP model éléments S,A,T,R
print("\n----------------------------")
print("START MDP model")
print("----------------------------\n")

# print model set of states S
print("STATES S : \n" + str(game.states))
# print model set of actions A
print("\nACTIONS A : \n" + str(game.actions))
# print model transition function T(s,a,s')
print("\nTRANSITION FUNCTION :")
for s in game.states:
    for a in game.actions:
        print("start state = " + s + ", action = " + a + ", next_states = " + str(game.transitions(s,a)))
# print model reward function R(s,a)
print("\nREWARD FUNCTION :")
for s in game.states:
    for a in game.actions:
        print("start state = " + s + ", action = " + a + ", reward = " + str(game.rewards(s,a)))
        
print("\n----------------------------")
print("END MDP model")
print("----------------------------\n")

# Run Value Iteration
print("\n----------------------------")
print("ITERATIONS OF MDP VALUE ITERATION")
print("----------------------------\n")
VI = valueIteration.valueIteration(game.states, game.actions, game.transitions, game.rewards, epsilon, gamma)

# Run a complete episode from initial state to end state following the optimal policy
print("\n----------------------------")
print("OPTIMAL POLICY À PARTIR DE S0")
print("----------------------------\n")
valueIteration.playEpisode("s0", game.isEnd, VI, game.actions, game.transitions, game.rewards, gamma)
print("\n----------------------------")
#print("OPTIMAL POLICY À PARTIR DE S2")
#print("----------------------------\n")
#valueIteration.playEpisode("s2", game.isEnd, VI, game.actions, game.transitions, game.rewards, gamma)