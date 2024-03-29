from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='analytica',
  version='0.0.3',
  description='Auto Data Analysis',
  long_description=open('README.txt').read(),
  url='',  
  author='Pawan Trivedi',
  license='MIT', 
  classifiers=classifiers,
  keywords='Data Analysis', 
  packages=find_packages(),
  install_requires=['numpy','pandas','seaborn','matplotlib','scipy'] 
)
