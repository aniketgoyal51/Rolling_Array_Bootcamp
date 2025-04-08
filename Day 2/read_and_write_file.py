file=open("D:/web dev personal/Leaning Practice/Rolling_Array_Bootcamp/Day 2/read_file_dome", "r") # r+=read and write , r=read , w=write , a=append at end

# read  --------------------------------------------------

print(file.readable())
for i in file.readlines():
    print(i)


#  write   -----------------------------------------------------

file=open("D:/web dev personal/Leaning Practice/Rolling_Array_Bootcamp/Day 2/write_file_dome", "w") # r+=read and write , r=read , w=write , a=append at end


file.write("this is a new text")


file.close()


