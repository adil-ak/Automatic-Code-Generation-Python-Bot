import os
import pandas as pd
import openai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()  # Load the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_csv():
    try:
       
        csv_file = request.files['csv_file']
        user_message = request.form['user_message']
        csv_path = 'uploaded.csv'
        csv_file.save(csv_path)

        
        df = pd.read_csv(csv_path)
        prompt = f"""
        You are a Python expert. Given this CSV file data:
        {df.head().to_string(index=False)}

        Write Python code to accomplish this task: "{user_message}".
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        generated_code = response['choices'][0]['message']['content'].strip()

        # Execute the generated code
        local_context = {"pd": pd, "csv_path": csv_path}
        try:
            exec(generated_code, {}, local_context)
            execution_result = local_context.get('result', 'Execution completed successfully, but no result was returned.')
        except Exception as e:
            execution_result = str(e)

        return jsonify({
            "generated_code": generated_code,
            "execution_result": execution_result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)