from setuptools import setup, find_packages

setup(
    name             = 'n_sphere',
    version          = '1.0.8.1',
    description      = 'Convert to Spherical Coordination or Rectangular Coordination in Python',
    long_description = open('README.md').read(),
    author           = 'Yunseong Jeong',
    author_email     = 'Yunseong14@naver.com',
    url              = 'https://github.com/Yunseong-Jeong/n_sphere',
    download_url     = 'https://github.com/Yunseong-Jeong/n_sphere/archive/master.zip',
    license          = 'MIT',
    install_requires = [],
    packages         = ['n_sphere'],
    keywords         = ['Hyper Sphere','n-sphere','Spherical Coordinate', 'Rectangular Coordination', 'Python', 'Real Number'],
    python_requires  = '>=3',
    package_data     =  {
    },
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)