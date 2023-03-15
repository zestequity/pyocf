"""Object describing convertible instrument issuance transaction by the issuer and"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/objects/transactions/issuance/ConvertibleIssuance.schema.json

from pydantic import Field
from pyocf.enums.convertibletype import ConvertibleType
from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.issuance.issuance import Issuance
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.conversion_triggers.automaticconversiononconditiontrigger import (
    AutomaticConversionOnConditionTrigger,
)
from pyocf.types.conversion_triggers.automaticconversionondatetrigger import (
    AutomaticConversionOnDateTrigger,
)
from pyocf.types.conversion_triggers.electiveconversionatwilltrigger import (
    ElectiveConversionAtWillTrigger,
)
from pyocf.types.conversion_triggers.electiveconversionindaterangetrigger import (
    ElectiveConversionInDateRangeTrigger,
)
from pyocf.types.conversion_triggers.electiveconversiononconditiontrigger import (
    ElectiveConversionOnConditionTrigger,
)
from pyocf.types.conversion_triggers.unspecifiedconversiontrigger import (
    UnspecifiedConversionTrigger,
)
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from pyocf.types.securityexemption import SecurityExemption
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class ConvertibleIssuance(Object, Transaction, SecurityTransaction, Issuance):
    """Object describing convertible instrument issuance transaction by the issuer and
    held by a stakeholder
    """

    object_type: Literal["TX_CONVERTIBLE_ISSUANCE"] = "TX_CONVERTIBLE_ISSUANCE"
    # Amount invested and outstanding on date of issuance of this convertible
    investment_amount: Monetary
    # What kind of convertible instrument is this (of the supported, enumerated types)
    convertible_type: ConvertibleType
    # In event the convertible can convert due to trigger events (e.g. Maturity, Next
    # Qualified Financing, Change of Control, at Election of Holder), what are the
    # terms?
    conversion_triggers: list[
        Annotated[
            Union[
                AutomaticConversionOnConditionTrigger,
                AutomaticConversionOnDateTrigger,
                ElectiveConversionAtWillTrigger,
                ElectiveConversionInDateRangeTrigger,
                ElectiveConversionOnConditionTrigger,
                UnspecifiedConversionTrigger,
            ],
            Field(discriminator="type"),
        ]
    ]
    # What pro-rata (if any) is the holder entitled to buy at the next round?
    pro_rata: Optional[Numeric]
    # If different convertible instruments have seniorty over one another, use this
    # value to build a seniority stack, with 1 being highest seniority and equal
    # seniority values assumed to be equal priority
    seniority: int
    # Identifier for the object
    id: str
    # Unstructured text comments related to and stored for the object
    comments: Optional[list[str]]
    # Identifier for the security (stock, plan security, warrant, or convertible) by
    # which it can be referenced by other transaction objects. Note that while this
    # identifier is created with an issuance object, it should be different than the
    # issuance object's `id` field which identifies the issuance transaction object
    # itself. All future transactions on the security (e.g. acceptance, transfer,
    # cancel, etc.) must reference this `security_id` to qualify which security the
    # transaction applies to.
    security_id: str
    # Date on which the transaction occurred
    date: Date
    # A custom ID for this security (e.g. CN-1.)
    custom_id: str
    # Identifier for the stakeholder that holds legal title to this security
    stakeholder_id: str
    # Date of board approval for the security
    board_approval_date: Optional[Date]
    # Unstructured text description of consideration provided in exchange for security
    # issuance
    consideration_text: Optional[str]
    # List of security law exemptions (and applicable jurisdictions) for this security
    security_law_exemptions: list[SecurityExemption]