import qlearning as qlearning
import game as game
import keyboard
import matplotlib.pyplot as plt 

# Mohamad Ali GHADDAR
# Ali ABDALLAH

# Initialize Q matrix to zero over the known states 
# Known system states is only start state of the considered environment
qlearningQAlpha1 = { game.s0 : { a:0.0 for a in game.actions }}
qlearningQAlpha5 = { game.s0 : { a:0.0 for a in game.actions }}
qlearningQAlpha9 = { game.s0 : { a:0.0 for a in game.actions }}
qlearningEpisodeScore1 = []
qlearningEpisodeScore5 = []
qlearningEpisodeScore9 = []
qlearningAverageScore1 = []
qlearningAverageScore5 = []
qlearningAverageScore9 = []

# number of learning iterations/episodes
# an episode is a run from start to end state
n = 10000
runAll = False

# Perform n episodes/iterations of Q-learning
for i in range(n):
  print("Iteration : " + str(i))
  
  qlearningQAlpha1, qlearningScore = qlearning.playEpisode(qlearningQAlpha1, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  alpha=0.1)
  qlearningEpisodeScore1.append(qlearningScore)

  qlearningQAlpha5, qlearningScore = qlearning.playEpisode(qlearningQAlpha5, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  alpha=0.5)
  qlearningEpisodeScore5.append(qlearningScore)

  qlearningQAlpha9, qlearningScore = qlearning.playEpisode(qlearningQAlpha9, 
                                  game.s0,
                                  game.actions,
                                  game.observe_next_state, 
                                  game.observe_reward, 
                                  game.isEnd,
                                  alpha=0.9)
  qlearningEpisodeScore9.append(qlearningScore)

  # Press n key to run one episode or c to run all
  # if not runAll:
  #   key = keyboard.read_key()
  #   if key == 'c':
  #       runAll = True
  #   elif key == 'n':
  #       continue
  if i%100==0 :
    qlearningAvg1 = sum(qlearningEpisodeScore1[-100:])/100
    qlearningAverageScore1.append(qlearningAvg1)

    qlearningAvg5 = sum(qlearningEpisodeScore5[-100:])/100
    qlearningAverageScore5.append(qlearningAvg5)

    qlearningAvg9 = sum(qlearningEpisodeScore9[-100:])/100
    qlearningAverageScore9.append(qlearningAvg9)

    plt.clf() # Important...
    plt.plot(qlearningAverageScore1, label="reward qlearning alpha 0.1")
    plt.plot(qlearningAverageScore5, label="reward qlearning alpha 0.5")
    plt.plot(qlearningAverageScore9, label="reward qlearning alpha 0.9")
    plt.legend(loc=4) #bottom right
    plt.title('Qlearning alpha')
    plt.ylabel('Average reward/Episode per 100 episodes')
    plt.xlabel('Episodes')
    plt.savefig( '~outputAlphaQlearning.png' )
          #plt.show()  



qlearning.printQ(qlearningQAlpha1)
qlearning.printQ(qlearningQAlpha5)
qlearning.printQ(qlearningQAlpha9)

