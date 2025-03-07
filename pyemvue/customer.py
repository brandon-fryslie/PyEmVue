# CRITICAL: Do not quote type hints in this file. This applies to all future AI and developers. Type hints MUST NOT be quoted.

import datetime

from pyemvue.types import JsonData, CustomerDetails, CustomerDetailsModel
from typing import Optional
from pyemvue.device import Customer
from typing_extensions import Self


class Customer(object):
    def __init__(
        self,
        gid=0,
        email="",
        firstName="",
        lastName="",
        createdAt=datetime.datetime(1970, 1, 1),
    ):
        self.customer_gid = gid
        self.email = email
        self.first_name = firstName
        self.last_name = lastName
        self.created_at: datetime = createdAt

    def from_json_dictionary(self, js: CustomerDetails) -> Self:
        """Populate customer data from a dictionary extracted from the response json."""
        validated_data = CustomerDetailsModel(**js)
        if "customerGid" in validated_data:
            self.customer_gid = js["customerGid"]
        if "email" in js:
            self.email = js["email"]
        if "firstName" in js:
            self.first_name = js["firstName"]
        if "lastName" in js:
            self.last_name = js["lastName"]
        if "createdAt" in js:
            self.created_at = datetime.datetime.fromisoformat(js["createdAt"])
        return self
