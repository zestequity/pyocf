"""Object describing a re-issuance of stock"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/objects/transactions/reissuance/StockReissuance.schema.json

from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.reissuance.reissuance import Reissuance
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from typing import Literal
from typing import Optional


class StockReissuance(Object, Transaction, SecurityTransaction, Reissuance):
    """Object describing a re-issuance of stock"""

    object_type: Literal["TX_STOCK_REISSUANCE"] = "TX_STOCK_REISSUANCE"
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
    # Identifier of the new security (or securities) issuance resulting from a
    # reissuance
    resulting_security_ids: list[str]
    # When stock is reissued as a result of a stock split, this field contains id of
    # the respective stock class split transaction. It is not set otherwise.
    split_transaction_id: Optional[str]
    # Free-form human-readable reason for stock reissuance
    reason_text: Optional[str]
