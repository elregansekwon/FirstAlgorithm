x=['순록','다람쥐','토끼','곰','거북이']
print(x)

print(x.index('거북이'))
print(x.index('다람쥐'))

x=[['raccoon',10,300],['fox',40,60],['reindeer',20,500],['cat',70,800]]
print((x))

# 사용자 이름이 'reindeer'인 게임 아이템 정보 꺼내기
print([y for y in x if y[0]=='reindeer'])
# for y in x: 바깥 배열 x에 있는 안쪽 배열 y 차례대로 검사
# if y[0]=='reindeer': 안쪽 배열의 1번째 데이터가 reindeer이면
# [y ~~~]: y 배열을 []안에 넣어서 출력