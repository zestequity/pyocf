"""Fixed-point string representation of a number (up to 10 decimal places"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/types/Numeric.schema.json

from decimal import Decimal
from pyocf.simplebase import SimpleBaseModel


class Numeric(SimpleBaseModel):
    """Fixed-point string representation of a number (up to 10 decimal places
    supported)
    """

    __root__: Decimal