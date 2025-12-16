import streamlit as st


def render_home():
    # Hero / intro section
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)

        col_left, col_right = st.columns([2, 1])

        with col_left:
            st.markdown("### 🧠 AI Task Manager")
            st.markdown("#### Smart, AI-powered task tracking for productive teams.")
            st.write(
                "Bring all your tasks, priorities, and team performance into a single, AI‑augmented dashboard. "
                "Spend less time juggling spreadsheets and more time actually getting work done."
            )

            st.markdown("**What you can do here:**")
            st.markdown(
                "- ✅ Capture and manage tasks with priorities and due dates\n"
                "- 🤖 Let AI highlight what is most urgent right now\n"
                "- 📊 Monitor progress and team performance in real time\n"
                "- 🔌 Connect to a backend API for live, synced data"
            )

            cta_col1, cta_col2 = st.columns([1.2, 1])
            with cta_col1:
                if st.button("🚀 Get Started", type="primary", use_container_width=True):
                    st.session_state.current_page = "📋 Tasks"
                    st.rerun()
            with cta_col2:
                st.caption("Jump straight into the Task Manager.")

        with col_right:
            st.markdown(
                """
                <div style="
                    background: radial-gradient(circle at top left, #0072ff22, #dd247622);
                    border-radius: 18px;
                    padding: 20px;
                    border: 1px solid rgba(0,0,0,0.05);
                    text-align: center;
                ">
                    <h4>Quick Snapshot</h4>
                    <p style="margin-bottom: 6px;">✅ Centralized task workspace</p>
                    <p style="margin-bottom: 6px;">🤖 AI-assisted prioritization</p>
                    <p style="margin-bottom: 6px;">📊 Visual performance analytics</p>
                    <p style="margin-bottom: 6px;">🔌 Optional API backend</p>
                    <p style="opacity: 0.8; font-size: 13px; margin-top: 10px;">Version 2.8 • Built with Streamlit</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # Secondary section: 3 feature cards
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)
        st.markdown("#### Why this dashboard?")

        fc1, fc2, fc3 = st.columns(3)

        with fc1:
            st.markdown("##### 📋 Structured Task Flows")
            st.write(
                "Keep every task traceable from creation to completion, with clear owners, due dates, and status."
            )

        with fc2:
            st.markdown("##### 🤖 AI-First Decisions")
            st.write(
                "Use the AI Assistant page to ask questions like *“What should I focus on today?”* and get context-aware answers."
            )

        with fc3:
            st.markdown("##### 📊 Data-Driven Insights")
            st.write(
                "Use the Analytics page to see priority distribution and user behavior scores, and spot bottlenecks early."
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # Tertiary section: Getting started steps
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)
        st.markdown("#### Quick start guide")

        st.markdown(
            "1. **Go to Tasks** – Add a few sample tasks with descriptions and deadlines.\n"
            "2. **Optionally switch to API mode** – Connect to your backend for live task data.\n"
            "3. **Open AI Assistant** – Ask about urgent tasks or blockers.\n"
            "4. **Check Analytics** – Review completion rates and team performance."
        )

        st.caption("Tip: Use the sidebar filters to focus on specific priorities or statuses.")
        st.markdown("</div>", unsafe_allow_html=True)
