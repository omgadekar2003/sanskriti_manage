# import streamlit as st
# from pathlib import Path
# import json
# import re

# # --------------------------------
# # CONFIG
# # --------------------------------

# st.set_page_config(
#     page_title="Funtrons Robotics Portal",
#     page_icon="🤖",
#     layout="wide"
# )

# DATA_DIR = Path("data")
# DATA_DIR.mkdir(exist_ok=True)

# for grade in ["Grade 7", "Grade 8", "Grade 9"]:
#     (DATA_DIR / grade).mkdir(exist_ok=True)

# # --------------------------------
# # HELPERS
# # --------------------------------

# def safe_name(text):
#     return re.sub(r'[<>:"/\\|?*]', '', text).strip()

# def save_activity(grade, title, description, files):
#     activity_path = DATA_DIR / grade / safe_name(title)
#     files_path = activity_path / "files"

#     activity_path.mkdir(parents=True, exist_ok=True)
#     files_path.mkdir(exist_ok=True)

#     metadata = {
#         "title": title,
#         "description": description
#     }

#     with open(activity_path / "metadata.json", "w", encoding="utf-8") as f:
#         json.dump(metadata, f, indent=4)

#     for file in files:
#         with open(files_path / file.name, "wb") as f:
#             f.write(file.getbuffer())

# def get_activities(grade):
#     grade_path = DATA_DIR / grade

#     if not grade_path.exists():
#         return []

#     return sorted(
#         [x for x in grade_path.iterdir() if x.is_dir()],
#         key=lambda x: x.name.lower()
#     )

# # --------------------------------
# # CUSTOM CSS
# # --------------------------------

# st.markdown("""
# <style>

# .block-container{
#     padding-top:2rem;
# }

# .grade-card{
#     background:#262730;
#     padding:20px;
#     border-radius:15px;
#     text-align:center;
#     margin-bottom:15px;
# }

# .activity-card{
#     background:#1E1E1E;
#     padding:15px;
#     border-radius:12px;
#     border:1px solid #333;
# }

# .small-text{
#     color:#9e9e9e;
# }

# </style>
# """, unsafe_allow_html=True)

# # --------------------------------
# # SIDEBAR
# # --------------------------------

# st.sidebar.title("🤖 Funtrons Portal")

# page = st.sidebar.radio(
#     "Navigation",
#     [
#         "📚 Student Portal",
#         "⚙️ Teacher Portal"
#     ]
# )

# # --------------------------------
# # STUDENT PORTAL
# # --------------------------------

# if page == "📚 Student Portal":

#     st.title("🤖 Robotics Learning Portal")
#     st.caption("Download project codes, worksheets, PPTs and resources.")

#     grade = st.selectbox(
#         "Select Grade",
#         ["Grade 7", "Grade 8", "Grade 9"]
#     )

#     st.divider()

#     activities = get_activities(grade)

#     if not activities:
#         st.info("No activities uploaded yet.")
#         st.stop()

#     search = st.text_input(
#         "🔍 Search Activity"
#     ).lower()

#     filtered = []

#     for activity in activities:
#         if search in activity.name.lower():
#             filtered.append(activity)

#     cols = st.columns(3)

#     for index, activity in enumerate(filtered):

#         metadata_file = activity / "metadata.json"

#         title = activity.name
#         description = ""

#         if metadata_file.exists():

#             with open(metadata_file, "r", encoding="utf-8") as f:
#                 meta = json.load(f)

#             title = meta.get("title", title)
#             description = meta.get("description", "")

#         with cols[index % 3]:

#             with st.container(border=True):

#                 st.subheader(title)

#                 st.caption(description)

#                 if st.button(
#                     "Open Activity",
#                     key=str(activity)
#                 ):
#                     st.session_state["selected"] = str(activity)

#     # -----------------------
#     # Activity Details
#     # -----------------------

#     if "selected" in st.session_state:

#         st.divider()

#         activity_path = Path(
#             st.session_state["selected"]
#         )

#         st.header(activity_path.name)

#         metadata_file = activity_path / "metadata.json"

#         if metadata_file.exists():

#             with open(metadata_file, "r") as f:
#                 meta = json.load(f)

#             st.write(
#                 meta.get("description", "")
#             )

#         files_path = activity_path / "files"

#         st.subheader("📥 Downloads")

#         if files_path.exists():

#             files = list(files_path.glob("*"))

#             if not files:
#                 st.warning("No files uploaded.")

#             for file in files:

#                 with open(file, "rb") as f:

#                     st.download_button(
#                         label=f"Download {file.name}",
#                         data=f.read(),
#                         file_name=file.name,
#                         use_container_width=True,
#                         key=file.name
#                     )

# # --------------------------------
# # TEACHER PORTAL
# # --------------------------------

# else:

#     st.title("⚙️ Teacher Portal")

#     st.info(
#         "Upload new activities and resources."
#     )

#     with st.form("upload_form"):

#         grade = st.selectbox(
#             "Grade",
#             ["Grade 7", "Grade 8", "Grade 9"]
#         )

#         activity_name = st.text_input(
#             "Activity Name"
#         )

#         description = st.text_area(
#             "Description"
#         )

#         uploaded_files = st.file_uploader(
#             "Upload Files",
#             accept_multiple_files=True
#         )

#         submit = st.form_submit_button(
#             "Create Activity"
#         )

#         if submit:

#             if not activity_name:
#                 st.error(
#                     "Enter activity name."
#                 )

#             else:

#                 save_activity(
#                     grade,
#                     activity_name,
#                     description,
#                     uploaded_files
#                 )

#                 st.success(
#                     f"{activity_name} added successfully."
#                 )

#                 st.rerun()

#     st.divider()

#     st.subheader("Existing Activities")

#     for grade in ["Grade 7", "Grade 8", "Grade 9"]:

#         with st.expander(grade):

#             activities = get_activities(grade)

#             if not activities:
#                 st.write("No activities.")

#             for activity in activities:
#                 st.write("📁", activity.name)










import streamlit as st
from pathlib import Path
import json
import re

# ---------------------------
# CONFIG
# ---------------------------

st.set_page_config(
    page_title="Sanskriti Robotics Portal",
    page_icon="🤖",
    layout="wide"
)

# Change this password
ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

for grade in ["Grade 7", "Grade 8", "Grade 9"]:
    (DATA_DIR / grade).mkdir(exist_ok=True)

# ---------------------------
# SESSION STATE
# ---------------------------

if "teacher_logged_in" not in st.session_state:
    st.session_state.teacher_logged_in = False

if "selected_activity" not in st.session_state:
    st.session_state.selected_activity = None

# ---------------------------
# FUNCTIONS
# ---------------------------

def safe_name(text):
    return re.sub(r'[<>:"/\\|?*]', '', text).strip()

def get_activities(grade):
    grade_path = DATA_DIR / grade

    if not grade_path.exists():
        return []

    return sorted(
        [folder for folder in grade_path.iterdir() if folder.is_dir()],
        key=lambda x: x.name.lower()
    )

def save_activity(grade, title, description, uploaded_files):
    activity_path = DATA_DIR / grade / safe_name(title)
    files_path = activity_path / "files"

    activity_path.mkdir(parents=True, exist_ok=True)
    files_path.mkdir(exist_ok=True)

    metadata = {
        "title": title,
        "description": description
    }

    with open(activity_path / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    for file in uploaded_files:
        with open(files_path / file.name, "wb") as f:
            f.write(file.getbuffer())

# ---------------------------
# CUSTOM CSS
# ---------------------------

st.markdown("""
<style>

.block-container{
    padding-top: 1rem;
}

.portal-title{
    text-align:center;
    padding:20px;
}

.activity-card{
    border:1px solid #333;
    border-radius:15px;
    padding:15px;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------

with st.sidebar:

    st.title("🤖 Robotics")

    if not st.session_state.teacher_logged_in:

        with st.expander("🔒 Teacher Login"):

            password = st.text_input(
                "Password",
                type="password"
            )

            if st.button("Login"):

                if password == ADMIN_PASSWORD:
                    st.session_state.teacher_logged_in = True
                    st.success("Login Successful")
                    st.rerun()

                else:
                    st.error("Wrong Password")

    else:

        st.success("Teacher Logged In")

        if st.button("Logout"):
            st.session_state.teacher_logged_in = False
            st.rerun()

# ---------------------------
# HEADER
# ---------------------------

st.markdown(
    """
    <div class="portal-title">
        <h1>🤖 Robotics Learning Portal</h1>
        <p>Download robotics codes, worksheets, images and project resources.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# TEACHER PANEL
# ---------------------------

if st.session_state.teacher_logged_in:

    st.divider()

    st.subheader("⚙️ Teacher Upload Panel")

    with st.form("upload_form"):

        grade = st.selectbox(
            "Select Grade",
            ["Grade 7", "Grade 8", "Grade 9"]
        )

        activity_name = st.text_input(
            "Activity Name"
        )

        description = st.text_area(
            "Activity Description"
        )

        uploaded_files = st.file_uploader(
            "Upload Files",
            accept_multiple_files=True
        )

        submit = st.form_submit_button(
            "Create Activity"
        )

        if submit:

            if activity_name.strip() == "":
                st.error("Enter Activity Name")

            else:

                save_activity(
                    grade,
                    activity_name,
                    description,
                    uploaded_files
                )

                st.success(
                    f"{activity_name} created successfully!"
                )

                st.rerun()

# ---------------------------
# STUDENT PORTAL
# ---------------------------

st.divider()

grade = st.selectbox(
    "📚 Select Grade",
    ["Grade 7", "Grade 8", "Grade 9"]
)

search = st.text_input(
    "🔍 Search Activity"
)

activities = get_activities(grade)

if search:
    activities = [
        a for a in activities
        if search.lower() in a.name.lower()
    ]

st.subheader(f"{grade} Activities")

if not activities:
    st.info("No activities available.")
else:

    cols = st.columns(3)

    for idx, activity in enumerate(activities):

        title = activity.name
        description = ""

        metadata_file = activity / "metadata.json"

        if metadata_file.exists():

            try:
                with open(metadata_file, "r", encoding="utf-8") as f:
                    meta = json.load(f)

                title = meta.get("title", title)
                description = meta.get(
                    "description",
                    ""
                )

            except:
                pass

        with cols[idx % 3]:

            st.markdown(
                f"""
                <div class="activity-card">
                    <h4>{title}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "Open Activity",
                key=f"btn_{activity}"
            ):
                st.session_state.selected_activity = str(activity)

# ---------------------------
# ACTIVITY PAGE
# ---------------------------

if st.session_state.selected_activity:

    st.divider()

    activity_path = Path(
        st.session_state.selected_activity
    )

    st.header(
        f"📂 {activity_path.name}"
    )

    metadata_file = activity_path / "metadata.json"

    if metadata_file.exists():

        with open(
            metadata_file,
            "r",
            encoding="utf-8"
        ) as f:

            meta = json.load(f)

        st.write(
            meta.get("description", "")
        )

    files_folder = activity_path / "files"

    st.subheader("📥 Downloads")

    if files_folder.exists():

        files = list(
            files_folder.glob("*")
        )

        if not files:
            st.warning(
                "No files uploaded."
            )

        for file in files:

            with open(file, "rb") as f:

                st.download_button(
                    label=f"📥 {file.name}",
                    data=f.read(),
                    file_name=file.name,
                    use_container_width=True,
                    key=f"download_{file.name}"
                )