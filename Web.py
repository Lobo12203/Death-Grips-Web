import streamlit as st

st.divider()
def red_divider(thickness=3):
    st.markdown(f'<hr style="border:{thickness}px solid red">', unsafe_allow_html=True)
    
st.title("Death Grips Web")
red_divider()
st.write("""
The thirdworlds.net website serves as Death Grips' digital epicenter—their official website—where fans can find everything they need: releases, videos, merchandise, shows, and contact information. From there, they directly manage many of the things that connect the band to their audience, maintaining an aesthetic that harmonizes with their sound: aggressive, direct, somewhat raw, but without losing their identity.

One of the core values of thirdworlds.net is its role as a historical archive as well as a platform for updates. For example, Exmilitary was offered for free on this site when it debuted, demonstrating that the band has used the web not only to sell, but to distribute audiovisual art directly to the public. There is also access to old shows, full albums, lyrics, and official downloads.

The name “Third Worlds” is no accident: it is both the band's imprint and a declaration of artistic independence. Links to the industry are present, but Death Grips has shown that it prefers to have control over its production and distribution, and thirdworlds.net is a key part of that. There have also been times when the site has been a source of controversy: for example, there was a blackout when No Love Deep Web was leaked, fueling rumors of censorship or interference from the label, although what happened was never fully confirmed.
""")
st.title("Image of the Web")
red_divider()
col1, col2 = st.columns(2)
col1.image("Titleweb.png")
col2.image("videosweb.png")
col1.image("releaseweb.png")
col2.image("contactweb.png")