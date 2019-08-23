import time
import numpy as np
import DQN
import gym
import math
import tensorflow as tf
import Env


ENV_NAME = 'FiveChess-v0'
STEP = 300  # Step limitation in an episode
TEST = 10  # The number of experiment test every 100 episode


def main():
    # initialize OpenAI Gym env and dqn agent
    env = gym.make(ENV_NAME)
    agent = DQN.DQN(env)
    SIZE = env.SIZE

    agent.copyWeightsToTarget()
    saver = tf.train.import_meta_graph('model/model-7500.meta')
    with tf.Session() as sess:
        new_saver = tf.train.import_meta_graph('model/model-7500.meta')
        new_saver.restore(sess,tf.train.latest_checkpoint('model/'))
    total_reward = 0
    for i in range(TEST):
        state = env.reset()
        state = np.reshape(state, [-1])
        camp = -1
        state = np.append(state, camp)

        for j in range(STEP):
            env.render()
            action = agent.action(state)  # direct action for test

            action = [math.floor(action / SIZE), action % SIZE, camp]
            state, reward, done, _ = env.step(action)
            state = np.reshape(state, [-1])
            if j % 2 == 0:
                camp = 1
            else:
                camp = -1
            state = np.append(state, camp)

            total_reward += reward
            time.sleep(0.5)
            if done:
                env.render()
                print('done')
                time.sleep(3)
                break
    ave_reward = total_reward / TEST
    print('episode: ', episode, 'Evaluation Average Reward:', ave_reward)


if __name__ == '__main__':
    main()