# Rock Paper Scissors Game

## Overview
The **Rock Paper Scissors Game** project is a Python implementation of the classic hand game, extended to include various computer-controlled strategies. This project is designed to demonstrate how different algorithms can be used to create strategies for playing against opponents, making it an engaging exploration of decision-making in games.

The game supports several predefined player strategies, including random choices and more sophisticated approaches that attempt to predict and counter the opponent's next move.

## Purpose
The purpose of this project is to:

- Implement multiple strategies for the **Rock Paper Scissors** game.
- Demonstrate decision-making techniques through algorithms that predict an opponent's next move.
- Showcase Python programming skills, particularly in handling game logic and implementing different AI strategies.

## Key Features Demonstrated
1. **Game Logic Implementation**
   - Developed a function to handle the core game logic, determining the winner for each round based on player choices.
   - Handled different win/loss scenarios and calculated the win rate for Player 1.

2. **Player Strategies**
   - Implemented various player strategies, including:
     - **Quincy**: Uses a repetitive sequence of choices to make decisions.
     - **Mrugesh**: Analyzes the opponent's most frequent recent moves to decide the next play.
     - **Kris**: Always responds with the ideal counter to the opponent's last move.
     - **Abbey**: Uses a predictive model based on the last two opponent plays to determine the next move.
     - **Human**: Allows a human player to manually input moves.
     - **Random Player**: Makes random choices each round.

3. **Simulation and Evaluation**
   - Simulated multiple games between different players, calculating and printing the win rate for Player 1.
   - Provided a verbose mode to print each round's results, enhancing the understanding of each strategy's effectiveness.

## Tools Used
- **Python**: Used for implementing the game logic, strategies, and running simulations.
- **Random Module**: Utilized to generate random moves for the **Random Player** strategy.

## Project Components
1. **Game Function**
   - The `play()` function handles running multiple rounds between two players, tracking results, and calculating win rates.
   - The function supports a `verbose` mode to provide detailed output for each round.

2. **Player Strategies**
   - Implemented several strategies to determine moves, including **Quincy**, **Mrugesh**, **Kris**, **Abbey**, **Human**, and **Random Player**.
   - Each strategy employs a unique approach, from simple repetitive moves to more complex predictive algorithms.

3. **Evaluation and Analysis**
   - Calculated the win rate for Player 1 after a series of games to evaluate the effectiveness of different strategies.
   - Compared how different algorithms perform against each other, providing insight into the strengths and weaknesses of each approach.

## Example Output
After running a game between two players, the final output may look like:

```
Final results: {'p1': 5, 'p2': 3, 'tie': 2}
Player 1 win rate: 62.5%
```
This indicates that Player 1 won **62.5%** of the games, providing a metric to assess the effectiveness of Player 1's strategy.

## Notes
This project demonstrates the use of algorithms in decision-making scenarios like games. By implementing different player strategies, it highlights how varied approaches can lead to different outcomes in a competitive environment.

## Author
- **Mohamad Ali Ghaddar**

Feel free to reach out for collaboration or if you have any questions about this project.