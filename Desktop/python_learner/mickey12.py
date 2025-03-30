student = [1, 2, 3, 4, 5]
print(student)
student = [i+100 for i in student] 
print (student)

student = ('iron man', 'thor', 'i am groot')
student = [len(i) for i in student]
print (student)

student = ('iron man','thor', 'i am groot')
student = [i.upper() for i in student]
print(student)