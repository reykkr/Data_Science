import sarsa as sarsa
import game as game
import keyboard
import matplotlib.pyplot as plt 

# Mohamad Ali GHADDAR
# Ali ABDALLAH

# Initialize Q matrix to zero over the known states 
# Known system states is only start state of the considered environment
sarsaQGamma9 = { game.s0 : { a:0.0 for a in game.actions }}
sarsaQGamma6 = { game.s0 : { a:0.0 for a in game.actions }}
sarsaQGamma2 = { game.s0 : { a:0.0 for a in game.actions }}
sarsaEpisodeScore9 = []
sarsaEpisodeScore6 = []
sarsaEpisodeScore2 = []
sarsaAverageScore9 = []
sarsaAverageScore6 = []
sarsaAverageScore2 = []

# number of learning iterations/episodes
# an episode is a run from start to end state
n = 10000
runAll = False

# Perform n episodes/iterations of Q-learning
for i in range(n):
  print("Iteration : " + str(i))
  
  sarsaQGamma9, sarsaScore = sarsa.playEpisode(sarsaQGamma9, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  gamma=0.9)
  sarsaEpisodeScore9.append(sarsaScore)

  sarsaQGamma6, sarsaScore = sarsa.playEpisode(sarsaQGamma6, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  gamma=0.6)
  sarsaEpisodeScore6.append(sarsaScore)

  sarsaQGamma2, sarsaScore = sarsa.playEpisode(sarsaQGamma2, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  gamma=0.2)
  sarsaEpisodeScore2.append(sarsaScore)

  # Press n key to run one episode or c to run all
  # if not runAll:
  #   key = keyboard.read_key()
  #   if key == 'c':
  #       runAll = True
  #   elif key == 'n':
  #       continue
  if i%100==0 :
    sarsaAvg9 = sum(sarsaEpisodeScore9[-100:])/100
    sarsaAverageScore9.append(sarsaAvg9)

    sarsaAvg6 = sum(sarsaEpisodeScore6[-100:])/100
    sarsaAverageScore6.append(sarsaAvg6)

    sarsaAvg2 = sum(sarsaEpisodeScore2[-100:])/100
    sarsaAverageScore2.append(sarsaAvg2)

    plt.clf() # Important...
    plt.plot(sarsaAverageScore9, label="reward sarsa gamma 0.9")
    plt.plot(sarsaAverageScore6, label="reward sarsa gamma 0.6")
    plt.plot(sarsaAverageScore2, label="reward sarsa gamma 0.2")
    plt.legend(loc=4) #bottom right
    plt.title('sarsa Gamma')
    plt.ylabel('Average reward/Episode per 100 episodes')
    plt.xlabel('Episodes')
    plt.savefig( '~outputGammasarsa.png' )
          #plt.show()  



sarsa.printQ(sarsaQGamma9)
sarsa.printQ(sarsaQGamma6)
sarsa.printQ(sarsaQGamma2)

