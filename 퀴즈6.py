# 1부터 100까지 수를 2의 배수,3의 배수, 5의 배수로 분류하려고 한다.
numbers_1 = []
numbers_2 = []
numbers_3 = []

for i in range (1, 101) :
    if i % 2 == 0 :
        numbers_1.append(i)
    if i % 3 == 0 :
        numbers_2.append(i)
    if i % 5 == 0 :
        numbers_3.append(i)
print(numbers_1)
print(numbers_2)
print(numbers_3)