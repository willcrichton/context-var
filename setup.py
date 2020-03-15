from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(name='context-var',
          version='0.1.0',
          description='React-style context variables',
          url='http://github.com/willcrichton/context-var',
          author='Will Crichton',
          author_email='wcrichto@cs.stanford.edu',
          license='Apache 2.0',
          packages=find_packages(),
          setup_requires=['pytest-runner'],
          tests_require=['pytest'],
          zip_safe=False)
