"""Type representation of an ISO 3166-1 alpha 2 country code"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/types/CountryCode.schema.json

from pydantic import constr
from pyocf.simplebase import SimpleBaseModel


class CountryCode(SimpleBaseModel):
    """Type representation of an ISO 3166-1 alpha 2 country code"""

    __root__: constr(regex=r"^[A-Z]{2}$")
