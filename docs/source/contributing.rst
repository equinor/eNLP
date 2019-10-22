.. _contributing:

Contributing
============

Introduction
------------

This is guide intended for those wishing to contribute to this project.

For this project, some of the assigned roles are as follows:

    - **Repository Owner**: Claire Birnie
    - **Review Team**: Eivind Sjaastad, Bjarte Johansen, Jennifer Sampson

If you wish to become a member of the Review Team please contact the repository owner.


Roles and Responsibilities
--------------------------
The success of the package and its continual evolution is dependent on community involvement. The table below details
the roles and responsibilities of persons vital to the growth of the package.


+-------------+------------------------------+----------------------------------------------------------------------+
| **Role**    | **Description**              | **Responsibilities**                                                 |
+-------------+------------------------------+----------------------------------------------------------------------+
|             |                              | - Should a user identify any bugs in the code they are               |
|             | Someone who uses the package |                                                                      |
|             |                              |   responsible for bringing this to the attention of the review       |
| User        | however does not edit it     |                                                                      |
|             |                              |   team through issue tracking in GitHub                              |
|             |                              |                                                                      |
|             |                              | - Suggest new features                                               |
+-------------+------------------------------+----------------------------------------------------------------------+
|             |                              | -  Ensuring all code follows the coding and documentation standards  |
|             | Someone who both uses and    |                                                                      |
|             |                              | - Ensuring that all previous tests are passed and that comprehensive |
| Contributor | further develops the package |                                                                      |
|             |                              |   new tests have been written and passed for all new classes/modules |
|             |                              |                                                                      |
|             |                              | - Updating the environment requirements (if needed)                  |
|             |                              |                                                                      |
|             |                              | - Should a contributor identify any bugs or desire new features in   |
|             |                              |                                                                      |
|             |                              |   the code they are responsible for bringing this to the attention of|
|             |                              |                                                                      |
|             |                              |   the review team through issue tracking in GitHub                   |
+-------------+------------------------------+----------------------------------------------------------------------+
|             |                              | - Perform full QC for all merge requests in the suggested environment|
|             |  Someone who frequently uses |                                                                      |
| Review Team |                              |  setup (either from documentation or environment/requirements file)  |
|             | and further develops the     |                                                                      |
|             |                              | - Merge feature branches that pass QC step                           |
|             | package                      |                                                                      |
|             |                              | - Communicate to contributor if/why a branch has failed the QC step  |
|             |                              |                                                                      |
|             |                              | - Delete feature branches after merging                              |
|             |                              |                                                                      |
|             |                              | - Fix bugs identified by contributors                                |
|             |                              |                                                                      |
|             |                              | - Review bug reports and features suggestions                        |
|             |                              |                                                                      |
|             |                              | - Prioritisation of bug reports and features                         |
|             |                              |                                                                      |
+-------------+------------------------------+----------------------------------------------------------------------+
|             |                              | - Responsible ultimately for releases                                |
|             | The initial, main developer  |                                                                      |
| Repository  |                              | - Make the repository and open-source it                             |
|             | of the package               |                                                                      |
| Owner       |                              | - Choose review team                                                 |
|             |                              |                                                                      |
|             |                              | - Head of review team, ensuring that reviews are carried out in a    |
|             |                              |                                                                      |
|             |                              |  timely manner                                                       |
|             |                              |                                                                      |
|             |                              | - Perform a monthly repository cleanup                               |
+-------------+------------------------------+----------------------------------------------------------------------+





Note that in the case of a member of the review team actively adding features then they take on the role of a
contributor and another member of the review team must perform the review prior to allowing a merge

Code guidelines
===============
Design Principles
-----------------
**SOLID**
All work should follow the '''SOLID''' principles whenever possible to reduce chance of bug, reduce rework, and lower
maintenace cost. The solid principle is as follows:
    - **S** ingle Responsiblility - Modules or classes should only change for one reason
    - **O** pen/closed - Entities should be open for extension but closed for modification
    - **L** iskov substitution - Derived classes must be substitutable for their base classes
    - **I** nterface segreation - Interfaces should be cohesive and not introduce unnecessary dependencies
    - **D** ependency inversion - High- and low-level interaction should be mediated by abstractions

An in-depth explanation of the SOLID  principles can be found on
https://hackernoon.com/solid-principles-made-easy-67b1246bcdf


**Function vs Classes**
Use functions whenever possible and use classes only when necessary

**Dependencies**
All necessary packages that needs to be install should be specified in the setup.py file. If strict version control of
dependent packages is needed, use a requirement.txt

**Test-Driven Design**
It is expected that all contributors follow the test-driven design principle whenever possible to reduce waste and
ensure quality. Write your test first and only write enough code to pass the test.



Code and Documentation
----------------------
All code must follow PEP8 guidelines - https://www.python.org/dev/peps/pep-0008/  with a minimum Pylint score of at
least 7 (https://www.pylint.org ). PEP8 is widely accepted Python style guide that improves readability of the code by
promoting consistency, and pylint is a tool to test compliance to PEP8.

We also recommend following the Google Python Style Guide -
https://github.com/google/styleguide/blob/gh-pages/pyguide.md as it covers more than PEP8 particularly in regards to
documentation and it is comprehensive, well written and widely used.

Some of the key points in the *Google Python Style Guide* include:

**Docstrings**:

A docstring should be organized as a summary line (one physical line) terminated by a period, question mark, or
exclamation point, followed by a blank line, followed by the rest of the docstring starting at the same cursor position
as the first quote of the first line.


**Functions and Methods**:

A function must have a docstring:
A docstring should give enough information to write a call to the function without reading the function's code.

Certain aspects of a function should be documented in special sections, listed below.

*Args*: List each parameter by name. A description should follow the name and be separated by a colon and a space.
The description should include required type(s) if the code does not contain a corresponding type annotation.

*Returns*: Describe the type and semantics of the return value.

*Raises*:  List all exceptions that are relevant to the interface.


**Classes**

Classes should have a docstring below the class definition describing the class. If your class has public attributes,
they should be documented here.


Additionally, each package must also include a readme file that answers the following questions:
    - What does this project do? 
    - Why is this project useful? 
    - How do I get started? 
    - Where can I get more help?


Tests
-----
Tests should be created for all new modules/classes and should cover a range of possible scenarios (e.g., test all
possible input combinations). The coverage package can be used to help identify what aspects of the code are not
covered by tests. 

Pytest - https://docs.pytest.org/en/latest/ is the recommended testing tool.

Development, Committing and releasing Process
---------------------------------------------

We recommend the fork workflow of Atlassian:
https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow  for development. Where each developer (or
group of developers) make a fork of the official master repository and contribute within.

    - A developer 'forks' an 'official' server-side repository. This creates his/her own server-side copy.
    - The new server-side copy is cloned to their local system.
    - A Git remote path for the 'official' repository is added to the local clone.
    - A new local feature branch is created.
    - The developer makes changes on the new branch.
    - New commits are created for the changes.
    - The branch gets pushed to the developer's own server-side copy.
    - The developer opens a pull request from the new branch to the 'official' repository.
    - The pull request gets approved for merge and is merged into the original server-side repository




Within each fork, we recommend using the GitFlow workflow of Atlassian:
https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow for development, where a master (of this
fork) branch and a development branch are kept in parallel. Development work is done in the feature branch and pushed
into the development branch when ready. The workflow within each fork is decided by each developer (or group of
developers).
