# Surrogates

`surrogates` is a small, tested Python 3 package
to encode and decode pairs of
[surrogate characters](https://en.wikipedia.org/wiki/Universal_Character_Set_characters#Surrogates)
in Python strings.
It is licensed under [the MIT license](https://opensource.org/licenses/MIT).


# Installation
```console
# pip install --user surrogates
```


# Usage

```console
# python3 -m IPython
[..]
In [1]: import surrogates

In [2]: surrogates.encode('😘')
Out[2]: '\ud83d\ude18'

In [3]: surrogates.decode('\uD83D\uDE18')
Out[3]: '😘'

In [4]: hex(ord('😘'))
Out[4]: '0x1f618'
```


# Develop & run tests

```
cd "$(mktemp -d)"
git clone https://github.com/hartwork/surrogates
cd surrogates/
python3 -m venv py3
source py3/bin/activate
./setup.py test
```
