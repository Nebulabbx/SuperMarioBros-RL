from stable_baselines3 import PPO
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from gym.wrappers import GrayScaleObservation, ResizeObservation
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv

# 1. Setup the EXACT same environment as training
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
env = GrayScaleObservation(env, keep_dim=True)
env = ResizeObservation(env, 84)
env = DummyVecEnv([lambda: env])
env = VecFrameStack(env, 4, channels_order='last')

# 2. Load your specific saved model
# Replace '80000' with the number of your latest checkpoint
model_path = './train/best_model_100000' 
model = PPO.load(model_path)

print(f"Loaded model: {model_path}")

# 3. Watch Mario play
state = env.reset()
while True:
    # Use deterministic=True for the best performance (no guessing)
    action, _ = model.predict(state, deterministic=True)
    state, reward, done, info = env.step(action)
    
    # This turns on the game window!
    env.render()
    
    if done:
        state = env.reset()