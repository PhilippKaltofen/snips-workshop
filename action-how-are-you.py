#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import random

INTENT_HOW_ARE_YOU = "PhilippKaltofen:how_are_you"
INTENT_GOOD = "PhilippKaltofen:feeling_good"
INTENT_BAD = "PhilippKaltofen:feeling_bad"
INTENT_ALRIGHT = "PhilippKaltofen:feeling_average"

INTENT_FILTER_FEELING = [INTENT_GOOD, INTENT_BAD, INTENT_ALRIGHT]


def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .subscribe_intent(INTENT_GOOD, feeling_good_callback) \
         .subscribe_intent(INTENT_BAD, feeling_bad_callback) \
         .subscribe_intent(INTENT_ALRIGHT, feeling_alright_callback) \
         .start()

response_variation = ["Mir geht es nicht gut. ", "Mir gehts scheiße. Schau doch mal aus dem Fenster. "]
response_snips = "Und dir?"
response_good = ["Schoen fuer dich.", "Wenigstens einem", "Na dann...", "Wer - hat gefragt?", "Coole Story."]
response_bad = ["Ach echt, dir auch?", "Was ne Überraschung.", "Dann sind wir schon zwei."]
response_alright = ["Okay.", "Wie bitte?"]

def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = response_variation[random.randint(0, len(response_variation) -1)] + response_snips
    hermes.publish_continue_session(session_id, response, INTENT_FILTER_FEELING)


def feeling_good_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = response_good[random.randint(0, len(response_good) -1)]
    hermes.publish_end_session(session_id, response)


def feeling_bad_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = response_bad[random.randint(0, len(response_bad) -1)]
    hermes.publish_end_session(session_id, response)


def feeling_alright_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = response_alright[random.randint(0, len(response_alright) -1)]
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
