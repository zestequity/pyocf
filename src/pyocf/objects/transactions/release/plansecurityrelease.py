"""Object describing a plan security release transaction"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/objects/transactions/release/PlanSecurityRelease.schema.json

from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.release.release import Release
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from typing import Literal
from typing import Optional


class PlanSecurityRelease(Object, Transaction, SecurityTransaction, Release):
    """Object describing a plan security release transaction"""

    object_type: Literal["TX_PLAN_SECURITY_RELEASE"] = "TX_PLAN_SECURITY_RELEASE"
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
    # The settlement date for the shares released, typically after the release
    # transaction date
    settlement_date: Date
    # The release price used to determine the value of the security at the time of
    # release
    release_price: Monetary
    # Quantity of shares released
    quantity: Numeric
    # Unstructured text description of consideration provided in exchange for security
    # release
    consideration_text: Optional[str]
    # Identifier of the new security (or securities) issuance resulting from a release
    # transaction
    resulting_security_ids: list[str]
