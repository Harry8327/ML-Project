from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r", encoding="utf-8") as file_obj:
        for line in file_obj:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("-e ") or line.startswith("--editable"):
                continue
            requirements.append(line)
    return requirements


setup(
    name="MLPROJECT",
    version="0.0.1",
    author="Harsh",
    author_email="tgharsh17@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)
