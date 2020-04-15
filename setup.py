import os
from distutils.core import setup
from setuptools import find_packages

def src(pth):
    return os.path.join(os.path.dirname(__file__), pth)

# Project description
descr = """
        Python library of NLP functions originally collated by Equinor Knowledge and AI Data Science team.
        """

# Setup
setup(
    name='enlp',
    description=descr,
    long_description=open(src('README.md')).read(),
    long_description_content_type='text/markdown',
    keywords=['nlp'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    author='Equinor ASA',
    author_email='clbi@equinor.com',
    install_requires=['numpy', 'matplotlib', 'pandas', 'spacy==2.0.18', 'nltk', 'gensim', 'scikit-learn', 'rake-nltk', 'wordcloud'],
    packages=find_packages(exclude=['tests']),
    use_scm_version=dict(root = '.',
                         relative_to = __file__,
                         write_to = src('enlp/version.py')),
    setup_requires=['pytest-runner', 'setuptools_scm'],
    test_suite='tests',
    tests_require=['pytest'],
    zip_safe=True)

