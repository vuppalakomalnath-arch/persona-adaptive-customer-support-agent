import streamlit as st

from src.persona_detector import detect_persona
from src.rag_pipeline import retrieve
from src.response_generator import generate_response
from src.escalation import should_escalate
from src.handoff import create_handoff_summary


st.set_page_config(
    page_title="Persona Support Agent",
    page_icon="🤖",
    layout="wide"
)
if "history" not in st.session_state:
    st.session_state.history = []
st.title("🤖 Persona-Adaptive Customer Support Agent")
st.sidebar.title("Conversation History")

for item in st.session_state.history:

    st.sidebar.markdown(
        f"**Query:** {item['query']}"
    )

    st.sidebar.markdown(
        f"Persona: {item['persona']}"
    )

    st.sidebar.markdown("---")

query = st.text_area(
    "Enter customer message"
)

if st.button("Submit"):

    if query:
        try:
            persona = detect_persona(query)

            docs = retrieve(query)
            retrieved_docs=[
                doc for doc, score in docs
            ]

            response = generate_response(
                query,
                persona,
                retrieved_docs
            )

            escalate = should_escalate(
                query,
                docs
            )
            st.session_state.history.append(
                {
                    "query": query,
                    "persona": persona,
                    "response": response,
                    "escalate": escalate
                }
            )
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Detected Persona",
                    persona
                )

            with col2:

                st.metric(
                    "Escalation",
                    "Required" if escalate else "Not Required"
                )

            st.subheader("Retrieved Sources")

            for doc, score in docs:
                st.info(
                    f"{doc.metadata.get('source','Unknown')}: {doc.page_content[:200]}..."
                )
                confidence=round(1/(1+score),2)
            
                st.write(
                    f"Confidece Score: {confidence}"
                )    


            st.subheader("Generated Response")
            st.write(response)

            st.subheader("Escalation Status")
        except Exception as e:
            st.error(
                f"Gemini API Error: {str(e)}"    )
            st.stop()
        if escalate:
            st.error(
                    "Escalation Required"
                )

            summary = create_handoff_summary(
                    persona,
                    query,
                    docs
                )

            st.subheader(
                    "Human Handoff Summary"
                )

            st.json(summary)
        else:

            st.success(
                    "No Escalation Needed"
                )
            st.markdown("---")
            st.markdown(
                """
    ### Features Demonstrated

    ✅ Persona Detection

    ✅ Retrieval-Augmented Generation

    ✅ Adaptive Responses

    ✅ Human Escalation

    ✅ Handoff Summary

    ✅ Confidence-Based Retrieval

    ✅ Conversation Memory
    """
            )   