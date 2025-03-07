from typing import Dict, Union, List, Tuple, Optional, TYPE_CHECKING
from pyemvue.models import CustomerDetailsModel
from datetime import datetime
from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from pyemvue.device import VueUsageDevice, OutletDevice, ChargerDevice
JsonData: TypeAlias = Dict[str, Union[str, int, float, bool, None, Dict, List]]
CustomerDetails: TypeAlias = Dict[str, Union[int, str, datetime]]
DeviceResponse: TypeAlias = Dict[str, Union[int, str, List[Dict[str, Union[str, int, float, bool, None]]]]]
OutletResponse: TypeAlias = List[Dict[str, Union[int, bool, Optional[int], Optional[str]]]]
ChargerResponse: TypeAlias = List[Dict[str, Union[int, str, bool, Optional[int]]]]
AuthTokens: TypeAlias = Dict[str, str]
DeviceUsageMap: TypeAlias = Dict[int, VueUsageDevice]
UsageDataWithTimestamp: TypeAlias = Tuple[List[float], Optional[datetime]]
DeviceStatus: TypeAlias = Tuple[List[OutletDevice], List[ChargerDevice]]
