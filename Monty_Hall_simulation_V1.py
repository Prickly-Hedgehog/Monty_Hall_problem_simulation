import random

doors = [0, 0, 0]

no_wins = 0
wins_switch = 0
wins_stay = 0

iterations = 10000

print("iterations: ", iterations, "\n\n")

for i in range(iterations):

  doors = [0, 0, 0]
  prize = random.randint(0, 2)
  doors[prize] = 1

  selected_door = random.randint(0, 2)

  if i <= iterations / 2:
    if doors[selected_door] == 1:
      wins_stay += 1

    else:
      no_wins += 1
    continue

  openable_doors = [i for i in range(len(doors)) if doors[i] == 0 and i != selected_door]

  doors[random.choice(openable_doors)] = 2

  switch_door = [i for i in range(len(doors)) if doors[i] != 2 and i != selected_door]

  if doors[switch_door[0]] == 1:
    wins_switch += 1
    continue

  else:
    no_wins += 1

print("switch wins: ", wins_switch, "\nstay wins: ", wins_stay, "\nno wins: ",no_wins)

total_wins = wins_switch + wins_stay

fraction_switch = round((wins_switch / total_wins) * 100, 3)
fraction_stay = round((wins_stay / total_wins) * 100, 3)

print("\nswitch wins: ", fraction_switch, "%", "\nstay wins: ", fraction_stay,"%")