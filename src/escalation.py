def should_escalate(query, docs):

    sensitive_keywords = [
        "billing",
        "legal",
        "lawsuit",
        "account deletion",
        "refund dispute",
        "payment failure"
    ]

    query_lower = query.lower()

    # Sensitive issues
    if any(
        keyword in query_lower
        for keyword in sensitive_keywords
    ):
        return True

    # No documents found
    if len(docs) == 0:
        return True
    top_score=docs[0][1]
    if top_score > 1.5:
        return True
    return False