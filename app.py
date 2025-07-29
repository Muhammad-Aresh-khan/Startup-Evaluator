import utils.session
import streamlit as st
from crew import run_crew

st.set_page_config(page_title="Startup Helper", page_icon="🚀")
st.title("🚀 Startup Evaluator with CrewAI")

idea = st.text_area("Describe your startup idea")

if st.button("Generate Insights") and idea:
    with st.spinner("Agents are working..."):
        result = run_crew(idea)

    st.success("Done!")

    # Display structured task results
    st.subheader("📋 Results from Each Agent")

    if hasattr(result, "tasks_output"):
        for idx, task in enumerate(result.tasks_output):
            st.markdown(f"### 🔹 Task {idx+1}: {task.agent}")
            st.markdown(f"**Description:** {task.description}")
            st.markdown("**Output:**")
            st.markdown(task.raw, unsafe_allow_html=True)
    else:
        st.warning("No task output found.")
