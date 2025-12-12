input = []
with open("Day2\Day2input.txt") as f:
  for line in f:
    input.append(line.strip().split(","))

#print(ranges[0][0].split("-"))
ranges = []
for i in input[0]:
    ranges.append(i.split("-"))
score = 0
for i in ranges:
   
    start = int(i[0])
    end = int(i[1]) 


    for j in range(start, end + 1):
        s= str(j)
        length = len(s)

        pattern_found = False

        for chunk_len in range(1, (length // 2) +1 ):

            if length % chunk_len == 0:
                pattern = s[:chunk_len]
                repeat_count = length // chunk_len 
                if pattern * repeat_count == s:
                    pattern_found = True
                    break
        if pattern_found:
            score += j
print(score)