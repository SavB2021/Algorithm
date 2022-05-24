from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

        You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

        To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

        Return the modified image after performing the flood fill.


        :param image: list of lists
        :param sr: start row
        :param sc: start column
        :param newColor: integer representing newColor
        :return: list of lists
        """
        prevC = image[sr][sc]
        if prevC == newColor:
            return image
        return self.floodFillUtil(image, sr, sc, prevC, newColor)

    def floodFillUtil(self, screen, x, y, prevC, newC):
        # Base cases
        if x < 0 or x >= len(screen) or y < 0 or y >= len(screen[0]) or screen[x][y] != prevC or screen[x][y] == newC:
            return

            # Replace the color at (x, y)
        else:
            screen[x][y] = newC

        # Recur for north, east, south and west
        self.floodFillUtil(screen, x + 1, y, prevC, newC)
        self.floodFillUtil(screen, x - 1, y, prevC, newC)
        self.floodFillUtil(screen, x, y + 1, prevC, newC)
        self.floodFillUtil(screen, x, y - 1, prevC, newC)
        return screen
