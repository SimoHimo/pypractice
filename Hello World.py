import time
# import string
# alphabets = list(string.ascii_letters)
# alphabets.exteend(list(string.punctuation))
alphabets = [' ','!','a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
myMessege = "Hello_World!"
newMessege = ' '
index = 0


print("\n\n\n \033[92m")
for i in myMessege:
    for j in alphabets:
    
        print(newMessege+j, end="\r")
        time.sleep(0.1)
        
        if j == i:
            
            newMessege += j 
            print(newMessege, end="\r")
            index+=1
            break
        
    if newMessege == myMessege:
        break
    
print(newMessege+"\n\n\n")
