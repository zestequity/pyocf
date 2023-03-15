"""Type represention of an ISO-8601 date, e.g. 2022-01-28"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/types/Date.schema.json

from datetime import date
from pyocf.simplebase import SimpleBaseModel


class Date(SimpleBaseModel):
    """Type represention of an ISO-8601 date, e.g. 2022-01-28"""

    __root__: date