from __future__ import annotations
from collections import deque


"""
TODO:
- rotate_and_remove 구현하기 
"""


def create_circular_queue(n: int) -> deque[int]:
    """1부터 n까지의 숫자로 deque를 생성합니다."""
    return deque(range(1, n + 1))

def rotate_and_remove(queue: deque[int], k: int) -> int:
    """
    큐에서 k번째 원소를 제거하고 반환합니다.
    """
    for i in range(k-1):
        queue.rotate(-1)
    return queue.popleft()

def create_circular_queue_docstring(n:int) -> deque[int]:
    """
    1부터 n까지의 숫자로 (1씩 증가) deque 생성
    생성된 deque 반환
    """
    return deque(range(1, n+1))

def rotate_and_remove_docstring(queue: deque[int], k:int) -> int:
    """
    0~k-1까지 반복 : k번 반복
        deque의 요소를 왼쪽으로 한 칸씩 이동 
    -> 결과 : 가장 왼쪽에 k가 있음. 
    popleft : 가장 왼쪽 요소 제거 및 반환
    """
    return queue.popleft()