from distutils.core import setup
setup(
    name = 'LoginRadius',
    version= '3.2.0',
    packages=["LoginRadius","LoginRadius.sdk"],
    description = 'Customer identity and access management for Python.',
    author='LoginRadius',
    author_email='developers@loginradius.com',
    url='http://loginradius.com/',
    classifiers=['Programming Language :: Python', 'Programming Language :: Python :: 2.7',
                 'Operating System :: OS Independent', 'License :: OSI Approved :: MIT License',
                 'Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers',
                 'Topic :: Internet', 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)
