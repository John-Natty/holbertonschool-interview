#!/usr/bin/python3
"""Module for the making change problem."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Args:
        coins (list): List of coin values.
        total (int): Target amount.

    Returns:
        int: Fewest number of coins needed, 0 if total <= 0,
             or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # This value represents an impossible amount for now.
    # The maximum useful number of coins cannot be greater than total
    # if coin 1 exists, so total + 1 is safe as "infinity".
    impossible = total + 1

    # dp[amount] will store the fewest coins needed for this amount.
    dp = [impossible] * (total + 1)

    # To make 0, we need 0 coins.
    dp[0] = 0

    # Build the answer for each amount from 1 up to total.
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                # If we use this coin, we look at the best solution
                # for the remaining amount: amount - coin.
                previous_amount = amount - coin

                # Add 1 because we are using the current coin.
                candidate = dp[previous_amount] + 1

                # Keep the best minimum result.
                if candidate < dp[amount]:
                    dp[amount] = candidate

    # If dp[total] was never updated, total cannot be reached.
    if dp[total] == impossible:
        return -1

    return dp[total]
