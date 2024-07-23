# ################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # Local scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion() # this will give 2
# print(potion_strength) # this will give NameError (not defined) because it's local scope

# # Global scope

# player_health = 10


# def drink_potion():
#   potion_strength = 2
#   print(player_health)

# drink_potion() # this will give 10

# There is no block scope

# Modifying global scope - this is not recommended

# enemies = 1

# def increase_enemies():
#   global enemies
#   enemies +=1
#   print(f"enemies inside function:{enemies}")

# increase_enemies()
# print(f"enemies outside function:{enemies}")

# Modifying global scope - better
enemies = 1

def increase_enemies():
  print(f"enemies inside function:{enemies}")
  return enemies + 1
  

enemies = increase_enemies()
print(f"enemies outside function:{enemies}")