#!/bin/bash

# Count the number of lines containing the word "python" in question_tags.csv
count_tags=$(grep -ic "python" question_tags.csv)

# Count the number of lines containing the word "python" in questions.csv
count_questions=$(grep -ic "python" questions.csv)

# Output the results
echo "Lines containing 'python' in question_tags.csv: $count_tags"
echo "Lines containing 'python' in questions.csv: $count_questions"