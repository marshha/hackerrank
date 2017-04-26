# Enter your code here. Read input from STDIN. Print output to STDOUT
def min_dist(vals):
    #Compute and return final answer over here
    min_dist = None
    vals_sorted = sorted(vals)
    for x in xrange(1, len(vals_sorted)):
        curr_abs = abs(vals_sorted[x] - vals_sorted[x-1])
        if min_dist == None:
            min_dist = curr_abs
        elif min_dist > curr_abs:
            min_dist = curr_abs

    return min_dist

if __name__ == '__main__':
    n = int(raw_input().strip())
    vals = map(int, raw_input().split())
    print min_dist(vals)

