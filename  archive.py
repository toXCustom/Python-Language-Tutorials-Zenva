print("Hi!")
print("Paweł Mróz")
# name = value
x_position = 10
print(x_position)

x_position = 15
print(x_position)

pi = 3.14
print(pi)

is_game_over = False
is_game_over = True
print(is_game_over)
print(type(is_game_over))

is_game_over = 1
print(is_game_over)
print(type(is_game_over))

name = 'Paweł'
is_game_over_text = "False"
print(name)
print(type(name))
print(is_game_over_text)
print(type(is_game_over_text))

age = 31
print(age)
print(type(age))
name_and_age = "Paweł: {}".format(age)
print(name_and_age)

# + - * / % // ** =

x_position = 10
# x_position = 11
forward = x_position + 1
print(x_position)
print(forward)
backward = x_position - 1
print(backward)

remainder = 5 % 2
print(remainder)
floor_division = 5 // 2
print(floor_division)

five_sqared = 5 ** 2
print(five_sqared)

x_position = x_position + 1
print(x_position)
x_position += 1
print(x_position)

first_name = "Paweł "
last_name = "Mróz"
print (first_name + last_name)

# > >= < <= == != not or and

x_position = 10
end_position = 10
is_at_end = x_position == end_position
print(is_at_end)

is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

not_is_at_end = not is_at_end
print(not_is_at_end)

# score = 10
# is_game_over = score >= 10 and is_at_end
score = 9
is_game_over = score >= 10 or is_at_end
print(is_game_over)

# name = [5, True, "string"]

enemy_positions = [5, 10, 15]
print(enemy_positions)
enemy_positions = [5, 10, 15, 20]
print(enemy_positions)
print(enemy_positions[0])
print(len(enemy_positions))
enemy_positions[0] = 6
print(enemy_positions)
print(enemy_positions[0:2])

enemy_positions.append(25)
enemy_positions[0] = 5
print(enemy_positions)

enemy_positions.insert(1, 9)
print(enemy_positions)

enemy_positions.remove(5)
print(enemy_positions)

del(enemy_positions[2])
print(enemy_positions)

high_score = ("Paweł", 120)
print(high_score)

high_score = ("Davide", 150)
print(high_score)

# high_score[0] = "Gabriele"

name = high_score[0]
print(name)

print(len(high_score))

print("Holly" in high_score)

print(name[0])
print(name[0:2])
print("Hol" in name)
print(len(name))

# dict = {key: value, key: value}

actions = {"r": 1, "l": -1}
print(actions)

print(actions["r"])
# print(actions["g"])
print(actions.get("g"))

actions["r"] = 2
actions["u"] = 1
print(actions)

print(actions.keys())
print(actions.values())
print(actions.items())

del(actions["u"])
print(actions)

actions.pop("r")
print(actions)

# if condition = True:
#   execute some code

key = "l"

if key == "r":
  print("Move right!")
elif key == "l":
  print("Move left!")
else:
  print("Invalid key")

print("Done")

# while condition = True:
#   execute some code multiple times

position = 0
end_position = 10
enemy_position = 15

while position < end_position:
  position += 1
  print(position)
  if position == enemy_position:
    print("Game over!")
    break

if position == end_position:
  print("You have reach the end!")

# for item in coollection:
#   execute code using that item

enemy_positions = [5, 10, 15]

for enemy_position in enemy_positions:
  print(enemy_position)
  
for i in range(0, 5):
  print("Hello")

# def function_name():
#   asd asd asd

position = 0

def move_player():
  global position
  position += 1
  print(position)

move_player()

position = 0

def move_player(position, by_amount):
  position += by_amount
  return position

position = move_player(position, 3)
print(position)
position = move_player(position, 5)
print(position)

class GameObject:
  def __init__(self, name, x_pos, y_pos):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos

game_object = GameObject("Enemy", 1, 2)
print(game_object.name)
game_object.name = "Enemy 1"
print(game_object.name)

class GameObject:
  def __init__(self, name, x_pos, y_pos):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos

  def move(self, by_x_amount, by_y_amount):
    self.x_pos += by_x_amount
    self.y_pos += by_y_amount

game_object = GameObject("Enemy", 1, 2)
print(game_object.name)
game_object.name = "Enemy 1"
print(game_object.name)

print(game_object.x_pos)
print(game_object.y_pos)

game_object.move(5, 10)
print(game_object.x_pos)
print(game_object.y_pos)

other_game_object = GameObject("Player 2", 2, 0)
print(other_game_object.name)
print(other_game_object.x_pos)
print(other_game_object.y_pos)

other_game_object.name = "New name for Player 2"
print(other_game_object.name)
print(game_object.name)

