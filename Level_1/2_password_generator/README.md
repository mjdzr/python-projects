# 🔐 Streamlit Password Generator

A web-based password generator built with **Streamlit**, supporting:
- Random passwords with customizable strength
- Memorable word-based passwords
- Numeric PIN codes

![Banner](./images/banner.jpg)

## Features

### 1.Random Password Generator
- Adjustable length (4–64)
- Optional inclusion of numbers and symbols

### 2.Memorable Password Generator
- Select number of words
- Custom separator
- Capitalization toggle
- Minimum and maximum word length filter

### 3.PIN Generator
- Numeric PINs of adjustable length

## Project Structure
- **password_generator.py**: Python module containing the password generator classes.
- **dashboard.py**: Python script to create a streamlit web app.
- **README.md**: Documentation of the project. You are currently here!

## Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io)
- [NLTK](https://www.nltk.org/) – used for English vocabulary in memorable passwords

To install NLTK, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```python
import nltk
nltk.download('words')
```

## Usage
To run the streamlit web app:
```bash
streamlit run src/dashboard.py
```

## Functionality Overview

- **RandomPasswordGenerator:**
generates a random password with a user-specified length. Users can choose to include numbers and special characters to increase password strength.

- **MemorablePasswordGenerator:**
creates a password by combining multiple English words. Users can configure the number of words, the separator character, capitalization, and minimum/maximum word length. Support for using a custom vocabulary list can also be added.

- **PinGenerator:**
Generates a numeric PIN code based on the desired length.