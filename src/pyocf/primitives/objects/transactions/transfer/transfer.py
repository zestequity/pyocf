"""Abstract object describing a security transfer or secondary sale transaction"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/primitives/objects/transactions/transfer/Transfer.schema.json

from pydantic import BaseModel
from typing import Optional


class Transfer(BaseModel):
    """Abstract object describing a security transfer or secondary sale transaction"""

    # Unstructured text description of consideration provided in exchange for security
    # transfer
    consideration_text: Optional[str]
    # Identifier for the security that holds the remainder balance (for partial
    # transfers)
    balance_security_id: Optional[str]
    # Array of identifiers for new security (or securities) created as a result of the
    # transaction
    resulting_security_ids: list[str]
