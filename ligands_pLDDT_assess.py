#AlphaFold v3 allows predictions with ligands and ions
#The AlphaFold webserver produces .cif files that contain the pLDDT values for the ligands
#This script contains a function to extract those values into a dictionary
#A function to write those values into a file is also included
#
#It can be used in a commnad line in a simple way:
#python3 ligands_pLDDT_assess.py FILENAME
#
#You can test this with:
#python3 ligands_pLDDT_assess.py ./example/fold_gl50803_17286_model_0.cif
import sys


def get_avg_pLDDTs(cif_file):

	ligands = {}
	ligands_avg_pLDDT = {}

	with open(cif_file, "r") as f:
		for l in f:
			if l.startswith("HETATM"):
				ligand_name = l.split()[5]
				ligand_pLDDT = float(l.split()[-4])
				if not ligand_name in ligands:
					ligands[ligand_name] = [ligand_pLDDT]
				else:
					ligands[ligand_name].append(ligand_pLDDT)

	for ligand in ligands:
		avg_pLDDT = sum(ligands[ligand])/len(ligands[ligand])
		ligands_avg_pLDDT[ligand] = avg_pLDDT

	ligands_avg_pLDDT = {k: v for k, v in sorted(ligands_avg_pLDDT.items(), key=lambda item: item[1], reverse=True)}
	return ligands_avg_pLDDT

def write_results(cif_file, ligands_avg_pLDDTs):

	file_name = sys.argv[1][:-4]

	results = ""
	for ligand in ligands_avg_pLDDTs:
		results += f"{ligand} : {ligands_avg_pLDDTs[ligand]:.2f}\n"

	print(file_name)
	with open(f"{file_name}.ligands_score", "w") as f:
		f.write(results)

if __name__ == "__main__":
	ligands_avg_pLDDTs = get_avg_pLDDTs(sys.argv[1])
	write_results(sys.argv[1],ligands_avg_pLDDTs)