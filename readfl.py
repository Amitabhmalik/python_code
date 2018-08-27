# program to print the contents of the file
a=open("disp.txt","w")
b=int(raw_input("Enter the range:"))
for i in range(b):
	a.write(str(i))

a.close()

