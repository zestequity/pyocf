"""Enumeration of types of relationships between stakeholder and issuer"""

# Autogenerated, do not edit.
# Copyright © 2023 Shoobx, Fidelity Investments
#
# Based on the Open Captable Format schema:
# Copyright © 2023 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/main/schema/enums/StakeholderRelationshipType.schema.json

from enum import Enum


class StakeholderRelationshipType(Enum):
    """Enumeration of types of relationships between stakeholder and issuer"""

    ENUM_ADVISOR = "ADVISOR"
    ENUM_BOARD_MEMBER = "BOARD_MEMBER"
    ENUM_CONSULTANT = "CONSULTANT"
    ENUM_EMPLOYEE = "EMPLOYEE"
    ENUM_EX_ADVISOR = "EX_ADVISOR"
    ENUM_EX_CONSULTANT = "EX_CONSULTANT"
    ENUM_EX_EMPLOYEE = "EX_EMPLOYEE"
    ENUM_EXECUTIVE = "EXECUTIVE"
    ENUM_FOUNDER = "FOUNDER"
    ENUM_INVESTOR = "INVESTOR"
    ENUM_NON_US_EMPLOYEE = "NON_US_EMPLOYEE"
    ENUM_OFFICER = "OFFICER"
    ENUM_OTHER = "OTHER"
