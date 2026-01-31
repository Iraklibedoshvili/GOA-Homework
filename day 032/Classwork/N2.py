def Square(length = 10):
    square_area = length ** length
    square_perimeter =  length * 4
    return  square_area,square_perimeter
square_area1,square_perimeter1 = Square(5)
square_area2,square_perimeter2 = Square()