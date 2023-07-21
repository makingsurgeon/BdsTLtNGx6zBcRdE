from setuptools import setup
  
setup(
    name='deposit_marketing',
    version='0.1',
    description='A package to predict customers who have subscribed to loan',
    author='Zihui Ouyang',
    author_email='makingsurgeon@gmail.com',
    packages=['my_package'],
    install_requires=[
        'scikit-learn',
        'pandas',
    ],
)