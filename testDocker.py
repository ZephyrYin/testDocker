#!/usr/bin/env python
# coding=utf-8
import docker
import os

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
cli = docker.Client(base_url='unix://var/run/docker.sock', version=str(VERSION), timeout=TIMEOUT)
cli.images(name = imageName)
containers = []
curPath = os.getcwd()
for test in tests:
	print test
        containers.append(cli.create_container(image = imageName, command =  'ls'))
	ID = containers[-1].get('Id')
	print ID
        os.system('sudo cp ' + test + ' /var/lib/docker/aufs/mnt/'+ ID+'/'+test)
        cli.start(ID)
        print cli.logs(ID)
