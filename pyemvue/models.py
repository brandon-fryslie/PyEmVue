from pydantic import BaseModel
from typing import Dict, Union, List, Optional
from datetime import datetime

class JsonDataModel(BaseModel):
    data: Dict[str, Union[str, int, float, bool, None, Dict, List]]

class CustomerDetailsModel(BaseModel):
    customerGid: int
    email: str
    firstName: str
    lastName: str
    createdAt: datetime
