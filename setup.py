from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='mnlp',
      version='0.1.2',
      description='Mongolian Natural Language Processing Module.',
      long_description=readme(),
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6',
            'Topic :: Text Processing :: Linguistic',
      ],
      keywords='nlp mongolian',
      url='http://github.com/byam/mnlp',
      author='Byambasuren Ganbaatar',
      author_email='byambaa.mng@gmail.com',
      license='MIT',
      packages=['mnlp'],
      zip_safe=False,
      scripts=['bin/mnlp-stopwords'],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
