# Python AI Developer Assignment

This project is part of a technical assignment designed to build a system that integrates code generation with automated execution. The application uses Python, Flask, and OpenAI's API to process user inputs dynamically.

## Objective

The application allows users to:
1. Upload a CSV file.
2. Enter a text-based query describing the operation they want to perform on the CSV data.
3. Generate Python code dynamically using OpenAI's GPT-3.5-turbo model.
4. Execute the generated Python code and return the result or errors, if any.

---

## Key Features

- **CSV File Handling**: Parse and process uploaded CSV files.
- **Code Generation**: Generate Python code based on the content of the CSV and user instructions.
- **Dynamic Execution**: Execute generated Python code securely and return results.
- **Error Handling**: Robust mechanisms to handle incorrect inputs or API errors.

---

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

---

## Installation and Setup

### Prerequisites
Ensure you have Python 3.x installed on your system.

### Steps
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>