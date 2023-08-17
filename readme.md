# SQL Query Obfuscation and De-obfuscation Tool

## Purpose

This tool allows users to securely share SQL queries without exposing sensitive table and column names. It obfuscates these names into randomized strings of equal length and provides a method to de-obfuscate them back into the original readable format.

## Features

- **Obfuscation:** Convert table and column names in SQL queries into randomized strings of equal length.
- **De-obfuscation:** Convert obfuscated table and column names back to their original form.
- **Prompt Handling:** Handle prompts that ask questions about specific columns in the SQL query, obfuscating and de-obfuscating them as needed.

## User Stories

1. **Obfuscation:**
   - Input a SQL file containing a query.
   - Have the Python script read this SQL file and obfuscate table and column names.
   - Have the Python script output the obfuscated SQL query in a separate file.

2. **De-obfuscation:**
   - Take obfuscated text (queries and prompts) and convert it back to readable form.
   - Have the Python script read the obfuscated text file and a mapping file.
   - Have the Python script output the readable text in a new text file.

3. **Prompt Handling:**
   - Input a prompt in a text file that asks a question about a specific column in the SQL query.
   - Have this prompt obfuscated in the same way as the SQL queries.
   - Have the Python script output the obfuscated prompt in a separate file.

## Directory Structure

```plaintext
obsfu/
├── app/
│   ├── obfuscator.py
│   └── deobfuscator.py
├── input_files/
│   ├── example_query.sql
│   └── prompt.txt
├── output_files/
│   ├── example_query_obfuscated.sql
│   └── mapping.json
└── responses/
    ├── obfuscated_response.txt
    └── response_clean.txt

## Usage

1. Place your SQL file and prompt text file in the `input_files/` directory.
2. Run `obfuscator.py` to obfuscate the SQL queries and prompts. The obfuscated files and mapping file will be saved in the `output_files/` directory.
3. Place the obfuscated response text file in the `responses/` directory.
4. Run `deobfuscator.py` to de-obfuscate the responses based on the mapping file. The de-obfuscated response will be saved in the `responses/` directory as `response_clean.txt`.

## Dependencies

- Python 3.x

## Installation

1. Clone the repository to your local machine.
2. Navigate to the `obsfu/app/` directory.
3. Run the Python scripts as per the usage instructions.

## Error Handling

The tool handles file not found errors gracefully with user-friendly error messages.