# PyJulip

PyJuLIP interface

Runs from inside the libatoms Docker after following the next few steps:

Julia: 
- `] add https://github.com/cortner/NBodyIPs.jl.git` (for NBodyIPs support - required for the ./example/test.py), 
- `] update` (JuLIP seems to be ancient (?) and requires updating)

Python:
- `ipython setup.py install`
- `ipython ./example/test.py`

I tried Python3 but running `python3 -m pip install --user julia` gives me the following error inside the Docker..

`Your Python interpreter "/usr/bin/python3"
is statically linked to libpython.  Currently, PyJulia does not fully
support such Python interpreter.`
