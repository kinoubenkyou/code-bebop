CODE BEBOP
================

Personal tech blog

Published at: [kinoubenkyou.github.io/code-bebop/](kinoubenkyou.github.io/code-bebop/)

Dependency
------------

* pelican
* ghp-import

```shell
pip3 install pelican ghp-import
```

Usage
--------

Local:

```shell
pelican -r
# on another tab
python3 -m pelican.server
```

Publish on Github:

```shell
pelican -s publishconf.py
ghp-import -p output
```
