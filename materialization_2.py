

hour = int(input())
count = 0

for i in range(hour+1) : # 주의!) hour가 5인 경우, 0-4이니 +1을 해준다. 
    for  j in range(60) : 
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) :
                count += 1
                
print(count)

                
            
    

    


    
    
    