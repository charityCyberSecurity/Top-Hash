#!/usr/bin/python3
import glob, os, hashlib

os.getcwd()

hashValue = [] 
#hashValue 
for file in os.listdir("files"):
    if file.endswith(".txt"):
        with open(os.path.join("files", file), 'rb') as f:
            print(file)
            file_contents = f.read()
            hash=hashlib.sha1(file_contents).hexdigest()
            hashValue.append(hash)

print("Hash value of all the contnts:")
print(hashValue)
print("\n")
if(len(hashValue)%2!=0):
        hashValue.append(hashValue[-1])
while(len(hashValue)>1):
    j=0
    for i in range(0, len(hashValue)-1):
        f = str(hashValue[i]+hashValue[i+1])
        hashValue[j]=hashlib.sha1(f.encode()).hexdigest()
        
        i+=2
        j+=1
    del hashValue[j:]

if (len(hashValue)==1):
    print("Top Hash is:") 
    print(hashValue)
    with open("check.aap", "a") as a:
        a.write(hashValue[0])
    print("The Top Hash has been saved in check.aap") 
        
    
