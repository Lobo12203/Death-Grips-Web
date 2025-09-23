import streamlit as st

st.set_page_config(
    page_title="Death Grips",
    page_icon=":pirate_flag:"
    )

st.title("Death grips its a complicated band")
st.badge("god content", color="green", icon=":material/done_outline:")
st.write("Death Grips is an American experimental hip-hop band formed in 2010 in Sacramento, California. The group consists of Stefan Burnett, known as MC Ride, who delivers raw and intense vocals, Zach Hill, a drummer and producer known for his chaotic and complex drumming style, and Andy Morin, often called Flatlander, who handles production, sampling, and electronic sound design. Their music blends hip-hop with elements of punk, industrial, noise, and electronic, creating a sound that is aggressive, unpredictable, and influential.The band quickly gained attention with their debut mixtape Exmilitary (2011), followed by their first studio album The Money Store (2012), which received critical acclaim for its originality and energy. Later releases like No Love Deep Web (2012), Government Plates (2013), and the double album The Powers That B (2015) pushed boundaries further, often challenging listeners with abrasive sounds and confrontational themes.Death Grips are also known for their unconventional approach to the music industry: they have leaked their own albums, canceled shows, and rarely give interviews, adding to their mysterious and rebellious reputation. Their visual style, cover art, and live performances reflect the same chaotic and experimental energy as their music. Despite their difficult-to-classify sound, Death Grips have developed a dedicated global following and are considered one of the most innovative and disruptive acts in modern experimental music.")

# Helper function for red divider
def red_divider(thickness=3):
    st.markdown(f'<hr style="border:{thickness}px solid red">', unsafe_allow_html=True)


st.divider()  
col1, col2 = st.columns(2)
col1.image("members1.webp")
col2.image("members2.webp")

# Members section
st.header("Members")
red_divider()
st.write("here is some information of the members of the band")

st.header("MC Ride (Stefan Corbin Burnett)")
red_divider()
st.write(
    "He was born on May 10, 1978, in Sacramento, very private and avoids interviews, "
    "studied visual arts before turning to music, also active as a painter, rapped earlier "
    "in a group called Fyre with his brother, his lyrics are cryptic and surreal with aggressive delivery, "
    "adds punk-like intensity to Death Grips, has not released solo albums outside the group"
)
st.image("MCride.jpg")

st.header("Zach Hill")
red_divider()
st.write(
    "He was born on December 28, 1979, in Sacramento, started drumming young and left high school at 15, "
    "known for chaotic and experimental drumming style that drives Death Grips’ sound, "
    "also works as a visual artist, played in bands like Hella, Nervous Cop and Drumgasm, "
    "released solo albums including Astrological Straits and Face Tat, collaborated widely and created projects "
    "like the I.L.Y’s with Andy Morin and Undo K from HOT, influenced by experimental rock and avant-garde rhythm styles"
)
st.image("Zachhill.webp")

st.header("Andy Morin (Flatlander)")
red_divider()
st.write(
    "He was born on May 16, 1986, less public than the others and avoids the spotlight, "
    "handles the production side of Death Grips with sampling, electronics, and noise textures, "
    "co-founded the I.L.Y’s with Zach Hill releasing several albums, launched A2B2 Records as an experimental label "
    "and creative platform, has uploaded solo experimental tracks to SoundCloud, brings the industrial and electronic "
    "influences that shape much of Death Grips’ atmosphere"
)
st.image("Andymorin.webp")

st.header("Death Grips overall")
red_divider()
st.write("their sound blends hip-hop, punk, industrial, noise and electronic music, influenced by acts like björk whose vocals feature on niggas on the moon, they are known for chaotic live shows, cryptic aesthetics and breaking industry norms such as leaking their own albums, records like fashion week (instrumental) and the powers that b (double album) show their experimental approach and refusal to follow conventions")
st.image("members3.webp")