input_data = []
test_data = [
[987654321111111],
[811111111111119],
[234234234234278],
[818181911112111]
]

tot_joltage = 0
#Skapar lista med listor
with open("Day3/Day3input.txt") as f:
  for line in f:
    input_data.append(line.strip().split(","))
#print(input_data)

for lists in input_data:
  offset = -11
  offset2 = 0
  string_joltage = ""
  list_string = str(lists[0])
  #Finds Ten digit
  for i in range(0,12):
    
    for n in range(9,0,-1):
      number = ""
      try:

        #Ensuring slicing works as intended since slicing with 0 just gives a empty list 
        if offset == 0:
          active_list = list_string[offset2:]
        else:
          active_list = list_string[offset2:offset]

        res = active_list.index(str(n))
        number = active_list[res]
        print(number)
        #print(f"Ental är: {b2}")
        break
      except ValueError:
        #print(f"Number {n2} is not in current list")
        continue
    offset += 1
    offset2 += res +1
    
 
    string_joltage += number 
 # print(f"joltage for this battery is {int(string_joltage)}")
  #print(f"total joltage is now {int(string_joltage)} + {int(tot_joltage)} = {int(string_joltage) + int(tot_joltage)}")
  print(string_joltage)
  tot_joltage += int(string_joltage)
print(tot_joltage)
  
#print(tot_joltage)