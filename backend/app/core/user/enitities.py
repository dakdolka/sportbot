from dataclasses import dataclass, field
from typing import Any, Optional, List, Text
from .enums import Sex

@dataclass
class User:
    tg_id: str
    id: Optional[int] = None
    
@dataclass
class User_AI_info:
    sex: Sex
    height: int
    weight: int
    equipment: Text
    data_reachable: Text
    u_id: Optional[int] = None
    id: Optional[int] = None
    ...


@dataclass
class User_statistics:
    u_id: Optional[int] = None
    id: Optional[int] = None
    ...