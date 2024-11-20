# Suart
"Suart is a chatbot designed to analyze your text files. You can input a file and ask questions about specific keywords from the content. Suart will provide the most relevant answers based on the text."
# Setup
To import the necessary packages into your local environment and ensure they are available in your .venv (virtual environment), you need to follow these steps:
1. Create a Virtual Environment (if you haven't already):
   Open your terminal and navigate to your project directory. Then create a virtual environment by running:
<img width="682" alt="Screenshot 2024-11-20 at 9 49 23 AM" src="https://github.com/user-attachments/assets/dabd10d4-9239-4560-8bdf-1fb54d95f8fb">

2. Activate the Virtual Environment:
   After creating the virtual environment, activate it. The command differs based on your operating system:

On Windows:

<img width="682" alt="Screenshot 2024-11-20 at 9 51 43 AM" src="https://github.com/user-attachments/assets/530294ea-bc53-4f01-a7aa-bac2f736da01">

<img width="697" alt="Screenshot 2024-11-20 at 9 54 12 AM" src="https://github.com/user-attachments/assets/3498fcae-a38b-4103-83d9-1cebef165a6e">

Note: You might require to install some extra library features like 'punkt', Just give a command, 

<img width="669" alt="Screenshot 2024-11-20 at 9 59 35 AM" src="https://github.com/user-attachments/assets/c5d1004c-6694-4cfb-8712-8dca87773744">

# Run the program
1. Once everything is setup then, go to terminal

<img width="671" alt="Screenshot 2024-11-20 at 10 03 58 AM" src="https://github.com/user-attachments/assets/2809605e-c126-4b12-8ae0-45a84a6dc5e6">

2. Access your application:
   
Open your web browser and navigate to http://127.0.0.1:5000/asking . You should see your chatbot interface. When you type a message and click "Send", it will send the input to the Flask backend, which will process it and return a response to be displayed in the chatbox.

# How the Code Works 🚀
1. Data File: The Data.txt file contains human-readable text data that serves as the foundation for the project.

2. Main Code: The entire functionality is encapsulated in the main.py file, which drives the project.

3. API Setup: Flask is used to create a simple API, making it easy to interact with the backend.

4. API Endpoint: The primary route, http://127.0.0.1:5000/asking, triggers the process. Upon accessing this route, the Data.txt file is read and processed into tokens.

6. Tokenization: Using NLTK, the text data is split into unique word tokens, which enable efficient searching.

6. User Interaction: A web template, created with HTML, is displayed to the user.
The HTML file includes a script to collect user input and send a GET request to a secondary API endpoint.

7. Search Endpoint: The route http://127.0.0.1:5000/question/<str> accepts user input as a string. It searches the Data.txt file for the first occurrence of the input token and returns the corresponding statement.

8. Output: The matched statement is displayed to the user. 🎉

Happy Coding! 💻
