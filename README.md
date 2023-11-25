# LLM-NLP Student Simulator
This *Large Language Model Natural Language Processor (LLM-NLP) Student Simulator* is designed to use LLMs to help simulate student input on NLP-graded free response problems.

## Table of Contents
- [Installation](#installation)
- [Running the Code](#running-the-code)
- [Statistics and Data](#statistics-and-data)


## Installation
1. Clone down this repository
1. Set or create an environment variable called `OPENAI_API_KEY` that contains your OpenAI API key
1. Run `pip install openai`
1. (optional) Update the model parameter used in `src/QueryGPT.py` as desired. `gpt-3.5-turbo` is the cheapest recommended model for this system, but `gpt-4` based models may give better performance. Please refer to [OpenAI's official docs](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) for more information.
1. (optional) Adjust the response temperature parameter in `src/QueryGPT.py` to encourage more or less creative responses from the model. This parameter is on a scale from 0-2, with lower values being more dependable and strictly generated, and higher values being more creative and randomly generated. NOTE: 1.0 is the default value, with values over ~1.5 being known to often begin returning nonsense.

## Running the Code
Usage: `python ./main.py`.

When the code is run, the following will happen:

1. The user is prompted for a question. **Here, input the free-response question that will be given to students.**
1. Next the user is prompted for a question id - **input the id of the question** (to be used when saving data to disk). A new id will create the relevant files, whereas an existing id will append to the relevant files.
1. Using that data, a GPT model is queried and many student responses are simulated; some correct, others incorrect.
1. Next, each response is presented and graded by the user.  **Type "C" or "Correct" to mark the response as correct, and "I" or "Incorrect" to mark the response as incorrect.**
1. Statistics are recorded for how often the GPT model correctly labeled the provided responses. These statistics are reported for both the session and overall lifetime of the program.
1. Finally, the generated response data is saved to file in the `output` directory, and is now available for use in NLP models.

## Statistics and Data
Lifetime statistics about GPT labeling are stored in `lifetime_stats.csv`. This file is created after the first run.

Simulated response text data is generated in the `output` directory. This directory is created after the first run, and will contain the questions asked, the responses generated, and the scores assigned to each response.
