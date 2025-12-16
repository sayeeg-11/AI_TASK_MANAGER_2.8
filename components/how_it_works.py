import streamlit as st


def render_how_it_works():
    # Hero / intro section
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)
        st.subheader("⚙️ How It Works")
        st.markdown("#### Your complete guide to AI-powered task management")

        col_left, col_right = st.columns([2, 1])

        with col_left:
            st.markdown(
                "**Follow these 4 simple steps to manage tasks like a pro:**\n"
                "From creation → AI prioritization → tracking → insights."
            )

            cta_col1, cta_col2 = st.columns([1.2, 1])
            with cta_col1:
                if st.button("📋 Start with Tasks", type="primary", use_container_width=True):
                    st.session_state.current_page = "📋 Tasks"
                    st.rerun()
            with cta_col2:
                st.caption("Try the Task Manager now.")

        with col_right:
            st.markdown(
                """
                <div style="
                    background: radial-gradient(circle at top left, #0072ff22, #ff512f22);
                    border-radius: 18px;
                    padding: 20px;
                    border: 1px solid rgba(0,0,0,0.05);
                    text-align: center;
                ">
                    <h4>🔄 Complete Workflow</h4>
                    <p style="margin-bottom: 6px;">1. Add Tasks</p>
                    <p style="margin-bottom: 6px;">2. AI Prioritizes</p>
                    <p style="margin-bottom: 6px;">3. Track Progress</p>
                    <p style="margin-bottom: 6px;">4. Analyze Results</p>
                    <p style="opacity: 0.8; font-size: 13px; margin-top: 10px;">4-Step Process</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # Workflow steps with cards
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)
        st.markdown("### 📋 The 4-Step Workflow")

        step1, step2 = st.columns(2)
        with step1:
            st.markdown("#### 1️⃣ **Capture Tasks**")
            st.write(
                "• Add tasks with description, deadline, assignee, and status\n"
                "• Choose **CSV mode** for local files or **API mode** for live backend data\n"
                "• Bulk import and edit capabilities built-in"
            )

        with step2:
            st.markdown("#### 2️⃣ **AI Prioritization**")
            st.write(
                "• AI analyzes task descriptions to suggest **High/Medium/Low** priority\n"
                "• Automatic fallback to safe defaults if AI unavailable\n"
                "• Smart sorting by priority + deadline"

            )

        step3, step4 = st.columns(2)
        with step3:
            st.markdown("#### 3️⃣ **Track & Update**")
            st.write(
                "• Update status: **Pending → In Progress → Completed**\n"
                "• **Bulk status changes** for multiple tasks at once\n"
                "• Assign/unassign team members with full ownership tracking"
            )

        with step4:
            st.markdown("#### 4️⃣ **Analyze Performance**")
            st.write(
                "• **Priority pie charts** showing workload distribution\n"
                "• **User behavior scores** (completion rates per person)\n"
                "• Identify bottlenecks and high-performers instantly"
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # Feature showcase cards
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)
        st.markdown("### ✨ Core Features")

        fc1, fc2, fc3, fc4 = st.columns(4)

        with fc1:
            st.markdown("##### 📋 **Task Manager**")
            st.caption("Create, edit, delete, bulk actions")

        with fc2:
            st.markdown("##### 🤖 **AI Assistant**")
            st.caption("Ask questions, get insights")

        with fc3:
            st.markdown("##### 📊 **Analytics**")
            st.caption("Visualize priorities & performance")

        with fc4:
            st.markdown("##### 🔌 **API Ready**")
            st.caption("Live backend integration")

        st.markdown("</div>", unsafe_allow_html=True)

    # Quick tips section
    with st.container():
        st.markdown("<div class='block-style'>", unsafe_allow_html=True)
        st.markdown("#### 🚀 Pro Tips")
        
        tips_col1, tips_col2 = st.columns(2)
        with tips_col1:
            st.markdown(
                "**Filters work everywhere:**\n"
                "• Sidebar priority/status filters apply to Tasks, AI, and Analytics\n"
                "**Get Started:**\n"
                "• Add 2-3 sample tasks → See AI in action → Check analytics"
            )
        
        with tips_col2:
            st.markdown(
                "**Data Sources:**\n"
                "• **CSV**: Local files (tasks_cleaned.csv)\n"
                "• **API**: Live backend (127.0.0.1:5000)\n"
                "**AI Status:** Currently uses fallback priority (Gemini integration ready)"
            )

        st.markdown("</div>", unsafe_allow_html=True)
