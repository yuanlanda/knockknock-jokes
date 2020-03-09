# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import random

JOKES = [("Doctor", "🤪😂"),
         ("Deja", "Knock-knock"),
         ("Robin", "Robin you, now hand over the cash."),
         ("Opportunity", "That is impossible. Opportunity doesn’t come knocking twice!"),
         ("Doris", "Dorisopen, so I thought I'd drop by!")]


class ActionJokeSetup(Action):

    def name(self) -> Text:
        return "action_joke_setup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if len(JOKES) == 0:
            dispatcher.utter_message(text="Sorry, I have no joke now 😂")

            return
        else:
            jix = random.choice(range(len(JOKES)))

            dispatcher.utter_message(text=JOKES[jix][0])

            return [SlotSet("jix", jix)]


class ActionJokePunchline(Action):

    def name(self) -> Text:
        return "action_joke_punchline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if len(JOKES) == 0:
            dispatcher.utter_message(text="Sorry, I have no joke now 😂")
        else:
            jix = int(tracker.get_slot("jix"))
            joke = JOKES[jix]
            dispatcher.utter_message(text=joke[1])

            JOKES.pop(jix)


        return []
