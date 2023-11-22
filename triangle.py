class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def is_valid(self):
        if len(self.sides) != 3 or 0 in self.sides:
            print("Ошибка неверные числа.")
        elif sum(self.sides) <= max(self.sides) * 2:
            print("Ошибка: такого треугольника не может быть.")
        else:
            print("Треугольник возможен.")

triangle = Triangle([2, 3, 4])
triangle.is_valid()
