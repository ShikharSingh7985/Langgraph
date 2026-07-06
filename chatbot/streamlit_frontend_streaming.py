import streamlit as st
from chat_backend import chatbot
from langchain_core.messages import HumanMessage

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # first add the message to message_history
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    
    
    
    
    
    
    
    
    
    

  
# Overall Intuition:
# - This code creates a Streamlit chatbot UI.
# - It imports a chatbot backend from another file.
# - It stores chat history inside st.session_state so messages remain visible after rerun.
# - First, it displays all previous messages from session history.
# - Then it takes new user input using st.chat_input().
# - If the user enters a message, it shows the user message on screen.
# - Then it sends that message to the backend chatbot using streaming.
# - The assistant response is streamed live on the Streamlit page.
# - Finally, both user and assistant messages are saved in session history.
# """

# import streamlit as st  # Imports Streamlit library for building the web app UI
# from chat_backend import chatbot  # Imports chatbot object/function from the chat_backend.py file
# from langchain_core.messages import HumanMessage  # Imports HumanMessage class to represent user's message in LangChain format

# # st.session_state -> dict ->  # st.session_state behaves like a dictionary and stores data across Streamlit reruns
# CONFIG = {'configurable': {'thread_id': 'thread-1'}}  # Creates a config dictionary with a fixed thread_id to maintain conversation thread

# if 'message_history' not in st.session_state:  # Checks whether message_history key is not already present in session_state
#     st.session_state['message_history'] = []  # Creates an empty list to store chat messages if it does not exist

# # loading the conversation history  # This section displays previously stored messages on the page
# for message in st.session_state['message_history']:  # Loops through every saved message in message_history
#     with st.chat_message(message['role']):  # Creates a chat bubble based on message role like user or assistant
#         st.text(message['content'])  # Displays the content/text of that saved message

# #{'role': 'user', 'content': 'Hi'}  # Example format of a user message stored in message_history
# #{'role': 'assistant', 'content': 'Hi=ello'}  # Example format of an assistant message stored in message_history

# user_input = st.chat_input('Type here')  # Creates a chat input box and stores user's typed message

# if user_input:  # Runs this block only when the user enters some text

#     # first add the message to message_history  # This section stores and displays the user's latest message
#     st.session_state['message_history'].append({'role': 'user', 'content': user_input})  # Adds user's message to session history
#     with st.chat_message('user'):  # Creates a user chat bubble in the UI
#         st.text(user_input)  # Displays the user's input message

#     # first add the message to message_history  # This section generates and displays assistant response
#     with st.chat_message('assistant'):  # Creates an assistant chat bubble in the UI

#         ai_message = st.write_stream(  # Streams the assistant response on screen and stores final response text
#             message_chunk.content for message_chunk, metadata in chatbot.stream(  # Takes only content from each streamed message chunk
#                 {'messages': [HumanMessage(content=user_input)]},  # Sends the current user input to chatbot in LangChain message format
#                 config= {'configurable': {'thread_id': 'thread-1'}},  # Passes thread_id config so chatbot can maintain conversation context
#                 stream_mode= 'messages'  # Tells chatbot to stream output as message chunks
#             )
#         )

#     st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})  # Saves assistant's final response in session history
    
    
    
