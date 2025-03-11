import datetime
import pandas as pd
import streamlit as st


def validate_input(input, default):
    if input not in st.session_state:
        st.session_state[input] = default


now = datetime.datetime.now()


st.title("Form Test")

##
# Form Validation
#
validate_input("text_input", "Enter text here")
validate_input("text_area", "Enter text here")
validate_input("date_input", now.today())
validate_input("time_input", now.time())
validate_input("number_input", 1)
validate_input("select_box", "")
validate_input("multi_select", [])
validate_input("color_picker", "#000000")
validate_input("select_slider", "Option 1")
validate_input("slider", 1)
validate_input("toggle", False)
validate_input("checkbox", False)
validate_input("radio", "Option 1")

##
# Form Input
#
st.header("Form Input")
with st.form(key="form"):
    st.subheader("Text Input")
    st.text_input("Text Input", key="text_input")
    st.text_area("Text Area", key="text_area")
    st.date_input("Date Input", key="date_input")
    st.time_input("Time Input", key="time_input")
    st.number_input("Number Input", 1, 100, key="number_input")
    st.subheader("Select Input")
    st.selectbox(
        "Select Box", ["", "Option 1", "Option 2", "Option 3"], key="select_box"
    )
    st.multiselect(
        "Multi Select", ["Option 1", "Option 2", "Option 3"], key="multi_select"
    )
    st.color_picker("Color Picker", key="color_picker")
    st.subheader("Slider Input")
    st.select_slider(
        "Select Slider",
        options=["Option 1", "Option 2", "Option 3"],
        key="select_slider",
    )
    st.slider("Slider", 1, 100, key="slider")
    st.subheader("Switch Input")
    st.toggle("Toggle", key="toggle")
    st.checkbox("Checkbox", key="checkbox")
    st.radio("Radio", ["Option 1", "Option 2", "Option 3"], key="radio")
    st.subheader("Complex Input")
    uploaded_file = st.file_uploader("File Uploader", type=["txt"], key="file_uploader")
    audio_value = st.audio_input("Audio Input", key="audio_input")
    camera_value = st.camera_input("Camera Input", key="camera_input")
    st.divider()
    st.form_submit_button("Submit")

##
# Form Output
#
st.header("Form Output")

st.subheader("Simple Input")

df = pd.DataFrame(
    {
        "Input": [
            "Text Input",
            "Text Area",
            "Date Input",
            "Time Input",
            "Number Input",
            "Select Box",
            "Multi Select",
            "Color Picker",
            "Select Slider",
            "Slider",
            "Toggle",
            "Checkbox",
            "Radio",
        ],
        "Value": [
            st.session_state.text_input,
            st.session_state.text_area,
            st.session_state.date_input.strftime("%Y-%m-%d"),
            st.session_state.time_input.strftime("%H:%M"),
            st.session_state.number_input,
            st.session_state.select_box,
            ", ".join(st.session_state.multi_select),
            st.session_state.color_picker,
            st.session_state.select_slider,
            st.session_state.slider,
            st.session_state.toggle,
            st.session_state.checkbox,
            st.session_state.radio,
        ],
    },
)

st.table(df)

st.subheader("File Upload")

if uploaded_file is not None:
    st.text(uploaded_file.getvalue())
else:
    st.text("No file uploaded.")

st.subheader("Audio Input")

st.audio(audio_value)

st.subheader("Camera Input")

if camera_value:
    st.image(camera_value)
