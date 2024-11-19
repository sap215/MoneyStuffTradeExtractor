from simplegmail import Gmail
from simplegmail.query import construct_query
import openai

# OpenAI API key
openai.api_key = 'your_openai_api_key'

# Gmail API connection
gmail = Gmail() # This will open a browser window asking you to log in to your Gmail account

# Define a function to generate a chat prompt using ChatGPT (which takes a prompt as an input)
def generate_chat_prompt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini", # The 'gpt-4o-mini' model is $0.150/1M input tokens, you can choose whichever model you want (link to pricing: https://openai.com/api/pricing/)
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define the query parameters to search for unread emails from 'noreply@news.bloomberg.com'
query_params = {
    'sender': 'email-address', # Change this to the email address you want to read emails from
    "unread": True
}

# Get the messages that match the query parameters (should only be one)
messages = gmail.get_messages(query=construct_query(query_params))

# Extract the email content and generate a prompt for ChatGPT
extracted_prompt = "Give me an overview of the potential trading strategies that are discussed in the following email. Focus on potential systematic strategies, i.e., strategies that I can automate and build trading algorithms (e.g., stat arb, hft, etc) out of " + "\n" + messages[0].plain

# Generate a response using ChatGPT
chatGPT_output = generate_chat_prompt(extracted_prompt)

# Email subject (to myself)
email_subject = "Trade Ideas From " + messages[0].subject

# Send an email to myself with the content of the the ChatGPT output
gmail.send_message(
    sender='your_gmail_address',
    to='your_gmail_address',
    subject=email_subject,
    msg_plain=chatGPT_output
)

# Mark the Money Stuff email as read
messages[0].mark_as_read()