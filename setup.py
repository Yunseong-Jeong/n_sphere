from setuptools import setup, find_packages

setup(
    name             = 'n-sphere',
    version          = '1.0',
    description      = 'Convert to Spherical Coordination or Rectangular Coordination in Python',
    author           = 'Yunseong Jeong',
    author_email     = 'Yunseong14@naver.com',
    url              = 'https://github.com/Yunseong-Jeong/N-sphere-coordinate',
    download_url     = 'https://github.com/Yunseong-Jeong/N-sphere-coordinate/archive/master.zip',
    install_requires = ['numpy'],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['Spherical Coordinate', 'Rectangular Coordination', 'Python', 'Real Number'],
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