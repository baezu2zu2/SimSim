import random as r
import

class Tile:
    def __init__(self, high: int, is_water: bool, is_building: bool, building_height: int or None):
        self.high = high
        self.is_water = is_water
        self.is_building = is_building
        self.building_height = building_height


class Board:
    def __init__(self, size, board_type):
        self.board = []
        self.size = size
        for i in range(size):
            dst = []
            for j in range(size):
                dst.append(None)
            self.board.append(dst)

        if board_type == 'mountain':
            peek = (r.randint(0, size-1), r.randint(0, size-1))
            peek_high = r.randint(5, 10)
            # noinspection PyTypeChecker
            self.board[peek[1]][peek[0]] = Tile(peek_high, False, False, None)
            self.lower(peek[1], peek[0], peek_high)

    def lower(self, x, y, high):
        for i in range(-1, 1):
            new_tile_num = 0
            for j in range(-1, 1):
                if i == j == 0 or not self.board[y + i][x + i]:
                    continue
                new_high = high - r.randint(1, 2)
                # noinspection PyTypeChecker
                self.board[y + i][x + i] = Tile(new_high, False, False, None)
                self.lower(x+i, y+i, new_high)

    def visualize_map(self):
        gl.glClearColor(1.0, 1.0, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glut.glutSolidCube(0.5)


if __name__ == '__main__':
    board = Board(30, 'mountain')
