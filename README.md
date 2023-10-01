# Intelligent Chatbot for Question-Answering

This Python-based chatbot is designed to answer questions using a provided CSV dataset. It incorporates natural language processing libraries to enhance its intelligence. To use this chatbot, follow these steps:

## Project Workflow

1. **Reading the CSV File**: The chatbot starts by reading a CSV file that contains questions and their corresponding answers.

2. **Lemmatizing the Data**: The text data undergoes lemmatization to remove unnecessary word endings and retain meaningful base forms. This ensures that the chatbot considers the main words in questions.

3. **Creating a Spell Checker Training Model**: A custom spell checker model is created using the TextBlob Spelling Python library. This is necessary because standard spell checkers may not recognize specialized words. The custom dataset improves the bot's spelling correction capabilities.

4. **Vectorizing the Questions Data**: To process text data, it needs to be converted into a format that the machine can understand. In this chatbot, text data is transformed into vectors of 0s and 1s. This is achieved using the TfidfVectorizer library from sklearn, which also considers stop words.

5. **Finding the Correct Answer (After Correcting Spelling)**: The chatbot checks for spelling mistakes in user input. If a mistake is detected, it prompts the user for confirmation. The user can respond with "yes" to get the corrected answer or "no" to rephrase the question. Similar processing occurs if the user's question is slightly different from the available questions in the dataset.

6. **Cosine Similarity**: To find the correct answer, the chatbot calculates the cosine similarity between the vectorized user input and the vectorized questions in the dataset. The resulting matrix is flattened into a single array.

7. **Shutting Down the Bot**: If the user wishes to exit the conversation, they can simply type "bye."

## Steps to Run the Chatbot

Follow these steps to run the chatbot:

1. **Install Required Libraries**: Make sure you have the necessary libraries installed in your Python environment. You can install them using `pip`:

   ```bash
   pip install pandas scikit-learn textblob numpy regex
   ```

2. **Clone the Chatbot Repository**: Clone the chatbot repository to your local machine.

   ```bash
   git clone <repository_url>
   ```

3. **Navigate to the Chatbot Directory**: Change your current working directory to the chatbot project directory.

   ```bash
   cd chatbot_project_directory
   ```

4. **Update Training Data File Path**: Open the Python script and locate the `File_path` variable. Replace the value with the path to your training data CSV file. This file should contain the dataset that the chatbot will use for answering questions.

5. **Specify Spell Checker Model File Path**: In the script, locate the `model_file_path` variable. Update it with the path to your trained spell checker model file.

6. **Run the Program**: Launch the chatbot program in a Python environment by executing the script.

   ```bash
   python chatbot.py
   ```

7. **Ask Questions**: You can now interact with the chatbot by asking questions. Keep in mind that the questions should consist of more than one keyword to receive meaningful answers.

8. **Exiting the Chatbot**: To exit the chatbot, simply type "bye."

## Conclusion

In summary, this chatbot is an intelligent tool capable of providing possible correct answers based on the provided dataset. It possesses the ability to correct word mistakes and confirm user questions if they deviate from the available dataset. This makes it a valuable tool for answering questions and providing information from a structured dataset.

Feel free to explore and further enhance this chatbot according to your needs. If you have any questions or suggestions, please don't hesitate to reach out. Enjoy using this intelligent chatbot!
