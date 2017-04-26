# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
    #Compute and return final answer over here
    answer = 0
    prices_sorted = sorted(prices)
    for x in xrange(0, len(prices_sorted)):
        if rupees >= prices_sorted[x]:
            rupees -= prices_sorted[x]
            answer += 1
        else:
            break

    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)

