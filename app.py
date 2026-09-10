

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import textwrap



# The Streamlit theme for the filters is configured in
# .streamlit/config.toml. This prevents the default red primary color
# from being applied to multiselect tags.

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EduPro Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ==========================================================
   MAIN APPLICATION
   ========================================================== */

.stApp {
    background-color: #F5F7FB;
}

hr {
    border-color: #E2E8F0 !important;
}


/* ==========================================================
   SIDEBAR
   ========================================================== */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #172554 0%,
        #1E3A8A 100%
    );
}

section[data-testid="stSidebar"] > div {
    background: transparent;
}


/* Sidebar text */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #FFFFFF !important;
}


/* Sidebar radio buttons */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    color: #FFFFFF !important;
    font-weight: 500;
}


/* ==========================================================
   MAIN TITLES
   ========================================================== */

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #172554;
    margin-bottom: 2px;
}

.sub-title {
    font-size: 17px;
    color: #475569;
    margin-top: 0px;
}


/* ==========================================================
   SECTION TITLES
   ========================================================== */

.section-title {
    color: #172554;
    font-size: 27px;
    font-weight: 750;
    margin-top: 10px;
}


/* ==========================================================
   KPI CARDS
   ========================================================== */

.kpi-card {
    background: #FFFFFF;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 5px 18px rgba(15, 23, 42, 0.08);
    border: 1px solid #E2E8F0;
    min-height: 125px;
}

.kpi-title {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
}

.kpi-value {
    color: #172554;
    font-size: 30px;
    font-weight: 800;
    margin-top: 7px;
}

.kpi-icon {
    font-size: 25px;
}


/* ==========================================================
   INFORMATION CARDS
   ========================================================== */

.info-card {
    background: #FFFFFF;
    padding: 22px;
    border-radius: 18px;
    border-left: 5px solid #4F46E5;
    box-shadow: 0px 4px 15px rgba(15, 23, 42, 0.06);
}


/* ==========================================================
   INTERACTIVE FILTER AREA
   ========================================================== */

.filter-box {
    background: #FFFFFF;
    border: 1px solid #D9E2F0;
    border-radius: 18px;
    padding: 20px 22px;
    margin: 8px 0 20px 0;
    box-shadow: 0 4px 16px rgba(23, 37, 84, 0.06);
}

.filter-title {
    color: #172554;
    font-size: 20px;
    font-weight: 750;
    margin-bottom: 5px;
}

.filter-description {
    color: #64748B;
    font-size: 14px;
    line-height: 1.5;
}

/* Interactive filter section */
div[data-testid="stMultiSelect"] {
    background: transparent !important;
    padding: 0 !important;
}


/* ==========================================================
   BUTTON
   ========================================================== */

.stDownloadButton button {
    background-color: #4F46E5 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 10px 20px !important;
}

.stDownloadButton button:hover {
    background-color: #3730A3 !important;
    color: white !important;
}


/* ==========================================================
   GENERAL TEXT
   ========================================================== */

h1, h2, h3, h4 {
    color: #172554 !important;
}

p {
    color: #334155;
}


/* ==========================================================
   DATAFRAME
   ========================================================== */

div[data-testid="stDataFrame"] {
    border-radius: 12px;
}


/* ==========================================================
   FOOTER
   ========================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}



/* ==========================================================
   FINAL CLEAN MULTISELECT DESIGN
   ========================================================== */

/* Filter labels */
.stMultiSelect label,
.stMultiSelect label p,
.stMultiSelect [data-testid="stWidgetLabel"] p {
    color: #334155 !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}

/* Make the complete multiselect control light */
.stMultiSelect div[data-baseweb="select"] {
    background: transparent !important;
    border-radius: 12px !important;
}

.stMultiSelect div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05) !important;
    min-height: 48px !important;
}

/* Inner control area */
.stMultiSelect div[data-baseweb="select"] > div > div {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border-radius: 12px !important;
}

/* Text inside filters */
.stMultiSelect div[data-baseweb="select"] input,
.stMultiSelect div[data-baseweb="select"] span:not([data-baseweb="tag"] span) {
    color: #334155 !important;
}

/* Selected tags: soft blue-grey instead of red */
.stMultiSelect div[data-baseweb="tag"],
.stMultiSelect span[data-baseweb="tag"] {
    background-color: #E8EEF7 !important;
    background: #E8EEF7 !important;
    border: 1px solid #CBD8E8 !important;
    border-radius: 7px !important;
    color: #334155 !important;
    box-shadow: none !important;
}

.stMultiSelect div[data-baseweb="tag"] span,
.stMultiSelect span[data-baseweb="tag"] span {
    background: transparent !important;
    color: #334155 !important;
}

/* Tag close X */
.stMultiSelect div[data-baseweb="tag"] svg,
.stMultiSelect span[data-baseweb="tag"] svg {
    fill: #64748B !important;
    color: #64748B !important;
}

/* Dropdown arrow and clear button */
.stMultiSelect div[data-baseweb="select"] svg {
    fill: #64748B !important;
    color: #64748B !important;
}

/* Dropdown menu */
div[role="listbox"] {
    background: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 10px !important;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.10) !important;
}

div[role="option"],
div[role="option"] * {
    color: #334155 !important;
    background-color: #FFFFFF !important;
}

div[role="option"]:hover,
div[role="option"][aria-selected="true"] {
    background-color: #F1F5F9 !important;
}

/* Soft focus state */
.stMultiSelect div[data-baseweb="select"]:focus-within > div {
    border-color: #94A3B8 !important;
    box-shadow: 0 0 0 2px rgba(148, 163, 184, 0.18) !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PLOTLY THEME
# ============================================================

PLOT_BG = "#FFFFFF"
PAPER_BG = "#FFFFFF"
TEXT_COLOR = "#172554"
SECONDARY_TEXT = "#475569"
GRID_COLOR = "#E2E8F0"


def apply_chart_style(fig, height=450):

    fig.update_layout(
        height=height,

        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,

        font=dict(
            family="Arial",
            color=TEXT_COLOR,
            size=13
        ),

        title=dict(
            font=dict(
                family="Arial",
                size=20,
                color=TEXT_COLOR
            ),
            x=0.02,
            xanchor="left"
        ),

        xaxis=dict(
            title_font=dict(
                color=TEXT_COLOR,
                size=14
            ),
            tickfont=dict(
                color=TEXT_COLOR,
                size=12
            ),
            showgrid=False,
            zeroline=False,
            linecolor="#94A3B8",
            linewidth=1
        ),

        yaxis=dict(
            title_font=dict(
                color=TEXT_COLOR,
                size=14
            ),
            tickfont=dict(
                color=TEXT_COLOR,
                size=12
            ),
            gridcolor=GRID_COLOR,
            gridwidth=1,
            zeroline=False,
            linecolor="#94A3B8",
            linewidth=1
        ),

        legend=dict(
            font=dict(
                color=TEXT_COLOR,
                size=12
            ),
            bgcolor="#FFFFFF",
            bordercolor="#E2E8F0",
            borderwidth=1
        ),

        margin=dict(
            l=70,
            r=40,
            t=75,
            b=70
        ),

        hoverlabel=dict(
            bgcolor="#172554",
            font=dict(
                color="#FFFFFF",
                size=13
            )
        )
    )

    return fig


# ============================================================
# LOAD DATA
# ============================================================

FILE_PATH = "edupro_cleaned.csv"

try:

    df = pd.read_csv(FILE_PATH)

except FileNotFoundError:

    st.error(
        "❌ CSV file not found. Please keep "
        "'edupro_cleaned.csv' in the same folder as app.py."
    )

    st.stop()


# ============================================================
# DATA CLEANING
# ============================================================

if "TransactionDate" in df.columns:

    df["TransactionDate"] = pd.to_datetime(
        df["TransactionDate"],
        errors="coerce"
    )


if "TransactionID" in df.columns:

    df = df.drop_duplicates(
        subset=["TransactionID"]
    )


numeric_columns = [
    "UserAge",
    "Amount",
    "CoursePrice",
    "CourseDuration",
    "CourseRating",
    "TeacherRating",
    "YearsOfExperience"
]

for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# SIDEBAR BRANDING
# ============================================================

st.sidebar.markdown("## 🎓 EduPro")
st.sidebar.markdown("**Learning Analytics Platform**")
st.sidebar.caption("Learner behavior • Enrollment • Course preferences")

st.sidebar.divider()


# ============================================================
# NAVIGATION
# ============================================================

page = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Executive Overview",
        "👥 Learner Demographics",
        "📈 Age-wise Enrollment",
        "🚻 Gender Preferences",
        "📚 Course Popularity",
        "🎛️ Interactive Analysis",
        "📋 Data Explorer"
    ]
)


# ============================================================
# KPI CARD FUNCTION
# ============================================================

def kpi_card(title, value, icon):
    return textwrap.dedent(f"""
    <div class="kpi-card">
        <div>
            <span class="kpi-icon">{icon}</span>
            <span class="kpi-title">{title}</span>
        </div>
        <div class="kpi-value">{value}</div>
    </div>
    """).strip()



# ============================================================
# PAGE 1
# EXECUTIVE OVERVIEW
# ============================================================

if page == "🏠 Executive Overview":

    st.markdown(
        '<div class="main-title">🎓 EduPro Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Executive overview of learner behavior, '
        'enrollment patterns and course preferences'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.divider()


    # ========================================================
    # KPI
    # ========================================================

    total_enrollments = len(df)

    unique_learners = df["UserID"].nunique()

    avg_age = round(
        df["UserAge"].mean(),
        1
    )

    categories = df["CourseCategory"].nunique()


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.markdown(
            kpi_card(
                "Total Enrollments",
                f"{total_enrollments:,}",
                "📚"
            ),
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            kpi_card(
                "Unique Learners",
                f"{unique_learners:,}",
                "👥"
            ),
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            kpi_card(
                "Average Learner Age",
                f"{avg_age}",
                "🎂"
            ),
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            kpi_card(
                "Course Categories",
                f"{categories}",
                "📖"
            ),
            unsafe_allow_html=True
        )


    st.write("")

    st.markdown(
        '<div class="section-title">'
        '📊 Platform Snapshot'
        '</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)


    # ========================================================
    # AGE DONUT
    # ========================================================

    with col1:

        age_data = (
            df["UserAgeGroup"]
            .value_counts()
            .reset_index()
        )

        age_data.columns = [
            "Age Group",
            "Enrollments"
        ]

        fig = px.pie(
            age_data,
            names="Age Group",
            values="Enrollments",
            hole=0.55,
            title="Learner Distribution by Age Group"
        )

        fig.update_traces(
            textfont=dict(
                color=TEXT_COLOR,
                size=13
            )
        )

        fig = apply_chart_style(
            fig,
            430
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GENDER DONUT
    # ========================================================

    with col2:

        gender_data = (
            df["UserGender"]
            .value_counts()
            .reset_index()
        )

        gender_data.columns = [
            "Gender",
            "Enrollments"
        ]

        fig = px.pie(
            gender_data,
            names="Gender",
            values="Enrollments",
            hole=0.55,
            title="Enrollment Distribution by Gender"
        )

        fig.update_traces(
            textfont=dict(
                color=TEXT_COLOR,
                size=13
            )
        )

        fig = apply_chart_style(
            fig,
            430
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # CATEGORY RANKING
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '🏆 Top Course Categories'
        '</div>',
        unsafe_allow_html=True
    )


    category_data = (
        df["CourseCategory"]
        .value_counts()
        .reset_index()
    )

    category_data.columns = [
        "Course Category",
        "Enrollments"
    ]

    category_data = category_data.sort_values(
        "Enrollments",
        ascending=True
    )


    fig = px.bar(
        category_data,
        x="Enrollments",
        y="Course Category",
        orientation="h",
        text="Enrollments",
        title="Course Category Popularity"
    )

    fig.update_traces(
        textposition="outside",
        textfont=dict(
            color=TEXT_COLOR,
            size=12
        )
    )

    fig = apply_chart_style(
        fig,
        500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.info(
        "💡 Use the navigation menu on the left to explore "
        "demographics, age patterns, gender preferences and "
        "course popularity."
    )


# ============================================================
# PAGE 2
# LEARNER DEMOGRAPHICS
# ============================================================

elif page == "👥 Learner Demographics":

    st.markdown(
        '<div class="main-title">'
        '👥 Learner Demographics'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Understand who is using the EduPro platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    col1, col2 = st.columns(2)


    # ========================================================
    # AGE GROUP
    # ========================================================

    with col1:

        age_data = (
            df["UserAgeGroup"]
            .value_counts()
            .reset_index()
        )

        age_data.columns = [
            "Age Group",
            "Enrollments"
        ]

        fig = px.bar(
            age_data,
            x="Age Group",
            y="Enrollments",
            title="📊 Enrollment by Age Group",
            text="Enrollments"
        )

        fig.update_traces(
            textposition="outside",
            textfont=dict(
                color=TEXT_COLOR
            )
        )

        fig = apply_chart_style(
            fig,
            450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # GENDER
    # ========================================================

    with col2:

        gender_data = (
            df["UserGender"]
            .value_counts()
            .reset_index()
        )

        gender_data.columns = [
            "Gender",
            "Enrollments"
        ]

        fig = px.pie(
            gender_data,
            names="Gender",
            values="Enrollments",
            hole=0.45,
            title="👤 Gender Distribution"
        )

        fig.update_traces(
            textfont=dict(
                color=TEXT_COLOR,
                size=13
            )
        )

        fig = apply_chart_style(
            fig,
            450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # AGE HISTOGRAM
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '🎂 Learner Age Distribution'
        '</div>',
        unsafe_allow_html=True
    )


    fig = px.histogram(
        df,
        x="UserAge",
        nbins=20,
        title="Age Distribution of EduPro Learners"
    )

    fig.update_traces(
        marker_line_width=1,
        textfont=dict(
            color=TEXT_COLOR
        )
    )

    fig = apply_chart_style(
        fig,
        450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # AGE VS GENDER
    # ========================================================

    cross = pd.crosstab(
        df["UserAgeGroup"],
        df["UserGender"]
    ).reset_index()


    gender_columns = [
        c for c in cross.columns
        if c != "UserAgeGroup"
    ]


    fig = px.bar(
        cross,
        x="UserAgeGroup",
        y=gender_columns,
        barmode="group",
        title="Age Group vs Gender"
    )

    fig = apply_chart_style(
        fig,
        450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PAGE 3
# AGE-WISE ENROLLMENT
# ============================================================

elif page == "📈 Age-wise Enrollment":

    st.markdown(
        '<div class="main-title">'
        '📈 Age-wise Enrollment'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Explore how enrollment varies across learner age groups'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # AGE ENROLLMENT
    # ========================================================

    age_enrollment = (
        df.groupby("UserAgeGroup")
        .size()
        .reset_index(
            name="Enrollments"
        )
    )


    fig = px.bar(
        age_enrollment,
        x="UserAgeGroup",
        y="Enrollments",
        text="Enrollments",
        title="📊 Enrollment Volume by Age Group"
    )

    fig.update_traces(
        textposition="outside",
        textfont=dict(
            color=TEXT_COLOR
        )
    )

    fig = apply_chart_style(
        fig,
        450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # AGE VS CATEGORY
    # ========================================================

    st.subheader(
        "🔥 Course Category Preference Across Age Groups"
    )


    age_category = pd.crosstab(
        df["UserAgeGroup"],
        df["CourseCategory"]
    ).reset_index()


    age_columns = [
        c for c in age_category.columns
        if c != "UserAgeGroup"
    ]


    fig = px.bar(
        age_category,
        x="UserAgeGroup",
        y=age_columns,
        barmode="stack",
        title="Age Group vs Course Category"
    )

    fig = apply_chart_style(
        fig,
        550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # AGE VS LEVEL
    # ========================================================

    st.subheader(
        "🎯 Age Group vs Course Level"
    )


    age_level = pd.crosstab(
        df["UserAgeGroup"],
        df["CourseLevel"]
    ).reset_index()


    level_columns = [
        c for c in age_level.columns
        if c != "UserAgeGroup"
    ]


    fig = px.bar(
        age_level,
        x="UserAgeGroup",
        y=level_columns,
        barmode="group",
        title="Course Level Preference by Age Group"
    )

    fig = apply_chart_style(
        fig,
        500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PAGE 4
# GENDER PREFERENCES
# ============================================================

elif page == "🚻 Gender Preferences":

    st.markdown(
        '<div class="main-title">'
        '🚻 Gender-based Preferences'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Compare course selection patterns between genders'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # CATEGORY VS GENDER
    # ========================================================

    gender_category = pd.crosstab(
        df["CourseCategory"],
        df["UserGender"]
    ).reset_index()


    gender_columns = [
        c for c in gender_category.columns
        if c != "CourseCategory"
    ]


    fig = px.bar(
        gender_category,
        x="CourseCategory",
        y=gender_columns,
        barmode="group",
        title="📚 Course Category Preference by Gender"
    )

    fig = apply_chart_style(
        fig,
        550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # GENDER VS LEVEL
    # ========================================================

    st.subheader(
        "🎯 Gender vs Course Level"
    )


    gender_level = pd.crosstab(
        df["UserGender"],
        df["CourseLevel"]
    ).reset_index()


    gender_level_columns = [
        c for c in gender_level.columns
        if c != "UserGender"
    ]


    fig = px.bar(
        gender_level,
        x="UserGender",
        y=gender_level_columns,
        barmode="group",
        title="Course Level Preference by Gender"
    )

    fig = apply_chart_style(
        fig,
        500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # COURSE TYPE
    # ========================================================

    st.subheader(
        "💳 Free vs Paid Course Preference"
    )


    gender_type = pd.crosstab(
        df["UserGender"],
        df["CourseType"]
    ).reset_index()


    type_columns = [
        c for c in gender_type.columns
        if c != "UserGender"
    ]


    fig = px.bar(
        gender_type,
        x="UserGender",
        y=type_columns,
        barmode="stack",
        title="Course Type Enrollment by Gender"
    )

    fig = apply_chart_style(
        fig,
        450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PAGE 5
# COURSE POPULARITY
# ============================================================

elif page == "📚 Course Popularity":

    st.markdown(
        '<div class="main-title">'
        '📚 Course Popularity'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Discover the courses and categories attracting '
        'the most learners'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # CATEGORY RANKING
    # ========================================================

    category_data = (
        df["CourseCategory"]
        .value_counts()
        .reset_index()
    )


    category_data.columns = [
        "Course Category",
        "Enrollments"
    ]


    category_data = category_data.sort_values(
        "Enrollments",
        ascending=True
    )


    fig = px.bar(
        category_data,
        x="Enrollments",
        y="Course Category",
        orientation="h",
        text="Enrollments",
        title="🏆 Course Category Ranking"
    )


    fig.update_traces(
        textposition="outside",
        textfont=dict(
            color=TEXT_COLOR
        )
    )


    fig = apply_chart_style(
        fig,
        550
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    col1, col2 = st.columns(2)


    # ========================================================
    # COURSE LEVEL
    # ========================================================

    with col1:

        level_data = (
            df["CourseLevel"]
            .value_counts()
            .reset_index()
        )


        level_data.columns = [
            "Course Level",
            "Enrollments"
        ]


        fig = px.pie(
            level_data,
            names="Course Level",
            values="Enrollments",
            hole=0.5,
            title="🎯 Course Level Distribution"
        )


        fig.update_traces(
            textfont=dict(
                color=TEXT_COLOR,
                size=13
            )
        )


        fig = apply_chart_style(
            fig,
            450
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # COURSE TYPE
    # ========================================================

    with col2:

        type_data = (
            df["CourseType"]
            .value_counts()
            .reset_index()
        )


        type_data.columns = [
            "Course Type",
            "Enrollments"
        ]


        fig = px.pie(
            type_data,
            names="Course Type",
            values="Enrollments",
            hole=0.5,
            title="💳 Free vs Paid Courses"
        )


        fig.update_traces(
            textfont=dict(
                color=TEXT_COLOR,
                size=13
            )
        )


        fig = apply_chart_style(
            fig,
            450
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ========================================================
    # TOP 10 COURSES
    # ========================================================

    st.subheader(
        "⭐ Top 10 Most Enrolled Courses"
    )


    top_courses = (
        df["CourseName"]
        .value_counts()
        .head(10)
        .reset_index()
    )


    top_courses.columns = [
        "Course Name",
        "Enrollments"
    ]


    fig = px.bar(
        top_courses.sort_values(
            "Enrollments"
        ),
        x="Enrollments",
        y="Course Name",
        orientation="h",
        text="Enrollments",
        title="Top 10 Courses"
    )


    fig.update_traces(
        textposition="outside",
        textfont=dict(
            color=TEXT_COLOR
        )
    )


    fig = apply_chart_style(
        fig,
        550
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PAGE 6
# INTERACTIVE ANALYSIS
# ============================================================

elif page == "🎛️ Interactive Analysis":

    st.markdown(
        '<div class="main-title">'
        '🎛️ Interactive Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Build your own learner segment using the filters below'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # FILTER BOX
    # ========================================================

    with st.container(border=True):
        st.markdown('<div class="filter-title">🔎 Customize Your Analysis</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="filter-description">Select age group, gender, course category and course level to dynamically analyze a specific learner segment.</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # FILTERS
    # ========================================================

    col1, col2 = st.columns(2)


    # AGE FILTER
    with col1:

        age_options = sorted(
            df["UserAgeGroup"]
            .dropna()
            .unique()
        )

        selected_age = st.multiselect(
            "👤 Age Group",
            options=age_options,
            default=list(age_options),
            help="Select one or more learner age groups."
        )


    # GENDER FILTER
    with col2:

        gender_options = sorted(
            df["UserGender"]
            .dropna()
            .unique()
        )

        selected_gender = st.multiselect(
            "🚻 Gender",
            options=gender_options,
            default=list(gender_options),
            help="Select one or more genders."
        )


    col3, col4 = st.columns(2)


    # CATEGORY FILTER
    with col3:

        category_options = sorted(
            df["CourseCategory"]
            .dropna()
            .unique()
        )

        selected_category = st.multiselect(
            "📚 Course Category",
            options=category_options,
            default=list(category_options),
            help="Select one or more course categories."
        )


    # LEVEL FILTER
    with col4:

        level_options = sorted(
            df["CourseLevel"]
            .dropna()
            .unique()
        )

        selected_level = st.multiselect(
            "🎯 Course Level",
            options=level_options,
            default=list(level_options),
            help="Select one or more course levels."
        )


    st.divider()


    # ========================================================
    # APPLY FILTERS
    # ========================================================

    filtered_df = df[
        df["UserAgeGroup"].isin(
            selected_age
        )
        &
        df["UserGender"].isin(
            selected_gender
        )
        &
        df["CourseCategory"].isin(
            selected_category
        )
        &
        df["CourseLevel"].isin(
            selected_level
        )
    ].copy()


    # ========================================================
    # EMPTY DATA
    # ========================================================

    if len(filtered_df) == 0:

        st.warning(
            "⚠️ No records match your selected filters. "
            "Please change your filter selection."
        )

        st.stop()


    # ========================================================
    # FILTERED KPIs
    # ========================================================

    filtered_enrollments = len(
        filtered_df
    )

    filtered_learners = (
        filtered_df["UserID"]
        .nunique()
    )

    filtered_avg_age = round(
        filtered_df["UserAge"].mean(),
        1
    )

    filtered_categories = (
        filtered_df["CourseCategory"]
        .nunique()
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.markdown(
            kpi_card(
                "Filtered Enrollments",
                f"{filtered_enrollments:,}",
                "📚"
            ),
            unsafe_allow_html=True
        )


    with c2:

        st.markdown(
            kpi_card(
                "Filtered Learners",
                f"{filtered_learners:,}",
                "👥"
            ),
            unsafe_allow_html=True
        )


    with c3:

        st.markdown(
            kpi_card(
                "Average Age",
                f"{filtered_avg_age}",
                "🎂"
            ),
            unsafe_allow_html=True
        )


    with c4:

        st.markdown(
            kpi_card(
                "Categories",
                f"{filtered_categories}",
                "📖"
            ),
            unsafe_allow_html=True
        )


    st.write("")


    # ========================================================
    # FILTERED CATEGORY
    # ========================================================

    category_filtered = (
        filtered_df["CourseCategory"]
        .value_counts()
        .reset_index()
    )


    category_filtered.columns = [
        "Course Category",
        "Enrollments"
    ]


    fig = px.bar(
        category_filtered,
        x="Course Category",
        y="Enrollments",
        text="Enrollments",
        title="📊 Course Category Popularity After Filtering"
    )


    fig.update_traces(
        textposition="outside",
        textfont=dict(
            color=TEXT_COLOR
        )
    )


    fig = apply_chart_style(
        fig,
        500
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # AGE VS CATEGORY
    # ========================================================

    age_category_filtered = pd.crosstab(
        filtered_df["UserAgeGroup"],
        filtered_df["CourseCategory"]
    ).reset_index()


    age_columns = [
        c for c in age_category_filtered.columns
        if c != "UserAgeGroup"
    ]


    fig = px.bar(
        age_category_filtered,
        x="UserAgeGroup",
        y=age_columns,
        barmode="stack",
        title="🔥 Age Group vs Course Category"
    )


    fig = apply_chart_style(
        fig,
        550
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # COURSE LEVEL
    # ========================================================

    level_filtered = (
        filtered_df["CourseLevel"]
        .value_counts()
        .reset_index()
    )


    level_filtered.columns = [
        "Course Level",
        "Enrollments"
    ]


    fig = px.pie(
        level_filtered,
        names="Course Level",
        values="Enrollments",
        hole=0.5,
        title="🎯 Selected Learners by Course Level"
    )


    fig.update_traces(
        textfont=dict(
            color=TEXT_COLOR,
            size=13
        )
    )


    fig = apply_chart_style(
        fig,
        450
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # DOWNLOAD
    # ========================================================

    st.subheader(
        "📥 Export Filtered Data"
    )


    csv = filtered_df.to_csv(
        index=False
    ).encode("utf-8")


    st.download_button(
        label="⬇️ Download Filtered CSV",
        data=csv,
        file_name="edupro_filtered_data.csv",
        mime="text/csv"
    )


# ============================================================
# PAGE 7
# DATA EXPLORER
# ============================================================

elif page == "📋 Data Explorer":

    st.markdown(
        '<div class="main-title">'
        '📋 Data Explorer'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">'
        'Explore the EduPro dataset directly'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # DATASET KPIs
    # ========================================================

    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "Rows",
            f"{df.shape[0]:,}"
        )


    with c2:

        st.metric(
            "Columns",
            df.shape[1]
        )


    with c3:

        st.metric(
            "Missing Values",
            int(
                df.isnull()
                .sum()
                .sum()
            )
        )


    st.write("")


    # ========================================================
    # COURSE SEARCH
    # ========================================================

    search = st.text_input(
        "🔎 Search Course Name",
        placeholder="Type a course name..."
    )


    display_df = df.copy()


    if search:

        display_df = display_df[
            display_df["CourseName"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]


    st.dataframe(
        display_df,
        use_container_width=True,
        height=550
    )


    # ========================================================
    # STATISTICS
    # ========================================================

    st.subheader(
        "📊 Dataset Statistics"
    )


    st.dataframe(
        df.describe(
            include="all"
        ).transpose(),
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    textwrap.dedent("""
    <div style="
        text-align:center;
        color:#64748B;
        padding:15px;
    ">
        🎓 <b>EduPro Online Learning Analytics</b><br>
        Built with Python • Pandas • Plotly • Streamlit
    </div>
    """).strip(),
    unsafe_allow_html=True
)

# ============================================================
# FINAL FILTER STYLE OVERRIDE
# Placed at the END so it overrides Streamlit/BaseWeb widget CSS.
# ============================================================
st.markdown("""
<style>
/* Filter labels */
div[data-testid="stMultiSelect"] label {
    color: #334155 !important;
    font-weight: 600 !important;
}

/* White filter field */
div[data-testid="stMultiSelect"] [data-baseweb="select"],
div[data-testid="stMultiSelect"] [data-baseweb="select"] > div,
div[data-testid="stMultiSelect"] [role="combobox"] {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border-color: #D6DEE9 !important;
    color: #334155 !important;
    border-radius: 10px !important;
}

/* Selected pills */
div[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    background: #E8EEF7 !important;
    background-color: #E8EEF7 !important;
    border: 1px solid #C9D4E3 !important;
    color: #334155 !important;
    border-radius: 6px !important;
}

div[data-testid="stMultiSelect"] [data-baseweb="tag"] span,
div[data-testid="stMultiSelect"] [data-baseweb="tag"] div {
    background: transparent !important;
    background-color: transparent !important;
    color: #334155 !important;
}

/* Tag close icon */
div[data-testid="stMultiSelect"] [data-baseweb="tag"] svg {
    color: #64748B !important;
    fill: #64748B !important;
}

/* Input text */
div[data-testid="stMultiSelect"] input {
    color: #334155 !important;
    -webkit-text-fill-color: #334155 !important;
}

/* Dropdown */
div[data-baseweb="popover"],
div[data-baseweb="popover"] [role="listbox"],
div[data-baseweb="popover"] [role="option"] {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    color: #334155 !important;
}

div[data-baseweb="popover"] [role="option"]:hover {
    background: #F1F5F9 !important;
}

/* Make clear/dropdown icons neutral */
div[data-testid="stMultiSelect"] svg {
    color: #64748B !important;
    fill: #64748B !important;
}


/* Clean Streamlit multiselect appearance */
div[data-testid="stMultiSelect"] {
    background: transparent !important;
}

div[data-testid="stMultiSelect"] [data-baseweb="select"] {
    background: #FFFFFF !important;
    border: 1px solid #D7DEE8 !important;
    border-radius: 10px !important;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05) !important;
}

div[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    background: #E8EEF6 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 6px !important;
    color: #334155 !important;
}

div[data-testid="stMultiSelect"] [data-baseweb="tag"] span {
    color: #334155 !important;
}

div[data-testid="stMultiSelect"] input {
    color: #334155 !important;
    -webkit-text-fill-color: #334155 !important;
}

div[data-testid="stMultiSelect"] svg {
    color: #64748B !important;
    fill: #64748B !important;
}

</style>
""", unsafe_allow_html=True)
