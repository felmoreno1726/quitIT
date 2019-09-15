import subprocess
import time

#bashCommand1 = 'raspistill -o test.jpeg'
bashCommand2 = 'bash setup2.sh'
bashCommand3 = 'bash setup.sh'
bashCommand4 = 'rm out.txt'
bashCommand5 = 'sleep 10m'
bashCommand6 = 'bash setup3.sh'


for i in range(30):
	#process1 = subprocess.Popen(bashCommand1.split(), stdout=subprocess.PIPE)
	#output1, error1 = process1.communicate()

	process2 = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
	output2, error2 = process2.communicate()

	time.sleep(10)

	print("Done IBM")

	with open('out.txt') as myfile:
		content = myfile.read()

	print(content.split('"')[17])
	if(content.split('"')[17] == 'smoking'):
		print("Smoking!")
		process4 = subprocess.Popen(bashCommand6.split(), stdout=subprocess.PIPE)
		output4, error4 = process4.communicate()
		process3 = subprocess.Popen(bashCommand3.split(), stdout=subprocess.PIPE)
		output3, error3 = process3.communicate()
		time.sleep(10)

	process4 = subprocess.Popen(bashCommand4.split(), stdout=subprocess.PIPE)
	output4, error4 = process4.communicate()

	process5 = subprocess.Popen(bashCommand5.split(), stdout=subprocess.PIPE)
	output5, error5 = process5.communicate()