"""Type representation of a government identifier for tax purposes (e.g. EIN) and"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/types/TaxID.schema.json

from pydantic import BaseModel
from pyocf.types.countrycode import CountryCode


class TaxID(BaseModel):
    """Type representation of a government identifier for tax purposes (e.g. EIN) and
    corresponding country code (ISO-3166)
    """

    # Tax identifier as string
    tax_id: str
    # Issuing country code (ISO 3166-1 alpha-2) for the tax identifier
    country: CountryCode