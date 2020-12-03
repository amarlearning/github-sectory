from setuptools import setup

setup(
    name='github-sectory',
    version='1.3.5',
    description='CLI for downloading sub-directory of any Github repository!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amarlearning/Github-Sectory',
    author='Amar Prakash Pandey (@amarlearning)',
    author_email='amar.om1994@gmail.com',
    license='MIT',
    keywords='github repository download sub-directory',
    install_requires=['clint', 'requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    scripts=['github-sectory']
)
