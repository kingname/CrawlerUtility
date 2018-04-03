from setuptools import setup, find_packages
setup(
    name='CrawlerUtility',
    packages=find_packages(exclude=[]),
    version='0.0.3',
    description='Utilities to simplify the development of your webcrawler',
    author='Kingname',
    author_email='contact@kingname.info',
    url='https://github.com/kingname/CrawlerUtility',
    keywords=['scrapy', 'requests', 'crawler'],
    python_requires='>=3.4',
    license='PyPA',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: PyPA',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
    ]
)
