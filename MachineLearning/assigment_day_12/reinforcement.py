#train a reinforcement learning to navigate to cross road with action right ,left ,right
import numpy as np
import random

#environment set up 
road_length = 5 # the road will have five position 0,4 our goal is to reach position 4
actions = ['left','right'] #agent can take left and right

#Q-table initialization 
Q = np.zeros((road_length, len(actions)))   #
# hyperparameters
episodes = 1000 #numbers of training interactions leads to better learning rates
learning_rate = 0.8  #0 ,1 alpha learning rate ,,this helps the agent to adapt very quickly 
gama = 0.9# it will have a light reward 
epsilon = 0.3 #helps the agent to discover paths  #exploration rates 
#training loop
for episode in range(episodes):
    state = 0 #start position 0
    
    while state != 4: # goal is position 4
        #epsilon greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 1)
        else:
            action = np.argmax(Q[state])