"""Type representation of an automatic trigger on a date."""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/types/conversion_triggers/AutomaticConversionOnDateTrigger.schem
# a.json

from pydantic import Field
from pyocf.primitives.types.conversion_triggers.conversiontrigger import (
    ConversionTrigger,
)
from pyocf.types.conversion_rights.convertibleconversionright import (
    ConvertibleConversionRight,
)
from pyocf.types.conversion_rights.stockclassconversionright import (
    StockClassConversionRight,
)
from pyocf.types.conversion_rights.warrantconversionright import WarrantConversionRight
from pyocf.types.date import Date
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class AutomaticConversionOnDateTrigger(ConversionTrigger):
    """Type representation of an automatic trigger on a date."""

    # Date on which trigger occurs automatically (if it hasn't already occured)
    trigger_date: Date
    # Id for this conversion trigger, unique within list of ConversionTriggers in
    # parent convertible issuance's `conversion_triggers` field.
    trigger_id: str
    # Human-friendly nickname to describe the conversion right
    nickname: Optional[str]
    # Long-form description of the trigger
    trigger_description: Optional[str]
    type: Literal["AUTOMATIC_ON_DATE"] = "AUTOMATIC_ON_DATE"
    # When the conditions of the trigger are met, how does the convertible convert?
    conversion_right: Annotated[
        Union[
            ConvertibleConversionRight,
            WarrantConversionRight,
            StockClassConversionRight,
        ],
        Field(discriminator="type"),
    ]
