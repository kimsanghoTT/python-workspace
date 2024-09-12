'''
자바에선
for(i = 0; i < 3; i++){
    System.out.println("i값 : " + i);
}

파이썬에선
for 변수명 in 배열들:
    print(변수명)
'''
과일들=["사과", "오렌지", "포도"]
for f in 과일들:
    print(f)

#배열이 아니라 특정 숫자 사이를 출력해야 할 때

for i in range(1, 6): # range(1이상, 6미만)
    print(i)

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")