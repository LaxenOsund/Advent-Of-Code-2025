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
    if filename != "test_data":
        with open(filename) as f:
            for line in f:
                if "-" in line:
                            parts = line.split("-")
                            spans.append([int(parts[0]), int(parts[1])])

            return spans
    else:
        for line in test_data:
                if "-" in line:
                            parts = line.split("-")
                            spans.append([int(parts[0]), int(parts[1])])
        return spans

                
def solve(spans):
    # 1. Sort spans by their start numbe
    spans.sort(key=lambda x: x[0])

    merged = []
    
    for current_start, current_end in spans:
        if not merged:
            merged.append([current_start, current_end])
            continue
        
        # Look at the last span we added
        last_span = merged[-1]
        last_end = last_span[1]

        if current_start <= last_end:
            #Overlap
            last_span[1] = max(last_end, current_end)
        else:
            # No overlap
            merged.append([current_start, current_end])

    total_count = 0
    for start, end in merged:
        total_count += (end - start + 1)
        
    return total_count
"""TEST"""
#spans = load_input("test_data")

spans = load_input("Day5/Day5input.txt")
print(solve(spans))