import random
from src import Output
from src import QueryGPT
from src import Stats

def Start():
    initialPrompt = '''You are now in student simulator mode.\n\nYour input will be a Test Question.\n\nYour output will be 10 generated, creative, and unique responses simulating various potential answers a student may give. The first 5 responses will be correct and the second 5 will be incorrect. Each of the 10 total responses will be on their own lines, and will contain exclusively the simulated response text (with absolutely no labels, numbering, meta-data indicators, or additional information of any kind).'''
    
    print("---------------------------------------------------------")
    print("Please input the TEST QUESTION, and a unique QUESTION ID.")
    print("---------------------------------------------------------")
    question = input("Test Question: ")
    qid = input("Question Id: (e.g. 1.1, 3.7, etc) ")
    print()

    print("-------------")
    print("Generating...")
    print("-------------")
    query = f"Test Question: {question}.\n"
    gpt_prompt = [
        {"role": "system", "content": f"{initialPrompt}"},
        {"role": "user", "content": f"{query}"}
    ]
    # TODO actually generate responses
    gpt_generations = QueryGPT.query_chatgpt(gpt_prompt)
    # gpt_generations = ['A prototype program serves as a working model that helps identify potential issues and evaluate the feasibility of a solution before fully implementing it.\nA prototype program allows for early user feedback and interaction, which can help refine and improve the final solution.\nA prototype program helps in testing and validating the design choices, functionality, and user interface of a solution before investing significant time and resources into development\nA prototype program serves as a powerful tool for communication and collaboration among stakeholders, enabling them to visualize and comprehend the proposed solution.\nA prototype program allows for iterative development, where changes and improvements can be made based on user feedback and requirements.\nA prototype program is a final version of the software that is ready to be released to users.\nA prototype program is a dummy model used solely for showcasing, with no actual functionality.\nA prototype program is used to identify problems in the original program.\nA prototype program is an illusionary solution to a problem.\nA prototype program is a mirror image of the final solution, with no adjustments needed.']
    print()

    # str (text) -> bool (is_correct)
    answers = {}
    for gpt_generation in gpt_generations:
        raw_responses = list(filter(bool, gpt_generation.split('\n')))
        if len(raw_responses) != 10:
            print("ERROR - Response Format Error.")
        else:
            # First 5 are correct
            for raw_response in raw_responses[:5]:
                answers[raw_response] = True
            # Last 5 are incorrect
            for raw_response in raw_responses[5:]:
                answers[raw_response] = False
    
    # Shuffle order of responses so the user can grade them with minimal bias
    shuffled_text = list(answers.keys())
    random.shuffle(shuffled_text)

    print("-------------------------------------------------------------------------")
    print("Please GRADE the following generated answers as [C]orrect or [I]ncorrect.")
    print("--> ", question)
    print("-------------------------------------------------------------------------")
    # Allow the user to grade each question
    labeled_correctly = 0
    labeled_incorrectly = 0
    for text in shuffled_text:
        user_input = input(f'ANSWER: {text}\n').lower()
        while True:
            if user_input in ('c', 'correct', 'right', 'yes', 'true'):
                if answers[text]:
                    labeled_correctly += 1
                else:
                    labeled_incorrectly += 1
                    # If incorrect, fix the label
                    answers[text] = not answers[text]
                break
            elif user_input in ('i', 'incorrect', 'wrong', 'no', 'false'):
                if not answers[text]:
                    labeled_correctly += 1
                else:
                    labeled_incorrectly += 1
                    # If incorrect, fix the label
                    answers[text] = not answers[text]
                break
            else:
                user_input = input('Invalid input - Please enter "C" or "I".')
    
    # Update and report persistent statistics
    total_correct, total_incorrect = Stats.update_stats(labeled_correctly, labeled_incorrectly)
    current_percent = 0.00
    if labeled_correctly + labeled_incorrectly != 0:
        current_percent = round((labeled_correctly / (labeled_correctly + labeled_incorrectly)) * 100, 2)
    lifetime_percent = 0.00
    if total_correct + total_incorrect != 0:
        lifetime_percent = round((total_correct / (total_correct + total_incorrect)) * 100, 2)
    print("--------------------------------------------------------------------")
    print(f"Answers correctly labeled by GPT Model: {labeled_correctly} / {labeled_correctly + labeled_incorrectly} ({current_percent:.2f})%")
    print(f"Lifetime answers correctly labeled by GPT Model: {total_correct} / {total_correct + total_incorrect} ({lifetime_percent:.2f}%)")
    print("--------------------------------------------------------------------")

    # Save off generated response data into correct format
    output_path = Output.output_new_data(question, qid, answers)
    print('Responses saved to path: ' + output_path)
    print()
