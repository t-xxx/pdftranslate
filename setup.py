import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'),mode='r', encoding='utf-8') as fr:
    long_description = fr.read()

setuptools.setup(
    name="PDFTranslate",
    version="0.1.0",
    description="PDFTranslate Location List",
    long_description=long_description,
    packages=setuptools.find_packages(),
    url="https://github.com/3x-boy/PDFTranslate",
    author="3x_boy",
    keywords="PDFTranslate",
    license="MIT",
    install_requires = ['googletrans', 'pyPDF2'],
    classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.7.3',
    ],
)