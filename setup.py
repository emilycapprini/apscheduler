# coding: utf-8
import os.path

from setuptools import setup, find_packages


here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.rst')
readme = open(readme_path).read()

setup(
    name='APScheduler',
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag'
    },
    description='In-process task scheduler with Cron-like capabilities',
    long_description=readme,
    author=u'Alex Grönholm',
    author_email='apscheduler@nextday.fi',
    url='https://github.com/agronholm/apscheduler',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='scheduling cron',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    setup_requires=[
        'setuptools_scm'
    ],
    install_requires=[
        'setuptools >= 0.7',
        'six >= 1.4.0',
        'pytz',
        'tzlocal >= 1.2',
    ],
    extras_require={
        ':python_version == "2.7"': ['futures', 'funcsigs'],
        'asyncio:python_version == "2.7"': ['trollius'],
        'asyncio:python_version == "3.3"': ['asyncio'],
        'gevent': ['gevent'],
        'twisted': ['twisted'],
        'sqlalchemy': ['sqlalchemy >= 0.8'],
        'mongodb': ['pymongo >= 2.8'],
        'rethinkdb': ['rethinkdb'],
        'tornado': ['tornado >= 4.3'],
    },
    zip_safe=False,
    entry_points={
        'apscheduler.triggers': [
            'date = apscheduler.triggers.date:DateTrigger',
            'interval = apscheduler.triggers.interval:IntervalTrigger',
            'cron = apscheduler.triggers.cron:CronTrigger'
        ],
        'apscheduler.executors': [
            'debug = apscheduler.executors.debug:DebugExecutor',
            'threadpool = apscheduler.executors.pool:ThreadPoolExecutor',
            'processpool = apscheduler.executors.pool:ProcessPoolExecutor',
            'asyncio = apscheduler.executors.asyncio:AsyncIOExecutor [asyncio]',
            'gevent = apscheduler.executors.gevent:GeventExecutor [gevent]',
            'tornado = apscheduler.executors.tornado:TornadoExecutor [tornado]',
            'twisted = apscheduler.executors.twisted:TwistedExecutor [twisted]'
        ],
        'apscheduler.jobstores': [
            'sqlalchemy = apscheduler.jobstores.sqlalchemy:SQLAlchemyJobStore [sqlalchemy]',
        ]
    }
)
