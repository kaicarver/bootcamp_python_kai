# Notes

These are some notes from doing the 42AI Python bootcamp.

Problems with installed version of `python`, `pip`.

```bash
$ python -V
Python 3.7.3
```

OK!

```bash
(base) kai@bluesteel:~/bootcamp_python$ pip
Traceback (most recent call last):
  File "/home/kai/.local/bin/pip", line 7, in <module>
    from pip._internal import main
  File "/home/kai/.local/lib/python3.6/site-packages/pip/_internal__init__.py", line 40, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "/home/kai/.local/lib/python3.6/site-packages/pip/_internal/cliautocompletion.py", line 8, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "/home/kai/.local/lib/python3.6/site-packages/pip/_internal/climain_parser.py", line 7, in <module>
    from pip._internal.cli import cmdoptions
  File "/home/kai/.local/lib/python3.6/site-packages/pip/_internal/clicmdoptions.py", line 15, in <module>
    from distutils.util import strtobool
ModuleNotFoundError: No module named 'distutils.util'
```

Uh-oh. I know I had installed version of Python in the past, maybe with anaconda, but do I remember? Noo...

Stackoverflow tells me this solves the pip not even _running_ problem.

```bash
$ sudo apt-get install python3-distutils
```

OK, pip now runs! Hooray!

But...

```bash
$ pip -V                                                                                                                               pip 19.2.3 from /home/kai/.local/lib/python3.6/site-packages/pip (python 3.6) 
```
