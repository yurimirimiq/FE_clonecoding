absent = [2, 5]
nobook = [7]
for student in range(1, 11) : 
    if student in absent : 
        continue
    elif student in nobook :
        print (f"{student} 교무실로")
        break
    print(f"{student} 책을 읽자! ")