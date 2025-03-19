from functions.chat import init_client, start_chat, add_chat_message, add_assistant_chat_message

if __name__ == "__main__":
    # init
    client = init_client()
    start_chat()
    print(f" - Note: write 'exit' to finish chat")

    message = input("\n - Add message: ")
    while message != 'exit':
        # user message
        response = add_chat_message(client, message)
        print(f"\n - response: {response}")
        # add assistant feedback
        add_assistant_chat_message(response)
        # ask again to continue or exit
        message = input("\n - Add message: ")


