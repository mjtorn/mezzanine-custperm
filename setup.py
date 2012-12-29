# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from setuptools import setup, find_packages

NAME = 'mezzanine-custperm'
VERSION = '0.0.1'

DESCR = """\
Add more customizable filters before OwnableAdmin
"""

AUTHOR = u'Markus Törnqvist'
AUTHOR_EMAIL = 'mjt@fadconsulting.com'

URL = 'https://github.com/mjtorn/mezzanine-custperm'

setup(
    name=NAME,
    version=VERSION,
    description=DESCR,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools'],
)

# EOF

