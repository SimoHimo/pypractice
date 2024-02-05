import time
bold = '\033[1m'
alphabets = [' ','!','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
myMessege = "Hello Madam!"
newMessege = ' '
variable = ' '
index = 0
print("\n\n\n")
for i in myMessege:
    for j in alphabets:
        variable = j
        print(newMessege+j, end="\r")
        time.sleep(0.10)
        if j == myMessege[index]:
            newMessege = newMessege+j
            print(newMessege, end="\r")
            index+=1
            break
        
    if newMessege == myMessege:
        break
    
print(bold+"\n\n   \t\t"+newMessege+"\n\n")
