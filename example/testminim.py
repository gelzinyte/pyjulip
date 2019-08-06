import numpy as np

from ase.build import bulk
from ase.calculators.lj import LennardJones
from ase.optimize import LBFGSLineSearch
from ase.constraints import UnitCellFilter

import pyjulip

bulk_at = bulk("Cu", cubic=True)
sigma = (bulk_at*2).get_distance(0, 1)*(2.**(-1./6))
calc = LennardJones(sigma=sigma, epsilon=0.05)

N_cell = 3
at0 = bulk_at * N_cell
del at0[0]

at_ref = at0.copy()
at_ref.set_calculator(calc)
opt = LBFGSLineSearch(at_ref)
opt.run(fmax=1e-6)

at_ref_var_cell = at0.copy()
at_ref_var_cell.set_calculator(calc)
opt = LBFGSLineSearch(UnitCellFilter(at_ref_var_cell))
opt.run(fmax=1e-6)

for variable_cell in [False, True]:
    at = at0.copy()
    at.set_calculator(calc)
    opt = pyjulip.JulipOptimizer(at, variable_cell=variable_cell)
    opt.run(fmax=1e-6)

    if variable_cell:
        assert np.abs(at.positions - at_ref_var_cell.positions).max() < 1e-6
        assert np.abs(at.cell - at_ref_var_cell.cell).max() < 1e-6
    else:
        assert np.abs(at.positions - at_ref.positions).max() < 1e-6
