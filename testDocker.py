import docker
import time
c = docker.Client(base_url = 'unix://var/run/docker.sock')
c.images(name = 'busybox')
busyBox = []
for i in range(3):
	print i
	busyBox.append(c.create_container(image = 'busybox', command='echo this is container ' + str(i)))
	c.start(busyBox[-1].get('Id'))
	print busyBox[-1].get('Id')
	print c.logs(busyBox[-1].get('Id'))

time.sleep(2)

for b in busyBox:
	print 'stop'
	print b.get('Id')
	c.stop(b.get('Id'))

