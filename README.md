# Titanic Classification Model

Welcome to the Titanic Classification Model repository! This project features a machine learning model designed to predict passenger survival using the Titanic dataset. The model is conveniently packaged using `tox` for efficient environment management.

## Quick Start

Clone the repository and set up the environment with just a few commands:

```bash
git clone https://github.com/Ubeydkhoiri/titanic-classification-model.git
cd titanic-classification-model
pip install tox
```

## Usage
Utilize the power of tox to streamline your workflow with two dedicated virtual environments:

1. test_package: Execute train_pipeline.py and run pytest on the tests.

```
tox -e test_package
```

2. checks: Perform type checking, linting, and formatting checks with flake8, isort, black, and mypy.

```bash
tox -e checks
```

## Contributions
We welcome contributions! Prior to submitting a pull request, ensure your code aligns with project standards by running the provided checks and tests using tox.

## License
This project is licensed under the [MIT License](https://github.com/Ubeydkhoiri/titanic-classification-model/LICENSE).

Happy coding!
