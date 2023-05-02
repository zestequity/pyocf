"""Describes condition / triggers to be satisfied for vesting to occur"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/types/vesting/VestingCondition.schema.json

from pydantic import BaseModel
from pydantic import Field
from pyocf.types.numeric import Numeric
from pyocf.types.vesting.vestingconditionportion import VestingConditionPortion
from pyocf.types.vesting.vestingeventtrigger import VestingEventTrigger
from pyocf.types.vesting.vestingscheduleabsolutetrigger import (
    VestingScheduleAbsoluteTrigger,
)
from pyocf.types.vesting.vestingschedulerelativetrigger import (
    VestingScheduleRelativeTrigger,
)
from pyocf.types.vesting.vestingstarttrigger import VestingStartTrigger
from typing import Annotated
from typing import Optional
from typing import Union


class VestingCondition(BaseModel):
    """Describes condition / triggers to be satisfied for vesting to occur"""

    # Reference identifier for this condition
    id: str
    # Detailed description of the condition
    description: Optional[str]
    # If specified, the fractional part of the whole security that is vested, e.g.
    # 25:100 for 25%. Use `quantity` for a fixed vesting amount.
    portion: Optional[VestingConditionPortion]
    # If specified, the fixed amount of the whole security to vest, e.g. 10000 shares.
    # Use `portion` for a proportional vesting amount.
    quantity: Optional[Numeric]
    # Describes how this vesting condition is met, resulting in vesting the specified
    # tranche of shares
    trigger: Annotated[
        Union[
            VestingStartTrigger,
            VestingScheduleAbsoluteTrigger,
            VestingScheduleRelativeTrigger,
            VestingEventTrigger,
        ],
        Field(discriminator="type"),
    ]
    # List of ALL VestingCondition IDs that can trigger after this one. If there are
    # none, use an empty array.
    # Conditions should be in priority order in the array, ordered from the highest
    # priority to the lowest.
    next_condition_ids: list[str]
