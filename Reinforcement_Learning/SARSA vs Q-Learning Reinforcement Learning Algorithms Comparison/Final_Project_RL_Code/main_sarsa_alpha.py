import sarsa as sarsa
import game as game
import keyboard
import matplotlib.pyplot as plt 

# Mohamad Ali GHADDAR
# Ali ABDALLAH

# Initialize Q matrix to zero over the known states 
# Known system states is only start state of the considered environment
sarsaQAlpha1 = { game.s0 : { a:0.0 for a in game.actions }}
sarsaQAlpha5 = { game.s0 : { a:0.0 for a in game.actions }}
sarsaQAlpha9 = { game.s0 : { a:0.0 for a in game.actions }}
sarsaEpisodeScore1 = []
sarsaEpisodeScore5 = []
sarsaEpisodeScore9 = []
sarsaAverageScore1 = []
sarsaAverageScore5 = []
sarsaAverageScore9 = []

# number of learning iterations/episodes
# an episode is a run from start to end state
n = 10000
runAll = False

# Perform n episodes/iterations of sarsa
for i in range(n):
  print("Iteration : " + str(i))
  
  sarsaQAlpha1, sarsaScore = sarsa.playEpisode(sarsaQAlpha1, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  alpha=0.1)
  sarsaEpisodeScore1.append(sarsaScore)

  sarsaQAlpha5, sarsaScore = sarsa.playEpisode(sarsaQAlpha5, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  alpha=0.5)
  sarsaEpisodeScore5.append(sarsaScore)

  sarsaQAlpha9, sarsaScore = sarsa.playEpisode(sarsaQAlpha9, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  alpha=0.9)
  sarsaEpisodeScore9.append(sarsaScore)

  # Press n key to run one episode or c to run all
  # if not runAll:
  #   key = keyboard.read_key()
  #   if key == 'c':
  #       runAll = True
  #   elif key == 'n':
  #       continue
  if i%100==0 :
    sarsaAvg1 = sum(sarsaEpisodeScore1[-100:])/100
    sarsaAverageScore1.append(sarsaAvg1)

    sarsaAvg5 = sum(sarsaEpisodeScore5[-100:])/100
    sarsaAverageScore5.append(sarsaAvg5)

    sarsaAvg9 = sum(sarsaEpisodeScore9[-100:])/100
    sarsaAverageScore9.append(sarsaAvg9)

    plt.clf() # Important...
    plt.plot(sarsaAverageScore1, label="reward sarsa alpha 0.1")
    plt.plot(sarsaAverageScore5, label="reward sarsa alpha 0.5")
    plt.plot(sarsaAverageScore9, label="reward sarsa alpha 0.9")
    plt.legend(loc=4) #bottom right
    plt.title('sarsa alpha')
    plt.ylabel('Average reward/Episode per 100 episodes')
    plt.xlabel('Episodes')
    plt.savefig( '~outputAlphasarsa.png' )
          #plt.show()  



sarsa.printQ(sarsaQAlpha1)
sarsa.printQ(sarsaQAlpha5)
sarsa.printQ(sarsaQAlpha9)

