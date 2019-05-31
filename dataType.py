class Theater:
  name=''
  location=''
  capacity=0
  def __init__(self, a, b, c):
    self.name=a
    self.location=b
    self.capacity=c

  def set(self, a, b, c):
    self.name=a
    self.location=b
    self.capacity=c

class Play:
  name=''
  genre=''
  price=0
  def __init__(self, a, b, c):
    self.name=a
    self.genre=b
    self.price=c

  def set(self, a, b, c):
    self.name=a
    self.genre=b
    self.price=c

class audience:
  name=''
  sex=''
  age=0
  def __init__(self, a, b, c):
    self.name=a
    self.sex=b
    self.age=c

  def set(self, a, b, c):
    self.name=a
    self.sex=b
    self.age=c
