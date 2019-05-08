#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import random

INTENT_AUFMUNTERN = "PhilippKaltofen:muntere_auf"
INTENT_CHECK = "PhilippKaltofen:skala_check"

def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_AUFMUNTERN, aufmuntern_callback) \
         .subscribe_intent(INTENT_CHECK, check_callback) \
         .start()

response_aufmuntern = "Na klar. Auf einer Skala von 1 bis 10, wenn 1 das schlechteste ist. Wie ist deine Laune?"
response_aufmuntern_weiter = "Wie ist jetzt deine Laune?"
witze = ["Alle beschweren sich wegen dem Wetter, außer Germanistik-Studenten. Die beschwerden sich wegen des Wetters.", "Warum sind Blondinenwitze so kurz? Damit auch Maenner sie verstehen.", "Warum trinken Maeuse keinen Alkohol. Weil sie Angst vor dem Kater haben."]
laune = ""
iteration = 0

def aufmuntern_callback(hermes, intent_message):
    session_id = intent_message.session_id
    if iteration == 0:
        response = response_aufmuntern
    else
        response = response_aufmuntern_weiter
    iteration+=1
    hermes.publish_continue_session(session_id, response, INTENT_CHECK)

def check_callback(hermes, intent_message):
    laune = intent_message.laune
    if laune > 8:
        response = "Okay, dann brauchst du mich ja gar nicht mehr."
    else
        response = "Gut, ich erzaehle dir einen Witz. " + witze(random.randint(0, len(witze) - 1))
    hermes.publish_continue_session(session_id, response, INTENT_AUFMUNTERN)