from setuptools import setup

setup(
    name='tsp_solver',
    version='1.0',
    packages=['tsp'],
    install_requires=[''],
    entry_points={'console_scripts': ['tsp_solver = tsp:main']},
    author='Your Name',
    author_email='your@email.com',
    description='TSP Solver',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/tsp_solver',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)