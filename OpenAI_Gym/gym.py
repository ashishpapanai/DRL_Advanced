import random


class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observations(self) -> list[float]:
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> list[int]:
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def Actions(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")

        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.total_reward = 0.0

    def step(self, env: Environment) -> int:
        current_obs = env.get_observations()  # Observe Environment
        actions = env.get_actions()  # Take an action
        reward = env.Actions(random.choice(actions))  # Get the reward
        self.total_reward += reward  # Update the total reward


if __name__ == "__main__":
    env = Environment() # Create an environment
    agent = Agent() # Create an agent
    while not env.is_done(): # While the game is not over
        agent.step(env) # Make a step

    print("Total reward: {}".format(agent.total_reward)) # Print the total reward
