# 프로그램에서 재사용 가능한 코드 블록
# 특정 연산이 반복되는 코드는 항상 함수 코드로 작성
# 특정 작업을 수행하는 독립적 단위
# 함수를 활용하면 코드의 구조화,중복 방지, 유지 보수성 향상

# def 함수 이름 (매개변수) :
# 코드블록,함수에서 실행할 코드
# return value
# 코드 블록 실행 이후 결과 값

def add_numbers(number_1,number_2) :
    result = number_1 + number_2
    print(result)
    return result

c = add_numbers(3,5,)
d = add_numbers(number_1:50,number_2:30)