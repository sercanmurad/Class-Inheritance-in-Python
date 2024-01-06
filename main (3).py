class Animal:
  def __init__(self):
    self.num_eyes = 2

  def are_animal(self):
    print("I am an animal")

  def breathe(self):
    print("Inhale, exhale")

class Fish(Animal):
  def __init__(self):
    super().__init__()

  def swim(self):
    print("I can swim")

  def breathe(self):
    super().breathe()
    print("doing this underwater")

nemo=Fish()
nemo.swim()
nemo.are_animal()
print(nemo.num_eyes)
nemo.breathe()