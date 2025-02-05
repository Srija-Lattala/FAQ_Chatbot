# FAQ_Chatbot: Python Programming

## Description
This project is a simple FAQ chatbot built using **Streamlit** and **LangChain**. It answers common questions about Python programming by leveraging the **Google Gemini API**.

## Features
- Answers frequently asked questions about Python programming.
- Built using `Streamlit` for the user interface.
- Uses the `LangChain` library for prompt generation.
- Integrated with **Google Gemini API**.

## Installation
Follow these steps to run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/FAQ-Chatbot-Python.git
   cd FAQ-Chatbot-Python
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your API key:
   - Create a `.env` file in the project folder.
   - Add the following line:
     ```
     GOOGLE_API_KEY=your_actual_google_api_key
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## FAQ Data
The chatbot currently supports these questions:
- What is Python?
- How do I install Python?
- What are Python data types?
- What is a function in Python?
- What is a list in Python?

## Preview
![Chatbot Preview](assets/chatbot-preview.png)

## Future Enhancements
- Add more topics and FAQs.
- Improve answer quality with advanced APIs.
- Enhance UI design with CSS or Streamlit components.

## License
This project is licensed under the MIT License.
