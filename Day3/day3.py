input_data = []
test_data = [
[987654321111111],
[811111111111119],
[234234234234278],
[818181911112111]
]
tot_joltage = 0
#Skapar lista med listor
with open("Day3\Day3input.txt") as f:
  for line in f:
    input_data.append(line.strip().split(","))
#print(input_data)

for lists in input_data:
  
  list_string = str(lists)[2:102]
  print(list_string)
  print(str(lists))
  #Finds Ten digit
  for n1 in range(9,0,-1):

    try:
      res = list_string.index(str(n1))
      print(f"{res} == {len(list_string)}" )
      if res == len(list_string)-1:
        continue
      b1 = list_string[res]
      print(f"Tiotal är: {list_string[res]}")
      lists = list_string[res+1:]
      #print(f"Index for biggest number: {res}. List now looks like \n {lists}")
      break
    except ValueError:
      print(f"Number {n1} is not in current list")
    
  for n2 in range(9,0,-1):
    try:
      res2 = lists.index(str(n2))

      b2 = lists[res2]
      print(f"Ental är: {b2}")
      break
    except ValueError:
      print(f"Number {n2} is not in current list")
 
  string_joltage = b1 + b2
  print(f"joltage for this battery is {int(string_joltage)}")
  print(f"total joltage is now {int(string_joltage)} + {int(tot_joltage)} = {int(string_joltage) + int(tot_joltage)}")
  tot_joltage += int(string_joltage)
  
  print 
print(tot_joltage)