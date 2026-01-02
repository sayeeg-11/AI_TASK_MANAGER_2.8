import streamlit as st

def sidebar_navigation():
    """
    Streamlit Sidebar Navigation Component with Saved Filter Views
    Returns the selected page name
    """
    
    # ---------- Initialize session state for saved views ----------
    if "saved_views" not in st.session_state:
        st.session_state.saved_views = {}
    if "current_filters" not in st.session_state:
        st.session_state.current_filters = {
            "priority": "All",
            "status": "All"
        }
    
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

    # ---------- Saved Filter Views ----------
    st.sidebar.subheader("💾 Saved Views")
    
    # Dropdown to load saved views
    view_names = ["None"] + list(st.session_state.saved_views.keys())
    selected_view = st.sidebar.selectbox(
        "Load View:",
        view_names,
        key="selected_saved_view",
        on_change=lambda: load_saved_view()
    )
    
    def load_saved_view():
        if selected_view != "None" and selected_view in st.session_state.saved_views:
            st.session_state.current_filters = st.session_state.saved_views[selected_view].copy()
            st.rerun()
    
    # Save current filters button
    if st.sidebar.button("💾 Save Current Filters"):
        with st.sidebar.container():
            view_name = st.text_input("View Name:", key="new_view_name")
            if st.button("Confirm Save") and view_name:
                st.session_state.saved_views[view_name] = st.session_state.current_filters.copy()
                st.sidebar.success(f"Saved '{view_name}'")
                st.rerun()
    
    # Display and manage saved views
    if st.session_state.saved_views:
        for name, filters in st.session_state.saved_views.items():
            col1, col2, col3 = st.sidebar.columns([3, 1, 1])
            with col1:
                st.caption(f"📋 {name}")
            with col2:
                if st.button("✏️", key=f"rename_{name}", help="Rename"):
                    # Simple rename logic - could be expanded
                    pass
            with col3:
                if st.button("🗑️", key=f"delete_{name}", help="Delete"):
                    del st.session_state.saved_views[name]
                    st.rerun()

    st.sidebar.divider()

    # ---------- Current Filters (Quick Filters) ----------
    with st.sidebar.expander("🔍 Current Filters", expanded=True):
        priority = st.selectbox(
            "Priority",
            ["All", "High", "Medium", "Low"],
            index=["All", "High", "Medium", "Low"].index(st.session_state.current_filters["priority"]),
            key="filter_priority_current"
        )
        status = st.selectbox(
            "Status",
            ["All", "Pending", "In Progress", "Completed"],
            index=["All", "Pending", "In Progress", "Completed"].index(st.session_state.current_filters["status"]),
            key="filter_status_current"
        )
        
        # Update current filters
        st.session_state.current_filters["priority"] = priority
        st.session_state.current_filters["status"] = status
        
        st.caption("These will be saved with 'Save Current Filters'")

    st.sidebar.divider()

    # ---------- Sidebar Footer ----------
    st.sidebar.caption("🚀 Version 2.8")
    st.sidebar.caption("Made with ❤️ using Streamlit")

    return selected_page

# Helper function to get current filters for use in Tasks/Analytics pages
def get_current_filters():
    """Returns the current filter state for applying to data"""
    return st.session_state.current_filters if "current_filters" in st.session_state else {}
