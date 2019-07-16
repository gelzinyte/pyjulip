# PyJulip

======================================================================================

Runs from inside the libatoms Docker after following the next few steps:

Julia: 
- `] add https://github.com/cortner/NBodyIPs.jl.git` (for NBodyIPs support - required for the test.py), 
- `] update` (JuLIP seems to be ancient (?) and requires updating)

Python:
- `ipython setup.py install`
- `ipython ./example/test.py`


======================================================================================



Python3: We need pip3 in Docker first

Let's get pip3
- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
- `python3 get-pip.py`

Install pyjulia3
- `python3 -m pip install --user julia`

Initialise with Julia
- `python3 -c "import julia; julia.install()"`

We get the following error.... so no Python3 support yet
`Your Python interpreter "/usr/bin/python3"
is statically linked to libpython.  Currently, PyJulia does not fully
support such Python interpreter.`
