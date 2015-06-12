FROM ubuntu:12.04
WORKDIR /TEST 
ADD tests.config /TEST/
ADD execute.py /TEST/
ADD runContainer.py /TEST/
ADD test1.py /TEST/
ADD test2.py /TEST/
CMD python runContainer.py