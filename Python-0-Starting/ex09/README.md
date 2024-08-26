# ft_package

**ft_package** is a simple Python package that provides a utility function for counting occurrences of an item in a list.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

### 1. Building and Installing

To build and/or install the package, use the provided 

```bash
python build.py
```

-   The building process will create a distributable `.tar.gz` and `.whl` file in the `dist/` directory.
-   The installing process will install via whl `./dist/ft_package-0.0.1-py3-none-any.whl` but it can also be installed using the **.tar** `pip install ./dist/ft_package-0.0.1.tar.gz`

### 2. Verifying the Installation

To check if the package is installed correctly, run:

```bash
pip show -v ft_package
```

You should see details like the package name, version, author, and more.

## Usage

Once installed, you can use the package in your Python scripts. The package includes a function called `count_in_list` that counts occurrences of an item in a list.

### Example:

```python
from ft_package import count_in_list

# Example usage
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## Testing

The package includes a basic test script located in the `tests/` directory. You can run it directly to ensure everything is working:

```bash
python tests/tester.py
```

If the tests pass, you should see the message:

```
All tests passed!
```

## Project Structure

```
├── ft_package
│   ├── core.py
│   └── __init__.py
├── setup.py
├── build.py
├── clear.py
└── tests
    └── tester.py
├── LICENSE
├── README.md
```

- **`ft_package/`**: Contains the package’s source code.
- **`setup.py`**: Configuration script for building and installing the package.
- **`tests/`**: Contains test scripts.
- **`build.py`**: Script to build and/or install the package
- **`clear.py`**: Script to build uninstall the package and remove its created directories
## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

