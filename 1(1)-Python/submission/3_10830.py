from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        self.matrix[key[0]][key[1]] = value % Matrix.MOD

    def __setitem__docstring(self, key: tuple[int, int], value: int) -> None:
        """
        행렬 특정 위치에 값 할당 
        MOD 이용해서 나머지를 저장"""

    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result

    def __pow__(self, n: int) -> Matrix:
        assert self.shape[0] == self.shape[1]
        if n==0:
            return Matrix.eye(self.shape[0])
        elif n==1:
            return self.clone()
        
        half = self ** (n//2)
        result = half @ half

        if n%2 ==1:
            result = result @ self
        
        return result
    
    def __pow__docstring(self, n: int) -> None:
        """
        n: 거듭제곱할 지수 (>=0)
        n==0인 경우:
            return 항등행렬
        n==1인 경우:
            return self
        n>1:
            짝수인 경우 -> A^(n//2)를 제곱해서 반환
            홀수인 경우 -> A^(n//2)를 제곱하고 A를 곱해서 반환
        """
        pass


    def __repr__(self) -> str:
        return '\n'.join(' '.join(str(cell % Matrix.MOD) for cell in row) for row in self.matrix)
    

    def __repr__docstring(self) -> None:
        """
        최종 행렬을 문자열로 한 행씩 나타냄
        """
        pass


from typing import Callable
import sys


"""
-아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()