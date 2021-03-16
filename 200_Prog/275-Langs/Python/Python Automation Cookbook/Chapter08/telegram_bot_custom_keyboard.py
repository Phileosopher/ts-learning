import time
import telepot
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space

from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '<YOUR TOKEN>'


# Define the information to return per command
def get_help():
    msg = '''
    Use one of the following commands:
        help: To show this help
        offers: To see this week offers
        events: To see this week events
    '''
    return msg


def get_offers():
    msg = '''
    This week enjoy these amazing offers!
        20% discount in beach products
        15% discount if you spend more than €50
    '''
    return msg


def get_events():
    msg = '''
    Join us for an incredible party the Thursday in our Sun City shop!
    '''
    return msg


COMMANDS = {
    'help': get_help,
    'offers': get_offers,
    'events': get_events,
}

# Create a custom keyboard with only the valid responses
keys = [[KeyboardButton(text=text)] for text in COMMANDS]
KEYBOARD = ReplyKeyboardMarkup(keyboard=keys)


class MarketingBot(telepot.helper.ChatHandler):

    def open(self, initial_msg, seed):
        self.sender.sendMessage(get_help(), reply_markup=KEYBOARD)
        # prevent on_message() from being called on the initial message
        return True

    def on_chat_message(self, msg):
        # If the data sent is not test, return an error
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type != 'text':
            self.sender.sendMessage("I don't understand you. "
                                    "Please type 'help' for options",
                                    reply_markup=KEYBOARD)
            return

        # Make the commands case insensitive
        command = msg['text'].lower()
        if command not in COMMANDS:
            self.sender.sendMessage("I don't understand you. "
                                    "Please type 'help' for options",
                                    reply_markup=KEYBOARD)
            return

        message = COMMANDS[command]()
        self.sender.sendMessage(message, reply_markup=KEYBOARD)

    def on__idle(self, event):
        self.close()


# Create and start the bot
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MarketingBot, timeout=10),
])
MessageLoop(bot).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
