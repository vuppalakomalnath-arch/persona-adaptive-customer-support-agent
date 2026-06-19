def create_handoff_summary(
    persona,
    query,
    docs
):

    return {
        "persona": persona,
        "issue": query,
        "documents_used": [
            doc.metadata.get(
                "source",
                "unknown"
            )
            for doc, score in docs
        ],
        "attempted_steps": [
            "Knowledge base retrieval",
            "AI response generation"
        ],
        "recommendation":
        "Escalate to human support specialist",
        "status":
        "pending human review"

    }