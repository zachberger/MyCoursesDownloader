from setuptools import setup, find_packages

setup(name='MyCoursesDownloader',
	version='0.1.3',
	description='Written instead of studying.',
	author='Colum McGaley',
	author_email='c.mcgaley@gmail.com',
	url='https://github.com/volfco/MyCoursesDownloader',
	packages=find_packages(),
	install_requires=['requests', 'BeautifulSoup4']
)