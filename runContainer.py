#!/usr/bin/env python
# coding=utf-8
import docker
import os
import time

VERSION = 1.9
TIMEOUT = 10
TESTS_CONFIG_NAME = 'tests.config'

def readConfig():
    with open(TESTS_CONFIG_NAME) as file:
        lines = file.readlines()
        imageName = lines[0].rstrip()
        tests = [line.rstrip() for line in lines[1:]]
        return imageName, tests

#imageName, tests = readConfig()
imageName = 'ubuntu:12.04'
tests = ['test1.py', 'test2.py']
cli = docker.Client(base_url='unix://var/run/docker.sock', version='auto', timeout=TIMEOUT)
cli.images(name = imageName)
containers = []
IDs = []
curPath = os.getcwd()
print curPath
for test in tests:
	containers.append(cli.create_container(image = imageName, command =  'python /mnt/testVol/' + test, volumes='/mnt/testVol', host_config=docker.utils.create_host_config(binds={
        curPath: {
            'bind': '/mnt/testVol',
            #'ro': False
        }
    })))
	ID = containers[-1].get('Id')
	IDs.append(ID)
	print ID
	#os.system('docker cp ' + test + ' /var/lib/docker/aufs/mnt/'+ ID+'/'+test)
	cli.start(ID)
	print cli.logs(ID)
