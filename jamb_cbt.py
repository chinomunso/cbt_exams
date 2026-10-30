import streamlit as st
import random
import time
import json
from datetime import datetime
import copy

st.set_page_config(page_title="NONY TECHS CBT 9 Subjects + Payment", layout="wide", page_icon="📝")

# ========== CONFIG ==========
SUBJECTS = ["English", "Mathematics", "Physics", "Chemistry", "Biology", "Economics", "Government", "Computer Studies", "Current Affairs"]
PRICE_PER_SUBJECT = 500
FULL_PACKAGE = 3000

# ========== REAL QUESTIONS BANK (90 REAL QUESTIONS - RANDOMIZED) ==========
REAL_QUESTIONS = {
    "English": [
        {"q": "Choose the word nearest in meaning to 'Benevolent'", "options": ["A. Wicked", "B. Kind", "C. Lazy", "D. Harsh"], "answer": "B. Kind"},
        {"q": "What is past tense of 'go'?", "options": ["A. Goed", "B. Went", "C. Gone", "D. Going"], "answer": "B. Went"},
        {"q": "Which is a noun? 'The boy runs fast'", "options": ["A. The", "B. Boy", "C. Runs", "D. Fast"], "answer": "B. Boy"},
        {"q": "Synonym for 'Diligent'?", "options": ["A. Lazy", "B. Hardworking", "C. Sleepy", "D. Rude"], "answer": "B. Hardworking"},
        {"q": "Correct spelling?", "options": ["A. Accomodate", "B. Accommodate", "C. Acommodate", "D. Accomodete"], "answer": "B. Accommodate"},
        {"q": "Antonym of 'Ancient'", "options": ["A. Old", "B. Modern", "C. Past", "D. Antique"], "answer": "B. Modern"},
        {"q": "Plural of 'Child' is?", "options": ["A. Childs", "B. Childrens", "C. Children", "D. Childes"], "answer": "C. Children"},
        {"q": "Which is correct?", "options": ["A. She don't like rice", "B. She doesn't like rice", "C. She not like rice", "D. She no like rice"], "answer": "B. She doesn't like rice"},
        {"q": "A person who writes books is a/an?", "options": ["A. Author", "B. Doctor", "C. Farmer", "D. Pilot"], "answer": "A. Author"},
        {"q": "Choose article: ___ honest man", "options": ["A. A", "B. An", "C. The", "D. No article"], "answer": "B. An"},
    ],
    "Mathematics": [
        {"q": "What is 25% of 200?", "options": ["A. 25", "B. 50", "C. 75", "D. 100"], "answer": "B. 50"},
        {"q": "Solve: 2x + 3 = 11", "options": ["A. 2", "B. 3", "C. 4", "D. 5"], "answer": "C. 4"},
        {"q": "Area of circle radius 7 (π=22/7)", "options": ["A. 154", "B. 144", "C. 164", "D. 174"], "answer": "A. 154"},
        {"q": "Simplify: 5² + 3²", "options": ["A. 25", "B. 34", "C. 16", "D. 30"], "answer": "B. 34"},
        {"q": "What is LCM of 4 and 6?", "options": ["A. 12", "B. 24", "C. 6", "D. 2"], "answer": "A. 12"},
        {"q": "Triangle 3,4,5 is?", "options": ["A. Equilateral", "B. Right-angled", "C. Isosceles", "D. Obtuse"], "answer": "B. Right-angled"},
        {"q": "Mean of 2,4,6,8,10?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "B. 6"},
        {"q": "Convert 0.5 to fraction", "options": ["A. 1/2", "B. 1/3", "C. 1/4", "D. 2/3"], "answer": "A. 1/2"},
        {"q": "Value of π approx?", "options": ["A. 2.14", "B. 3.14", "C. 4.14", "D. 3.41"], "answer": "B. 3.14"},
        {"q": "10² - 9² = ?", "options": ["A. 1", "B. 19", "C. 100", "D. 81"], "answer": "B. 19"},
    ],
    "Physics": [
        {"q": "SI unit of force?", "options": ["A. Watt", "B. Newton", "C. Joule", "D. Pascal"], "answer": "B. Newton"},
        {"q": "Acceleration due to gravity?", "options": ["A. 5 m/s²", "B. 10 m/s²", "C. 15 m/s²", "D. 20 m/s²"], "answer": "B. 10 m/s²"},
        {"q": "Light fastest in?", "options": ["A. Water", "B. Glass", "C. Vacuum", "D. Air"], "answer": "C. Vacuum"},
        {"q": "Which is vector?", "options": ["A. Mass", "B. Speed", "C. Velocity", "D. Distance"], "answer": "C. Velocity"},
        {"q": "Ohm's Law: V = ?", "options": ["A. IR", "B. I/R", "C. R/I", "D. I²R"], "answer": "A. IR"},
        {"q": "Unit of current?", "options": ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"], "answer": "B. Ampere"},
        {"q": "Energy in stretched spring is?", "options": ["A. Kinetic", "B. Potential", "C. Heat", "D. Chemical"], "answer": "B. Potential"},
        {"q": "Sound cannot travel through?", "options": ["A. Water", "B. Air", "C. Vacuum", "D. Steel"], "answer": "C. Vacuum"},
        {"q": "Lens for myopia?", "options": ["A. Convex", "B. Concave", "C. Plano", "D. Bifocal"], "answer": "B. Concave"},
        {"q": "Work done = ?", "options": ["A. Force x Distance", "B. Mass x Velocity", "C. Power / Time", "D. Force / Area"], "answer": "A. Force x Distance"},
    ],
    "Chemistry": [
        {"q": "Symbol for Sodium?", "options": ["A. So", "B. Na", "C. S", "D. N"], "answer": "B. Na"},
        {"q": "pH of neutral?", "options": ["A. 0", "B. 7", "C. 14", "D. 1"], "answer": "B. 7"},
        {"q": "H2O is?", "options": ["A. Hydrogen", "B. Water", "C. Oxygen", "D. Salt"], "answer": "B. Water"},
        {"q": "Atomic no. of Carbon?", "options": ["A. 6", "B. 8", "C. 12", "D. 4"], "answer": "A. 6"},
        {"q": "Noble gas is?", "options": ["A. Oxygen", "B. Nitrogen", "C. Helium", "D. Chlorine"], "answer": "C. Helium"},
        {"q": "Acid turns blue litmus to?", "options": ["A. Blue", "B. Red", "C. Green", "D. Yellow"], "answer": "B. Red"},
        {"q": "Lightest element?", "options": ["A. Helium", "B. Hydrogen", "C. Lithium", "D. Oxygen"], "answer": "B. Hydrogen"},
        {"q": "Common salt formula?", "options": ["A. KCl", "B. NaCl", "C. CaCl2", "D. MgCl2"], "answer": "B. NaCl"},
        {"q": "CO2 is?", "options": ["A. Carbon monoxide", "B. Carbon dioxide", "C. Carbonate", "D. Carbon"], "answer": "B. Carbon dioxide"},
        {"q": "Number of elements in periodic table?", "options": ["A. 118", "B. 92", "C. 100", "D. 108"], "answer": "A. 118"},
    ],
    "Biology": [
        {"q": "Powerhouse of cell?", "options": ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Chloroplast"], "answer": "B. Mitochondria"},
        {"q": "Photosynthesis in?", "options": ["A. Mitochondria", "B. Chloroplast", "C. Nucleus", "D. Ribosome"], "answer": "B. Chloroplast"},
        {"q": "Chromosomes in human?", "options": ["A. 44", "B. 46", "C. 48", "D. 23"], "answer": "B. 46"},
        {"q": "Largest organ?", "options": ["A. Heart", "B. Brain", "C. Skin", "D. Liver"], "answer": "C. Skin"},
        {"q": "Blood pumped by?", "options": ["A. Lungs", "B. Heart", "C. Kidney", "D. Liver"], "answer": "B. Heart"},
        {"q": "Vitamin from sunlight?", "options": ["A. A", "B. B", "C. C", "D. D"], "answer": "D. D"},
        {"q": "Study of living things?", "options": ["A. Biology", "B. Chemistry", "C. Physics", "D. Geology"], "answer": "A. Biology"},
        {"q": "Oxygen carried by?", "options": ["A. White blood cells", "B. Red blood cells", "C. Platelets", "D. Plasma"], "answer": "B. Red blood cells"},
        {"q": "Example of vertebrate?", "options": ["A. Snail", "B. Fish", "C. Insect", "D. Worm"], "answer": "B. Fish"},
        {"q": "Blood group discovered by?", "options": ["A. Landsteiner", "B. Darwin", "C. Mendel", "D. Pasteur"], "answer": "A. Landsteiner"},
    ],
    "Economics": [
        {"q": "Father of Economics?", "options": ["A. Adam Smith", "B. Keynes", "C. Karl Marx", "D. Marshall"], "answer": "A. Adam Smith"},
        {"q": "Demand/supply determines?", "options": ["A. Price", "B. Weather", "C. Taste", "D. Population"], "answer": "A. Price"},
        {"q": "Scale of preference means?", "options": ["A. Listing wants by importance", "B. Buying everything", "C. Saving all money", "D. No choice"], "answer": "A. Listing wants by importance"},
        {"q": "Inflation means?", "options": ["A. Rise in general price", "B. Fall in price", "C. Stable price", "D. No price"], "answer": "A. Rise in general price"},
        {"q": "Which is factor of production?", "options": ["A. Land", "B. Money", "C. Car", "D. House"], "answer": "A. Land"},
        {"q": "Budget is?", "options": ["A. Plan of income and expenditure", "B. List of friends", "C. Bank account", "D. Loan"], "answer": "A. Plan of income and expenditure"},
        {"q": "Market where shares traded?", "options": ["A. Stock Exchange", "B. Supermarket", "C. Open market", "D. Black market"], "answer": "A. Stock Exchange"},
        {"q": "Opportunity cost is?", "options": ["A. Cost of next best alternative foregone", "B. Cost of all alternatives", "C. Free cost", "D. No cost"], "answer": "A. Cost of next best alternative foregone"},
        {"q": "Money is medium of?", "options": ["A. Exchange", "B. War", "C. Hatred", "D. Politics"], "answer": "A. Exchange"},
        {"q": "Value of naira determined by?", "options": ["A. CBN", "B. Customer", "C. Trader", "D. Student"], "answer": "A. CBN"},
    ],
    "Government": [
        {"q": "Nigeria became republic in?", "options": ["A. 1960", "B. 1963", "C. 1970", "D. 1999"], "answer": "B. 1963"},
        {"q": "First military coup in Nigeria?", "options": ["A. 1966", "B. 1960", "C. 1970", "D. 1983"], "answer": "A. 1966"},
        {"q": "Number of arms of govt?", "options": ["A. 2", "B. 3", "C. 4", "D. 5"], "answer": "B. 3"},
        {"q": "Current constitution is?", "options": ["A. 1999", "B. 1979", "C. 1963", "D. 1960"], "answer": "A. 1999"},
        {"q": "Head of judiciary?", "options": ["A. CJN", "B. President", "C. Senate President", "D. Governor"], "answer": "A. CJN"},
        {"q": "Democracy means?", "options": ["A. Government of people by people", "B. Government by army", "C. Government by king", "D. No government"], "answer": "A. Government of people by people"},
        {"q": "INEC means?", "options": ["A. Independent National Electoral Commission", "B. Internal National Election Council", "C. International Election Commission", "D. None"], "answer": "A. Independent National Electoral Commission"},
        {"q": "Nigeria has how many states?", "options": ["A. 36", "B. 37", "C. 30", "D. 40"], "answer": "A. 36"},
        {"q": "Senate has how many members?", "options": ["A. 109", "B. 360", "C. 100", "D. 50"], "answer": "A. 109"},
        {"q": "ECOWAS HQ is in?", "options": ["A. Lagos", "B. Abuja", "C. Accra", "D. Dakar"], "answer": "B. Abuja"},
    ],
    "Computer Studies": [
        {"q": "Father of computer?", "options": ["A. Charles Babbage", "B. Bill Gates", "C. Steve Jobs", "D. Mark Zuckerberg"], "answer": "A. Charles Babbage"},
        {"q": "Brain of computer?", "options": ["A. CPU", "B. Monitor", "C. Keyboard", "D. Mouse"], "answer": "A. CPU"},
        {"q": "1KB = ?", "options": ["A. 1000 bytes", "B. 1024 bytes", "C. 512 bytes", "D. 2048 bytes"], "answer": "B. 1024 bytes"},
        {"q": "Which is input device?", "options": ["A. Printer", "B. Monitor", "C. Keyboard", "D. Speaker"], "answer": "C. Keyboard"},
        {"q": "WWW means?", "options": ["A. World Wide Web", "B. Wide World Web", "C. Web Wide World", "D. None"], "answer": "A. World Wide Web"},
        {"q": "OS is?", "options": ["A. Windows", "B. MS Word", "C. Excel", "D. PowerPoint"], "answer": "A. Windows"},
        {"q": "Binary numbers are?", "options": ["A. 0 and 1", "B. 1 and 2", "C. 0-9", "D. A-Z"], "answer": "A. 0 and 1"},
        {"q": "RAM means?", "options": ["A. Random Access Memory", "B. Read Access Memory", "C. Run Access Memory", "D. None"], "answer": "A. Random Access Memory"},
        {"q": "Stores data permanently?", "options": ["A. RAM", "B. ROM", "C. Cache", "D. Register"], "answer": "B. ROM"},
        {"q": "Internet browser is?", "options": ["A. Google Chrome", "B. MS Word", "C. Photoshop", "D. VLC"], "answer": "A. Google Chrome"},
    ],
    "Current Affairs": [
        {"q": "President of Nigeria (2026)?", "options": ["A. Bola Tinubu", "B. Atiku", "C. Obi", "D. Buhari"], "answer": "A. Bola Tinubu"},
        {"q": "Capital of Edo State?", "options": ["A. Benin City", "B. Auchi", "C. Ekpoma", "D. Uromi"], "answer": "A. Benin City"},
        {"q": "Independence Day?", "options": ["A. Oct 1", "B. Jan 1", "C. Dec 25", "D. May 29"], "answer": "A. Oct 1"},
        {"q": "Currency of Nigeria?", "options": ["A. Naira", "B. Cedi", "C. Dollar", "D. Rand"], "answer": "A. Naira"},
        {"q": "Largest continent?", "options": ["A. Africa", "B. Asia", "C. Europe", "D. America"], "answer": "B. Asia"},
        {"q": "W.H.O HQ?", "options": ["A. Geneva", "B. New York", "C. London", "D. Abuja"], "answer": "A. Geneva"},
        {"q": "EFCC means?", "options": ["A. Economic and Financial Crimes Commission", "B. Every Fraud Case Closed", "C. Economic Fraud Control Center", "D. None"], "answer": "A. Economic and Financial Crimes Commission"},
        {"q": "National anthem changed in?", "options": ["A. 2024", "B. 2020", "C. 1960", "D. 1990"], "answer": "A. 2024"},
        {"q": "Geo-political zones?", "options": ["A. 6", "B. 5", "C. 7", "D. 8"], "answer": "A. 6"},
        {"q": "CBN Governor 2024-2026?", "options": ["A. Cardoso", "B. Emefiele", "C. Soludo", "D. Sanusi"], "answer": "A. Cardoso"},
    ]
}

if 'paid' not in st.session_state: st.session_state.paid = False
if 'selected_subjects' not in st.session_state: st.session_state.selected_subjects = []
if 'cbt_started' not in st.session_state: st.session_state.cbt_started = False
if 'results' not in st.session_state: st.session_state.results = []

st.title("📝 CBT Platform - 9 Subjects + Paystack")
st.header("STEP 1: Select & Pay")
col1, col2 = st.columns([2,1])
with col1:
    selected = st.multiselect("Choose subjects:", SUBJECTS, default=st.session_state.selected_subjects)
    st.session_state.selected_subjects = selected
    total = FULL_PACKAGE if len(selected)==9 else len(selected)*PRICE_PER_SUBJECT
    if selected: st.info(f"Total: ₦{total:,} for {len(selected)} subjects")

with col2:
    if not st.session_state.paid:
        email = st.text_input("Email", "student@email.com")
        method = st.selectbox("Method", ["Test Mode (Free Demo)", "Paystack Live"])
        if st.button(f"Pay ₦{total}", disabled=(total==0)):
            if method.startswith("Test"):
                time.sleep(1)
                st.session_state.paid = True
                st.session_state.paid_email = email
                st.session_state.paid_amount = total
                st.rerun()
            else:
                st.markdown(f"Use Paystack API with amount {total*100} kobo")
    else:
        st.success("✅ PAYMENT CONFIRMED")
        if st.button("Reset"): 
            st.session_state.paid=False
            st.rerun()

if st.session_state.paid and st.session_state.selected_subjects:
    st.divider()
    st.header("STEP 2: Real Random Questions Test")
    if not st.session_state.cbt_started:
        subject = st.selectbox("Subject to write:", st.session_state.selected_subjects)
        num_q = st.slider("Number of questions", 5, 20, 10)
        duration = st.slider("Time (minutes)", 5, 60, 15)
        if st.button(f"START {subject.upper()}"):
            raw_qs = random.sample(REAL_QUESTIONS[subject], min(num_q, len(REAL_QUESTIONS[subject])))
            qs = copy.deepcopy(raw_qs)
            seen = set()
            final_qs = []
            for q in qs:
               if q['q'] not in seen:
                  seen.add(q['q'])
                  random.shuffle(q['options'])
                  final_qs.append(q)
            st.session_state.current_questions = final_qs
            st.session_state.cbt_started = True
            st.session_state.duration = duration


           
            st.session_state.current_questions = qs
            st.session_state.current_subject = subject
            
            st.session_state.start_time = datetime.now()
            st.session_state.cbt_started = True
            st.session_state.answers = {}
            st.rerun()
    else:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        remaining = st.session_state.duration*60 - elapsed
        if remaining <=0:
            st.error("Time Up!")
            st.session_state.cbt_started=False
            st.rerun()
        mins, secs = divmod(int(remaining),60)
        st.metric("Time Left", f"{mins:02d}:{secs:02d}")
        st.progress(min(elapsed/(st.session_state.duration*60),1.0))
        for i,q in enumerate(st.session_state.current_questions):
            st.markdown(f"**Q{i+1}. {q['q']}**")
            st.session_state.answers[i]=st.radio(f"Q{i+1}", q['options'], key=f"q_{i}", index=None)
            st.divider()
        if st.button("Submit"):
            score = sum(1 for i,qq in enumerate(st.session_state.current_questions) if st.session_state.answers.get(i)==qq['answer'])
            st.session_state.results.append({"subject":st.session_state.current_subject,"score":score,"total":len(st.session_state.current_questions),"date":datetime.now().strftime("%Y-%m-%d %H:%M")})
            st.success(f"Score: {score}/{len(st.session_state.current_questions)}")
            st.session_state.cbt_started=False
            st.rerun()

if st.session_state.results:
    st.divider()
    st.header("Results")
    import pandas as pd
    df = pd.DataFrame(st.session_state.results)
    st.dataframe(df, use_container_width=True)
    st.download_button("Download CSV", df.to_csv(index=False).encode('utf-8'), "results.csv", "text/csv")
