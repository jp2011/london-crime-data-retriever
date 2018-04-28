from setuptools import find_packages, setup

setup(
    name="London Crime Data Retriever",
    author="Jan Povala",
    email="jan.povala@gmail.com",
    version="0.1.0",
    packages=find_packages(exclude=['*tests']),
    install_requires=['argparse', 'sqlite3', 'pandas'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'london-crime-retriever = crimeretriever.command:process'
        ]})
