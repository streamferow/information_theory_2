"""
Channel Capacity Calculator Backend
Information Theory - Task #2

Binary communication channel with two types of errors:
- P: Probability of bit flip (0↔1)
- M: Probability of erasure (signal unrecognizable)

Based on Shannon's Information Theory
"""

import math
from typing import Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ChannelParams:
    """Channel parameters"""
    N: float  # Signal rate (bits per second)
    P: float  # Bit flip probability
    M: float  # Erasure probability
    
    def validate(self) -> Optional[str]:
        """Validate parameters, return error message if invalid"""
        if self.N <= 0:
            return "N must be positive"
        if self.P < 0 or self.P > 0.5:
            return "P must be between 0 and 0.5"
        if self.M < 0 or self.M > 0.5:
            return "M must be between 0 and 0.5"
        if self.P + self.M > 1:
            return "P + M must not exceed 1"
        return None


@dataclass
class CalculationResult:
    """Calculation results"""
    H_X: float      # Source entropy
    H_Y_X: float    # Conditional entropy H(Y|X)
    H_Y: float      # Receiver entropy H(Y)
    I_XY: float     # Mutual information I(X;Y)
    capacity: float # Channel capacity C = N * I(X;Y)
    
    def to_dict(self) -> Dict:
        return {
            "H_X": round(self.H_X, 6),
            "H_Y_X": round(self.H_Y_X, 6),
            "H_Y": round(self.H_Y, 6),
            "I_XY": round(self.I_XY, 6),
            "capacity": round(self.capacity, 6)
        }


def log2(x: float) -> float:
    """Base-2 logarithm"""
    if x <= 0:
        return 0
    return math.log2(x)


def entropy(p: float) -> float:
    """Binary entropy function: H(p) = -p*log2(p) - (1-p)*log2(1-p)"""
    if p <= 0 or p >= 1:
        return 0
    return -p * log2(p) - (1 - p) * log2(1 - p)


def calculate_channel_capacity(params: ChannelParams) -> Tuple[Optional[CalculationResult], Optional[str]]:
    """
    Calculate channel capacity using Shannon's formulas
    
    For a binary channel with:
    - P: probability of bit flip (0→1 or 1→0)
    - M: probability of erasure (signal becomes unrecognizable '?')
    
    Channel model:
    - P(Y=0|X=0) = 1 - P - M  (correct transmission)
    - P(Y=1|X=0) = P          (bit flip)
    - P(Y=?|X=0) = M          (erasure)
    
    Similar for X=1.
    
    Formulas:
    I(X;Y) = H(Y) - H(Y|X)  (mutual information)
    C = N * I(X;Y)          (channel capacity in bits/sec)
    """
    
    # Validate
    error = params.validate()
    if error:
        return None, error
    
    N, P, M = params.N, params.P, params.M
    
    # Source entropy H(X) = 1 for equiprobable binary source
    H_X = 1.0
    
    # Probability of correct transmission
    q_correct = 1 - P - M
    
    # Conditional entropy H(Y|X)
    # H(Y|X) = -[(1-P-M)*log2(1-P-M) + P*log2(P) + M*log2(M)]
    H_Y_X = 0.0
    if q_correct > 0:
        H_Y_X -= q_correct * log2(q_correct)
    if P > 0:
        H_Y_X -= P * log2(P)
    if M > 0:
        H_Y_X -= M * log2(M)
    
    # For equiprobable input X:
    # P(Y=0) = 0.5*(1-P-M) + 0.5*P = 0.5*(1-M)
    # P(Y=1) = 0.5*P + 0.5*(1-P-M) = 0.5*(1-M)
    # P(Y=?) = M
    p_Y0 = 0.5 * (1 - M)
    p_Y1 = 0.5 * (1 - M)
    p_YE = M
    
    # Receiver entropy H(Y)
    H_Y = 0.0
    if p_Y0 > 0:
        H_Y -= p_Y0 * log2(p_Y0)
    if p_Y1 > 0:
        H_Y -= p_Y1 * log2(p_Y1)
    if p_YE > 0:
        H_Y -= p_YE * log2(p_YE)
    
    # Mutual information I(X;Y) = H(Y) - H(Y|X)
    I_XY = max(0, H_Y - H_Y_X)
    
    # Channel capacity
    capacity = N * I_XY
    
    return CalculationResult(
        H_X=H_X,
        H_Y_X=H_Y_X,
        H_Y=H_Y,
        I_XY=I_XY,
        capacity=capacity
    ), None


def generate_chart_data(N: float, fixed_M: float, step: float = 0.01) -> list:
    """Generate data for capacity vs P chart"""
    data = []
    p = 0.0
    while p <= 0.5:
        if p + fixed_M <= 1:
            params = ChannelParams(N=N, P=p, M=fixed_M)
            result, _ = calculate_channel_capacity(params)
            if result:
                data.append({
                    "p": round(p, 4),
                    "capacity": round(result.capacity, 4),
                    "ideal": N
                })
        p += step
    return data


def main():
    """CLI interface for testing"""
    print("=" * 60)
    print("  CHANNEL CAPACITY CALCULATOR - Information Theory Task #2")
    print("=" * 60)
    print()
    
    # Get input from user
    try:
        N = float(input("Enter N (signal rate, bits/sec) [1000]: ") or "1000")
        P = float(input("Enter P (flip probability) [0.01]: ") or "0.01")
        M = float(input("Enter M (erasure probability) [0.05]: ") or "0.05")
    except ValueError:
        print("Error: Invalid input")
        return
    
    params = ChannelParams(N=N, P=P, M=M)
    result, error = calculate_channel_capacity(params)
    
    if error:
        print(f"\nError: {error}")
        return
    
    print("\n" + "=" * 60)
    print("  RESULTS")
    print("=" * 60)
    print(f"  Source Entropy H(X):      {result.H_X:.6f} bits/symbol")
    print(f"  Conditional H(Y|X):       {result.H_Y_X:.6f} bits/symbol")
    print(f"  Receiver Entropy H(Y):    {result.H_Y:.6f} bits/symbol")
    print(f"  Mutual Information I(X;Y): {result.I_XY:.6f} bits/symbol")
    print(f"  Channel Capacity C:        {result.capacity:.2f} bits/sec")
    print("=" * 60)
    
    # Show efficiency
    efficiency = (result.capacity / N) * 100
    print(f"  Efficiency: {efficiency:.2f}% of ideal channel")
    print()


if __name__ == "__main__":
    main()
