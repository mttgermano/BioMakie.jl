import gemmi
import json

doc = gemmi.cif.read_file("components.cif.gz")

print("# Collection of known heavy bonds, for a PDB structure file. The knowledge-based bonds defined here are retrieved directly from https://www.wwpdb.org/.")
print("heavyresbonds = Dict(")
for block in doc:
    name = block.name

    bonds = []

    for row in block.find("_chem_comp_bond.", [
        "atom_id_1",
        "atom_id_2"
    ]):
        a = row[0]
        b = row[1]

        if a[0] != '"': a = f'"{a}"'
        if b[0] != '"': b = f'"{b}"'

        bonds.append(f'[{a},{b}]')

    print(f'"{name}" => [{",".join(bonds)}],')
print(")")
