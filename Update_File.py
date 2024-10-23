def update(file_path,key,value):

    with open(file_path,"r") as file:
        lines=file.readlines()
        print(lines)

    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
               file.write(f'{key}=={value} \n') 
            else:
               file.write(line)   

update("hello.txt","a",500)