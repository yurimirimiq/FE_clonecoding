"""
#while
customer = "토르"
index = 5
while index >= 1 :
    print (f"{customer}, 커피가 준비되었습니다. {index}번 남았어요")
    index -= 1
    if index == 0:
        print ("커피가 폐기 처분되었습니다.")
"""
'''
customer = "아이언맨"
index = 1
while True :
    print(f"{customer}, 커피가 준비되었습니다. 호출 {index}회")
    index += 1 
    #무한
'''

customer = "thor"
person = "unknown"

while person != customer :
    print(f"{customer}, 커피가 준비되었습니다. ")
    person = input("이름이 어떻게 되세요? ")