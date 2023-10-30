"""The setup script for installing the package."""
from setuptools import setup, find_packages


# read the contents of the README
with open('README.md') as README_md:
    README = README_md.read()


setup(
    name='mario_bros_env',
    version='0.0.1',
    description='Super Mario Bros. for Farama Gymnasium',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords=' '.join([
        'OpenAI-Gym',
        'Farama Gymnasium',
        'NES',
        'Super-Mario-Bros',
        'Reinforcement-Learning-Environment',
    ]),
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: Free For Educational Use',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    url='https://github.com/jakobkg/mario-bros-env',
    author='Christian Kauten',
    author_email='kautencreations@gmail.com',
    license='Proprietary',
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    install_requires=['nes-py>=8.1.4'],
    entry_points={
        'console_scripts': [
            'mario_bros_env = mario_bros_env._app.cli:main',
        ],
    },
)
