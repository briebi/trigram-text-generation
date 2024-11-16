# README: Trigram Text Generator from Novel

## Overview

This Python script processes a novel, builds a trigram language model, and generates text based on the trigrams. The script reads the novel line by line, cleans and preprocesses the text, and constructs a trigram dictionary for word prediction. It then generates random text using the trigram model.

---

## Features

1. **Text Preprocessing**:
   - Removes unnecessary characters and formats sentences for consistent processing.
   - Handles abbreviations like "Mr.", "Mrs.", and "St." to avoid sentence breaks.

2. **Trigram Model Creation**:
   - Builds a dictionary-based trigram model that maps pairs of words to possible third words.

3. **Text Generation**:
   - Generates random text based on the trigram model, ensuring sentences flow naturally.

4. **Progress Tracking**:
   - Displays progress as it processes lines of the novel.

---

## Prerequisites

- Python 3.x

---

## Setup Instructions

1. **Install Python**:  
   Ensure Python 3.x is installed.  
   [Download Python](https://www.python.org/downloads/)

2. **Prepare the Novel File**:  
   Place a plain text file of the novel (e.g., `tale_of_2_cities_nll.txt`) in the same directory as the script.

3. **Run the Script**:  
   Execute the script in your Python environment:  
   ```bash
   python trigram_text_generator.py
