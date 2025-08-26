import streamlit as st
from data_loader import load_data
from query_engine import get_query_from_question
import pandas as pd

st.title("🧠 Conversational BI Bot")

# Initialize chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Load data
df = load_data()

# Show preview
with st.expander("🔍 Preview Dataset"):
    st.dataframe(df)

# User question input
question = st.text_input("Ask a question about your BI data:")

if question:
    with st.spinner("🤖 Thinking..."):
        # Get code from GPT
        code = get_query_from_question(question, df)
        st.code(code, language='python')

        try:
            local_vars = {"df": df.copy()}
            exec(code, {}, local_vars)
            result = local_vars.get("result", None)

            # Show result
            if isinstance(result, pd.DataFrame):
                st.dataframe(result)
                result_preview = result.to_markdown(index=False)
            elif result is not None:
                st.write(result)
                result_preview = str(result)
            else:
                st.info("✅ Code executed but no result was returned.")
                result_preview = "No result returned."

            # Save to memory
            st.session_state.chat_history.append({
                "question": question,
                "code": code,
                "result": result_preview
            })

        except Exception as e:
            st.error(f"❌ Error running the code: {e}")

# Clear chat button
if st.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []

# Show chat history
if st.session_state.chat_history:
    st.markdown("## 🕑 Chat History")
    for i, entry in enumerate(reversed(st.session_state.chat_history), 1):
        st.markdown(f"**{i}. Q:** {entry['question']}")
        st.code(entry["code"], language="python")
        st.markdown(f"**🧾 Result:**\n\n{entry['result']}")
        st.markdown("---")
