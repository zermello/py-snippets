"""
Streamlit UI for main.py's file handling logic.

Same four operations as the original CLI script — create, update
(rename / append / overwrite), read, delete — just driven by UI
controls instead of input(). All operations act on real files on
disk (relative to wherever this app is run from), exactly like the
original script did with Path().
"""

from pathlib import Path

import streamlit as st

st.set_page_config(page_title="File Ops", page_icon="📁", layout="centered")

CUSTOM_CSS = """
<style>
    .stApp {
        background: #0f1115;
        color: #e8eaed;
    }
    h1, h2, h3 { font-family: "Trebuchet MS", sans-serif; }
    .op-card {
        background: #171a21;
        border: 1px solid #2a2f3a;
        border-radius: 14px;
        padding: 22px 24px;
        margin-bottom: 16px;
    }
    .stButton > button {
        border-radius: 8px;
        border: 1px solid #2a2f3a;
        background: #1d212a;
        color: #e8eaed;
    }
    .stButton > button:hover {
        border-color: #6f6bff;
        color: #22d3ee;
    }
    div[data-baseweb="tab-list"] { gap: 4px; }
    footer, #MainMenu { visibility: hidden; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("📁 File Ops")
st.caption("A UI for create / read / update / delete — same logic as main.py, just click instead of type.")


# ----------------------------------------------------------------------------
# Core logic — same behavior as the original functions, but returning
# (success, message) instead of calling input()/print() directly, so the
# UI layer can display results.
# ----------------------------------------------------------------------------

def create_file(name: str, data: str):
    try:
        path = Path(name)
        if not path.exists():
            with open(path, "w") as fs:
                fs.write(data)
            return True, f"Created '{name}'."
        else:
            return False, "File name already exists"
    except Exception as err:
        return False, f"An error has occured as {err}"


def rename_file(name: str, new_name: str):
    try:
        path = Path(name)
        if not path.exists():
            return False, "File does not exist!"
        if Path(new_name).exists():
            return False, "This name already exists! Try another name"
        path.rename(new_name)
        return True, f"Renamed '{name}' → '{new_name}'."
    except Exception as err:
        return False, f"An error has occured as {err}"


def append_file(name: str, text: str):
    try:
        path = Path(name)
        if not path.exists():
            return False, "File does not exist!"
        with open(path, "a") as fs:
            fs.write(text)
        return True, f"Appended to '{name}'."
    except Exception as err:
        return False, f"An error has occured as {err}"


def overwrite_file(name: str, text: str):
    try:
        path = Path(name)
        if not path.exists():
            return False, "File does not exist!"
        with open(path, "w") as fs:
            fs.write(text)
        return True, f"Overwrote '{name}'."
    except Exception as err:
        return False, f"An error has occured as {err}"


def read_file(name: str):
    try:
        path = Path(name)
        if not path.exists():
            return False, "file name doesn't exist"
        with open(path, "r") as fs:
            return True, fs.read()
    except Exception as err:
        return False, f"An error has occured as {err}"


def delete_file(name: str):
    try:
        path = Path(name)
        if not path.exists():
            return False, "Path name does not exist"
        path.unlink()
        return True, f"Deleted '{name}'."
    except Exception as err:
        return False, f"An error has occured as {err}"


# ----------------------------------------------------------------------------
# UI — one tab per operation, mirroring the original menu (1-4)
# ----------------------------------------------------------------------------
tab_create, tab_update, tab_read, tab_delete = st.tabs(
    ["1 · Create", "2 · Update", "3 · Read", "4 · Delete"]
)

with tab_create:
    st.markdown('<div class="op-card">', unsafe_allow_html=True)
    st.subheader("Create a new file")
    name = st.text_input("What is the file name?", key="create_name")
    data = st.text_area("What you want to write?", key="create_data", height=140)
    if st.button("Create", key="create_btn"):
        if not name:
            st.warning("Enter a file name first.")
        else:
            ok, msg = create_file(name, data)
            (st.success if ok else st.error)(msg)
    st.markdown("</div>", unsafe_allow_html=True)

with tab_update:
    st.markdown('<div class="op-card">', unsafe_allow_html=True)
    st.subheader("Update a file")
    name = st.text_input("What is the name of the file?", key="update_name")

    choice_label = st.radio(
        "What do you want to do?",
        ["1 : rename the file", "2 : appending the content", "3 : overwriting the file"],
        key="update_choice",
    )

    if choice_label.startswith("1"):
        new_name = st.text_input("What is the new name?", key="rename_new_name")
        if st.button("Rename", key="rename_btn"):
            if not name or not new_name:
                st.warning("Enter both the current and new file name.")
            else:
                ok, msg = rename_file(name, new_name)
                (st.success if ok else st.error)(msg)

    elif choice_label.startswith("2"):
        text = st.text_area("What you need to add?", key="append_text", height=120)
        if st.button("Append", key="append_btn"):
            if not name:
                st.warning("Enter a file name first.")
            else:
                ok, msg = append_file(name, text)
                (st.success if ok else st.error)(msg)

    else:  # overwrite
        text = st.text_area("What do you want to overwrite this with?", key="overwrite_text", height=120)
        if st.button("Overwrite", key="overwrite_btn"):
            if not name:
                st.warning("Enter a file name first.")
            else:
                ok, msg = overwrite_file(name, text)
                (st.success if ok else st.error)(msg)

    st.markdown("</div>", unsafe_allow_html=True)

with tab_read:
    st.markdown('<div class="op-card">', unsafe_allow_html=True)
    st.subheader("Read a file")
    name = st.text_input("What is the name of the file?", key="read_name")
    if st.button("Read", key="read_btn"):
        if not name:
            st.warning("Enter a file name first.")
        else:
            ok, msg = read_file(name)
            if ok:
                st.code(msg if msg else "(file is empty)", language=None)
            else:
                st.error(msg)
    st.markdown("</div>", unsafe_allow_html=True)

with tab_delete:
    st.markdown('<div class="op-card">', unsafe_allow_html=True)
    st.subheader("Delete a file")
    name = st.text_input("Enter the filename you want to delete", key="delete_name")
    confirm = st.checkbox("I understand this can't be undone", key="delete_confirm")
    if st.button("Delete", key="delete_btn", disabled=not confirm):
        if not name:
            st.warning("Enter a file name first.")
        else:
            ok, msg = delete_file(name)
            (st.success if ok else st.error)(msg)
    st.markdown("</div>", unsafe_allow_html=True)

st.caption(f"Working directory: `{Path.cwd()}` — file names are relative to this folder, same as the original script.")