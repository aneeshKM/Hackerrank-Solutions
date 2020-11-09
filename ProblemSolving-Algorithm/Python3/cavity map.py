def cavityMap(grid):

if __name__ == '__main__':
    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid_item = cavityMap(grid_item)
        grid.append(grid_item)