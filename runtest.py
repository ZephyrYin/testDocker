import os

DOCKER_FILE_NAME = 'Dockerfile'
TESTS_CONFIG_NAME = 'tests.config'
TEST_DIRECTORY = 'TEST'
EXECUTE_FILE_NAME = 'execute.py'
SCRIPT_NAME = 'runContainer.py'
IMAGE_NAME = 'ubuntu:12.04'

def genConfig(tests):
    with open(TESTS_CONFIG_NAME,'w') as file:
    	file.write(IMAGE_NAME + '\n')
        for test in tests:
            file.write(test + '\n')



def genDockerFile(tests):
    with open(DOCKER_FILE_NAME,'w') as dockerFile:
        dockerFile.write('FROM ' + IMAGE_NAME + '\n')
        dockerFile.write('WORKDIR /' + TEST_DIRECTORY +' \n')
        dockerFile.write('ADD ' + TESTS_CONFIG_NAME + ' /' + TEST_DIRECTORY + '/\n')
        dockerFile.write('ADD ' + EXECUTE_FILE_NAME + ' /' + TEST_DIRECTORY + '/\n')
        dockerFile.write('ADD ' + SCRIPT_NAME + ' /' + TEST_DIRECTORY + '/\n')
        for test in tests:
            dockerFile.write('ADD ' + test + ' /' + TEST_DIRECTORY + '/\n')
        dockerFile.write('CMD python ' + SCRIPT_NAME)

testNames = ['test1.py', 'test2.py']
os.chdir(os.getcwd())
genConfig(testNames)
genDockerFile(testNames)
os.system('sudo docker build -t testdf .')


