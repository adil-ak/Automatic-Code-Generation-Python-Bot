document.getElementById('csv-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('csv_file', document.getElementById('csv-file').files[0]);
    formData.append('user_message', document.getElementById('user-message').value);

    try {
        const response = await fetch('/process', {
            method: 'POST',
            body: formData,
        });
        const result = await response.json();

        if (result.error) {
            document.getElementById('generated-code').textContent = `Error: ${result.error}`;
            document.getElementById('execution-result').textContent = '';
        } else {
            document.getElementById('generated-code').textContent = result.generated_code;
            document.getElementById('execution-result').textContent = result.execution_result;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('generated-code').textContent = 'An error occurred. Check the console for details.';
        document.getElementById('execution-result').textContent = '';
    }
});
