from shapes import Circle,Rectangle,Triangle
def calc():
  shapes=[Circle(4),Rectangle(5,8),Triangle(3,4,5)]
  for shape in shapes:
    print(shape)
  print(f" the Area ={shape.__class__.__name__} is {shape.Area()}")
calc()