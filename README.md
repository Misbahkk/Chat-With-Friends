
# ChatWithFriends

ChatWithFriends is a Django project that allows users to create accounts and chat with their friends in real-time. It utilizes Python, JavaScript, CSS, HTML, and JSON to create a seamless chatting experience.


## Screenshots

<img width="866" alt="chatFriends" src="https://github.com/Misbahkk/Chat-With-Friends/assets/107263622/870b4b90-e021-4197-a1cf-6fa00b3b39ba">

## Features

- Friend List: Each user has a friend list where they can view their friends and initiate chats.
- Real-time Messaging: Users can send and receive messages from their friends in real-time without page refresh.
- Fullscreen mode
- Message History: Chat conversations are stored, allowing users to view their chat history.


## Technologies Used

- Python: The back-end of the project is developed using Python, specifically the Django framework.
- JavaScript: JavaScript is used for client-side scripting to handle real-time messaging and user interactions
- CSS: Cascading Style Sheets are used to enhance the visual appeal and layout of the web pages.
- JSON: JSON (JavaScript Object Notation) is used to transfer data between the client and server.
## Installation

To run the ChatWithFriends project on your local machine, follow these steps:

1. Ensure that Python is installed on your system. You can download the latest version of Python from the official website: `https://www.python.org/downloads/`
2. Clone the project repository using Git or download it as a ZIP file and extract it to a local directory.
3. Open a terminal or command prompt and navigate to the project's root directory
4. Install the project dependencies from the `requirements.txt` file:
```bash
  pip install -r requirements.txt

```
    
5. Set up the database:
- Configure the database settings in the `settings.py` file located in the `chatWithFriends` directory. Specify the database engine, name, user, password, etc., according to your preferences.
- Run the following command to apply the migrations and create the necessary tables:
```bash
python manage.py migrate
```
6. Start the development server:
```bash
python manage.py runserver
```
7. Access the application by visiting `http://localhost:8000` in your web browser.

## License

[MIT](https://choosealicense.com/licenses/mit/)

