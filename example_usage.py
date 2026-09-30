from client import LengthBiasRewardCalibrator

res = LengthBiasRewardCalibrator.calibrate_reward(0.92, 450, target_length=150, alpha=0.001)
print("Length Calibrated Reward:", res)
