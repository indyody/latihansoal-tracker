
import streamlit as st
import time
from datetime import datetime, timedelta
import pandas as pd

st.set_page_config(page_title="Latihan Soal Tracker", layout="centered")

st.title("📘 Latihan Soal Tracker")

# Sidebar timer
st.sidebar.header("⏱️ Timer Latihan")
if "start_time" not in st.session_state:
    st.session_state.start_time = None
    st.session_state.running = False

def start_timer():
    st.session_state.start_time = datetime.now()
    st.session_state.running = True

def stop_timer():
    st.session_state.running = False

if st.sidebar.button("Mulai"):
    start_timer()

if st.sidebar.button("Berhenti"):
    stop_timer()

if st.session_state.running and st.session_state.start_time:
    elapsed = datetime.now() - st.session_state.start_time
    st.sidebar.success(f"Waktu: {elapsed.seconds // 60} menit {elapsed.seconds % 60} detik")
    time.sleep(1)
    st.rerun()

# Log aktivitas belajar
st.subheader("📒 Log Aktivitas")
log = st.text_input("Tulis aktivitasmu (misal: latihan soal kelarutan, baca teori ikatan kimia)", key="log_input")
submit = st.button("Simpan Log")

if "logs" not in st.session_state:
    st.session_state.logs = []

if submit and log:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.logs.append({"waktu": timestamp, "aktivitas": log})

if st.session_state.logs:
    df_logs = pd.DataFrame(st.session_state.logs)
    st.write("### Riwayat Log")
    st.dataframe(df_logs)

# Progress belajar (dummy berdasarkan log)
st.subheader("📊 Progress Belajar")
progress_data = {}
for entry in st.session_state.logs:
    aktivitas = entry["aktivitas"].lower()
    if "kelarutan" in aktivitas:
        topic = "Kelarutan"
    elif "ikatan kimia" in aktivitas:
        topic = "Ikatan Kimia"
    elif "asam basa" in aktivitas:
        topic = "Asam Basa"
    else:
        topic = "Topik Lain"
    progress_data[topic] = progress_data.get(topic, 0) + 1

if progress_data:
    progress_df = pd.DataFrame({
        "Topik": list(progress_data.keys()),
        "Jumlah Aktivitas": list(progress_data.values())
    })
    st.bar_chart(progress_df.set_index("Topik"))
