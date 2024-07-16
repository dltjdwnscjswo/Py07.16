# 다음 이중 리스트의 평균값을 아래 출력 결과와 같이 각각 구하여라.
# my_list = [[100,200],[400,800],[1000,1400]]
my_list = [[100,200],[400,800],[1000,1400]]
var = 0
for i in my_list :
    for j in i :
        var = var + j
    print(var / len(i))
