# Notes

These are some notes from doing the 42AI Python bootcamp.

Or, in my case, a bit of a Python/AI "rebootcamp", since I've mostly been doing JavaScript these last few months.

## Day 0

### Versions...

Difficulties begin nearly at the very first instruction:  problems with installed version of `python`, `pip`.

My environment is WSL on Windows.

Problems start at the prompt. How many times have I installed Python in the last few years? Don't know. But my bash prompt looks like this:

```bash
(base) kai@bluesteel:~/bootcamp_python$ 
```

I think that `(base)` thing means something. Was my last install with something called `conda`? Or `anaconda`? Or `miniconda`? I have some vague memories of `virtualenv`. How should I remember? How should I know if it's up-to-date? Gosh I hate this system stuff...

> The version of Python to use is 3.7

Let's check...

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

Note: I also just remembered that I can maybe just use something like [Google Colab](https://colab.research.google.com/). May come in handy when I get sick of tracking problems with the 42 different versions of Python installed on my poor old overloaded Windows laptop.

### PDF table of contents looks bad

Each section goes down a deeper level.
