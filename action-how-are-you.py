#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import random

INTENT_HOW_ARE_YOU = "PhilippKaltofen:how_are_you"


def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .start()

responses = ["I'm not doing great", "I'm very well, thank you.", "Nice Bro, as always.", "What do you think?", "Dude, look at me.", "Please kill me."]

def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = responses[random.randint(0, len(responses))]
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
