# : 한줄 주석
''' 여러 줄 주석 '''

# print = java의 system.out.println
'''
java에서 출력할 땐 메인메서드 안에 출력메서드를 작성
public static void main(String args[]){
    System.out.println("하이요");
}
'''
print('하이요')

#변수 출력하기
name ="학생"
age = 20
print(f"{name}이고, {age}살 입니다.")