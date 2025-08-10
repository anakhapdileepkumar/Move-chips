def minCostToMoveChips(position):
    even_count = 0
    odd_count = 0
    
    for p in position:
        if p % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return min(even_count, odd_count)


positions = [1, 2, 3]
print(minCostToMoveChips(positions))  