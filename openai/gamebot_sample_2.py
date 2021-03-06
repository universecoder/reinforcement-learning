# Basic example : https://gym.openai.com/docs/
# Note the extra time.sleep(..) and env.close() statements

import gym
import time

env = gym.make('CartPole-v0')
for i_episode in range(5):
	observation = env.reset()
	for t in range(100):
		time.sleep(0.05)
		env.render()
		print(observation)
		action = env.action_space.sample()
		observation, reward, done, info = env.step(action)
		if done:
			print("Episode finished after {} timesteps".format(t+1))
			break

env.close()
