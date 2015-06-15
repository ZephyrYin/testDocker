import os
path = os.getcwd();
with open('/mnt/testVol/test1Output.txt','w') as file:
	file.write(path+'\n')
	for i in range(20):
		file.write(str(i) + '\n')
		print 'this is test 1 !'

