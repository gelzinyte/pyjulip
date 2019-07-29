import os
import pyjulip
from julia.core import JuliaError
from ase.lattice.cubic import BodyCenteredCubic
from ase.lattice.cubic import Diamond

def test(at, pot):
    for i in xrange(10):
        at.rattle(1E-4)
        at.set_calculator(pot)
        print at.get_potential_energy()

####


######

pot2 = pyjulip.pot("StillingerWeber()")

si_at = Diamond("Si", latticeconstant=5.43)
si_big_at = si_at * (2,2,2)

print "StillingerWeber()"

test(si_big_at, pot2)

######

pot3 = pyjulip.EAM("../data/w_eam4.fs")

w_at = BodyCenteredCubic("W", latticeconstant=3.16)
w_big_at = w_at * (2,2,2)

print "W_EAM"

test(w_big_at, pot3)

######

pot4 = pyjulip.FinnisSinclair("../data/W-pair-Wang-2014.plt", "../data/W-e-dens-Wang-2014.plt")

test(w_big_at, pot4)

try:
    pot = pyjulip.NBodyIPs("Ti_aPIP1_reg.json", fast=True)

    print "NBODYIPS"

    ti_at = BodyCenteredCubic("Ti", latticeconstant=3.32)
    ti_big_at = ti_at * (2,2,2)

    test(ti_big_at, pot)

except JuliaError:
    print("skipping NBodyIPs as not installed")
