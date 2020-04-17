PIP := $(shell command -v pip 2> /dev/null || command which pip 2> /dev/null)
PYTHON := $(shell command -v python3 2> /dev/null || command which python 2> /dev/null)

.PHONY: install dev-install install_conda dev-install_conda tests doc docupdate

pipcheck:
ifndef PIP
	$(error "Ensure pip or pip3 are in your PATH")
endif
	@echo Using pip: $(PIP)

pythoncheck:
ifndef PYTHON
	$(error "Ensure python or python3 are in your PATH")
endif
	@echo Using python: $(PYTHON)

install:
	make pipcheck
	$(PIP) install -r requirements.txt && $(PIP) install .

dev-install:
	make pipcheck
	$(PIP) install -r requirements-dev.txt && $(PIP) install -e .

install_conda:
	make pipcheck
	conda env create -f environment.yml && conda activate enlp && pip install .

dev-install_conda:
	make pipcheck
	conda env create -f environment-dev.yml && conda activate enlp && pip install -e .

tests:
	make pythoncheck
	$(PYTHON) setup.py test

doc:
	cd docs  && rm -rf source/api/generated && rm -rf source/examples &&\
	rm -rf build && make html && cd ..

doc_ext:
	cd docs  && rm -rf source/api/generated && rm -rf source/examples &&\
	rm -rf build && make html && make latexpdf && cd ..

docupdate:
	cd docs && make html && cd ..

clean-pyc:
	find . -name \*.pyc -delete
