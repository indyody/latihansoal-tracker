
import streamlit as st
import time

st.set_page_config(page_title="Latihan Soal Tracker", layout="centered")

st.title("🧠 Latihan Soal & Progres Belajar")

# Timer sederhana
if "start_time" not in st.session_state:
    st.session_state.start_time = None

st.subheader("⏱️ Timer Latihan")
if st.button("Mulai Timer"):
    st.session_state.start_time = time.time()
if st.session_state.start_time:
    elapsed = int(time.time() - st.session_state.start_time)
    st.write(f"Sudah latihan selama: **{elapsed // 60} menit {elapsed % 60} detik**")

# Log aktivitas
st.subheader("📝 Log Aktivitas")
with st.form("log_form"):
    aktivitas = st.text_input("Aktivitas (misal: Latihan soal kelarutan Ksp-S)")
    submitted = st.form_submit_button("Catat")
    if submitted and aktivitas:
        if "logs" not in st.session_state:
            st.session_state.logs = []
        st.session_state.logs.append(aktivitas)

# Tampilkan log
if "logs" in st.session_state and st.session_state.logs:
    st.subheader("📚 Riwayat Aktivitas")
    for i, log in enumerate(reversed(st.session_state.logs), 1):
        st.markdown(f"{i}. {log}")
