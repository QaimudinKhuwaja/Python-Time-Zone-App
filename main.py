import streamlit as st
from zoneinfo import ZoneInfo
from datetime import datetime


Time_Zones = [
    'UTC',
    'America/New_York',
    'Europe/London',
    'Asia/Tokyo',
    'Australia/Sydney',
    'Asia/Kolkata',
    'Asia/Singapore',
    'Asia/Jakarta',
    'Asia/Dhaka',
    'Asia/Kathmandu',
    'Asia/Rangoon',
    'Asia/Bangkok',
    'Asia/Shanghai',
    'Asia/Hong_Kong',
    'Asia/Taipei',
    'Asia/Vancouver',
    'Asia/Seoul',
    'Asia/Pyongyang',
    'Asia/Tashkent',
    'Asia/Yekaterinburg',
    'Asia/Kabul',
    'Asia/Tehran',
    'Asia/Karachi',
]

st.title('Time Converter🕔')

select_time_zone = st.multiselect("select time zone", Time_Zones, default=["Asia/Karachi", "UTC"])

for t in select_time_zone:
    current_time = datetime.now(ZoneInfo(t)).strftime('%Y-%m-%d %I:%M:%S %p')
    st.write(f"Current time: {t} : {current_time}")

st.subheader("Convert Time between Time Zones ➰")

current_time = st.time_input("Current Time:", datetime.now().time()) 

from_zone = st.selectbox("From time zone:", Time_Zones)
to_zone = st.selectbox("To time zone:", Time_Zones)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time).replace(tzinfo=ZoneInfo(from_zone))
    converted_time = dt.astimezone(ZoneInfo(to_zone)).strftime('%Y-%m-%d %I:%M:%S %p')
    st.write(f"Converted Time: {converted_time}")