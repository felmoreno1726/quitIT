import subprocess

bashCommand = 'curl -X PATCH -d "{\"trigger\":\"true\"}"  "https://quitit-2d3af.firebaseio.com/trigger.json"'
with open('out.txt') as myfile:
    content = myfile.read()
if(content.split('"')[17] == 'smoking'):
	print("Smoking!")
	#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	#output, error = process.communicate()

else:
	print("Nope")


