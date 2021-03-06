# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        facility = tracker.get_slot("facility_type")
        address = "12345 aramco dhahran"

        dispatcher.utter_message(text="Here is the address of the {}:{}".format(facility, address))

        return [SlotSet("address", address)]

class ActionApplicationSearch(Action):

    def name(self) -> Text:
        return "action_application_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        application = tracker.get_slot("application")
        address = "\\aramco.com\data\EASD"

        dispatcher.utter_message(text="Please run the following {} to install {}".format(address, application))

        return [SlotSet("address", address)]
