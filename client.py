"""Length Bias Penalty Reward Calibrator.
100% Python Standard Library.
"""

import math

class LengthBiasRewardCalibrator:
    """Normalizes model reward scores against verbosity and length bias."""
    @staticmethod
    def calibrate_reward(raw_reward: float, length: int, target_length: int = 150, alpha: float = 0.002, penalty_type: str = "linear") -> dict:
        excess_length = max(0, length - target_length)
        if penalty_type == "linear":
            penalty = alpha * excess_length
        else:
            penalty = 1.0 - math.exp(-alpha * excess_length)

        calibrated = raw_reward - penalty
        return {
            "raw_reward": round(raw_reward, 4),
            "length": length,
            "excess_length": excess_length,
            "length_penalty": round(penalty, 4),
            "calibrated_reward": round(calibrated, 4)
        }
