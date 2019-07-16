import os
import pyjulip
from ase.lattice.cubic import BodyCenteredCubic
from ase.lattice.cubic import Diamond

####

pot = pyjulip.NBodyIPs("Ti_aPIP1_reg.json", fast=True)

print "NBODYIPS"

ti_at = BodyCenteredCubic("Ti", latticeconstant=3.32)
ti_big_at = ti_at * (2,2,2)

for i in xrange(10):
    ti_big_at.rattle(1E-4)
    ti_big_at.set_calculator(pot)
    print ti_big_at.get_potential_energy()

######

pot2 = pyjulip.pot("StillingerWeber()")

si_at = Diamond("Si", latticeconstant=5.43)
si_big_at = si_at * (2,2,2)

print "StillingerWeber()"

for i in xrange(10):
    si_big_at.rattle(1E-4)
    si_big_at.set_calculator(pot2)
    print si_big_at.get_potential_energy()


######

pot3 = pyjulip.EAM("../data/w_eam4.fs")

w_at = BodyCenteredCubic("W", latticeconstant=3.16)
w_big_at = w_at * (2,2,2)

print "W_EAM"

for i in xrange(10):
    w_big_at.rattle(1E-4)
    w_big_at.set_calculator(pot3)
    print w_big_at.get_potential_energy()

######

pot4 = pyjulip.FinnisSinclair("../data/W-pair-Wang-2014.plt", "../data/W-e-dens-Wang-2014.plt")

w_at = BodyCenteredCubic("W", latticeconstant=3.16)
w_big_at = w_at * (2,2,2)

print "W_FS"

for i in xrange(10):
    w_big_at.rattle(1E-4)
    w_big_at.set_calculator(pot4)
    print w_big_at.get_potential_energy()
