coin_amounts = {0: 1}


def coin_change_counting_top_down(n):
    if n < 0:
        return float('inf')
    elif n in coin_amounts:
        return coin_amounts[n]
    else:
        ans = 0
        for c in base_coins:
            ans += coin_change_counting_top_down(n - c)
        coin_amounts[n] = ans
        return ans


def coin_change_counting_buttom_up(n):
    for i in range(1, n+1):
        ans = 0
        for c in base_coins:
            if i - c >= 0:
                ans += coin_amounts[i - c]
        coin_amounts[i] = ans

    return ans


coin = int(input())
base_coins = [int(coin) for coin in input().split()]
print(coin_change_counting_buttom_up(coin))
