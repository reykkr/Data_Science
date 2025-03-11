# **SARSA vs Q-Learning: Reinforcement Learning Algorithms Comparison**  

## **Overview**  
This project implements and compares **Q-Learning** and **SARSA (State-Action-Reward-State-Action)**, two popular **model-free reinforcement learning** algorithms. The key difference between them lies in how they update Q-values:  

- **Q-Learning (Off-policy):**  
  - Uses the **max Q-value** of the next state for updating.  
  - More aggressive as it assumes the best action is always taken.  
  - Formula:  
    \[
    Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]
    \]
  
- **SARSA (On-policy):**  
  - Uses the **actual next action taken** for updating.  
  - More conservative, as it updates based on the chosen policy.  
  - Formula:  
    \[
    Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma Q(s', a') - Q(s, a)]
    \]

## **Project Structure**
1. **Q-Learning Algorithm**
   - Uses **ε-greedy policy** for exploration.  
   - Updates Q-values using the max future Q-value.  

2. **SARSA Algorithm**
   - Uses **ε-greedy policy** for exploration.  
   - Updates Q-values using the **actual next action taken**.  

3. **Policy Selection (π)**
   - Determines the best action for a state based on learned Q-values.  

4. **Simulation & Performance Evaluation**
   - Runs episodes following the trained policy.  
   - Logs state-action-reward transitions.  
   - Computes total rewards for both algorithms.  

## **Key Features**
- **SARSA vs Q-Learning Comparison**: Analyzes differences in learning behaviors.  
- **Reinforcement Learning Simulation**: Runs episodes in an environment.  
- **Dynamic Learning**: Updates Q-values interactively.  
- **Exploration & Exploitation**: Uses **ε-greedy** strategy.  
- **Performance Tracking**: Logs Q-values and episode traces.  

## **Technologies Used**
- **Python**  
- **Reinforcement Learning** (SARSA & Q-Learning)  

## **How to Use**
1. **Initialize Environment**: Define **states, actions, rewards, transitions**.  
2. **Train Using SARSA & Q-Learning**: Call `sarsa()` and `qlearning()` functions.  
3. **Simulate Episodes**: Use `playEpisode()` to test learned policies.  
4. **Compare Performance**: Analyze Q-values and reward accumulations.  

## **Comparison Summary**
| **Algorithm** | **Exploration Strategy** | **Update Rule** | **Behavior** |  
|--------------|------------------------|----------------|-------------|  
| **Q-Learning** | Off-policy | Uses **max Q-value** of next state | **Optimistic**, assumes best actions |  
| **SARSA** | On-policy | Uses **actual next action** taken | **Risk-averse**, follows current policy |  

## **Future Improvements**
- **Adaptive ε & α**: Implement decaying exploration & learning rates.  
- **Deep Q-Learning (DQN)**: Extend Q-learning using neural networks.  
- **Multi-Agent RL**: Test with multiple learning agents.  

## **Author**
- **Mohamad Ali Ghaddar**  

This project provides insights into the behavior of **on-policy vs off-policy RL methods** and serves as a foundation for more advanced reinforcement learning applications. 🚀