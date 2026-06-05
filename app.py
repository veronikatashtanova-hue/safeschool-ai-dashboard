import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="SafeSchool AI Dashboard",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 SafeSchool AI Dashboard")
st.caption("AI-assisted safety and security monitoring prototype for the primary school project")

st.sidebar.header("Operation Mode")

mode = st.sidebar.radio(
    "Select school safety mode:",
    [
        "Normal school mode",
        "After-hours mode",
        "Security lockdown",
        "Fire mode"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("Last system update:")
st.sidebar.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if mode == "Normal school mode":
    alert_level = "Normal"
    main_message = "School is operating under normal daily conditions."
    status = {
        "G1 Main Pedestrian Gate": "Open for pedestrians",
        "G2 Emergency / Service Gate": "Closed to normal traffic",
        "Bollards at G1": "Raised",
        "Bollards at G2": "Raised",
        "Access-Controlled Doors": "Controlled",
        "Automated Windows": "Ventilation mode",
        "Fire Alarm System": "Normal",
        "CCTV System": "Monitoring"
    }
    alerts = [["Info", "All systems normal", "No action required"]]

elif mode == "After-hours mode":
    alert_level = "Warning"
    main_message = "After-hours mode is active. Semi-public facilities remain monitored."
    status = {
        "G1 Main Pedestrian Gate": "Limited pedestrian access",
        "G2 Emergency / Service Gate": "Closed",
        "Bollards at G1": "Raised",
        "Bollards at G2": "Raised",
        "Access-Controlled Doors": "Semi-public access only",
        "Automated Windows": "Closed and monitored",
        "Fire Alarm System": "Normal",
        "CCTV System": "Enhanced monitoring"
    }
    alerts = [
        ["Warning", "After-hours use is active", "Monitor sports, assembly and canteen areas"],
        ["Info", "Private zones remain controlled", "No action required"]
    ]

elif mode == "Security lockdown":
    alert_level = "Security"
    main_message = "Security lockdown activated. Envelope, gates and access zones are secured."
    status = {
        "G1 Main Pedestrian Gate": "Restricted",
        "G2 Emergency / Service Gate": "Emergency access only",
        "Bollards at G1": "Raised and locked",
        "Bollards at G2": "Raised and locked",
        "Access-Controlled Doors": "Locked by zone; free egress maintained",
        "Automated Windows": "Ground-floor windows closed",
        "Fire Alarm System": "Normal",
        "CCTV System": "AI anomaly detection active"
    }
    alerts = [
        ["Critical", "Lockdown mode activated", "Check G1, G2, windows and ACD status"],
        ["Warning", "AI CCTV anomaly detection active", "Review perimeter camera feed"]
    ]

else:
    alert_level = "Emergency"
    main_message = "Fire mode activated. Evacuation and emergency response have priority."
    status = {
        "G1 Main Pedestrian Gate": "Evacuation route active",
        "G2 Emergency / Service Gate": "Available for fire service",
        "Bollards at G1": "Emergency override available",
        "Bollards at G2": "Lowered for emergency access",
        "Access-Controlled Doors": "Fail-safe released",
        "Automated Windows": "Selected smoke-exhaust windows open",
        "Fire Alarm System": "Alarm active",
        "CCTV System": "Evacuation monitoring"
    }
    alerts = [
        ["Emergency", "Fire alarm active", "Evacuation routes prioritized"],
        ["Emergency", "G2 available for emergency services", "Keep emergency/service route clear"],
        ["Info", "Access-controlled doors released", "Egress maintained"]
    ]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Current mode", mode)
col2.metric("Alert level", alert_level)
col3.metric("External CCTV", "8 cameras")
col4.metric("Internal CCTV", "30 cameras")

st.info(main_message)

st.subheader("Live System Status")
status_df = pd.DataFrame(
    list(status.items()),
    columns=["System component", "Current status"]
)
st.dataframe(status_df, use_container_width=True)

st.subheader("Safety Devices in the Proposed Design")
devices = pd.DataFrame({
    "Device group": [
        "Gate G1",
        "Gate G2",
        "External CCTV",
        "Internal CCTV",
        "Access-controlled doors",
        "Retractable bollards",
        "Automated windows",
        "Fire alarm devices"
    ],
    "Quantity / code": [
        "1 main pedestrian gate",
        "1 emergency/service gate",
        "C1–C8 = 8 cameras",
        "CCTV-1–CCTV-30 = 30 cameras",
        "ACD-1–ACD-6 = 6 doors",
        "G1 and G2 bollard zones",
        "Schüco automated monitored windows",
        "Smoke detectors + manual call points"
    ],
    "Safety role": [
        "Daily controlled pedestrian access",
        "Emergency and service access",
        "Perimeter, parking, sports and open-area monitoring",
        "Entrance, corridors, stairs and shared-area monitoring",
        "Restrict movement between access zones",
        "Prevent unauthorized vehicle entry",
        "Close in security mode and open selected units in fire/smoke mode",
        "Activate fire mode and emergency response"
    ]
})
st.dataframe(devices, use_container_width=True)

st.subheader("Active Alerts")
alerts_df = pd.DataFrame(alerts, columns=["Level", "Alert", "Recommended action"])
st.dataframe(alerts_df, use_container_width=True)

st.subheader("AI / Automation Logic")
logic = pd.DataFrame({
    "Input": [
        "CCTV detects movement near perimeter after school hours",
        "Vehicle approaches G2",
        "Door remains open too long",
        "Security lockdown is activated",
        "Fire alarm is activated",
        "Bollard sensor reports movement or failure"
    ],
    "AI / automation decision": [
        "Classifies activity as abnormal for the time zone",
        "Checks RFID, ANPR or intercom authorization",
        "Checks door status against permitted opening time",
        "Activates security mode",
        "Activates fire mode",
        "Checks position and safety-loop signal"
    ],
    "System response": [
        "Alert is sent to the monitoring room",
        "Bollards lower only for authorized vehicles",
        "Warning appears in the dashboard",
        "Windows close; bollards remain raised; controlled doors lock by zone",
        "Controlled doors release; selected smoke-exhaust windows open; G2 becomes available",
        "Maintenance or security alert is displayed"
    ]
})
st.dataframe(logic, use_container_width=True)

st.subheader("Privacy and Safety Rules")
st.markdown("""
- No facial recognition is required for this prototype.
- Cameras are not placed in toilets, changing rooms, medical rooms or private sanitary areas.
- CCTV is used for movement, vehicle and restricted-zone monitoring.
- Fire mode has priority over normal security restrictions.
- Access-controlled doors must maintain free egress during evacuation.
""")
