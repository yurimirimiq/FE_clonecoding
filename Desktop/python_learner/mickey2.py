score1 = int(input("학생 1의 점수를 입력해주세요 : "))
score2 = int(input("학생 2의 점수를 입력해주세요 : "))

#if 조건문을 활용한 학점 구분
if score1 >= 90:
    grade = "A"

if (score1 < 90) and (score1 >=80) :
    grade = "B"

if (score1 < 80) and (score1 >=70) :
    grade = "C"

if (score1 < 70) and (score1 >=50) :
    grade = "D"

if score1 < 50:
    grade = "E"

#마지막 출력
print (f"학생 1의 점수는 {score1}점이고 학점은 {grade}입니다.")

#if 조건문을 활용한 학점 구분
if score2 >= 90:
    grade = "A"

if (score2 < 90) and (score2 >=80) :
    grade = "B"

if (score2 < 80) and (score2 >=70) :
    grade = "C"

if (score2 < 70) and (score2 >=50) :
    grade = "D"

if score2 < 50:
    grade = "E"

#마지막 출력
print (f"학생 2의 점수는 {score2}점이고 학점은 {grade}입니다.")

if score1 > score2 :
    print ("학생1의 점수가 학생2의 점수보다 높습니다!")

if score1 == score2 :
    print ("학생1의 점수가 학생2의 점수와 같습니다!")

if score1 < score2 :
    print ("학생1의 점수가 학생2의 점수보다 닞습니다!")