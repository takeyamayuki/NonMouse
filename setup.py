from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='nonmouse',
    version='2.7.0',
    packages=find_packages(),
    description='a webcam-based virtual gesture mouse that is easy to use with hands on the desk',
    author='Yuki TAKEYAMA',
    author_email='namiki.takeyama@gmail.com',
    url='https://github.com/takeyamayuki/NonMouse',
    license='Apache-2.0',
    install_requires=_requires_from_file('requirements.txt'),
    entry_points={'console_scripts': ['nonmouse=nonmouse.__main__:main',]},
    python_requires='>=3.6',
)
