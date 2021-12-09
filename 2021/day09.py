import numpy as np

from helper import get_data

data = np.array([list(line) for line in open(get_data(9), 'r').read().split('\n')], dtype=np.int64)

"""
--- Day 9: Smoke Basin ---

These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into
the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The 
submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location 
can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most 
locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have 
three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the 
third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent 
location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6,
and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, 
although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations 
will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four 
basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
"""


def find_low_points(heightmap):
    low_points = find_low_points_with_coordinates(heightmap)
    risk_levels = [1 + point[0] for point in low_points]
    print(f"The sum of the risk levels of all low points is {sum(risk_levels)}")
    return sum(risk_levels)


def find_low_points_with_coordinates(heightmap):
    low_points = []
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            if i > 0 and heightmap[i - 1][j] <= heightmap[i][j]:
                continue
            if i < heightmap.shape[0] - 1 and heightmap[i + 1][j] <= heightmap[i][j]:
                continue
            if j > 0 and heightmap[i][j - 1] <= heightmap[i][j]:
                continue
            if j < heightmap.shape[1] - 1 and heightmap[i][j + 1] <= heightmap[i][j]:
                continue
            low_points.append((heightmap[i][j], (i, j)))
    return low_points


def find_basins(heightmap):
    basin_sizes = []
    for point, (x, y) in find_low_points_with_coordinates(heightmap):
        coordinates = find_number_of_basin_neighbors(heightmap, x, y)
        basin_sizes.append(len(coordinates))
    product_largest_3 = np.prod(sorted(basin_sizes, reverse=True)[0:3])
    print(f"The product of the 3 largest basin sizes is {product_largest_3}")
    return product_largest_3


def find_number_of_basin_neighbors(heightmap, x, y):
    coordinates = set([(x, y), ])
    if x > 0 and heightmap[x - 1][y] > heightmap[x][y] and heightmap[x - 1][y] != 9:
        coordinates.update(find_number_of_basin_neighbors(heightmap, x - 1, y))
    if x < heightmap.shape[0] - 1 and heightmap[x + 1][y] > heightmap[x][y] and heightmap[x + 1][y] != 9:
        coordinates.update(find_number_of_basin_neighbors(heightmap, x + 1, y))
    if y > 0 and heightmap[x][y - 1] > heightmap[x][y] and heightmap[x][y - 1] != 9:
        coordinates.update(find_number_of_basin_neighbors(heightmap, x, y - 1))
    if y < heightmap.shape[1] - 1 and heightmap[x][y + 1] > heightmap[x][y] and heightmap[x][y + 1] != 9:
        coordinates.update(find_number_of_basin_neighbors(heightmap, x, y + 1))
    return coordinates


example_data = np.array([[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                         [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]])

assert find_low_points(example_data) == 15

find_low_points(data)

assert find_basins(example_data) == 1134

find_basins(data)
