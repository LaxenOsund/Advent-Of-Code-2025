test_data= [
"3-5",
"10-14",
"16-20",
"12-18",

"1",
"5",
"8",
"11",
"17",
"32",
]

def load_input(filename):
    spans = []
    ids = []
    if filename != "test_data":
        with open(filename) as f:
            for line in f:
                if "-" in line:
                            parts = line.split("-")
                            spans.append([int(parts[0]), int(parts[1])])
                elif line != "\n":
                    ids.append(int(line))
                else:
                    continue
            
            return ids,spans
    else:
        for line in test_data:
                if "-" in line:
                            parts = line.split("-")
                            spans.append([int(parts[0]), int(parts[1])])
                elif line != "\n":
                    ids.append(int(line))
                else:
                    continue
        return ids,spans

def inside(x,low,high):
        return low <= x <= high
                
def solve(ids,spans):
    fresh = 0
    for i in ids:
        for span in spans:
            if inside(i,span[0],span[1]):
                fresh += 1
                break 
    return fresh
"""TEST"""
#ids, spans = load_input("test_data")

ids,spans = load_input("Day5/Day5input.txt")
print(solve(ids,spans))