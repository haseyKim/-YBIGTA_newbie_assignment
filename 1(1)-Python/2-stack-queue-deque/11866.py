from lib import create_circular_queue, rotate_and_remove


"""
TODO:
- josephus_problem 구현하기
    # 요세푸스 문제 구현
        # 1. 큐 생성
        # 2. 큐가 빌 때까지 반복
        # 3. 제거 순서 리스트 반환
"""


def josephus_problem(n: int, k: int) -> list[int]:
    """
    요세푸스 문제 해결
    n명 중 k번째마다 제거하는 순서를 반환
    """
    # 구현하세요!
    target = create_circular_queue(n)
    result = []
    while len(target)!=0:
        if len(target)>=k:
            result.append(rotate_and_remove(target, k))

        elif len(target)<k:
            mod_k = k%len(target)
            if mod_k==0:
                mod_k = len(target)
            result.append(rotate_and_remove(target, mod_k))

    return result

def josephus_problem_docstring(n: int, k: int) -> list[int]:
    """
    1부터 n까지 들어있는 queue 생성 -> target에 저장
    비어있는 리스트 result 생성 -> 최종 반환용
    target이 빌 때까지 반복:
        target의 길이가 k보다 긴 경우:
            target의 k번째 요소 제거 후 rotate, 제거한 요소 result에 append
        else:
            mod_k는 k를 target의 길이로 나눈 나머지 (k만큼 가야하는데, target을 이미 여러번 돌았다고 봄)
            만약 mod_k가 0 (target의 길이가 k의 약수인 경우):
                mod_k를 그냥 target의 길이로 둠. (어차피 마지막 요소 뺌)
            target에서 mod_k번째 요소 제거하고 rotate, 제거한 요소 result에 append"""
    return result

def solve_josephus() -> None:
    """입, 출력 format"""
    n: int
    k: int
    n, k = map(int, input().split())
    result: list[int] = josephus_problem(n, k)
    
    # 출력 형식: <3, 6, 2, 7, 5, 1, 4>
    print("<" + ", ".join(map(str, result)) + ">")

def solve_josephus_docstring() -> None:
    """
    n 정수형 입력
    k 정수형 입력
    n, k 입력받은 숫자 각각 저장
    result는 josephus_problem(n, k) 실행해서 반환된 값 (정수형으로 구성된 list)
    print : result에 있는 요소들 <3, 5> 와 같은 출력형식에 맞춰 print"""

if __name__ == "__main__":
    solve_josephus()

"""코드 실행하면
solve_josephus() 함수 실행"""