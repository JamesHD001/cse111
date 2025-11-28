""" 
Author: Henry Daniel James.

Description:
Ask the user for a chemical formula.
Ask the user for the amount of the compound in grams (this is the sample_mass).
Compute and display the molar mass.
Compute and display the number of moles.

Extra credit feature(s)
Added a feature where the system identifies the compound name
based on the formula inputed by the user.

"""

from formula import parse_formula
COMPOUND_NAMES = {
    "O2": "Oxygen Gas",
    "N2": "Nitrogen Gas",
    "Cl2": "Chlorine Gas",
    "F2": "Fluorine Gas",
    "He": "Helium",
    "Ne": "Neon",
    "Ar": "Argon",
    "H2O": "Water",
    "CO": "Carbon Monoxide",
    "CO2": "Carbon Dioxide",
    "SO2": "Sulfur Dioxide",
    "SO3": "Sulfur Trioxide",
    "H2O2": "Hydrogen Peroxide",
    "MgO": "Magnesium Oxide",
    "CaO": "Calcium Oxide",
    "Fe2O3": "Iron(III) Oxide",
    "Fe3O4": "Magnetite",
    "HCl": "Hydrochloric Acid",
    "H2SO4": "Sulfuric Acid",
    "HNO3": "Nitric Acid",
    "H3PO4": "Phosphoric Acid",
    "NaOH": "Sodium Hydroxide",
    "KOH": "Potassium Hydroxide",
    "Ca(OH)2": "Calcium Hydroxide",
    "Mg(OH)2": "Magnesium Hydroxide",
    "NaCl": "Sodium Chloride",
    "KCl": "Potassium Chloride",
    "CaCO3": "Calcium Carbonate",
    "NaHCO3": "Sodium Bicarbonate",
    "CuSO4": "Copper(II) Sulfate",
    "ZnS": "Zinc Sulfide",
    "AgNO3": "Silver Nitrate",
    "CH4": "Methane",
    "C2H6": "Ethane",
    "C3H8": "Propane",
    "C4H10": "Butane",
    "C6H6": "Benzene",
    "C2H5OH": "Ethanol",
    "C6H12O6": "Glucose",
    "C12H22O11": "Sucrose",
    "NH3": "Ammonia",
    "CH3COOH": "Acetic Acid",
    "Na2CO3": "Sodium Carbonate",
    "K2SO4": "Potassium Sulfate",
    "CaSO4": "Calcium Sulfate",
    "Al2O3": "Aluminum Oxide",
    "SiO2": "Silicon Dioxide",
}


def make_periodic_table():
  periodic_table_dict = {
      "Ac": ["Actinium", 227],
      "Ag": ["Silver", 107.8682],
      "Al": ["Aluminum", 26.9815386],
      "Ar": ["Argon", 39.948],
      "As": ["Arsenic", 74.9216],
      "At": ["Astatine", 210],
      "Au": ["Gold", 196.966569],
      "B": ["Boron", 10.811],
      "Ba": ["Barium", 137.327],
      "Be": ["Beryllium", 9.012182],
      "Bi": ["Bismuth", 208.9804],
      "Br": ["Bromine", 79.904],
      "C": ["Carbon", 12.0107],
      "Ca": ["Calcium", 40.078],
      "Cd": ["Cadmium", 112.411],
      "Ce": ["Cerium", 140.116],
      "Cl": ["Chlorine", 35.453],
      "Co": ["Cobalt", 58.933195],
      "Cr": ["Chromium", 51.9961],
      "Cs": ["Cesium", 132.9054519],
      "Cu": ["Copper", 63.546],
      "Dy": ["Dysprosium", 162.5],
      "Er": ["Erbium", 167.259],
      "Eu": ["Europium", 151.964],
      "F": ["Fluorine", 18.9984032],
      "Fe": ["Iron", 55.845],
      "Fr": ["Francium", 223],
      "Ga": ["Gallium", 69.723],
      "Gd": ["Gadolinium", 157.25],
      "Ge": ["Germanium", 72.64],
      "H": ["Hydrogen", 1.00794],
      "He": ["Helium", 4.002602],
      "Hf": ["Hafnium", 178.49],
      "Hg": ["Mercury", 200.59],
      "Ho": ["Holmium", 164.93032],
      "I": ["Iodine", 126.90447],
      "In": ["Indium", 114.818],
      "Ir": ["Iridium", 192.217],
      "K": ["Potassium", 39.0983],
      "Kr": ["Krypton", 83.798],
      "La": ["Lanthanum", 138.90547],
      "Li": ["Lithium", 6.941],
      "Lu": ["Lutetium", 174.9668],
      "Mg": ["Magnesium", 24.305],
      "Mn": ["Manganese", 54.938045],
      "Mo": ["Molybdenum", 95.96],
      "N": ["Nitrogen", 14.0067],
      "Na": ["Sodium", 22.98976928],
      "Nb": ["Niobium", 92.90638],
      "Nd": ["Neodymium", 144.242],
      "Ne": ["Neon", 20.1797],
      "Ni": ["Nickel", 58.6934],
      "Np": ["Neptunium", 237],
      "O": ["Oxygen", 15.9994],
      "Os": ["Osmium", 190.23],
      "P": ["Phosphorus", 30.973762],
      "Pa": ["Protactinium", 231.03588],
      "Pb": ["Lead", 207.2],
      "Pd": ["Palladium", 106.42],
      "Pm": ["Promethium", 145],
      "Po": ["Polonium", 209],
      "Pr": ["Praseodymium", 140.90765],
      "Pt": ["Platinum", 195.084],
      "Pu": ["Plutonium", 244],
      "Ra": ["Radium", 226],
      "Rb": ["Rubidium", 85.4678],
      "Re": ["Rhenium", 186.207],
      "Rh": ["Rhodium", 102.9055],
      "Rn": ["Radon", 222],
      "Ru": ["Ruthenium", 101.07],
      "S": ["Sulfur", 32.065],
      "Sb": ["Antimony", 121.76],
      "Sc": ["Scandium", 44.955912],
      "Se": ["Selenium", 78.96],
      "Si": ["Silicon", 28.0855],
      "Sm": ["Samarium", 150.36],
      "Sn": ["Tin", 118.71],
      "Sr": ["Strontium", 87.62],
      "Ta": ["Tantalum", 180.94788],
      "Tb": ["Terbium", 158.92535],
      "Tc": ["Technetium", 98],
      "Te": ["Tellurium", 127.6],
      "Th": ["Thorium", 232.03806],
      "Ti": ["Titanium", 47.867],
      "Tl": ["Thallium", 204.3833],
      "Tm": ["Thulium", 168.93421],
      "U": ["Uranium", 238.02891],
      "V": ["Vanadium", 50.9415],
      "W": ["Tungsten", 183.84],
      "Xe": ["Xenon", 131.293],
      "Y": ["Yttrium", 88.90585],
      "Yb": ["Ytterbium", 173.054],
      "Zn": ["Zinc", 65.38],
      "Zr": ["Zirconium", 91.224]
    }
  return periodic_table_dict
  
def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
  total_mass = 0
  
  for symbol, quantity in symbol_quantity_list:
    atomic_mass = periodic_table_dict[symbol][1]
    total_mass += atomic_mass * quantity
    
  return total_mass




def main():
  molecular_formula = input("Enter the Molecular Formula of the sample: ")
  mass = input(float("Enter the mass in grams of the sample: "))
 
  periodic_table = make_periodic_table()
  symbol_quantity_list = parse_formula(molecular_formula)
  molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
  moles = mass / molar_mass
  compound_name = COMPOUND_NAMES.get(molecular_formula, "Unknown Compound")
  
  print(f"Compound Name: {compound_name}")
  print(f"The molar mass is: {molar_mass: .5f} g/mol ")
  print(f"The number of moles in the sample is: {moles: .5f}")
    
if __name__ == "__main__":
  main()