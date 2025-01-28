# Python AI Code Generation Bot

This project is a Python-based application that takes two inputs: a CSV file and a user message. Using OpenAI's API, it generates Python code to manipulate the data from the CSV file as requested by the user. The system then executes the generated Python code dynamically and returns the results.

## Features
- Accepts a CSV file and a user message.
- Uses OpenAI GPT-3 to generate Python code based on the user’s message.
- Executes the generated Python code to process the data from the CSV file.
- Returns both the generated code and the execution result.

## Setup Instructions

### Prerequisites:
- Python 3.x
- Install required Python libraries by running:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-developer-assignment.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ai-developer-assignment
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open your browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

6. Upload a CSV file and provide a user message. The app will generate Python code and show the result of the execution.

### Notes:
- The app uses OpenAI's GPT-3 API to generate Python code based on the user input and CSV data.
- Make sure to set up your OpenAI API key before running the application. You can include the API key in your code directly or store it in an `.env` file.
  
## Files:
- `app.py`: Main Python file for the application.
- `requirements.txt`: List of Python dependencies.
- `index.html`, `styles.css`, `scripts.js`: Frontend files for the user interface.

## Technologies Used:
- Python 3.x
- Flask (for the web framework)
- OpenAI GPT-3
- Pandas (for CSV manipulation)

## Example Inputs and Outputs:
### Input CSV:
### User Message:
`"Calculate the average salary of employees."`

### Generated Code:
```python
import pandas as pd

def process_csv(file_path):
    data = pd.read_csv(file_path)
    return data['Salary'].mean()

result = process_csv('input.csv')
print(result)

## Output:
70000.0


