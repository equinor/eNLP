.. _installation:

Installation
============


Step-by-step installation for users
-----------------------------------

Clone the repository

.. code-block:: bash

   >> git clone https://github.com/equinor/enlp.git

or download the zip file of the repository (green button in the top right corner of the main github repo page) and
install eNLP from terminal using the command:

.. code-block:: bash

   >> make install

Step-by-step installation for developers
----------------------------------------
Fork and clone the repository by executing the following in your terminal:

.. code-block:: bash

   >> git clone https://github.com/<your_name_here>/enlp.git

The first time you clone the repository run the following command:

.. code-block:: bash

   >> make dev-install

If you prefer to build a new Conda environment just for eNLP, run the following command:

.. code-block:: bash

   >> make dev-install_conda
   >> source activate enlp

To ensure that everything has been setup correctly, run tests:

.. code-block:: bash

    >> make tests

Make sure no tests fail, this guarantees that the installation has been successful.

If using Conda environment, always remember to activate the conda environment every time you open
a new *bash* shell by typing:

.. code-block:: bash

   >> source activate enlp