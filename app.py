import streamlit as st

st.set_page_config(page_title="AI Job Toolkit", page_icon=":briefcase:", layout="wide")

st.title("AI Job Toolkit")
st.markdown("### 10 Non-Coding AI Roles with Resumes, Cover Letters & Cold Emails")
st.markdown("Your one-stop toolkit to land AI jobs - no coding required!")

st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to:",
    ["Home", "Job List", "Resume Blocks", "Cover Letters", "Cold Emails", "About"]
)

JOBS = [
    {"no": 1, "role": "AI Prompt Engineer", "skills": "Prompt crafting, LLM knowledge, content creation", "tools": "ChatGPT, Claude, Perplexity, Midjourney"},
    {"no": 2, "role": "AI Content Writer", "skills": "Blog writing, SEO, AI-assisted writing", "tools": "Jasper, Copy.ai, Grammarly, SurferSEO"},
    {"no": 3, "role": "AI Chatbot Designer", "skills": "Conversational design, UX writing, flow mapping", "tools": "Dialogflow, ManyChat, Botpress"},
    {"no": 4, "role": "AI Product Manager", "skills": "Product strategy, roadmap planning, stakeholder management", "tools": "Notion, Jira, Figma, Miro"},
    {"no": 5, "role": "AI Sales Specialist", "skills": "Consultative selling, CRM, pipeline management", "tools": "Salesforce, HubSpot, Outreach"},
    {"no": 6, "role": "AI Marketing Manager", "skills": "Campaign planning, analytics, content strategy", "tools": "HubSpot, Google Analytics, Canva"},
    {"no": 7, "role": "AI SEO Specialist", "skills": "Keyword research, on-page SEO, content optimization", "tools": "Ahrefs, SEMrush, SurferSEO"},
    {"no": 8, "role": "AI Social Media Manager", "skills": "Content scheduling, community management, analytics", "tools": "Buffer, Hootsuite, Later"},
    {"no": 9, "role": "AI Video Editor (No-Code)", "skills": "Video editing, storytelling, captions", "tools": "CapCut, Runway, Descript"},
    {"no": 10, "role": "AI Research Assistant", "skills": "Literature review, summarization, note-taking", "tools": "Perplexity, Elicit, Scite"}
]

RESUME_TEMPLATES = {
    job["role"]: f"""
### {job["role"]} - Resume Summary

**Professional Summary**
Motivated professional with strong skills in {job["skills"].lower()}, proficient in {job["tools"]}. Passionate about leveraging AI tools to deliver high-quality results in remote and India-based roles.

**Key Skills**
- {job["skills"]}
- Tools: {job["tools"]}
- Remote-first, self-driven, quick learner

**Experience Highlights**
- Created engaging AI-powered content using industry-leading tools
- Delivered projects on time with 100% client satisfaction
- Collaborated with cross-functional teams in remote settings

**Education**
Relevant certifications in AI tools, prompt engineering, and digital content creation.

**Projects**
Portfolio of AI-assisted work available on GitHub and personal website.
"""
}

COVER_LETTER_TEMPLATES = {
    job["role"]: f"""
### {job["role"]} - Cover Letter

Dear Hiring Manager,

I am excited to apply for the {job["role"]} position at your organization. With expertise in {job["skills"].lower()} and hands-on experience with {job["tools"]}, I am confident in my ability to contribute meaningfully to your team.

In my previous work, I have successfully leveraged AI tools to streamline workflows, create compelling content, and deliver results that exceed expectations. I thrive in remote environments and am adept at collaborating across time zones.

I am particularly drawn to this role because of its focus on innovation and the opportunity to work with cutting-edge AI technologies. I am a quick learner, highly organized, and committed to continuous improvement.

Thank you for considering my application. I look forward to discussing how I can add value to your team.

Sincerely,
[Your Name]
"""
}

COLD_EMAIL_TEMPLATES = {
    job["role"]: f"""
### {job["role"]} - Cold Email

Subject: {job["role"]} Role - Skilled in {job["skills"].split(",")[0]}

Hi [Hiring Manager Name],

I came across your team and wanted to reach out. I specialize in {job["skills"].lower()} and work with tools like {job["tools"]}.

I have helped [brief achievement/example] and would love to bring similar results to your organization.

Would you be open to a quick 15-minute chat this week?

Best regards,
[Your Name]
[LinkedIn Profile] | [Portfolio Link]
"""
}

if section == "Home":
    st.markdown("---")
    st.info("Welcome to the AI Job Toolkit! Use the sidebar to navigate to different sections.")
    st.metric("Total Jobs", len(JOBS))
    st.metric("Resume Templates", len(RESUME_TEMPLATES))
    st.metric("Cover Letters", len(COVER_LETTER_TEMPLATES))
    st.metric("Cold Emails", len(COLD_EMAIL_TEMPLATES))
    
    st.markdown("### Quick Start")
    st.markdown("""
    1. **Job List** - Browse 10 non-coding AI roles with skills and tools
    2. **Resume Blocks** - Get a ready-to-use resume template for each role
    3. **Cover Letters** - Download a personalized cover letter template
    4. **Cold Emails** - Reach out to hiring managers with a professional cold email
    5. **About** - Learn more about this toolkit
    """)

elif section == "Job List":
    st.markdown("---")
    st.header("10 Non-Coding AI Job Roles")
    for job in JOBS:
        with st.container():
            st.markdown(f"#### {job['no']}. {job['role']}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Skills:** {job['skills']}")
            with col2:
                st.markdown(f"**Tools:** {job['tools']}")
            st.divider()

elif section == "Resume Blocks":
    st.markdown("---")
    st.header("Resume Templates by Role")
    selected_job = st.selectbox("Select a role", [job["role"] for job in JOBS])
    if selected_job:
        st.markdown(RESUME_TEMPLATES[selected_job])

elif section == "Cover Letters":
    st.markdown("---")
    st.header("Cover Letter Templates by Role")
    selected_job = st.selectbox("Select a role", [job["role"] for job in JOBS], key="cover")
    if selected_job:
        st.markdown(COVER_LETTER_TEMPLATES[selected_job])
        st.info("Tip: Replace [Your Name] and customize the bracketed sections before sending!")

elif section == "Cold Emails":
    st.markdown("---")
    st.header("Cold Email Templates by Role")
    selected_job = st.selectbox("Select a role", [job["role"] for job in JOBS], key="email")
    if selected_job:
        st.markdown(COLD_EMAIL_TEMPLATES[selected_job])
        st.info("Tip: Keep cold emails short, personalized, and action-oriented!")

elif section == "About":
    st.markdown("---")
    st.header("About AI Job Toolkit")
    st.markdown("""
    This toolkit is designed for job seekers in India and remote workers who want to break into AI-related roles **without coding**.
    
    ### What's Inside
    - **10 Handpicked AI Job Roles** - curated for beginners and career switchers
    - **Resume Templates** - role-specific, ATS-friendly formats
    - **Cover Letter Templates** - professional and customizable
    - **Cold Email Templates** - proven outreach strategies
    
    ### How to Use
    1. Pick a role from the Job List
    2. Copy the resume block and customize it
    3. Download the cover letter and add your details
    4. Send cold emails to hiring managers and recruiters
    
    ### Deployment
    - **Local:** `pip install -r requirements.txt && streamlit run app.py`
    - **Streamlit Cloud:** Connect this GitHub repo to [share.streamlit.io](https://share.streamlit.io)
    
    ### License
    Free to use for personal and educational purposes.
    """)
