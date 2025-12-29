import streamlit as st

st.set_page_config(page_title="Kuesioner Kesehatan", layout="centered")

# ===== SESSION STATE =====
if "page" not in st.session_state:
    st.session_state.page = 1
if "score" not in st.session_state:
    st.session_state.score = 0

def reset_app():
    st.session_state.page = 1
    st.session_state.score = 0

st.title("🩺 Kuesioner Pola Hidup Sehat")

# ===== PAGE 1 : TIDUR =====
if st.session_state.page == 1:
    st.image("assets/sleep.gif", width=300)

    tidur = st.radio(
        "1️⃣ Lama tidur per hari",
        ("< 5 jam", "5–7 jam", "7–9 jam")
    )

    if st.button("Next ➡️"):
        st.session_state.score += 1 if tidur == "< 5 jam" else 2 if tidur == "5–7 jam" else 3
        st.session_state.page = 2

# ===== PAGE 2 : MAKAN =====
elif st.session_state.page == 2:
    st.image("assets/eat.gif", width=300)

    makan = st.radio(
        "2️⃣ Pola makan",
        ("Sering fast food", "Cukup seimbang", "Seimbang & teratur")
    )

    col1, col2 = st.columns(2)
    if col1.button("⬅️ Back"):
        st.session_state.page = 1
    if col2.button("Next ➡️"):
        st.session_state.score += 1 if makan == "Sering fast food" else 2 if makan == "Cukup seimbang" else 3
        st.session_state.page = 3

# ===== PAGE 3 : OLAHRAGA =====
elif st.session_state.page == 3:
    st.image("assets/exercise.gif", width=300)

    olahraga = st.radio(
        "3️⃣ Frekuensi olahraga",
        ("Jarang", "1–2 kali / minggu", "≥ 3 kali / minggu")
    )

    col1, col2 = st.columns(2)
    if col1.button("⬅️ Back"):
        st.session_state.page = 2
    if col2.button("Tampilkan Hasil 📊"):
        st.session_state.score += 1 if olahraga == "Jarang" else 2 if olahraga == "1–2 kali / minggu" else 3
        st.session_state.page = 4

# ===== PAGE 4 : HASIL =====
elif st.session_state.page == 4:
    st.subheader("📊 Hasil Kuesioner")
    st.write(f"Total skor kamu: **{st.session_state.score}/9**")

    if st.session_state.score >= 8:
        st.image("assets/healthy.gif", width=300)
        st.success("🟢 Kamu sangat sehat. Pertahankan!")
    elif st.session_state.score >= 5:
        st.image("assets/medium.gif", width=300)
        st.warning("🟡 Kamu sehat, tapi masih bisa ditingkatkan.")
    else:
        st.image("assets/unhealthy.gif", width=300)
        st.error("🔴 Kamu perlu memperbaiki pola hidupmu.")

    if st.button("🔄 Test Ulang"):
        reset_app()
