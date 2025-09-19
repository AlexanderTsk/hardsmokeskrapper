from typing import Dict

class AttributeGroupAdapter:
    
    def __init__(self):
        self.group_mapping: dict[str, str] = {
            "Смак (відтінок)": "Відтінок",
            "Смак (міксологія)": "Міксологія",  
        }

    def adapt(self, external_value: str) -> str | None:
        return self.group_mapping.get(external_value, external_value)


class AttributeAdapter:
   
    def __init__(self):
        self.attribute_mapping: dict[str, str] = {
            "0": "Низька",
            "1": "Низька", 
            "2": "Середня", 
            "3": "Середня", 
            "4": "Висока",  
            "5": "Висока", 
            "Легкий": "Низька",
            "Середній": "Середня", 
            "Міцний": "Висока", 
        }

    def adapt(self, external_value: str) -> str | None:
        return self.attribute_mapping.get(external_value, external_value)
