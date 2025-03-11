# Reinforcement Learning: Value Iteration Algorithm

## Overview
This project implements the **Value Iteration** algorithm, a fundamental method in **Reinforcement Learning (RL)**, to compute the optimal **value function** and **policy** for a given Markov Decision Process (MDP). The algorithm iteratively updates state values until convergence, allowing an agent to make optimal decisions based on the learned policy.

## Project Structure

1. **Value Iteration Algorithm**
   - Initializes the **value function** to zero for all states.
   - Iteratively updates state values based on the **Bellman equation**.
   - Stops when the maximum change in values is below a given threshold **epsilon**.
   - Outputs the optimal value function **V(s)** for all states.

2. **Optimal Policy Extraction**
   - Determines the best action **π(s)** for each state by selecting the action that maximizes the expected value.

3. **Episode Simulation**
   - Runs a simulated episode from an initial state to an end state.
   - Selects actions using the **optimal policy** and transitions through states based on probabilities.
   - Prints the sequence of states, actions, and rewards.

## Key Skills Demonstrated
- **Dynamic Programming in RL**: Applied Value Iteration to solve MDPs.
- **Policy Optimization**: Derived the optimal policy using the computed value function.
- **Simulation of RL Agents**: Ran episodes to test the learned policy.
- **Handling Probabilistic Transitions**: Managed state transitions using probability distributions.

## Technologies Used
- **Python**: Programming language for implementing reinforcement learning.
- **Value Iteration**: Dynamic programming method for MDPs.

## How to Run the Project
1. **Requirements**: Ensure you have Python installed.
2. **Define the MDP**:
   - **States**: List of possible states.
   - **Actions**: Set of available actions per state.
   - **Transitions**: Probability distribution of next states given an action.
   - **Rewards**: Function mapping state-action pairs to rewards.
3. **Run the Algorithm**:
   - Call `valueIteration(states, actions, transitions, rewards, epsilon, gamma)` to compute **V(s)**.
   - Use `pi(V, state, actions, transitions, rewards, gamma)` to determine the best action.
   - Run `playEpisode(initial_state, isEnd, V, actions, transitions, rewards, gamma)` to simulate an episode.

## Project Highlights
- **Efficient Value Iteration**: Iteratively refines the value function until convergence.
- **Policy Extraction**: Computes the optimal policy based on state values.
- **Episode Simulation**: Demonstrates the effectiveness of the learned policy.

## Future Improvements
- **Q-Learning Implementation**: Extend the project to support Q-learning for model-free RL.
- **Policy Iteration**: Compare results with policy iteration.
- **Larger State Spaces**: Optimize the algorithm for more complex environments.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for any questions or collaboration opportunities.