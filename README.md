# OOP Ontology Modeling

A practice repository for modeling object-oriented programming concepts with OWL ontologies and using those ontology definitions to generate simple object-oriented code artifacts. The project experiments with model-to-text workflows for Python, Java, and C++ using input models, ontology files, and Python generator scripts.

The repository is primarily a learning and experimentation workspace. It keeps the ontology source files, sample input model, generation scripts, and generated output examples together so the modeling pipeline can be inspected end to end.

## Repository

```bash
git clone https://github.com/RaphaelZH/oop-ontology-modeling.git
cd oop-ontology-modeling
```

## Contents

| Path | Description |
| --- | --- |
| `1. Inputs/1. Input Models/` | Sample object-oriented input model files, including the registration form model. |
| `1. Inputs/2. Input Ontology/` | OWL ontology and properties files used by the model-to-text generator. |
| `1. Ontology Files/` | Generated or edited ontology files for programming-language parser modeling. |
| `2. Outputs/1. Python Files/` | Generated Python output examples. |
| `2. Outputs/2. Java Files/` | Generated Java output examples. |
| `2. Outputs/3. Cpp Files/` | Generated C++ output examples. |
| `BasicClassGenerator.py` | Builds the base OWL classes and properties used for programming-language grammar modeling. |
| `DictionaryGenerator.py` | Defines Python keyword, operator, and symbol dictionaries used by the parser ontology. |
| `parser.py` | Builds and saves the programming-language parser ontology, then queries syntactic chains with Prolog. |
| `M2T_tester.py` | Reads input models and ontology templates, then generates language-specific code output. |
| `model_parser.py` | Prints the structure of input `.model` files for inspection. |
| `script.py` | Experimental OWL-to-Python class generation script. |
| `venv-python3-10_requirements.txt` | Snapshot of a local Python environment used during development. |

## What This Project Explores

- Representing object-oriented concepts as ontology classes, properties, and individuals.
- Modeling language grammar elements such as keywords, operators, parser nodes, and syntactic chains.
- Reading XML-style `.model` files and mapping model elements to generated class code.
- Producing basic Python, Java, and C++ output from ontology-guided templates.
- Using `owlready2` and `pyswip` together for ontology manipulation and Prolog-style relationship queries.

## Requirements

- Python 3.10 or newer
- Java/Prolog runtime support if using `pyswip` with a local SWI-Prolog installation
- Python packages used by the scripts, especially:
  - `owlready2`
  - `pyswip`
  - `termcolor`

A full local environment snapshot is available in `venv-python3-10_requirements.txt`, but for a clean setup it is usually better to install only the packages required by the scripts you plan to run.

## Environment Setup

Create and activate a local virtual environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install owlready2 pyswip termcolor
```

Local virtual environments such as `.venv/` or `venv-python3-10/` should stay out of Git.

## Common Workflows

Inspect the sample input model:

```bash
python model_parser.py
```

Generate language-specific output from the input model and ontology templates:

```bash
python M2T_tester.py
```

Build or refresh the programming-language parser ontology:

```bash
python parser.py
```

Run the experimental ontology-to-Python class generator:

```bash
python script.py
```

Generated outputs are written under `2. Outputs/` or to script-specific output files such as `Python_OOP.py`.

## Notes on Generated Files

Some files in this repository are examples produced by earlier runs, including generated `.class` files and language-specific outputs. Treat them as reference artifacts for the modeling experiment rather than as a packaged application release.

If you rerun the scripts, generated files may change depending on the ontology content, input model, and local dependency versions.

## Git Hygiene

The repository should keep source ontologies, model examples, generator scripts, and useful output examples. Local caches and runtime-only files should remain untracked, including:

- `.DS_Store`
- `__pycache__/`
- local virtual environments
- temporary generated scratch files

## License

No repository-level license file is currently included. Check the project context and dependencies before redistributing code or derived artifacts.
