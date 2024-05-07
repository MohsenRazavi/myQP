coin_amounts = {0: 0}


def coin_change_top_down(n):
    if n < 0:
        return float('inf')
    elif n in coin_amounts:
        return coin_amounts[n]
    else:
        best_ans = float('inf')
        for c in base_coins:
            ans = coin_change_top_down(n - c) + 1
            if ans < best_ans:
                best_ans = ans
        coin_amounts[n] = best_ans
        return best_ans


def coin_change_buttom_up(n):
    for i in range(1, n+1):
        best_ans = float('inf')
        for c in base_coins:
            if i - c >= 0:
                ans = coin_amounts[i - c] + 1
                if ans < best_ans:
                    best_ans = ans
        coin_amounts[i] = best_ans

    return best_ans


coin = int(input())
base_coins = [int(coin) for coin in input().split()]
