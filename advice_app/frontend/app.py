import streamlit as st
import requests

# FastAPI base URL
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Advice Manager", page_icon="💡", layout="centered")

st.title("💡 Advice Management Dashboard")

# Sidebar navigation
menu = st.sidebar.radio("Navigation", ["View All", "Add Advice", "Update Advice", "Delete Advice"])

# --- View All Advices ---
if menu == "View All":
    st.subheader("📋 All Advices")
    response = requests.get(f"{API_URL}/advices/")
    if response.status_code == 200:
        data = response.json()
        if data:
            st.table(data)
        else:
            st.info("No advices found.")
    else:
        st.error("Failed to fetch advices from API.")

# --- Add Advice ---
elif menu == "Add Advice":
    st.subheader("➕ Add New Advice")
    title = st.text_input("Title")
    description = st.text_area("Description")
    category = st.text_input("Category")

    if st.button("Add Advice"):
        payload = {"title": title, "description": description, "category": category}
        res = requests.post(f"{API_URL}/advices/", json=payload)
        if res.status_code == 200:
            st.success("✅ Advice added successfully!")
        else:
            st.error(f"Failed to add advice. ({res.status_code})")

# --- Update Advice ---
elif menu == "Update Advice":
    st.subheader("✏️ Update Advice")
    id = st.number_input("Enter Advice ID", min_value=1, step=1)
    title = st.text_input("New Title")
    description = st.text_area("New Description")
    category = st.text_input("New Category")

    if st.button("Update"):
        payload = {"title": title, "description": description, "category": category}
        res = requests.put(f"{API_URL}/advices/{id}", json=payload)
        if res.status_code == 200:
            st.success("✅ Advice updated successfully!")
        else:
            st.error("❌ Failed to update advice.")

# --- Delete Advice ---
elif menu == "Delete Advice":
    st.subheader("🗑️ Delete Advice")
    id = st.number_input("Enter ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/advices/{id}")
        if res.status_code == 200:
            st.success("✅ Advice deleted successfully!")
        else:
            st.error("❌ Failed to delete advice.")
