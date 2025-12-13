test_data = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."
]

def load_input(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

def is_accesible(grid,row,col):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for r in range(row-1,row+2):
        if r == -1 or r == rows:
            continue 
        for c in range(col-1,col+2):
            if c == -1 or c == cols or (r,c) == (row,col):
                continue
            elif grid[r][c] == "@":
                count += 1
    return count < 4

def solve_paper(data):
    grid = [list(row) for row in data]
    rows = len(grid)
    cols = len(grid[0])
    accesible = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "@":
                #print(f"found @ at {row} , {col}")
                if is_accesible(grid,row,col):
                    accesible += 1
                    #print(f"@ is accesible at  {row} , {col}")
    return accesible
"""TEST"""
#print(solve_paper(test_data))

print(solve_paper(load_input("Day4/Day4input.txt")))

            