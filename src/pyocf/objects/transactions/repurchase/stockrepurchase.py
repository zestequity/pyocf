"""Object describing a stock repurchase transaction"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/objects/transactions/repurchase/StockRepurchase.schema.json

from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.repurchase.repurchase import Repurchase
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.monetary import Monetary
from pyocf.types.numeric import Numeric
from typing import Literal
from typing import Optional


class StockRepurchase(Object, Transaction, SecurityTransaction, Repurchase):
    """Object describing a stock repurchase transaction"""

    object_type: Literal["TX_STOCK_REPURCHASE"] = "TX_STOCK_REPURCHASE"
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
    # Repurchase price per share of the stock
    price: Monetary
    # Number of shares of stock repurchased
    quantity: Numeric
    # Unstructured text description of consideration provided in exchange for security
    # repurchase
    consideration_text: Optional[str]
    # Identifier for the security that holds the remainder balance (for partial
    # repurchases)
    balance_security_id: Optional[str]
