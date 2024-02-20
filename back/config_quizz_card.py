from typing import List, Dict
from card_data import card_data  # Import card_data
from card_quizz import list_card_by_frequency

def currentCards() -> List[Dict]:
        quizzCards = []
        for card_info in list_card_by_frequency:
            if card_info["day"] == 0:
                card_id = card_info["id"]
                for card in card_data:
                    if card["id"] == card_id:
                        quizzCards.append(card)
                        break  # Stop searching once the card is found
            else : 
                card_info["day"] = card_info["day"] - 1
        return quizzCards