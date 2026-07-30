def validate_output(result):

    required_fields = [
        "company",
        "invoice_number",
        "total_amount"
    ]

    missing = []

    for field in required_fields:
        if field not in result:
            missing.append(field)

    return missing