#start
text="Hello World"
print(text[0:5])
print(text[:4])#By default start slicing from index 0

#stop
print(text[6:10])#stop at last index but the last index won't be included
print(text[7:])#By default stop slicing in last index

#step(increment wise)
print(text[1::2])#start from index 1 and step 2 index