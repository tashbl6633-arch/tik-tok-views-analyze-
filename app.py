import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="International Growth Engine", page_icon="🚀", layout="wide")

st.title("🚀 TikTok International Solution Engine")
st.markdown("Paste your video link below to get your immediate global hook, audio, and concept solutions.")

st.markdown("---")

# The Link Paste Engine
st.subheader("📋 Paste Video Link for Instant Solutions")
video_url = st.text_input("Enter your TikTok video URL here:", placeholder="https://www.tiktok.com/@username/video/...")

if st.button("Generate Solution Blueprint"):
    if not video_url:
        st.warning("Please paste a valid TikTok link first.")
    else:
        with st.spinner("Analyzing your video link and generating live global strategies..."):
            try:
                # Direct Streamlit Secrets Check
                if "GEMINI_API_KEY" in st.secrets:
                    api_key = st.secrets["GEMINI_API_KEY"]
                else:
                    st.error("❌ Your API Key is missing inside Streamlit! Please check your Streamlit Cloud Dashboard settings under Secrets.")
                    st.stop()
                
                # Active Google Connection
                genai.configure(api_key=api_key)
                
                system_instruction = (
                    "You are an expert TikTok Growth Engine optimizing content for international markets (US/UK/Global) to hit 2,000-3,000 views.\n"
                    "CRITICAL: Do not tell the user what they did wrong. Do not give negative feedback. Provide ONLY action steps.\n"
                    "Give me exactly 3 international hooks, 1 trending background audio direction, and 1 global video structural concept based strictly on the content details found in the link."
                )
                
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    generation_config={"temperature": 0.7}
                )
                
                user_prompt = f"{system_instruction}\n\nAnalyze this video link right now: {video_url}"
                
                response = model.generate_content(user_prompt)
                
                # Output the unique real-time strategy plan
                st.success("Analysis Complete! Here is your Action Plan:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Engine Connection Error: {e}")
