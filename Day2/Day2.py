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

      if length % 2 == 0:
        mid = length//2
        if s[mid:] == s[:mid]:
          score += j
      
print(score)