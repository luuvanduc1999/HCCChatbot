
from typing import Any, Text, Dict, List

from pathlib import Path
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted 
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import SlotSet
import sqlite3
import random
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
import regex

client = MongoClient("mongodb+srv://luuvanduc:poiu1234@chathear.zkuk0.mongodb.net/chatbot?retryWrites=true&w=majority")
db = client.test
db = client['chat_bot']
collection_registry = db['registry']


class ActionSaveFormDLSH(Action):

    def name(self) -> Text:
        return 'action_save_form_dienlucvn_sinhhoat'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Any]:

        try:
            coll_name = ''
            document_data = {}

            for turn, event in enumerate(reversed(tracker.events)):
                name = event.get('name')
                # Check only for the latest form
                coll_name = 'bookings'
                document_data.update(tracker.slots)
                del document_data["requested_slot"]
                del document_data["session_started_metadata"]
                document_data["type"]="dienlucvn_sinhhoat"
            # Insert into DB only if recent and valid form was found
            if coll_name:
                print(document_data)
                collection_registry.insert_one(document_data)
                dispatcher.utter_message(text=f"Đăng ký thành công!" )
        
        except Exception:
            pass
        
        finally:
            return [AllSlotsReset()]
class ActionSaveFormBLX(Action):

    def name(self) -> Text:
        return 'action_save_form_gtvt_capmoibanglai'

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Any]:

        try:
            coll_name = ''
            document_data = {}

            for turn, event in enumerate(reversed(tracker.events)):
                name = event.get('name')
                # Check only for the latest form
                coll_name = 'bookings'
                document_data.update(tracker.slots)
                del document_data["requested_slot"]
                del document_data["session_started_metadata"]
                document_data["type"]="gtvt_capmoibanglai"
            # Insert into DB only if recent and valid form was found
            if coll_name:
                print(document_data)
                collection_registry.insert_one(document_data)
                dispatcher.utter_message(text=f"Đăng ký thành công!" )
        
        except Exception:
            pass
        
        finally:
            return [AllSlotsReset()]            

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Xin lỗi, tôi chưa hiểu ý bạn. Bạn có thể nói lại được không ?")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]