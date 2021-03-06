from setuptools import setup, find_packages

setup(
    name='se_ciot_helper',
    version='1.0.0',
    license='MIT',
    dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.9.3'],
    install_requires  = ['Adafruit-GPIO>=0.9.3', 'pyserial', 'adafruit-ads1x15'],
    packages=find_packages()
)
