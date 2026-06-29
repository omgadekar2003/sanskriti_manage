# import streamlit as st
# from pathlib import Path
# import json
# import re

# # ---------------------------
# # CONFIG
# # ---------------------------

# st.set_page_config(
#     page_title="Sanskriti Robotics Portal",
#     page_icon="🤖",
#     layout="wide"
# )

# # Change this password
# ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]


# DATA_DIR = Path("data")
# DATA_DIR.mkdir(exist_ok=True)

# for grade in ["Grade 7", "Grade 8", "Grade 9"]:
#     (DATA_DIR / grade).mkdir(exist_ok=True)

# # ---------------------------
# # SESSION STATE
# # ---------------------------

# if "teacher_logged_in" not in st.session_state:
#     st.session_state.teacher_logged_in = False

# if "selected_activity" not in st.session_state:
#     st.session_state.selected_activity = None

# # ---------------------------
# # FUNCTIONS
# # ---------------------------

# def safe_name(text):
#     return re.sub(r'[<>:"/\\|?*]', '', text).strip()

# def get_activities(grade):
#     grade_path = DATA_DIR / grade

#     if not grade_path.exists():
#         return []

#     return sorted(
#         [folder for folder in grade_path.iterdir() if folder.is_dir()],
#         key=lambda x: x.name.lower()
#     )

# def save_activity(grade, title, description, uploaded_files):
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

#     for file in uploaded_files:
#         with open(files_path / file.name, "wb") as f:
#             f.write(file.getbuffer())

# # ---------------------------
# # CUSTOM CSS
# # ---------------------------

# st.markdown("""
# <style>

# .block-container{
#     padding-top: 1rem;
# }

# .portal-title{
#     text-align:center;
#     padding:20px;
# }

# .activity-card{
#     border:1px solid #333;
#     border-radius:15px;
#     padding:15px;
#     margin-bottom:15px;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------------------
# # SIDEBAR
# # ---------------------------

# with st.sidebar:

#     st.title("🤖 Robotics")

#     if not st.session_state.teacher_logged_in:

#         with st.expander("🔒 Teacher Login"):

#             password = st.text_input(
#                 "Password",
#                 type="password"
#             )

#             if st.button("Login"):

#                 if password == ADMIN_PASSWORD:
#                     st.session_state.teacher_logged_in = True
#                     st.success("Login Successful")
#                     st.rerun()

#                 else:
#                     st.error("Wrong Password")

#     else:

#         st.success("Teacher Logged In")

#         if st.button("Logout"):
#             st.session_state.teacher_logged_in = False
#             st.rerun()

# # ---------------------------
# # HEADER
# # ---------------------------

# st.markdown(
#     """
#     <div class="portal-title">
#         <h1>🤖 Robotics Learning Portal</h1>
#         <p>Download robotics codes, worksheets, images and project resources.</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # ---------------------------
# # TEACHER PANEL
# # ---------------------------

# if st.session_state.teacher_logged_in:

#     st.divider()

#     st.subheader("⚙️ Teacher Upload Panel")

#     with st.form("upload_form"):

#         grade = st.selectbox(
#             "Select Grade",
#             ["Grade 7", "Grade 8", "Grade 9"]
#         )

#         activity_name = st.text_input(
#             "Activity Name"
#         )

#         description = st.text_area(
#             "Activity Description"
#         )

#         uploaded_files = st.file_uploader(
#             "Upload Files",
#             accept_multiple_files=True
#         )

#         submit = st.form_submit_button(
#             "Create Activity"
#         )

#         if submit:

#             if activity_name.strip() == "":
#                 st.error("Enter Activity Name")

#             else:

#                 save_activity(
#                     grade,
#                     activity_name,
#                     description,
#                     uploaded_files
#                 )

#                 st.success(
#                     f"{activity_name} created successfully!"
#                 )

#                 st.rerun()

# # ---------------------------
# # STUDENT PORTAL
# # ---------------------------

# st.divider()

# grade = st.selectbox(
#     "📚 Select Grade",
#     ["Grade 7", "Grade 8", "Grade 9"]
# )

# search = st.text_input(
#     "🔍 Search Activity"
# )

# activities = get_activities(grade)

# if search:
#     activities = [
#         a for a in activities
#         if search.lower() in a.name.lower()
#     ]

# st.subheader(f"{grade} Activities")

# if not activities:
#     st.info("No activities available.")
# else:

#     cols = st.columns(3)

#     for idx, activity in enumerate(activities):

#         title = activity.name
#         description = ""

#         metadata_file = activity / "metadata.json"

#         if metadata_file.exists():

#             try:
#                 with open(metadata_file, "r", encoding="utf-8") as f:
#                     meta = json.load(f)

#                 title = meta.get("title", title)
#                 description = meta.get(
#                     "description",
#                     ""
#                 )

#             except:
#                 pass

#         with cols[idx % 3]:

#             st.markdown(
#                 f"""
#                 <div class="activity-card">
#                     <h4>{title}</h4>
#                     <p>{description}</p>
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )

#             if st.button(
#                 "Open Activity",
#                 key=f"btn_{activity}"
#             ):
#                 st.session_state.selected_activity = str(activity)

# # ---------------------------
# # ACTIVITY PAGE
# # ---------------------------

# if st.session_state.selected_activity:

#     st.divider()

#     activity_path = Path(
#         st.session_state.selected_activity
#     )

#     st.header(
#         f"📂 {activity_path.name}"
#     )

#     metadata_file = activity_path / "metadata.json"

#     if metadata_file.exists():

#         with open(
#             metadata_file,
#             "r",
#             encoding="utf-8"
#         ) as f:

#             meta = json.load(f)

#         st.write(
#             meta.get("description", "")
#         )

#     files_folder = activity_path / "files"

#     st.subheader("📥 Downloads")

#     if files_folder.exists():

#         files = list(
#             files_folder.glob("*")
#         )

#         if not files:
#             st.warning(
#                 "No files uploaded."
#             )

#         for file in files:

#             with open(file, "rb") as f:

#                 st.download_button(
#                     label=f"📥 {file.name}",
#                     data=f.read(),
#                     file_name=file.name,
#                     use_container_width=True,
#                     key=f"download_{file.name}"
#                 )








import streamlit as st
from pathlib import Path
import json
import re
import requests
import base64
import os

# ---------------------------
# CONFIG
# ---------------------------

st.set_page_config(
    page_title="Sanskriti Robotics Portal",
    page_icon="🤖",
    layout="wide"
)

# Get secrets
ADMIN_PASSWORD = st.secrets["ADMIN_PASSWORD"]
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
GITHUB_REPO = st.secrets["GITHUB_REPO"]
GITHUB_BRANCH = st.secrets.get("GITHUB_BRANCH", "main")

# ---------------------------
# SESSION STATE
# ---------------------------

if "teacher_logged_in" not in st.session_state:
    st.session_state.teacher_logged_in = False

if "selected_activity" not in st.session_state:
    st.session_state.selected_activity = None

# ---------------------------
# GITHUB HELPER FUNCTIONS
# ---------------------------

def github_request(endpoint, method="GET", data=None):
    """Make authenticated GitHub API request"""
    url = f"https://api.github.com/repos/{GITHUB_REPO}{endpoint}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        return response
    except Exception as e:
        st.error(f"GitHub API error: {str(e)}")
        return None

def get_github_file_content(path):
    """Get file content from GitHub"""
    endpoint = f"/contents/{path}"
    response = github_request(endpoint)
    
    if response and response.status_code == 200:
        content = response.json()
        if isinstance(content, list):
            return content
        return content
    return None

def upload_to_github(file_path, content, commit_message):
    """Upload a file to GitHub"""
    endpoint = f"/contents/{file_path}"
    
    # Check if file exists
    existing = get_github_file_content(file_path)
    sha = existing.get("sha") if existing and not isinstance(existing, list) else None
    
    # Prepare data
    data = {
        "message": commit_message,
        "content": base64.b64encode(content).decode("utf-8"),
        "branch": GITHUB_BRANCH
    }
    
    if sha:
        data["sha"] = sha
    
    response = github_request(endpoint, "PUT", data)
    return response and response.status_code in [200, 201]

def list_github_directory(path):
    """List contents of a directory on GitHub"""
    endpoint = f"/contents/{path}"
    response = github_request(endpoint)
    
    if response and response.status_code == 200:
        content = response.json()
        if isinstance(content, list):
            return content
    return []

def safe_name(text):
    return re.sub(r'[<>:"/\\|?*]', '', text).strip()

def get_activities(grade):
    """Get activities from GitHub"""
    path = f"data/{grade}"
    items = list_github_directory(path)
    
    activities = []
    for item in items:
        if item.get("type") == "dir":
            activities.append(item.get("name"))
    
    return sorted(activities)

def get_activity_details(grade, activity_name):
    """Get activity metadata from GitHub"""
    metadata_path = f"data/{grade}/{activity_name}/metadata.json"
    content = get_github_file_content(metadata_path)
    
    if content and not isinstance(content, list):
        try:
            decoded = base64.b64decode(content.get("content", "")).decode("utf-8")
            return json.loads(decoded)
        except:
            pass
    return None

def save_activity(grade, title, description, uploaded_files):
    """Save activity to GitHub"""
    activity_name = safe_name(title)
    base_path = f"data/{grade}/{activity_name}"
    
    # Create metadata
    metadata = {
        "title": title,
        "description": description
    }
    
    # Upload metadata
    metadata_content = json.dumps(metadata, indent=4).encode("utf-8")
    success = upload_to_github(
        f"{base_path}/metadata.json",
        metadata_content,
        f"Add metadata for {title}"
    )
    
    if not success:
        st.error("Failed to upload metadata")
        return False
    
    # Upload files
    for file in uploaded_files:
        file_content = file.getvalue()
        file_path = f"{base_path}/files/{file.name}"
        success = upload_to_github(
            file_path,
            file_content,
            f"Add file {file.name} for {title}"
        )
        
        if not success:
            st.error(f"Failed to upload {file.name}")
            return False
    
    return True

def get_files_for_activity(grade, activity_name):
    """Get files for an activity from GitHub"""
    path = f"data/{grade}/{activity_name}/files"
    items = list_github_directory(path)
    
    files = []
    for item in items:
        if item.get("type") == "file":
            files.append(item.get("name"))
    
    return files

def download_file_from_github(grade, activity_name, filename):
    """Download a file from GitHub"""
    path = f"data/{grade}/{activity_name}/files/{filename}"
    content = get_github_file_content(path)
    
    if content and not isinstance(content, list):
        try:
            decoded = base64.b64decode(content.get("content", ""))
            return decoded
        except:
            pass
    return None

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
                with st.spinner("Uploading to GitHub..."):
                    success = save_activity(
                        grade,
                        activity_name,
                        description,
                        uploaded_files or []
                    )

                if success:
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
        if search.lower() in a.lower()
    ]

st.subheader(f"{grade} Activities")

if not activities:
    st.info("No activities available.")
else:

    cols = st.columns(3)

    for idx, activity_name in enumerate(activities):

        title = activity_name
        description = ""
        
        # Get metadata
        meta = get_activity_details(grade, activity_name)
        if meta:
            title = meta.get("title", activity_name)
            description = meta.get("description", "")

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
                key=f"btn_{activity_name}"
            ):
                st.session_state.selected_activity = f"{grade}/{activity_name}"

# ---------------------------
# ACTIVITY PAGE
# ---------------------------

if st.session_state.selected_activity:

    st.divider()
    
    try:
        grade, activity_name = st.session_state.selected_activity.split("/", 1)
    except:
        st.session_state.selected_activity = None
        st.rerun()
    
    st.header(f"📂 {activity_name}")

    # Get metadata
    meta = get_activity_details(grade, activity_name)
    if meta:
        st.write(meta.get("description", ""))

    st.subheader("📥 Downloads")

    # Get files
    files = get_files_for_activity(grade, activity_name)

    if not files:
        st.warning("No files uploaded.")
    else:
        for filename in files:
            file_data = download_file_from_github(grade, activity_name, filename)
            
            if file_data:
                st.download_button(
                    label=f"📥 {filename}",
                    data=file_data,
                    file_name=filename,
                    use_container_width=True,
                    key=f"download_{filename}"
                )