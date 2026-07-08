def route_claim(fields):

    missing = []

    for key, value in fields.items():
        if value is None or value == "" or value == []:
            missing.append(key)

    if missing:
        return {
            "missingFields": missing,
            "recommendedRoute": "Manual Review",
            "reasoning": "Mandatory fields are missing."
        }

    damage = int(str(fields["Estimated Damage"]).replace(",", ""))

    description = str(fields["Description"]).lower()

    claim_type = str(fields["Claim Type"]).lower()

    if "fraud" in description or "staged" in description or "inconsistent" in description:
        return {
            "missingFields": [],
            "recommendedRoute": "Investigation Flag",
            "reasoning": "Fraud-related keywords found."
        }

    if claim_type == "injury":
        return {
            "missingFields": [],
            "recommendedRoute": "Specialist Queue",
            "reasoning": "Injury claim."
        }

    if damage < 25000:
        return {
            "missingFields": [],
            "recommendedRoute": "Fast-track",
            "reasoning": "Damage below ₹25,000."
        }

    return {
        "missingFields": [],
        "recommendedRoute": "Normal Queue",
        "reasoning": "Standard processing."
    }