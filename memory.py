conversation_history = []


def add_memory(user, assistant):

    conversation_history.append(
        {
            "user": user,
            "assistant": assistant
        }
    )


def get_memory():

    return conversation_history