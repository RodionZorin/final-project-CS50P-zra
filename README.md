# IS POINT INSIDE POLYGON?
    #### Video Demo:  https://youtu.be/QCZXSzDA7zw
    #### Description:

**Program objective**

My program objective is to define if the user's point, say M, lies within or outside the given polygon, e.g. polygon ABCDE with 5 vertices. To do that the program projects triangles from M to ABCDE vertices doing it clockwise, precisely ABM, BCM, CDM, DEM, EAM. Then the ABCDE square, on the one hand, and the sum of ABM, BCM, CDM, DEM, EAM squares, on the other, are compared. If ABCDE square is equal to ABM, BCM, CDM, DEM, EAM squares, the point is inside. Otherwise the point is outside.

*Restrictions*:

1. Polygon vertices are to be enumerated clockwise or counterclockwise. Otherwise it is impossible to calculate polygon square via summing up triangle squares.

2. Polygon is to be convex, where none of the vertices are pointed inward: when a line crosses the convex polygon, it intersects at most the two sides of the polygon.

**Program possible usage**

My program main idea is inspired by a real life challenge. Say, you have a shop and you want to deliver your goods to your customers. However, your resources are limited, and you can accept orders only from a certain area. So, you can define this area as a polygon. When a customer orders a delivery, my program concept comes into play. Precisely, the program defines, if the customer is or outside the delivery area. In case the customer is inside, the order can be processed. Otherwise the customer can be invited to the shop to get his goods in person.

**Functions**

My program operates on a predefined polygon established as a CONSTANT, and consists of the main function and 7 additional functions.

1. get_point()

The function gets coord x and coord y of the user's point.

2. is_point_in_polygon(POLYGON, point_x, point_y)

Takes the polygon and the user's point coords, and defines if the point is inside the polygon. So, this function returns the final result, and all the other functions below work for this function.

3. get_coords(figure)

This function gets coordinates of vertices of a figure, for example of a polygon or triangle. It groups the the coordinates into two lists: coords_x contains coord x of all the vertices, coords_y contains coord y of all the vertices.

4. get_polygon_square(POLYGON, polygon_x, polygon_y)

Devides the polygon into triangles doing that clockwise. Gets each triangle vertices and calculates each triangle square. Returns the sum of triangle squares, i.e. the polygon square.

5. get_triangle_square(triangle_x, triangle_y)

Uses a special formula to calculate triangle square via triangle coordinates.

6. get_test_square(POLYGON, polygon_x, polygon_y, point_x, point_y)

Projects triangles from the user's figure to polygon vertices doing that clockwise. Gets each triangle vertices and calculates each triangle square. Returns the sum of triangle squares, i.e. a test square.

7. compare_squares(polygon_square, test_square)

Compares the polygon square and the test square. Returns True if the squares are equal, returns False if the squares are not equal.
