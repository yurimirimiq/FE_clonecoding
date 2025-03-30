import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

scores = {"수학":0 , "영어":50 , "코딩":100}
for sub, score in scores.items():
    #print(sub, score) 
    print (sub.ljust(8), str(score).rjust(4), sep=" : ")

for num in range (1, 21) : 
    print ("your waiting : " + str(num).zfill(3))

#zfill 

answer = input("아무값이나 입력 : ")
print ("입력하신 값은" +answer+ "입니다.")