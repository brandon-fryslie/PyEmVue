import datetime
from typing import Dict, Union
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
        self.created_at = createdAt

    def from_json_dictionary(self, js: Dict[str, Union[str, int, float, bool, None]]) -> Self:
        """Populate customer data from a dictionary extracted from the response json."""
        if "customerGid" in js:
            self.customer_gid = js["customerGid"]
        if "email" in js:
            self.email = js["email"]
        if "firstName" in js:
            self.first_name = js["firstName"]
        if "lastName" in js:
            self.last_name = js["lastName"]
        if "createdAt" in js:
            self.created_at = js["createdAt"]
        return self
