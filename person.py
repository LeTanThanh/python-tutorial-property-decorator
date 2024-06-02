class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self._age = age

  @property
  def age(self):
    return self._age
