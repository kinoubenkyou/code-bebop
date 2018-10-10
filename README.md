CODE BEBOP
================

Personal tech blog

Published at: [kinoubenkyou.github.io/code-bebop/](https://kinoubenkyou.github.io/code-bebop/)

Dependencies
------------

* python3
* pelican
* ghp-import

Usage
--------

Local:

```shell
pelican -r
# on another tab
cd output
python3 -m pelican.server
```

Publish on Github:

```shell
pelican -s publishconf.py
ghp-import -p output
```
