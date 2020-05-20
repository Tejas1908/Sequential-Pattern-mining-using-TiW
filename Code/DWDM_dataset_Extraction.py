# create database

# database = dict()
# database['sid']=[10,20,30,40]
# database['sequence']=[['a','abc','ac','d'],['ad','c','bc','ae'],['ad','bc','df'],['a','abc','d']]
# database['timestamp']=[[0,1,2,3],[1,2,3,4],[1,3,5],[2,3,4]]
#
# database['10'] = [['a', 0], ['abc', 1], ['ac', 2], ['d', 3]]
# database['20'] = [['ad', 1], ['c', 2], ['bc', 3], ['ae', 4]]
# database['30'] = [['ad', 1], ['bc', 3], ['df', 5]]
# database['cd40'] = [['a', 2], ['abc', 3], ['d', 4]]
#
# # print database
#
# for i in database.keys():
# 	print(i, end=' ')
# 	for j in database[i]:
# 		print(j[0], end=' ')
# 	for j in database[i]:
# 		print(j[1], end=' ')
# 	print()

import random

# lower = 111; upper = 999
# random_float = random.uniform(lower, upper)
# print(random_float)
def Randlist(start, end, num):
	res = []

	for j in range(num):
		val=(random.uniform(start, end))
	#	val=int(val)
		res.append(val)

	res.sort()
	return res


text_file= open("sample.data","r")
lines= text_file.readlines()
# line1= lines[0]
undelted_lines= lines
print("\nInput :\n")
print(lines)
x = dict()
for i in range(len(lines)):
	line1 = list(lines[i].split(" "))
	# print(line1)
	line1.pop()
	length = int(line1[0])
	# print(length)
	line1.pop(0)
	# x= dict()
	# print(line1)
	lst = []

	for j in range(length):
		sizeoflistoftime= int(line1[0])
		# print(sizeoflistoftime)
		line1.pop(0)
		# print(line1)

		listoftime=Randlist(0,1000,sizeoflistoftime)
		for k in range(sizeoflistoftime):
			line1.pop(0)
		# print(listoftime)

		lst.append(listoftime)
	# print("The list is :")
	# print(lst)
	x[i]=lst


# print(x)

# print(undelted_lines)
x2= dict()

for i in range(len(undelted_lines)):
	line1 = list(undelted_lines[i].split(" "))
	# print(line1)
	line1.pop()
	length = int(line1[0])
	# print(length)
	line1.pop(0)
	# print(line1)
	listoftime=[]
	for j in range(length):
		sizeoflistoftime= int(line1[0])
		# print(sizeoflistoftime)
		line1.pop(0)
		# print(line1)
		temp=""
		# listoftime=Randlist(0,1000,sizeoflistoftime)
		for k in range(sizeoflistoftime):
			temp=temp+line1[0]
			line1.pop(0)


		listoftime.append(temp)
	# print(listoftime)
	x2[i]=listoftime

print("\n\nTime stamp\n")
print(x)
print("\n\nSequence\n")
print(x2)