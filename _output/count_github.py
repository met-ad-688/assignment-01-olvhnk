import pandas as pd

# List of CSV files
files = ["question_tags.csv", "questions.csv"]
count = 0

for file in files:
    try:
        # Read CSV file with the python engine to handle potential issues
        df = pd.read_csv(file, dtype=str, on_bad_lines="skip", engine='python')

        # Count occurrences of "GitHub" (case-insensitive) in any column
        count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False, na=False).any(), axis=1).sum()

        print(f"Occurrences of 'GitHub' in {file}: {count}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

# Print total occurrences of "GitHub"
print(f"Total occurrences of 'GitHub': {count}")
