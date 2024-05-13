# Ligands_pLDDT_assessment
Script for ligand pLDDT extraction

AlphaFold v3 allows predictions with ligands and ions included. You can test the probability of interaction with your protein using the pLDDT scores which can be extracted from the cif file using this script.

You can use the script this way:

```python
python3 ligands_pLDDT_assess.py CIF_FILE
```

Example files are included for mitochondrial carrier:

```python
python3 ligands_pLDDT_assess.py ./example/fold_gl50803_17286_model_0.cif
```
