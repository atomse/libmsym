.PHONY: all reqs build install test

pes_parent_dir:=$(shell pwd)/$(lastword $(MAKEFILE_LIST))
pes_parent_dir:=$(shell dirname $(pes_parent_dir))

Project=$(shell basename $(pes_parent_dir))

all:
	make reqs
	make build
	make install
	make test

reqs:
	pipreqs --help >/dev/null 2>&1 || pip3 install pipreqs || pip3 install pipreqs --user
	pipreqs --force $(Project)
	sed -i 's/==/>=/g' requirements.txt
	sort requirements.txt -o requirements.txt
	cat requirements.txt 

build:
	[ -e ../../build/libmsym.so ] && cp -a ../../build/libmsym.so* libmsym/ || echo
	[ -e ../../build/libmsym.dylib ] && cp -a ../../build/libmsym.*dylib libmsym/ || echo
	rm -rf build/ sdist/ dist/ $(Project)-*/ $(Project).egg-info/
	python setup.py bdist_wheel -p `python -c 'import distutils.util; print(distutils.util.get_platform());'`
	twine check dist/*

install:
	cd /tmp; pip uninstall -yy $(Project); cd -; python setup.py install || python setup.py install --user

test:
	bash -c "export PYTHONPATH="$(PYTHONPATH):$(PWD)"; coverage run --source libmsym ./examples/msympy_example.py ./examples/h2.xyz -"
	echo `which $(Project)`
	coverage report -m

upload:
	twine upload dist/*

clean:
	rm -rf venv build *.egg-info dist
