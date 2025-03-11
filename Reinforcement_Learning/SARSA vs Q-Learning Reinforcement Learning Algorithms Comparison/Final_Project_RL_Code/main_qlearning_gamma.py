import qlearning as qlearning
import game as game
import keyboard
import matplotlib.pyplot as plt 

# Mohamad Ali GHADDAR
# Ali ABDALLAH

# Initialize Q matrix to zero over the known states 
# Known system states is only start state of the considered environment
qlearningQGamma9 = { game.s0 : { a:0.0 for a in game.actions }}
qlearningQGamma6 = { game.s0 : { a:0.0 for a in game.actions }}
qlearningQGamma2 = { game.s0 : { a:0.0 for a in game.actions }}
qlearningEpisodeScore9 = []
qlearningEpisodeScore6 = []
qlearningEpisodeScore2 = []
qlearningAverageScore9 = []
qlearningAverageScore6 = []
qlearningAverageScore2 = []

# number of learning iterations/episodes
# an episode is a run from start to end state
n = 10000
runAll = False

# Perform n episodes/iterations of Q-learning
for i in range(n):
  print("Iteration : " + str(i))
  
  qlearningQGamma9, qlearningScore = qlearning.playEpisode(qlearningQGamma9, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  gamma=0.9)
  qlearningEpisodeScore9.append(qlearningScore)

  qlearningQGamma6, qlearningScore = qlearning.playEpisode(qlearningQGamma6, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  gamma=0.6)
  qlearningEpisodeScore6.append(qlearningScore)

  qlearningQGamma2, qlearningScore = qlearning.playEpisode(qlearningQGamma2, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  gamma=0.2)
  qlearningEpisodeScore2.append(qlearningScore)

  # Press n key to run one episode or c to run all
  # if not runAll:
  #   key = keyboard.read_key()
  #   if key == 'c':
  #       runAll = True
  #   elif key == 'n':
  #       continue
  if i%100==0 :
    qlearningAvg9 = sum(qlearningEpisodeScore9[-100:])/100
    qlearningAverageScore9.append(qlearningAvg9)

    qlearningAvg6 = sum(qlearningEpisodeScore6[-100:])/100
    qlearningAverageScore6.append(qlearningAvg6)

    qlearningAvg2 = sum(qlearningEpisodeScore2[-100:])/100
    qlearningAverageScore2.append(qlearningAvg2)

    plt.clf() # Important...
    plt.plot(qlearningAverageScore9, label="reward qlearning gamma 0.9")
    plt.plot(qlearningAverageScore6, label="reward qlearning gamma 0.6")
    plt.plot(qlearningAverageScore2, label="reward qlearning gamma 0.2")
    plt.legend(loc=4) #bottom right
    plt.title('Qlearning Gamma')
    plt.ylabel('Average reward/Episode per 100 episodes')
    plt.xlabel('Episodes')
    plt.savefig( '~outputGammaQlearning.png' )
          #plt.show()  



qlearning.printQ(qlearningQGamma9)
qlearning.printQ(qlearningQGamma6)
qlearning.printQ(qlearningQGamma2)

