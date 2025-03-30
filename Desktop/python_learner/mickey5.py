score = int(input("점수를 입력하세요 (0-100) : "))

if score >=90 :
    grade = "A"
elif score >=90:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 50:
    grade = "D"
else :
    grade = "F"

print(f"성적은 {grade}입니다")