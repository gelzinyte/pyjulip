# PyJulip

======================================================================================

Runs from inside the libatoms Docker after following the next few steps:

Julia: 
- `] add https://github.com/cortner/NBodyIPs.jl.git` (for NBodyIPs support - required for the test.py), 
- `] update` (JuLIP seems to be ancient (?) and requires updating)

Python:
- `python setup.py install`
- `python ./example/test.py`


======================================================================================


Install pyjulia3
- `python -m pip install --user julia`

Initialise with Julia
- `python -c "import julia; julia.install()"`
