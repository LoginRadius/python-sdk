import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name = 'LoginRadius-v2',
    version='11.5.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
	packages=setuptools.find_packages(),
    description = 'Customer identity and access management for Python.',
    author='LoginRadius',
    author_email='developers@loginradius.com',
    url='https://loginradius.com/',
    install_requires=[
            'urllib3',
            'requests',
            'cryptography',
            'pbkdf2',
            'flask',
            ],
    classifiers=['Programming Language :: Python', 'Programming Language :: Python :: 2.7',
                 'Operating System :: OS Independent', 'License :: OSI Approved :: MIT License',
                 'Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers',
                 'Topic :: Internet', 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)
