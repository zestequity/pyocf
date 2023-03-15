"""Type representation of a primary contact person for a stakeholder (e.g. a fund)"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/types/ContactInfo.schema.json

from pydantic import BaseModel
from pyocf.types.email import Email
from pyocf.types.name import Name
from pyocf.types.phone import Phone


class ContactInfo(BaseModel):
    """Type representation of a primary contact person for a stakeholder (e.g. a fund)"""

    # Contact's name
    name: Name
    # Phone numbers to reach the contact at
    phone_numbers: list[Phone]
    # Emails to reach the contact at
    emails: list[Email]