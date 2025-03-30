
scores = [[52, 78, 93], [43, 85, 64], [77, 38, 91]]


student_num = 1

i =1 

for student in scores :
    print (f"학생 {student_num}의 점수 및 성적 : ")
    
    for value in student : 

        if value  >= 90 :
            grade = "A"

        elif value  >= 80 :
            grade = "B"

        elif value >= 70 :
            grade = "C"

        elif value >= 60 :
            grade = "D"

        else : 
            grade = "F"
        print (f"교과목 {i} : {value}점이며 성적은 {grade}")

        i += 1
    i -= 3

    student_num += 1
    print ()






