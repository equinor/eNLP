[![PyPI version](https://badge.fury.io/py/enlp.svg)](https://badge.fury.io/py/enlp)
[![Build Status](https://travis-ci.org/equinor/eNLP.svg?branch=master)](https://travis-ci.org/equinor/eNLP)
[![Azure Status](https://dev.azure.com/eNLP/eNLP/_apis/build/status/equinor.eNLP?branchName=master)](https://dev.azure.com/eNLP/eNLP/_build/latest?definitionId=1&branchName=master)
![OS-support](https://img.shields.io/badge/OS-linux,win,osx-850A8B.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d1adfcf2908348c4ae9f25a5f77374e4)](https://www.codacy.com/manual/cebirnie92/eNLP?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinor/eNLP&amp;utm_campaign=Badge_Grade)

# Equinor Shared NLP Package
This package contains functions often used in NLP ranging from processing to visualisation. The purpose behind the 
package is to collect in one place common functions where a package can be installed to setup an nlp-focussed
environment and most common nlp tasks can be carried out without having to install extra packages. 

# INSTALLATION
Install with pip:

    $ pip install enlp
    
To install the package directly from github: 

    $ pip install git+https://github.com/equinor/eNLP.git

If you wish to download the files directly and install, we recommend one of the 3 options as outlined below. Note that 
the first two options use a Makefile.

#####  Using the Makefile and conda environment:
Download or clone the repo and run 

    $ make install_conda
which will create a conda environment with the package installed and all the necessary requirements. Prior to using
the package remember to change into your new environment.

    $ source activate enlp
    
#####  Using the Makefile and pip requirements:   
Download or clone the repo and run 

    $ make install
    
##### Without using the Makefile:
Download or clone the repo and run

    $ pip install -r requirements.txt
    $ pip install . 

# DEVELOPING AND CONTRIBUTING 
We actively encourage others to contribute to the development of the package. 


### DEV INSTALLATION
To install the extra requirements for development, the following options can be 
followed:

#####  Using the Makefile and conda environment:
Download or clone the repo and run 

    $ make dev-install_conda
    $ source activate enlp
    
#####  Using the Makefile and pip requirements:  
Download or clone the repo and run 

    $ make dev-install
    
##### Without using the Makefile:
Download or clone the repo and run

    $ pip install -r requirements-dev.txt
    $ pip install -e .



## CONTRIBUTING GUIDELINES
Prior to contributing back to the package, please make the documentation and read the section on contributing. In 
particular, prior to contributing please ensure all tests run and all new code is adequately documented and any 
required new tests have been wrote.

## DEV DOCUMENTATION
The documentation includes reference documentation for all functions as well as an example gallery.

To make the documentation,
 
    $ make doc

And then open the documentation,

    $ cd /docs/build/html
    $ open index.html
.

All new features should have clear doc strings and have their paths included in the relevant file under 
`docs/source/api/`. 

Examples of usage are also very welcome to be added to the example gallery.

## TESTING
All new features should have tests written for them and should not break any of the old tests. To check tests run

    $ make tests
    
