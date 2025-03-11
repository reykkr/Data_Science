import sarsa as sarsa
import qlearning as qlearning
import game as game
import keyboard
import matplotlib.pyplot as plt 

# Mohamad Ali GHADDAR
# Ali ABDALLAH

# Initialize Q matrix to zero over the known states 
# Known system states is only start state of the considered environment
qlearningQ = { game.s0 : { a:0.0 for a in game.actions }}
sarsaQ = { game.s0 : { a:0.0 for a in game.actions }}
qlearningEpisodeScore = []
qlearningAverageScore = []
sarsaEpisodeScore = []
sarsaAverageScore = []
# number of learning iterations/episodes
# an episode is a run from start to end state
n = 10000
runAll = False

# Perform n episodes/iterations of Q-learning
for i in range(n):
  print("Iteration : " + str(i))
  
  qlearningQ, qlearningScore = qlearning.playEpisode(qlearningQ, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd)
  qlearningEpisodeScore.append(qlearningScore)

  sarsaQ, sarsaScore = sarsa.playEpisode(sarsaQ, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd)
  sarsaEpisodeScore.append(sarsaScore)

  # Press n key to run one episode or c to run all
  # if not runAll:
  #   key = keyboard.read_key()
  #   if key == 'c':
  #       runAll = True
  #   elif key == 'n':
  #       continue
  if i%100==0 :
    qlearningAvg = sum(qlearningEpisodeScore[-100:])/100
    qlearningAverageScore.append(qlearningAvg)
    sarsaAvg = sum(sarsaEpisodeScore[-100:])/100
    sarsaAverageScore.append(sarsaAvg)
    plt.clf() # Important...
    plt.plot(qlearningAverageScore, label="reward qlearning")
    plt.plot(sarsaAverageScore, label="reward sarsa")
    plt.legend(loc=4) #bottom right
    plt.title('Qlearning vs sarsa')
    plt.ylabel('Average reward/Episode per 100 episodes')
    plt.xlabel('Episodes')
    plt.savefig( '~output_Sarsa_Qlearning.png' )
          #plt.show()  



qlearning.printQ(qlearningQ)
sarsa.printQ(sarsaQ)
