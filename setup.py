from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'collage planner'
LONG_DESCRIPTION = 'gmu collage planner for my courses'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="collage", 
        version=VERSION,
        author="Eslam Elprince",
        author_email="eslamelprince@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'collage'],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)