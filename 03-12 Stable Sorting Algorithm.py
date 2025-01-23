# [음식이름, 가격(원), 소비기한(시간)]
x=[['새우튀김', 7000,12],['주먹밥', 1000, 8],['케이크',4000,4],['초밥',10000,8],['치즈',8000,72]]
print(x)

# key= 가격
# 내림차순 정렬
z = sorted(x, key=lambda y:y[1], reverse=True)
print(z)

# key= 소비 기한
# 오름차순 정렬
print(sorted(z,key=lambda y:y[2]))