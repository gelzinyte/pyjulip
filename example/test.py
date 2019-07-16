import os
import pyjulip
from ase.lattice.cubic import BodyCenteredCubic
from ase.lattice.cubic import Diamond

####

pot = pyjulip.pot("Ti_aPIP1_reg.json", fast=True)

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

for i in xrange(10):
    si_big_at.rattle(1E-4)
    si_big_at.set_calculator(pot2)
    print si_big_at.get_potential_energy()
