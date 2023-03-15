"""Enumeration of types of conversion rights."""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/enums/ConversionRightType.schema.json

from enum import Enum


class ConversionRightType(Enum):
    """Enumeration of types of conversion rights."""

    ENUM_CONVERTIBLE_CONVERSION_RIGHT = "CONVERTIBLE_CONVERSION_RIGHT"
    ENUM_WARRANT_CONVERSION_RIGHT = "WARRANT_CONVERSION_RIGHT"
    ENUM_STOCK_CLASS_CONVERSION_RIGHT = "STOCK_CLASS_CONVERSION_RIGHT"