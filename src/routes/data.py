from fastapi import FastAPI ,APIRouter,Depends,UbloadFile
from helpers.config import get_settings,Settings
from controllers import DateController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1/data"]
)
@data_router.post("/upload/{project_id}")

async def ubload_data (project_id: str, file: UbloadFile ,
                       app_settings: Settings =Depends(get_settings)):
    
    is_valid = DateController().validate_ubloaded_file(file=file)
    
    return is_valid