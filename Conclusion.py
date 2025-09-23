import streamlit as st

st.divider()
def red_divider(thickness=3):
    st.markdown(f'<hr style="border:{thickness}px solid red">', unsafe_allow_html=True)

st.title("Conclusion and recomendation")
red_divider()
st.write("""In conclusion, Death Grips is much more than an experimental hip-hop band: they are a project that redefines what it means to make music in the 21st century. Throughout their discography,
they have demonstrated a unique ability to unite genres as disparate as punk, electronic, noise, industrial, and rap, always with a spirit of confrontation and a DIY aesthetic that breaks with industry rules.
Their sound, sometimes chaotic and aggressive, sometimes hypnotic and cerebral, does not seek to please the listener, but rather to shake them up,
make them uncomfortable, and push them toward new ways of experiencing music.
The group's strength lies in the combination of its elements: Zach Hill's explosive percussion, Andy Morin's cold and risky production,
and the imposing presence of MC Ride, who turns every lyric into an act of violence or poetic rebellion. Together they have built a sound universe that is not limited to a defined style,
but constantly evolves, moving between brutality and the most radical experimentation.
Death Grips has also managed to maintain an aura of mystery and autonomy that reinforces its cultural impact. With unexpected releases, anti-industry attitudes,
and a conscious rejection of music market conventions, they have become a symbol of artistic resistance. Their legacy is measured not only in albums,
but in the influence they have left on an entire generation of artists and listeners who are looking for something different, something that escapes the conventional.
In short, Death Grips is a band that challenges, provokes, and pushes the boundaries of what is possible in music.
Their work is not easy to digest, but that is precisely where its power lies: in reminding us that music can also be confrontation, radical art, and absolute freedom.
""")

st.image("bloodmoon.gif", caption="death grips-blood moon")

st.header("Recomendations")
st.write("here are recomendations for the songs of each album")
red_divider()
st.header("Exmilitary and The Money Store")
red_divider()
col1, col2 = st.columns(2)
col1.write("Guillotine-Exmilitary")
col1.write("Spread Eagle Cross the Block-Exmilitary")
col1.write("Takyon (Death Yon)-Exmilitary")
col2.write("Get-got-The Money Store")
col2.write("System blower-The Money Store")
col2.write("Bitch please-The Money Store")

st.header("No Love Deep Web and Government Plates")
red_divider()
col1, col2 = st.columns(2)
col1.write("Lil Boy-No Love Deep Web")
col1.write("No Love-No Love Deep Web")
col1.write("Black Dice-No Love Deep Web")
col2.write("Birds-Government Plates")
col2.write("You Might Think He Loves You For..-Government Plates")
col2.write("This Is Violence Now (Don´t Get Me Wrong)-Government Plates")

st.header("The Powers That B and Bottomless Pit")
red_divider()
col1, col2 = st.columns(2)
col1.write("The Powers That B-The Powers That B")
col1.write("Billy Not Really-The Powers That B")
col1.write("On GP-The Powers That B")
col2.write("Giving Bad People Good Ideas-Bottomless Pit")
col2.write("Spikes-Bottomless Pit")
col2.write("Three Bedrooms In a Good Neighborhood-Bottomless Pit")

st.header("Year Of The Snitch and Singles/Ep")
red_divider()
col1, col2 = st.columns(2)
col1.write("Shitshow-Year Of The Snitch")
col1.write("Flies-Year Of The Snitch")
col1.write("Disappointed-Year Of The Snitch")
col2.write("True bulture-Death Grips Single")
col2.write("Steroids-EP")
col2.write("Face melter-Death Grips EP")

col1.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDVxYndhNDkyMmVqM3c0Z2w2a3RhcnM2aGg3MG9ucDhrZHQ0dmdibSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mTnF5u6rWMMZW/giphy.gif")
col2.image("death minions.webp")
st.write("Thats all thanks for reading this page made for 3 fans of death Grips")
st.write("Authors of the page:")
st.write("G/0o")
st.write("E/N1c")
st.write("M/Lo12")
st.write("if you want to contribute / correct contact us at this email address")
st.write("lobo122033@gmail.com")