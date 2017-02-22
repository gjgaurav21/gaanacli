from distutils.core import setup
setup(
    name = 'gaanacli',
    packages = ['gaanacli'],
    version = '0.1',
    scripts=['bin/gaanacli'],
    description = 'Open chrome tab and play youtube song directly from CLI',
    author = 'Karan Dev',
    author_email = 'karandev43@gmail.com',
    url = 'https://github.com/karan10/gaanacli',
    download_url = 'https://github.com/karan10/gaanacli/tarball/0.1',
    install_requires = ['requests'],
    keywords = ['youtube', 'songs', 'cli', 'python'],
    requires=['requests'],
    classifiers = [],
)
