import pathlib
import typing as tp
import random

import time
import multiprocessing

alphabet = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)

def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid

def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()

def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    if n**2 > len(values):
        raise "group: мало значений для составления таблицы"
    res = [[' ' for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = values[i*n + j]
    return res

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]].copy()

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    return [grid[i][pos[1]] for i in range(len(grid))]

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('src/lab3/puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    row = row - row % 3
    col = col - col % 3
    res = []
    for i in range(3):
        res += grid[row + i][col:col+3]
    return res

def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                return i, j
    return -1, -1

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    act_row = set(get_row(grid, pos))
    act_col = set(get_col(grid, pos))
    act_block = set(get_block(grid, pos))
    act_all = act_row | act_col | act_block
    return alphabet - act_all

def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    pos = find_empty_positions(grid)
    if pos[0] == -1:
        return grid
    for possible_values in find_possible_values(grid, pos):
        grid[pos[0]][pos[1]] = possible_values
        res = solve(grid)
        if res != [[]]:
            return res
    grid[pos[0]][pos[1]] = '.'
    return [[]]

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False
    >>> solution = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],        ]
    >>> check_solution(solution)
    True
    >>> solution = [["5", "5", "4", "6", "7", "8", "9", "1", "2"],            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],        ]
    >>> check_solution(solution)
    False
    """
    for i in range(len(solution)):
        if(set(get_row(solution, (i, 0))) != alphabet
                or set(get_col(solution, (i, 0))) != alphabet
                or set(get_block(solution, (i * 3 % 9, i // 3 * 3))) != alphabet):
            return False
    return True

def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    N = min(N, 81)
    res = [['.' for i in range(9)] for i in range(9)]
    res = solve(res)
    all_poses = [[i, j] for i in range(9) for j in range(9)]
    for pos in random.sample(all_poses, 81 - N):
        res[pos[0]][pos[1]] = '.'
    return res


def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solution = solve(grid)
    end = time.time()
    print()
    print(filename, "ответ получен за:", end - start)
    if not solution:
        print("Puzzle can't be solved")
    elif check_solution(solution) == False:
        print("Puzzle неправильно решён")
    else:
        display(solution)

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        p = multiprocessing.Process(target=run_solve, args=(filename,))
        p.start()