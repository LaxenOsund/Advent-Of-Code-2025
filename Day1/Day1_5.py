turns = []

test = ["R350","L349", "L22","R23"]
with open("Day1input.txt") as f:
  for line in f:
    turns.append(line.strip())
score = 0
value = 50
for line in turns:
    if line[0] == "L":
        for number in range(int(line[1:])):
            value -= 1
            if value == -1:
                value = 99
            if value == 0:
                score += 1   
                
    elif line[0] == "R":
        for number in range(int(line[1:])):
            value += 1
            if value == 100:
                value = 0
            if value == 0:
                score += 1

print(f"Score is: {score}")

      
