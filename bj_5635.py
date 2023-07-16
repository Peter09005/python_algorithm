cnt = int(input())
sum_dict = {}
info = []
for _ in range(cnt):
    info.append(input().split())

for idx in range(cnt):
    sum = int(info[idx][1]) + 30 * int(info[idx][2]) + 365*int(info[idx][3])
    sum_dict[idx] = sum

sorted_dict = sorted(sum_dict.items(), key = lambda item : item[1])
print(info[sorted_dict[cnt-1][0]][0])
print(info[sorted_dict[0][0]][0])

# -1 을 사용하면 , 맨 마지막 index로 쉽게 접근할수있다는걸 잊지말자.

# Python의 sort는 , 만약 앞에 내용이 같으면 , 뒤쪽 값을 비교한다.

# int(yyyy+mm.zfill(2)+dd.zfill(2)) 이렇게 주민등록번호 형태로 한뒤, 비교하는 방법도 좋은방법인것같다

# Sort를 하면 리스트형태로 변환되나보다.. 이건 잘 모르겠다

# 그냥 name 과 주민등록번호 형태를 for문으로 dict에 보관한뒤, min 함수 , max 함수를 통해 값을 추출한다 가 맞는거같다.