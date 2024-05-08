# The aim of the program is to define if the user's dot, say M, lies within or outside the given polygon, e.g. polygon ABCDE with 5 vertices.
# To do that the program projects triangles from M to ABCDE vertices doing it clockwise, precisely ABM, BCM, CDM, DEM, EAM.
# Then the ABCDE square, on the one hand, and the sum of ABM, BCM, CDM, DEM, EAM squares, on the other, are compared.
# If ABCDE square is equal to ABM + BCM + CDM + DEM + EAM squares, the dot is inside. Otherwise the dot is outside
# Restrictions:
# 1. Polygon vertices are to be enumerated clockwise or counterclockwise. Otherwise it is impossible to calculate polygon square via summing up triangle squares.
# 2. Polygon is to be convex, where none of the vertices are pointed inward: when a line crosses the convex polygon, it intersects at most the two sides of the polygon.

POLYGON = [(0, 0), (0, 2), (2, 5), (4, 5), (4, 0)] #Contains coordinates x, y of polygon vertices

def main():
    point_x, point_y = get_point()
    res = is_point_in_polygon(POLYGON, point_x, point_y)
    print("Point inside") if res else print("Point outside")

def get_point():
    """
    Gets coord x and coord y of the user's point
    """
    while True:
        try:
            point_x, point_y = input("Coordinate x, y: ").split(",")
            return float(point_x), float(point_y)
        except ValueError:
            print("Invalid format")

def is_point_in_polygon(POLYGON, point_x, point_y):
    """
    Takes the polygon and the user's point,
    and defines if the point is inside the polygon
    """
    polygon_x, polygon_y = get_coords(POLYGON)
    polygon_square = get_polygon_square(POLYGON, polygon_x, polygon_y)
    test_square = get_test_square(POLYGON, polygon_x, polygon_y, point_x, point_y)
    res = compare_squares(polygon_square, test_square)
    return res

def get_coords(figure):
    """
    Gets coordinates of vertices of a figure,
    and groups them into two lists:
    coords_x contains X's of all the vertices,
    coords_y contains Y's of all the vertices
    """
    coords_x = []
    coords_y = []
    for x, y in figure:
        coords_x.append(x)
        coords_y.append(y)
    return coords_x, coords_y

def get_polygon_square(POLYGON, polygon_x, polygon_y):
    """
    Devides the polygon into triangles doing that clockwise,
    gets each triangle vertices,
    calculates each triangle square,
    returns the sum of triangle squares, i.e. the polygon square
    """
    polygon_square = 0
    for i in range(1, len(POLYGON)-1):
        triangle = [(polygon_x[0], polygon_y[0]), (polygon_x[i], polygon_y[i]), (polygon_x[i+1], polygon_y[i+1])]
        triangle_x, triangle_y = get_coords(triangle)
        triangle_square = get_triangle_square(triangle_x, triangle_y)
        polygon_square += triangle_square
    return polygon_square

def get_triangle_square(triangle_x, triangle_y):
    """
    Uses the formula to calculate triangle square via triangle coordinates
    """
    triangle_square = abs((triangle_x[1]-triangle_x[0])*(triangle_y[2]-triangle_y[0])-(triangle_x[2]-triangle_x[0])*(triangle_y[1]-triangle_y[0])) / 2
    return triangle_square

def get_test_square(POLYGON, polygon_x, polygon_y, point_x, point_y):
    """
    Projects triangles from the user's figure to polygon vertices doing that clockwise,
    gets each triangle vertices,
    calculates each triangle square,
    returns the sum of triangle squares, i.e. a test square to compare with the polygon square
    """
    test_square = 0
    for i in range(-1, len(POLYGON)-1):
        triangle = [(polygon_x[i], polygon_y[i]), (polygon_x[i+1], polygon_y[i+1]), (point_x, point_y)]
        triangle_x, triangle_y = get_coords(triangle)
        triangle_square = get_triangle_square(triangle_x, triangle_y)
        test_square += triangle_square
    return test_square

def compare_squares(polygon_square, test_square):
    """
    Compares the polygon square and the test square projected from the user's figure,
    returns True if the squares are equal,
    returns False if the squares are not equal
    """
    return True if polygon_square == test_square else False

if __name__ == "__main__":
    main()
