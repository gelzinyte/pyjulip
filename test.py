import os
import pyjulip

pot = pyjulip.pot("Ti_aPIP1_reg.json", fast=True)

from ase.lattice.cubic import BodyCenteredCubic

at = BodyCenteredCubic("Ti", latticeconstant=3.32)

big_at = at * (2,2,2)

import time

t1 = time.time()

for i in xrange(10):
    big_at.rattle(1E-6)
    big_at.set_calculator(pot)
    print big_at.get_potential_energy()

t2 = time.time()

print t2-t1
