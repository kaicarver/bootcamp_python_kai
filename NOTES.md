# Notes

These are some notes from doing the 42AI Python bootcamp.

Or, in my case, a bit of a Python/AI "rebootcamp", since I've mostly been doing JavaScript these last few months.

- [Notes](#notes)
  - [Preliminary](#preliminary)
  - [Day 0](#day-0)
    - [Versions...](#versions)
    - [Colab](#colab)
    - [Ex 0](#ex-0)
    - [Other exercises](#other-exercises)

## Preliminary

I'd cloned the 42AI Python bootcamp (_née_ Piscine Python)

```bash
$ git remote -v
origin  https://github.com/kaicarver/bootcamp_python (fetch)
origin  https://github.com/kaicarver/bootcamp_python (push)
upstream        https://github.com/42-AI/bootcamp_python (fetch)
upstream        https://github.com/42-AI/bootcamp_python (push)
$
```

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
$ pip
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
$ pip -V 
pip 19.2.3 from /home/kai/.local/lib/python3.6/site-packages/pip (python 3.6) 
```

So pip references version 3.6... Aaargh.

```bash
$ which pip
/home/kai/.local/bin/pip
$ python -V
Python 3.7.3
$ which python
/home/kai/anaconda3/bin/python
$ pip -V
pip 19.2.3 from /home/kai/.local/lib/python3.6/site-packages/pip (python 3.6)
$ /home/kai/anaconda3/bin/pip -V
pip 19.3.1 from /home/kai/anaconda3/lib/python3.7/site-packages/pip (python 3.7)
$ /home/kai/anaconda3/bin/pip install pycodestyle
Requirement already satisfied: pycodestyle in /home/kai/anaconda3/lib/python3.7/site-packages (2.5.0)
```

OK so I just need to get rid of that other, `/home/kai/.local/bin/` version of Python...

By the way I should maybe update `pip`

```bash
$ pip install pycodestyle
Collecting pycodestyle
  Downloading https://files.pythonhosted.org/packages/0e/0c/04a353e104d2f324f8ee5f4b32012618c1c86dd79e52a433b64fceed511b/pycodestyle-2.5.0-py2.py3-none-any.whl (51kB)
     |████████████████████████████████| 51kB 2.0MB/s
Installing collected packages: pycodestyle
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/pycodestyle.py'
Consider using the `--user` option or check the permissions.

WARNING: You are using pip version 19.2.3, however version 20.0.2 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
$
```

Further detective work shows it is indeed conda initialize

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/kai/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/kai/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/kai/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/kai/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

and the workaround for now seems to be to just tack the conda stuff back at the front of the `PATH`:

```bash
export PATH="/home/kai/anaconda3/bin:$PATH"
```

How about updating everything to the latest version, since it was already installed?

```bash
$ conda verify
$ conda update

CondaValueError: no package names supplied
# If you want to update to a newer version of Anaconda, type:
#
# $ conda update --prefix /home/kai/anaconda3 anaconda


$ conda update --prefix /home/kai/anaconda3 anaconda

[lots of stuff, I have the full conda, not miniconda...]

$ python -V
Python 3.7.3
$ pip -V
pip 20.0.2 from /home/kai/anaconda3/lib/python3.7/site-packages/pip (python 3.7)
$
```

OK so `pip` got updated, along with a zillion `pip` packages. But the Python version seems kinda old.

```bash
$ conda update python
[...]
$ python -V
Python 3.7.7
```

Python version 3.7.7 seems not bad.

I see `conda` also offers some 3.8 versions, but the bootcamp requests 3.7, so let's quit while we're ahead.

```bash
$ conda search python
[...]
python                         3.7.6      h0371630_2  pkgs/main
python                         3.7.7 h191fe78_0_cpython  pkgs/main
python                         3.7.7 hcf32534_0_cpython  pkgs/main
python                         3.8.0      h0371630_0  pkgs/main
python                         3.8.0      h0371630_1  pkgs/main
python                         3.8.0      h0371630_2  pkgs/main
python                         3.8.1      h0371630_1  pkgs/main
python                         3.8.2      h191fe78_0  pkgs/main
python                         3.8.2      hcf32534_0  pkgs/main
```

### Colab

I also just remembered that I can maybe just use something like [Google Colab](https://colab.research.google.com/). May come in handy when I get sick of tracking problems with the 42 different versions of Python installed on my poor old overloaded Windows laptop.

### Ex 0

Find the commands to:

1. Output a list of installed packages.

```bash
$ pip list | wc -l
233
```

2. Output a list of installed packages and their versions.

```bash
$ conda list | wc-l
317
```

3. Show the package metadata of numpy.

```bash
$ cat ~/anaconda3/conda-meta/numpy-1.*
{
  "build": "py37h4f9e942_0",
...
  "url": "https://repo.anaconda.com/pkgs/main/linux-64/numpy-1.18.1-py37h4f9e942_0.conda",
  "version": "1.18.1"
}
```

4. Search for PyPI packages whose name or summary contains “tesseract”.

```bash
$ pip search tesseract
tesseract-ocr (0.0.1)             - A Python wrapper for Tesseract
tesseract-python (3.5.1)          - Self-contained Python module to Tesseract.
tesseract (0.1.3)                 - Tesselation based Recovery of Amorphous halo Concentrations
...
```

5. Freeze the packages and their current versions in a requirements.txt file you have to turn-in.

```bash
$ pip freeze > requirements.txt
```

### Other exercises

Just see the files in the respective directories.

