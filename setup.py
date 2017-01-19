from setuptools import setup

setup(
	name='github-sectory',
	version='1.1.4',
	description='CLI for downloading sub-directory of any Github repository!',
	url='https://github.com/amarlearning/Github-Sectory',
	author='Amar Prakash Pandey (@amarlearning)',
    author_email='amar.om1994@gmail.com',
	license='MIT',
	keywords='github repository download sub-directory',
	install_requires=['clint'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7'
	],
	scripts=['github-sectory']
)