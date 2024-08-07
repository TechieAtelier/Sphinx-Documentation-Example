from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 7)

    print(f"Circle Area with radius {circle.radius}: {circle.area()}")
    print(f"Rectangle Area with length {rectangle.length} and width {rectangle.width}: {rectangle.area()}")
    print(f"Triangle Area with base {triangle.base} and height {triangle.height}: {triangle.area()}")

if __name__ == "__main__":
    main()
