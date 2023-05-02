"""Type representation of a conversion right from a convertible into another non-"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/types/conversion_rights/WarrantConversionRight.schema.json

from pydantic import Field
from pyocf.primitives.types.conversion_rights.conversionright import ConversionRight
from pyocf.types.conversion_mechanisms.customconversionmechanism import (
    CustomConversionMechanism,
)
from pyocf.types.conversion_mechanisms.fixedamountconversionmechanism import (
    FixedAmountConversionMechanism,
)
from pyocf.types.conversion_mechanisms.percentcapitalizationconversionmechanism import (
    PercentCapitalizationConversionMechanism,
)
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class WarrantConversionRight(ConversionRight):
    """Type representation of a conversion right from a convertible into another non-
    plan security
    """

    type: Optional[Literal["WARRANT_CONVERSION_RIGHT"]] = "WARRANT_CONVERSION_RIGHT"
    # What conversion mechanism applies to calculate the number of resulting stock
    # class shares?
    conversion_mechanism: Annotated[
        Union[
            CustomConversionMechanism,
            PercentCapitalizationConversionMechanism,
            FixedAmountConversionMechanism,
        ],
        Field(discriminator="type"),
    ]
    # Is this stock class potentially convertible into a future, as-yet undetermined
    # stock class (e.g. Founder Preferred)
    converts_to_future_round: Optional[bool]
    # The identifier of the existing, known stock class this stock class can convert
    # into
    converts_to_stock_class_id: Optional[str]
