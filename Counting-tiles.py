import math

def checkio(radius):
    """
    Checking only right top corner (all four corners are symmetric
    :param radius: 
    :return list of bool, whether corner in circle 
    """
    length = int(math.ceil(radius))

    def isCornersInCircle(tiles: tuple, R: int):
        """
        :param tiles: left_bottom, right_top corners of tile. If both corners are inside the circle
                      then tile is fully covered by circle, 1 corner covered - partially
        :param R: circle radius
        :return: tuple of bool - is each corners of tile covered? 
        """
        result = []
        for tile in tiles:
            result.append(math.sqrt(tile[0]**2 + tile[1]**2) <= radius)
        return result


    full_squares, partial_squares = 0, 0

    for i in range(length):
        for j in range(length):
            left_bottom = (i,j)
            right_top = (i+1, j+1)
            tile_result = isCornersInCircle((left_bottom, right_top), radius)
            if sum(tile_result) == 1: partial_squares +=1
            elif sum(tile_result) == 2: full_squares += 1
    return [full_squares, partial_squares]

print(checkio(2))





checkio(2.1)
#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio(2) == [4, 12], "N=2"
#     assert checkio(3) == [16, 20], "N=3"
#     assert checkio(2.1) == [4, 20], "N=2.1"
#     assert checkio(2.5) == [12, 20], "N=2.5"