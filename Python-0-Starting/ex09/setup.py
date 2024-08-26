from setuptools import setup, find_packages


setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    author='jhogonca',
    author_email='jhogonca@student.42porto.com',
    url='https://github.com/SopadeGalinha/' +
        '42-Python-for-Data-Science/tree/main/ex09/ft_package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [],
    },
)
