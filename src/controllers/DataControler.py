from .BaseControler import BaseControler
from fastapi import UbloadFile

class DataControler(BaseControler):
    
    def __init__(self):
        
        super().__init__()
        self.size_scale = 1048576 
        
    def validate_ubloaded_file(self, file: UbloadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        
        if file.size > self.app_settings.FILE_MAX_SIZE:
            return False
        
        return False