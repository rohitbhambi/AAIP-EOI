import streamlit as st

st.set_page_config(page_title="AAIP Worker EOI Calculator", layout="centered")

st.title("🇨🇦 Alberta Advantage Immigration Program (AAIP) - Worker EOI Calculator")
st.markdown("This tool calculates your points according to the **AAIP Worker Expression of Interest Points Grid**.")

# ---- 1. Education ----
st.header("1. Education")
education = st.selectbox("Highest Level of Education Completed", [
    "Doctorate Degree", "Master’s Degree", "Bachelor’s Degree",
    "Trades Certificate/Diploma", "Diploma/Certificate", "Secondary School or lower"
])
edu_points_map = {
    "Doctorate Degree": 12,
    "Master’s Degree": 10,
    "Bachelor’s Degree": 7,
    "Trades Certificate/Diploma": 7,
    "Diploma/Certificate": 4,
    "Secondary School or lower": 0
}
edu_points = edu_points_map[education]

edu_location = st.selectbox("Location of Highest Level of Education Completed in Canada", [
    "Completed in Alberta", "Completed in another province/territory", "Completed outside Canada"
])
edu_loc_points = 10 if edu_location == "Completed in Alberta" else (6 if edu_location == "Completed in another province/territory" else 0)

# ---- 2. Language ----
st.header("2. Language Proficiency")
st.markdown("Minimum requirement: CLB 4 in all four abilities for English or NCLC 4 for French.")

lang_choice = st.selectbox("Which language gives you the highest points?", ["English", "French"])
if lang_choice == "English":
    clb = st.selectbox("Lowest CLB score across all abilities", [6, 5, 4, 3, "No test"])
    lang_points_map = {6: 10, 5: 8, 4: 5, 3: 0, "No test": 0}
    lang_points = lang_points_map[clb]
else:
    nclc = st.selectbox("Lowest NCLC score across all abilities", [6, 5, 4, 3, "No test"])
    lang_points_map_fr = {6: 8, 5: 5, 4: 3, 3: 0, "No test": 0}
    lang_points = lang_points_map_fr[nclc]

bilingual = st.checkbox("I have CLB/NCLC 4 or higher in both English and French")
bilingual_points = 3 if bilingual else 0

# ---- 3. Work Experience ----
st.header("3. Work Experience")
total_exp = st.selectbox("Total Work Experience (Canada + Abroad)", [
    "12+ months", "6-11 months", "Less than 6 months"
])
total_exp_points = 11 if total_exp == "12+ months" else (7 if total_exp == "6-11 months" else 3)

can_exp = st.selectbox("Work Experience in Canada", [
    "6+ months in Alberta", "6+ months in another province/territory", "Less than 6 months in Canada"
])
can_exp_points = 10 if can_exp == "6+ months in Alberta" else (6 if can_exp == "6+ months in another province/territory" else 0)

# ---- 4. Age ----
st.header("4. Age")
age_group = st.selectbox("Age group", ["18-20 years", "21-34 years", "35-49 years", "50 years and older"])
age_points_map = {
    "18-20 years": 3,
    "21-34 years": 5,
    "35-49 years": 4,
    "50 years and older": 3
}
age_points = age_points_map[age_group]

# ---- 5. Family Connection ----
st.header("5. Family Connection in Alberta")
family_connection = st.checkbox("I have a parent, child, or sibling in Alberta who is a Canadian PR or citizen over 18 years old")
family_points = 8 if family_connection else 0

# ---- 6. Economic Factors ----
st.header("6. Economic Factors - Alberta Job Offer")
job_offer = st.checkbox("I have a permanent full-time job offer in Alberta")
job_offer_points = 10 if job_offer else 0

rural_or_sector = st.selectbox("Special Job Offer Type", [
    "None", "Rural Renewal Stream designated community", "Tourism & Hospitality sector", "Law enforcement occupation"
])
rural_sector_points = 6 if rural_or_sector != "None" else 0

job_location = st.selectbox("Location of Job in Alberta", [
    "Calgary CMA", "Edmonton CMA", "Rural Renewal Stream community", "Other Alberta community"
])
job_location_points = 5 if job_location in ["Rural Renewal Stream community", "Other Alberta community"] else 0

regulated = st.checkbox("Job offer in a regulated occupation AND I hold valid Alberta certification/licensing")
regulated_points = 10 if regulated else 0

# ---- Calculate Total ----
total_score = (
    edu_points + edu_loc_points +
    lang_points + bilingual_points +
    total_exp_points + can_exp_points +
    age_points + family_points +
    job_offer_points + rural_sector_points +
    job_location_points + regulated_points
)

# ---- Output ----
if st.button("Calculate My AAIP EOI Score"):
    st.success(f"Your total AAIP Worker EOI score is: {total_score} / 100")

    st.subheader("Detailed Points Breakdown")
    st.write(f"Education: {edu_points} + Education Location: {edu_loc_points}")
    st.write(f"Language Proficiency: {lang_points} + Bilingual Bonus: {bilingual_points}")
    st.write(f"Work Experience: {total_exp_points} + Canadian Work Experience: {can_exp_points}")
    st.write(f"Age: {age_points}")
    st.write(f"Family Connection: {family_points}")
    st.write(f"Job Offer: {job_offer_points}")
    st.write(f"Special Job Offer Type: {rural_sector_points}")
    st.write(f"Job Location: {job_location_points}")
    st.write(f"Regulated Occupation Bonus: {regulated_points}")

    # Simple analysis
    if total_score >= 75:
        st.info("Strong profile — high likelihood of selection if program criteria met.")
    elif total_score >= 50:
        st.warning("Moderate profile — consider improving language, work experience, or getting a job offer.")
    else:
        st.error("Low profile — eligibility possible but selection unlikely without significant improvements.")
