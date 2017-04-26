# Enter your code here. Read input from STDIN. Print output to STDOUT
def min_cost(prices):
    #Compute and return final answer over here
    answer_arr = []
    prices_sorted = sorted(prices)
    for x in xrange(0, len(prices_sorted)):
        if not answer_arr:
            answer_arr.append(prices_sorted[x])
        elif ((prices_sorted[x] >= answer_arr[-1]) and
                (prices_sorted[x] <= answer_arr[-1] + 4)):
                continue
        else:
            answer_arr.append(prices_sorted[x])

    return len(answer_arr)

if __name__ == '__main__':
    n = int(raw_input().strip())
    prices = map(int, raw_input().split())
    print min_cost(prices)

