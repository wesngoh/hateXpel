# hateXpel: Hate Speech Classifier

This repository contains a Streamlit app demonstrating the use of Retrieval Augmented Generation (RAG) to classify hate speech.

The classifier provides an explanation for its reasoning and identifies the potential core and sub identity groups attacked in the speech.

**Trigger Warning:** Demonstration contains offensive language, profanities and other potentially distressing content.

## Preview
https://github.com/user-attachments/assets/21b03257-a755-4ab4-87e6-5d8e45a5160a


## Installation
To install and run the demo app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/wesngoh/hateXpel.git
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run home.py
    ```

## Usage
Once the app is running, open your web browser and navigate to `http://localhost:8501`. You can input text into the provided text box, and the app will classify the text as either hate speech or not hate speech.
