---part 1
sum_possible = 0
limit = {'red':12, 'green':13, 'blue':14}


with open('day2input.txt','r') as f:
  for i, line in enumerate(f.readlines()):
    impossible = False 
    picks = line.strip()[line.find(':')+2:].split(';')
    for p in picks:
      for part in p.split(', '):
        print(part)
        num, colour = part.split(' ')
        num = int(num)
        if num > limit[colour]:
          impossible = True
          break
      if impossible:
           break
    if not impossible:
      sum_possible += (i + 1) 
print(sum_possible)

---part 2

sum_possible = 0
limit = {'red': 12, 'green': 13, 'blue': 14}

with open('day2input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        impossible = False
        picks = line.strip()[line.find(':') + 2:].split(';')
        for p in picks:
            for part in p.split(', '):
                values = part.split(' ')
                if len(values) != 2:
                    # Skip invalid parts with more or fewer values
                    continue

                num, colour = values
                num = int(num)
                if num > limit[colour]:
                    print(f"Game {i + 1} is impossible due to {num} {colour} cubes")
                    impossible = True
                    break
            if impossible:
                break
        if not impossible:
            sum_possible += 1
            print(f"Game {i + 1} is possible")

print("Sum of possible game IDs:", sum_possible)
