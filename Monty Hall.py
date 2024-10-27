import numpy as np
import matplotlib.pyplot as plt

##Parameters
num_simulations = 10000
configurations = [
    (3, 1),    # 10 doors, 8 reveals
    (20, 18),   # 20 doors, 18 reveals
    (50, 48),   # 50 doors, 48 reveals
    (100, 98)   # 100 doors, 98 reveals
]
def monty_hall_simulation(num_doors: int, doors_to_reveal: int, num_simulations: int):
    """
    Simulates the Monty Hall problem with a variable number of doors and doors Monty opens,
    where the player always switches their choice.
    Args:
    - num_doors (int): Total number of doors in the game.
    - doors_to_reveal (int): Number of doors Monty will open to reveal goats.
    - num_simulations (int): Number of simulations to run.
    Returns:
    - float: Winning probability from the simulations.
    """
    wins = 0
    for _ in range(num_simulations):
        car_location = np.random.randint(0, num_doors)
        player_choice = np.random.randint(0, num_doors)
        
        # Determine doors Monty can open (not car_location or player_choice)
        possible_doors_to_open = [
            door for door in range(num_doors) 
            if door != player_choice and door != car_location
        ]
        
        # Monty opens the specified number of doors to reveal goats
        revealed_doors = np.random.choice(possible_doors_to_open, doors_to_reveal, replace=False)
        
        # Player switches to one of the remaining unopened doors (not initial choice or revealed doors)
        remaining_doors = [
            door for door in range(num_doors) 
            if door != player_choice and door not in revealed_doors
        ]
        new_choice = np.random.choice(remaining_doors)
        
        # Check if the new choice is the car location
        if new_choice == car_location:
            wins += 1
    # Calculate winning and losing probabilities
    win_rate = wins / num_simulations
    loss_rate = 1 - win_rate
    return win_rate, loss_rate

# Plotting the results in a 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
fig.suptitle('Monty Hall Problem Simulation: Winning and Losing Probabilities with Always Switching')

for i, (num_doors, doors_to_reveal) in enumerate(configurations):
    win_rate, loss_rate = monty_hall_simulation(num_doors, doors_to_reveal, num_simulations)
    row, col = divmod(i, 2)
    # Plot win and loss bars
    axs[row, col].bar(['Wins'], [win_rate], color='blue')
    axs[row, col].bar(['Losses'], [loss_rate], color='red')
    axs[row, col].set_ylim(0, 1)
    axs[row, col].set_title(f'{num_doors} Doors, {doors_to_reveal} Reveals')
    axs[row, col].text(0, win_rate + 0.02, f"{win_rate:.2%}", ha='center')
    axs[row, col].text(1, loss_rate + 0.02, f"{loss_rate:.2%}", ha='center')
    axs[row, col].set_ylabel('Probability')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
