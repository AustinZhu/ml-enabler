from setuptools import setup

setup(
    name="ml-enabler-cli",
    version='0.1.0',
    py_modules=['ml_enabler'],
    install_requires=[
        'Click',
        'numpy',
        'mercantile==1.0.4',
        'aiohttp==3.5.4',
        'backoff==1.8.0',
        'pytest==4.6.3',
        'Shapely==1.6.4.post2',
        'area==1.1.1'
    ],
    entry_points='''
        [console_scripts]
        ml-enabler=ml_enabler.cli:main_group
    ''',
)