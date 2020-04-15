# Equinor Shared NLP Package
This package is aimed at facilitating Natural Language Processing pipelines and includes functionalities often used in  
NLP ranging from processing to visualisation. By installing `eNLP` you will have access to a nlp-focussed environment  
that contains some of the most popular NLP libraries and facilitates their combined usage in a unique and easy way.


## SETUP 
If you just wish to use the package, download the repo and run 

    $ make install_conda

which will create a conda environment with the package installed and all the necessary requirements. Prior to using
the package remember to change into your new environment.

    $ source activate enlp

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

Please make the documentation and read the section on contributing. 

    $ make doc

All new features should have tests written for them and should not break any of the old tests. To check tests run

    $ make tests
    
