import os

def output_new_data(question, question_id, answers):
    raw_directory = "output/raw/"
    scores_directory = f"output/scores/{question_id}"

    raw_responses_file = os.path.join(raw_directory, question_id)
    raw_questions_file = os.path.join(raw_directory, 'questions')
    scores_question_file = os.path.join(scores_directory, 'gpt')

    # Ensure all directories exist
    if not os.path.exists(raw_directory):
        os.makedirs(raw_directory)
    if not os.path.exists(scores_directory):
        os.makedirs(scores_directory)
    
    # SAVE ACTUAL RESPONSES TO FILE
    if not os.path.exists(raw_responses_file):
        with open(raw_responses_file, 'w') as file:
            for answer, _ in answers.items():
                file.write(f"{question_id} {answer}\n")
    else:
        with open(raw_responses_file, 'a') as file:
            for answer, _ in answers.items():
                file.write(f"{question_id} {answer}\n")

    # SAVE QUESTION TO FILE
    if not os.path.exists(raw_questions_file):
        with open(raw_questions_file, 'w') as file:
            file.write(f"{question_id} {question}\n")
    else:
        lines = None
        updated = False
        with open(raw_questions_file, 'r') as file:
            lines = file.readlines()
            if not any(line.startswith(f"{question_id}") for line in lines):
                lines.append(f"{question_id} {question}\n")
                lines.sort()
                updated = True
        if updated:
            with open(raw_questions_file, 'w') as file:
                file.writelines(lines)

    # SAVE SCORES TO FILE
    if not os.path.exists(scores_question_file):
        with open(scores_question_file, 'w') as file:
            for _, is_correct in answers.items():
                file.write("5\n" if is_correct else "0\n")
    else:
        with open(scores_question_file, 'a') as file:
            for _, is_correct in answers.items():
                file.write("5\n" if is_correct else "0\n")

    return str(raw_responses_file)
