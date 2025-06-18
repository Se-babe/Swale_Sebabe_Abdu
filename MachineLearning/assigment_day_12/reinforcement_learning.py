import numpy as np
import random

# Environment setup
position = 5  # Positions: 0 to 4 (4 = goal)
actions = 3   # Actions: 0=Left, 1=Right, 2=Stay
car_position = 1  # Danger zone at position 1

# Initialize Q-table (states x actions)
Q = np.zeros((position, actions))

# Training parameters
episodes = 1000  # Number of training episodes
learning_rate = 0.8  # How fast the agent learns
gamma = 0.9  # Discount factor (importance of future rewards)
epsilon = 0.3  # Exploration rate (30% random actions)

# Training loop
for episode in range(episodes):
    state = random.randint(0, position - 1)  # Start at random position
    
    while state != position - 1:  # Until goal is reached
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  # Random action
        else:
            action = np.argmax(Q[state])  # Best known action
        
        # Simulate action
        if action == 0:  # Move Left
            next_state = max(0, state - 1)
        elif action == 1:  # Move Right
            next_state = min(position - 1, state + 1)
        else:  # Stay
            next_state = state
        
        # Assign rewards
        if next_state == position - 1:
            reward = 50  # Reached goal
        elif next_state == car_position:
            reward = -10  # Hit a car
        else:
            reward = -1  # Step penalty
        
        # Update Q-table
        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state  # Move to next state

# Test the trained agent
state = 0  # Start at position 0 (beginning of the road)
steps = 0
print("\nAgent's path to cross the road:")
while state != position - 1:
    action = np.argmax(Q[state])  # Choose best action
    if action == 0:
        next_state = max(0, state - 1)
        action_name = "Left"
    elif action == 1:
        next_state = min(position - 1, state + 1)
        action_name = "Right"
    else:
        next_state = state
        action_name = "Stay"
    
    print(f"Step {steps}: Position {state} -> Action {action_name} -> Next Position {next_state}")
    state = next_state
    steps += 1

print(f"\nCrossed the road in {steps} steps!")
print("\nFinal Q-table:")
print(Q)