class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_header, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param str message_header: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'header': message_header,
            'body': message_body,
            'sender': sender,
            'recipient': recipient,
            'is_read': False,

        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, N=None):
        """This method reads a user's inbox and returns a list of unread messages,
         up to a specified number. If N is not provided, all unread messages will be returned.

        :param user: A string representing the username of the user whose inbox is being read.
        :param N: An optional integer representing the maximum number of messages to return. If not provided, all
            unread messages will be returned.
        :return: A list of dictionaries, where each dictionary represents an unread message in the user's inbox.
        """
        if user not in self.boxes:
            return []

        messages = self.boxes[user]
        messages = messages if N is None else messages[:N]

        unread_messages = []
        for msg in messages:
            if not msg['is_read']:
                unread_messages.append(msg)
                msg['is_read'] = True

        return unread_messages

    def search_inbox(self, user, search_string):
        """
        This method searches a user's inbox for messages containing a specified string
        in either the message header or body. It returns a list of all matching messages.

        :param user: A string representing the username of the user whose inbox is being read.
        :param search_string: A string representing the text to search for in the message header or body.
        :return: A list of dictionaries, where each dictionary represents a message in the user's inbox that matches
        the search criteria.
        """
        if user not in self.boxes:
            return []

        messages = self.boxes[user]
        search_results = [msg for msg in messages if search_string in msg['header'] or search_string in msg['body']]

        return search_results


# Example usage
if __name__ == "__main__":
    # Create a PostOffice instance
    post_office = PostOffice(['Johnny', 'Jalen', 'Charlie'])

    # Users send messages to each other
    post_office.send_message("Johnny", "Jalen", "Hello Jalen", "How are you?")
    post_office.send_message("Jalen", "Johnny", "Re: Hello Jalen", "Hi Johnny, I'm doing well!")
    post_office.send_message("Johnny", "Jalen", "Meeting tomorrow", "Don't forget our meeting tomorrow at 10 AM.")
    post_office.send_message("Charlie", "Jalen", "Lunch", "Hey Jalen, want to grab lunch today?")
    post_office.send_message("Jalen", "Charlie", "Re: Lunch", "Sure, Charlie! Let's meet at noon.")

    # Jalen reads his inbox
    print('Jalen reads his box:')
    jalen_messages = post_office.read_inbox("Jalen", N=8)
    for msg in jalen_messages:
        print(f"{msg['sender']} -> {msg['recipient']}: {msg['header']}\n{msg['body']}\n")

    # Johnny searches his inbox for messages containing the string "Jalen"
    print('Johnny searches his inbox for messages containing the string "Jalen"')
    Johnny_search_results = post_office.search_inbox("Johnny", "Jalen")
    for msg in Johnny_search_results:
        print(f"{msg['sender']} -> {msg['recipient']}: {msg['header']}\n{msg['body']}\n")

    # Charlie reads all messages in his inbox
    print('Charlie reads all messages in his inbox:')
    charlie_messages = post_office.read_inbox("Charlie")
    for msg in charlie_messages:
        print(f"{msg['sender']} -> {msg['recipient']}: {msg['header']}\n{msg['body']}\n")
