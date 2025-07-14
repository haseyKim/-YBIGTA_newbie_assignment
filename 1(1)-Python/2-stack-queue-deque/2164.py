from lib import create_circular_queue


"""
TODO:
- simulate_card_game 구현하기
    # 카드 게임 시뮬레이션 구현
        # 1. 큐 생성
        # 2. 카드가 1장 남을 때까지 반복
        # 3. 마지막 남은 카드 반환
"""


def simulate_card_game(n: int) -> int:
    """
    카드2 문제의 시뮬레이션
    맨 위 카드를 버리고, 그 다음 카드를 맨 아래로 이동
    """
    # 구현하세요!
    queue = create_circular_queue(n)
    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())

    return queue[0]

def simulate_card_garme_docstring(n:int) -> int:
    """
    create_circular_queue(n)으로 1부터 n까지 들어있는 queue 생성
    queue의 길이가 1보다 큰 경우:
        queue의 첫번째 (가장 왼쪽 요소) 제거
        queue의 첫번째 (가장 왼쪽 요소) 마지막 (가장 오른쪽)으로 옮기기

    queue의 길이가 1이 되면 해당 요소 (첫 번째 요소) 반환
    """
    return queue[0]

def solve_card2() -> None:
    """입, 출력 format"""
    n: int = int(input())
    result: int = simulate_card_game(n)
    print(result)

def solve_card2_docstring() -> None:
    """n : 입력받은 숫자, int (정수형)으로 저장
    result : int(정수형) = simulate_card_game(n)의 실행 결과 저장"""
    print(result)

if __name__ == "__main__":
    solve_card2()

"""코드 실행되면, solve_card2() 함수 실행"""