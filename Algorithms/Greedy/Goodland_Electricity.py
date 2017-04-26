# Enter your code here. Read input from STDIN. Print output to STDOUT
def pylons(cities, k):
    #Compute and return final answer over here
    answer = 0

    cities_dict = {}

    for x in xrange(0, len(cities)):
        if cities[x] == 1:
            min_city = x - (k-1)
            if min_city < 0:
                min_city = 0

            max_city = x + (k-1)
            if max_city > len(cities) - 1:
                max_city = len(cities) - 1

            if min_city not in cities_dict:
                cities_dict[min_city] = max_city
            else:
                if cities_dict[min_city] < max_city:
                    cities_dict[min_city] = max_city

            #print x, min_city, max_city

    curr_city = 0
    while (curr_city + 1) < len(cities):
        matched = False
        for x in xrange(0, 2*k - 1):
            #print curr_city - x, curr_city, x
            if (curr_city - x) in cities_dict:
                matched = True
                curr_city = cities_dict[curr_city - x] + 1
                answer += 1
                break

        if not matched:
            #print "Could not progress from %s" % (curr_city,)
            return -1

    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    cities = map(int, raw_input().split())
    print pylons(cities, k)

