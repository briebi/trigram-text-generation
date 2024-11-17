# README: Trigram Text Generator

## Overview

This Python script processes a text file, builds a trigram language model, and generates coherent text based on the model. It supports multiple input files, allowing users to select from various novels or texts for analysis and text generation.

---

## Features

1. **Multiple File Support**:
   - Select from six available text files (e.g., *tale_of_2_cities.txt*) by changing the `novel_file` variable.

2. **Text Preprocessing**:
   - Cleans and formats lines by:
     - Removing unnecessary characters.
     - Handling abbreviations (e.g., "Mr.", "Mrs.", "St.") to prevent sentence breaks.

3. **Trigram Model Creation**:
   - Builds a dictionary-based trigram model to predict the next word given two preceding words.

4. **Text Generation**:
   - Generates random, readable text using the trigram model.

5. **Progress Updates**:
   - Displays processing progress in increments of 100 lines.

---

## Prerequisites

- **Python 3.x**
- **Text Files**:
  - Ensure the desired text file is in the same directory as the script.
  - Default file: `tale_of_2_cities.txt`
  - Available options:
    - `emma.txt`
    - `great_expectations.txt`
    - `story_dr_dolittle.txt`
    - `tale_of_2_cities.txt`
    - `winnie_the_pooh.txt`
    - `wizard_of_oz.txt`

---

## Usage

1. **Install Python**:  
   Ensure Python 3.x is installed on your system.  
   [Download Python](https://www.python.org/downloads/)

2. **Set Input File**:  
   Update the `novel_file` variable to the desired text file. For example:
   ```python
   novel_file = 'great_expectations.txt'


3. **Run the Script**:  
   Execute the script in your Python environment:  
   ```bash
   python main.py
