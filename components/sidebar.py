import streamlit as st


def sidebar_navigation():
    """
    Streamlit Sidebar Navigation Component
    Returns the selected page name
    """

    # ---------- Sidebar Header ----------
    st.sidebar.markdown("## 🧠 AI Task Manager")
    st.sidebar.caption("AI-Powered Productivity Dashboard")

    st.sidebar.divider()

    # ---------- Navigation Menu ----------
    pages = [
        "🏠 Home",
        "⚙️ How It Works",
        "📋 Tasks",
        "🤖 AI Assistant",
        "📊 Analytics",
        "👥 Team / Users",
        "⚙️ Settings"
    ]

    # Default active page
    if "current_page" not in st.session_state:
        st.session_state.current_page = pages[0]

    selected_page = st.sidebar.radio(
        label="Navigation",
        options=pages,
        index=pages.index(st.session_state.current_page),
        key="sidebar_navigation"
    )

    # Update active page
    st.session_state.current_page = selected_page

    st.sidebar.divider()

    # ---------- Optional Filters ----------
    with st.sidebar.expander("🔍 Quick Filters", expanded=False):
        st.selectbox(
            "Priority",
            ["All", "High", "Medium", "Low"],
            key="filter_priority"
        )

        st.selectbox(
            "Status",
            ["All", "Pending", "In Progress", "Completed"],
            key="filter_status"
        )

    st.sidebar.divider()

    # ---------- Sidebar Footer ----------
    st.sidebar.caption("🚀 Version 2.8")
    st.sidebar.caption("Made with ❤️ using Streamlit")

    return selected_page
