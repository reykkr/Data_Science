# Reinforcement Learning: Q-Learning Algorithm

## Overview
This project implements the **Q-Learning** algorithm, a fundamental **model-free** reinforcement learning technique used for decision-making in an environment modeled as a **Markov Decision Process (MDP)**. The algorithm learns an optimal **Q-function**, which represents the expected reward for taking an action in a given state, and uses it to determine the best policy.

## Project Structure

1. **Q-Learning Algorithm**
   - Initializes the **Q-table** to store Q-values for state-action pairs.
   - Uses an **ε-greedy policy** for exploration-exploitation trade-off.
   - Updates Q-values using the **Bellman equation**:
     \[
     Q(s, a) \leftarrow Q(s, a) + \alpha \left[ R + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
     \]
   - Iterates over multiple episodes to improve the Q-values.

2. **Optimal Policy Extraction**
   - Determines the best action **π(s)** for a given state using the learned Q-values.

3. **Episode Simulation**
   - Simulates an agent interacting with the environment, following the optimal policy.
   - Updates the Q-values dynamically as the episode progresses.
   - Stores the state-action-reward trajectory.

4. **Performance Evaluation**
   - **Trace Printing**: Logs the sequence of states, actions, and rewards in an episode.
   - **Statistics Reporting**: Computes total reward and displays learned Q-values.

## Key Features
- **Q-Learning with Exploration**: Implements an **ε-greedy policy** to balance exploration and exploitation.
- **Reinforcement Learning Simulation**: Simulates an agent playing episodes based on Q-learning.
- **Dynamic Learning**: Updates Q-values as the agent interacts with the environment.
- **State-Action-Reward Logging**: Keeps track of learning progress and decision-making.

## Technologies Used
- **Python**: Core programming language for reinforcement learning.
- **Q-Learning**: Model-free reinforcement learning algorithm.

## How to Use
1. **Initialize Environment**:
   - Define **states**, **actions**, and **transition functions**.
   - Implement the **reward function** and **termination conditions**.

2. **Train the Q-Learning Agent**:
   - Call `qlearning(states, actions, transitions, reward, epsilon, gamma)` to learn the Q-values.

3. **Simulate an Episode**:
   - Use `playEpisode(Q, next_state, reward, s0, isEnd, actions)` to run an episode and observe behavior.

4. **Evaluate Performance**:
   - Use `printTrace(episode_name, trace)` to analyze the sequence of actions.
   - Call `printStat(Q, trace)` to display the total reward and Q-values.

## Project Highlights
- **Model-Free RL**: Q-learning does not require knowledge of transition probabilities.
- **Exploration & Exploitation**: Uses ε-greedy strategy for balanced learning.
- **State-Action Value Learning**: Computes the best actions to take based on accumulated experience.
- **Customizable Environment**: Works with any MDP by defining states, actions, transitions, and rewards.

## Future Improvements
- **Deep Q-Networks (DQN)**: Extend the project using neural networks for function approximation.
- **Multi-Agent RL**: Implement multiple agents learning simultaneously.
- **Adaptive Exploration**: Use **decaying ε** to optimize learning efficiency over time.

## Author
- **Mohamad Ali Ghaddar**

This project serves as a strong foundation for reinforcement learning applications and can be extended to real-world problems like **robot control, autonomous driving, and game playing**.