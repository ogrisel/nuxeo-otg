.PHONY: test clean setup-env

test: env
	PYTHONPATH=`pwd` nosetests -w tests

setup-env:
	virtualenv env
	./env/bin/pip install --upgrade -s -E env -r dependencies.txt

env: 
	virtualenv env
	./env/bin/pip install --upgrade -s -E env -r dependencies.txt

clean:
	rm -rf env
	find . -name "*~" | xargs rm -f
	find . -name "*.pyc" | xargs rm -f
	find . -name "*.class" | xargs rm -f

