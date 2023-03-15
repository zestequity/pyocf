"""Object describing the conversion ratio adjustment of a stock class that has a"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/main/schema/objects/transactions/adjustment/StockClassConversionRatioAdjustm
# ent.schema.json

from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.stockclasstransaction import (
    StockClassTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.conversion_mechanisms.ratioconversionmechanism import (
    RatioConversionMechanism,
)
from pyocf.types.date import Date
from typing import Literal
from typing import Optional


class StockClassConversionRatioAdjustment(Object, Transaction, StockClassTransaction):
    """Object describing the conversion ratio adjustment of a stock class that has a
    RatioConversionMechanism conversion mechanism where there was an actual
    repricing due to a down-round. The actual determination of the new conversion
    ratio / conversion price is calculated outside of OCF, so the specific mechanism
    - e.g. broad-based weighted-average anti-dilution protection vs. full ratchet
    anti-dilution protection.
    """

    object_type: Literal[
        "TX_STOCK_CLASS_CONVERSION_RATIO_ADJUSTMENT"
    ] = "TX_STOCK_CLASS_CONVERSION_RATIO_ADJUSTMENT"
    # Identifier for the object
    id: str
    # Unstructured text comments related to and stored for the object
    comments: Optional[list[str]]
    # Date on which the transaction occurred
    date: Date
    # Identifier of the StockClass object, a subject of this transaction
    stock_class_id: str
    # New conversion ratio mechanism describing new conversion price and conversion
    # ratio in effect following a repricing - based on original issue price to new
    # conversion price (provided in this transaction). For 2-for-1 split the numerator
    # of the ratio is 2 and the denominator is 1.
    new_ratio_conversion_mechanism: RatioConversionMechanism
