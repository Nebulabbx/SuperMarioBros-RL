# SuperMarioBros-RL
A Reinforcement Learning agent trained to play Super Mario Bros using Stable Baselines3 and PPO.
# AI-SuperMario: Reinforcement Learning with PPO

An AI agent trained to play *Super Mario Bros* using **Proximal Policy Optimization (PPO)**. This project leverages the `stable-baselines3` library and a custom-wrapped Gym environment to teach Mario how to navigate Level 1-1.

---

##  The "Golden" Environment Configuration

Due to breaking changes in modern Python libraries (specifically NumPy 2.0+), this project requires a very specific set of legacy versions to avoid `OverflowError` and `render_mode` crashes.

### Software Versions
| Package | Version | Reason |
| :--- | :--- | :--- |
| **Python** | `3.10.x` | Base language version. |
| **Stable Baselines3** | `1.8.0` | Avoids `render_mode` errors found in v2.0+. |
| **Gym** | `0.21.0` | Native compatibility with `gym-super-mario-bros`. |
| **NumPy** | `< 2.0.0` (1.26.4) | Prevents the 8-bit integer `OverflowError` in `nes-py`. |
| **OpenCV-Python** | `< 4.9` | Maintains compatibility with NumPy 1.x. |

---

## Setup & Installation

### 1. The Manual Fix (Crucial)
Before running, you **must** manually fix the math bug in the `nes-py` library:
1. Open `.\mario_fix\Lib\site-packages\nes_py\_rom.py`.
2. Go to **Line 198**.
3. Change: `return self.prg_rom_start + self.prg_rom_size * 2**10`
4. To: `return int(self.prg_rom_start) + int(self.prg_rom_size) * 1024`
5. Disclaimer: if this doesnt work out for you remember the stable_baselines[extra] does over write numpy and shimmy to latest versions to manually overright it to older version using:`
python -m pip uninstall -y stable-baselines3 shimmy
python -m pip install --force-reinstall "numpy<2.0.0"`

# 2. Install the compatible version (1.8.0)
python -m pip install stable-baselines3[extra]==1.8.0

### 2. Install Dependencies
```powershell
python -m pip install "setuptools==65.5.0" "wheel==0.38.4"
python -m pip install gym==0.21.0 gym-super-mario-bros==7.4.0 nes-py==8.2.1
python -m pip install stable-baselines3[extra]==1.8.0 "opencv-python<4.9" "numpy<2.0.0"
```  
#When the program is trained to your satisfaction use:`taskkill /F /IM python.exe /T` and then run the "test_mario.py" to see the program play mario {currently its only trained to 110000 step by m}



