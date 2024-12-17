import os
from pathlib import Path

list_of_files =[
    ".github/workflows/.gitkeep"
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/logger.py",
    "src/exception.py",
    "src/utils.py",
    "setup.py",
    "requirements.txt",
    "src/config/configuration.py",
    "src/constants/__init__.py",
    "src/entity/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, file = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or os.path.getsize(filepath) ==0:
        with open(filepath, "w") as f:
            pass