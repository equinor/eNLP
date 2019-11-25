# Equinor Shared NLP Package
This package contains functions often used in NLP ranging from processing to visualisation. The purpose behind the 
package is to collect in one place common functions where a package can be installed to setup an nlp-focussed
environment and most common nlp tasks can be carried out without having to install extra packages. 


## SETUP 
If you just wish to use the package, download the repo and run 

    $ make install_conda
    
which will create a conda environment with the package installed and all the necessary requirements. Prior to using
the package remember to change into your new environment.

    $ source activate enlp
    
For those who prefer not to use conda, download the repo and run

    $ make install
    
And for Windows users, download the repo and run

    $ pip install -r requirements.txt
    $ pip install .


## EXAMPLE USAGE
The documentation has a number of example usages in its gallery. 

To make the documentation,
 
    $ make doc

And then open the documentation and navigate to the example gallery,

    $ cd /docs/build/html
    $ open index.html
.


## CONTRIBUTING
If you wish to edit or contribute to the package, you can make an environment and install the package, with

    $ make dev-install_conda
    
or, if you prefer not to use conda, 

    $ make dev-install
    
or, for windows users,

    $ pip install -r requirements-dev.txt
    $ pip install -e .
    
Please make the documentation and read the section on contributing. 

    $ make doc

All new features should have tests written for them and should not break any of the old tests. To check tests run

    $ make tests
    
