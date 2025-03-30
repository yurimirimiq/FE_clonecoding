# 학생 점수 리스트 (샘플)
scores = [
    23, 33, 45, 65, 78, 88, 90, 93, 100,
    83, 75, 60, 59, 40, 99, 85, 67, 74,
    91, 95, 68, 72, 88, 90, 93, 84, 100
]

# 학점 판별 함수
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 메인 실행부
for i, score in enumerate(scores, start=1):
    grade = get_grade(score)
    print(f"학생{i} 점수: {score} → 학점: {grade}")