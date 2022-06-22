from setuptools import setup, find_packages

from todo_extract import version

setup(
    name="todo_extract",
    description='Extract TODO items from the text file.',
    author='Krystian Safjan',
    author_email='ksafjan@gmail.com',
    url='https://github.com/izikeros/todo-extractor',
    license='MIT',
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": ["todo-extract=todo_extract.main:main"],
    },
    version=version.__version__,
)
