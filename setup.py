import pathlib
from setuptools import find_packages
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The README text
README = (HERE / "README.md").read_text()
description = 'Aspect Based Sentiment Analysis: ' \
              'Transformer & Interpretability (TensorFlow)'

setup(
    name='aspect-based-sentiment-analysis',
    version="1.1.2",  # Semantic: MAJOR, MINOR, and PATCH
    url='https://github.com/ScalaConsultants/Aspect-Based-Sentiment-Analysis',
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    author=' Rafal Rolczynski',
    author_email='rafal.rolczynski@gmail.com',
    include_package_data=False,
    packages=find_packages(),
    install_requires=[
        'tensorflow-cpu~=2.1',
        'transformers~=2.5',
        'pytest',
        'scikit-learn',
        'ipython',
        'google-cloud-storage',
        'testfixtures',
        'optuna',
        'spacy'
    ],
    python_requires='~=3.7',
)
