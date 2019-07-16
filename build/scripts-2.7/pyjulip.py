import numpy as np
from ase.calculators.calculator import Calculator
from ase.constraints import voigt_6_to_full_3x3_stress, full_3x3_to_voigt_6_stress

from julia import Main
from julia import ASE
from julia import JuLIP

from julia.JuLIP import energy
from julia.JuLIP import forces
from julia.JuLIP import stress

ASEAtoms = Main.eval("ASEAtoms(a) = ASE.ASEAtoms(a)")
ASECalculator = Main.eval("ASECalculator(c) = ASE.ASECalculator(c)")
fixedcell = Main.eval("fixedcell(a) = JuLIP.Constraints.FixedCell(a)")
variablecell = Main.eval("variablecell(a) = JuLIP.Constraints.VariableCell(a)")

convert = Main.eval("julip_at(a) = JuLIP.Atoms(a)")

from julia import Julia

julia = Julia()
julia.using("JuLIP")

def pot(potname, fast=False):
    try:
        julia.eval("IP = " + potname)
        ASE_IP = JulipCalculator("IP")
        return ASE_IP
    except:
        print("couldn't find potential")

def NBodyIPs(potname, fast=False):
    try:
        julia.using("NBodyIPs")
        julia.eval("IP, info = load_ip(\""+ potname + "\")")
        if fast:
            julia.eval("IP = fast(IP)")
        ASE_IP = JulipCalculator("IP")
        return ASE_IP
    except:
        print("couldn't find .json file")

def FinnisSinclair(potname1, potname2):
    try:
        julia.eval("IP = JuLIP.Potentials.FinnisSinclair(\"" + potname1 + "\", \"" + potname2 + "\")")
        ASE_IP = JulipCalculator("IP")
        return ASE_IP
    except:
        print("couldn't find potential")

def EAM(potname):
    try:
        julia.eval("IP = JuLIP.Potentials.EAM(\"" + potname + "\")")
        ASE_IP = JulipCalculator("IP")
        return ASE_IP
    except:
        print("couldn't find potential")


class JulipCalculator(Calculator):
    """
    ASE-compatible Calculator that calls JuLIP.jl for forces and energy
    """
    implemented_properties = ['forces', 'energy', 'stress']
    default_parameters = {}
    name = 'JulipCalculator'

    def __init__(self, julip_calculator):
        Calculator.__init__(self)
        self.julip_calculator = Main.eval(julip_calculator) #julia.eval

    def calculate(self, atoms, properties, system_changes):
        Calculator.calculate(self, atoms, properties, system_changes)
        julia_atoms = ASEAtoms(atoms)
        julia_atoms = convert(julia_atoms)
        self.results = {}
        if 'energy' in properties:
            self.results['energy'] = energy(self.julip_calculator, julia_atoms)
        if 'forces' in properties:
            self.results['forces'] = np.array(forces(self.julip_calculator, julia_atoms))
        if 'stress' in properties:
            voigt_stress = full_3x3_to_voigt_6_stress(np.array(stress(self.julip_calculator, julia_atoms)))
            self.results['stress'] = voigt_stress
