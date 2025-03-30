from random import *
print (int((random()*45)+5))
print (int((random()*45)+5))
print (int((random()*45)+5))
print (int((random()*45)+5))
print (int((random()*45)+5))
print (int((random()*45)+5))

cnt = 0 #총 탑승 승객 수 
for i in range(1, 51) : 
    time = randrange(5, 51)
    if 5<= time <= 15 : #5분-15분 이내의 손님
        print ("[0] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else : 
        print ("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(i, time))

print ("총 탑승 승객 : {0}분 ".format(cnt))