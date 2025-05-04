# Password Generator

This Python project provides a flexible framework for generating different types of passwords. It includes three types of password generators:

1. **PIN Generator**: Generates numeric-only PINs.
2. **Random Password Generator**: Generates strong random passwords using letters, digits, and symbols (based on user's choice).
3. **Memorable Password Generator**: Generates human-readable passwords using real English words.

## File Structure
```bash
├── README.md
├── requirements.txt
└── src
    ├── main.ipynb
    └── main.py
```
## Requirements

- Python 3.6+
- [NLTK](https://www.nltk.org/)

You can install NLTK with:

```bash
pip install nltk
```

## Usage
To run the default Memorable Password Generator:

```bash
python main.py
```

## Classes
- **PasswordGenerator**: Abstract base class with a generate() method.
- **PinGenerator**: Generates numeric-only PINs of custom length.
- **RandomPasswordGenerator**: Customizable random passwords using ASCII characters.
- **MemorablePasswordGenerator**: Human-readable word-based passwords from NLTK corpus