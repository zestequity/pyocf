"""Type representation of automatic trigger on a tive or condition."""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/types/conversion_triggers/AutomaticConversionOnConditionTrigger.
# schema.json

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
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class AutomaticConversionOnConditionTrigger(ConversionTrigger):
    """Type representation of automatic trigger on a tive or condition."""

    # Legal language describing what conditions must be satisfied for the conversion
    # to take place (ideally, this should be excerpted from the instrument where
    # possible)
    trigger_condition: str
    # Id for this conversion trigger, unique within list of ConversionTriggers in
    # parent convertible issuance's `conversion_triggers` field.
    trigger_id: str
    # Human-friendly nickname to describe the conversion right
    nickname: Optional[str]
    # Long-form description of the trigger
    trigger_description: Optional[str]
    type: Literal["AUTOMATIC_ON_CONDITION"] = "AUTOMATIC_ON_CONDITION"
    # When the conditions of the trigger are met, how does the convertible convert?
    conversion_right: Annotated[
        Union[
            ConvertibleConversionRight,
            WarrantConversionRight,
            StockClassConversionRight,
        ],
        Field(discriminator="type"),
    ]
