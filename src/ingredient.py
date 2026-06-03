class Ingredient:
  def __init__(self, name: str, quantity: float, unit: str):
    self.name = name
    self.quantity = quantity
    self.unit = unit
  @property
  def quantity(self):
    return self._quantity
  @quantity.setter
  def quantity(self, value):
    if value <=0:
      raise ValueError("Количество должно быть положительным")
    self._quantity = float(value)
  def __str__(self):
    return f"{self.name}: {self.quantity} {self.unit}"
  def __repr__(self):
    return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
  def __eq__(self, another_ingridient):
    if not isinstance(another_ingridient, Ingredient):
            return False
    return self.name == another_ingridient.name and self.unit == another_ingridient.unit