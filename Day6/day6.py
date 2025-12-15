test_data = [
    ["123", "328",  "51", "64"], 
    [" 45", "64",  "387", "23"], 
    ["  6", "98",  "215", "314"],
    ["*",   "+",   "*",   "+" ]
]
def load_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.split())
    return data


def solve(data):
    result = 0
    for col in range(len(data[0])):
        operator = data[-1][col]
        if operator == "*":
            result += multiplication(data,col)
        else:
            result +=addition(data,col)
    return result
def addition(data,col):
    col_res = 0
    for row in range(len(data)-1):
        col_res +=int(data[row][col])
    return col_res

def multiplication(data,col):
    col_res = 1
    for row in range(len(data)-1):
        col_res *=int(data[row][col])
    return col_res


"""TEST"""
#print(solve(test_data))

data = load_input("Day6/Day6input.txt")
#print(data[0])
print(solve(data))

