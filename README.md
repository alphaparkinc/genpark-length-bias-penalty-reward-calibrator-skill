# genpark-length-bias-penalty-reward-calibrator-skill

Verbosity penalty calibrator discounting inflated reward signals associated with excessively long model outputs.

## Architecture

```mermaid
flowchart LR
    Length[Token Length] --> Excess[max(0, Length - Target)]
    Excess --> Penalty[Penalty = alpha * Excess]
    Raw[Raw Model Reward] --> Discount[Calibrated Reward = Raw - Penalty]
    Penalty --> Discount
```

## Features
- **Linear and Exponential Decay**: Flexible penalty profiles.
- **Zero Dependencies**: 100% Python Standard Library.
