class GameObject:
  def __init__(self, name, x_pos, y_pos):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos

  def move(self, by_x_amount, by_y_amount):
    self.x_pos += by_x_amount
    self.y_pos += by_y_amount

class Enemy(GameObject):
  def __init__(self, name, x_pos, y_pos, health):
    super().__init__(name, x_pos, y_pos)
    self.health = health  

  def take_damage(self, damage_amount):
    self.health -= damage_amount
  
game_object = GameObject("Player 1", 1, 2)
enemy = Enemy("Enemy 1", 5, 10, 100)

print(game_object.name)
print(enemy.name)

print(enemy.health)
enemy.take_damage(20)
print(enemy.health)