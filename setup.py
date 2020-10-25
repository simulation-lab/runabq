from setuptools import find_packages, setup


setup(
    name='runabq',
    version='0.9.1',

    author='kino',
    author_email='simulation.space.labs@gmail.com',
    url='https://github.com/simulation-lab/runabq',

    description='abaqus input-file continuous execution script.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    python_requires='~=3.8',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'click~=7.1',
    ],

    entry_points={
        'console_scripts': [
            'runabq=runabq.core:run'
        ]
    },

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],

)
