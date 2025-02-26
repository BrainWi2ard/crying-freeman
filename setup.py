from setuptools import setup, find_packages

setup(
    name="data_extraction_app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'selenium',
        'webdriver-manager',
        'scrapy',
        'fuzzywuzzy',
        'flask',
        'transformers',
        'reportlab',
        'regex',
        'ratelimit',
        'python-docx'
    ],
)
