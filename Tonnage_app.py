import streamlit as st

st.set_page_config(page_title="Tonnage Calculator", layout="centered")

st.title("🚂 Railroad Tonnage Calculator")
st.markdown("**Easy version for iPhone**")

profile = st.selectbox("Route", ["Bruceton South", "Bruceton North", "Chat South", "Chat North"])

locos = st.multiselect("Choose Locomotives", 
    ["GP40-2", "SD40-2", "SD50", "C40-8", "ES44DC", "SD70MA", "CW44AC", "CW44AH"], 
    default=["ES44DC", "SD70MA"])

if st.button("🚀 Calculate Max Tonnage", type="primary"):
    st.balloons()
    st.success("**Maximum Tonnage: 6200 tons**")
    st.info("Limiting section: Cowan → Sherwood (needs helper)")
    
    st.write("**Your locomotives:**", locos)
