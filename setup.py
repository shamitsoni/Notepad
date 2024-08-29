from setuptools import setup, find_packages

setup(
    name='NotepadApp',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'notepad = main:main',
        ],
    },
)
