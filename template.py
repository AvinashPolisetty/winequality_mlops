import os

directories=[
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir in directories:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"),"w") as f:
        pass

files=[
     "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass