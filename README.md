 About my cbt app:

*1. Purpose:*
To help students in Nigeria practice for JAMB, Post-UTME, WAEC, NECO, and school CBT exams on their phone/laptop, just like real exam hall.

*2. How Many Questions:*
- *900 total questions*
- *9 subjects*
- *100 questions per subject:*
    - English Language
    - Mathematics
    - Physics
    - Chemistry
    - Biology
    - Economics
    - Government
    - Computer Studies
    - Current Affairs

*3. How It Works (like real JAMB):*
- Student enters name
- Selects subject (e.g., Mathematics)
- Clicks *START*
- System picks *random questions* from the 100 (e.g., 20 random)
- *Timer counts down* (like real exam)
- Student selects A, B, C, D
- Clicks *Next / Previous*
- Clicks *Submit*
- *Instant result:* Score, percentage, correct answers, corrections

*4. The Bug You Had (now fixed):*
- Old: First and last question same (`What is 2+2?` repeated)
- Reason: My placeholder bank had duplicates + your code mutated main bank
- New: All 100 per subject are *100% unique* - never repeats in same test

*5. Tech Inside:*
- *Language:* Python
- *Website:* Streamlit (makes Python look like website)
- *Data:* JSON file with 900 questions
- *Logic:*
    - `random.sample` = pick without replacement (no repeat)
    - `copy.deepcopy` = don't spoil main bank
    - `set()` = track seen questions

*6. Who Uses It:*
- Students practicing for JAMB
- Schools doing CBT practice
- Tutorial centers
- You can sell access or give free

*7. Where It Lives:*
- On GitHub (your code)
- On Streamlit Cloud (your live link - e.g., `https://your-cbt-app.streamlit.app`)
- Anyone with link can use, no login needed

*8. Files in Your Repo:*
- `cbt_app.py` = Main app (the website)
- `questions_900_UNIQUE_FINAL.json` = 900 questions
- `requirements.txt` = Tells Streamlit what to install (`streamlit`, `pandas`)
- `README.md` = Description for people visiting your GitHub

*In short:* It's a *free, online, JAMB exam simulator* you built. Students can practice 900 different questions anytime, and it marks them instantly like real JAMB.

- How scoring works?
- How to add your own school's questions?
- How to make money with it?
