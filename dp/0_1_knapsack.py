#You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
#code
if __name__ == "__main__":
    tests = int(input())
    for i in range(tests):
        number_of_items = int(input())
        capacity = int(input())
        values = list(map(int,input().split()))
        weights = list(map(int,input().split()))
        knapsack = [[0]*(capacity + 1) for i in range(number_of_items+1)]
        for i in range(1, number_of_items+1):
            for j in range(1, capacity+1):
                if weights[i-1] <= j:
                    knapsack[i][j] = max(knapsack[i-1][j], values[i-1]+knapsack[i-1][j-weights[i-1]])
                else:
                    knapsack[i][j] = knapsack[i-1][j]
        print(knapsack[number_of_items][capacity])
