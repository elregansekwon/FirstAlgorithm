# 구입액 데이터만 정렬
x=[5000,12000,3000,8000,15000]
print(x)

print(sorted(x)) # 오름차순 정렬
print(sorted(x, reverse=True)) # 내림차순 정렬

# 고객 이름과 구입액 정렬
x=[['rabbit',5000],['snake',12000],['bear',3000],['raccoon',8000],['beetle',15000]]
print(x)

# 안쪽 배열의 1번째 데이터 기준 오름차순 정렬
print(sorted(x))
# 안쪽 배열의 2번째 데이터 기중 내림차순 정렬
print(sorted(x,key=lambda y:y[1],reverse=True))
# key: 정렬 키 지정
# lambda: key와 함께 사용 -> 정렬 키 지정 선택
# y: 안쪽 배열(고객 이름과 구매액)
# y[1]: 안쪽 배열의 2번째 데이터 기준


