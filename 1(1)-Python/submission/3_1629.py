# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    빠른 거듭제곱 알고리즘 구현
    분할 정복을 이용, 시간복잡도 고민!
    """
    if exp ==1:
        return base%mod
    elif exp % 2 ==0:
        answer = fast_power(base, exp//2, mod)
        return (answer**2)%mod
    else:
        answer = fast_power(base, exp//2, mod)
        return (base*answer**2)%mod
    


def fast_power_docstring(base: int, exp: int, mod: int) -> int:
    """
    만약 진수가 1이면 (제곱 필요 X):
        그냥 base%mod 반환
        return base%mod
    만약 진수가 짝수라면:
        진수%2 대신 넣고 fast_power하고
        return 할때 제곱해준 거에서 %mod 하고 반환
        return (answer**2)%mod
    만약 진수가 홀수라면:
        진수%2 대신 넣어서 fast_power하고
        답 구할 때 한번 더 진수 곱해준 거에서 %mod 하고 반환
        return (base*answer**2)%mod
        """
    return base%mod

def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 
    pass

def main_docstring() -> None:
    """
    A B C 모두 정수형으로 받아서
    저장하기!
    
    result는 fast_power(A, B, C) 결과물
    print(result)
    """
    pass
    
if __name__ == "__main__":
    main()