import streamlit as st

st.divider()
def red_divider(thickness=3):
    st.markdown(f'<hr style="border:{thickness}px solid red">', unsafe_allow_html=True)
    
st.title("Concerts")
st.image("mc concert.jpeg")
red_divider()
st.write("""One of Death Grips' most powerful aspects is their live performance. Seeing them in concert is an intense, visceral, unpredictable experience: no long breaks, brutal energy, where the mix of noise, electronics, percussion, and MC Ride's voice is felt in your body as much as in your ears. The shows tend to be sweat-drenched, with an audience that barely breathes, and explosive moments you won't soon forget. These aren't concerts to relax at—they're for immersing yourself in something aggressive, experimental, almost ritualistic.

If you want to know where and when Death Grips is playing, there are several reliable sources to check:

Their official website, thirdworlds.net, has a shows section (“shows” or “tour dates”) where they announce live performances and venues.

Concert tracking platforms such as Songkick, Bandsintown, Last.fm, etc. There you can follow the group, activate alerts, and be notified if they announce a date near your city.

Also, ticket sales sites such as Ticketmaster, SeatGeek, StubHub, among others, depending on the country. These show confirmed concerts and offer tickets when they are in presale or general sale.

At this time (2025), it appears that there are no confirmed upcoming dates for Death Grips on many of these platforms, at least for some regions. But that doesn't mean they won't play again — just that they haven't announced anything new publicly yet.
""")
st.title("Videos of the corcerts")
red_divider()
col1, col2 = st.columns(2)
col1.video("https://youtu.be/B1MDtEfvGBE?si=ybv2SlVB0aF-aMIw")
col1.write("Death Grips Concert Live in Berlin 2023")
col2.video("https://youtu.be/ihV6hEwO7do?si=-34A0GLExDVbbGd_")
col2.write("Death Grips Live At Sick New World (13/05/23)")
col1.video("https://youtu.be/IU0i0gg74_U?si=GB9TSyW0mMoEfd_Z")
col1.write("Death Grips — Live at South Side Ballroom, Dallas, TX (06/10/2023)")
col2.video("https://youtu.be/Xv3atmDavmU?si=ZCrsDobFPIdv4ht8")
col2.write("Death Grips — Paradiso Amsterdam (12/06/23)")
col1.video("https://youtu.be/iCjnjruW_es?si=LmVQvE1bObJctCl3")
col1.write("Death Grips — The Fillmore Charlotte (Full Set, 12/08/2023)")
col2.video("https://youtu.be/qFD74t9SWFE?si=bD-r3STAKRDf5c11")
col2.write("Death Grips — Live at The Observatory North Park, San Diego (Full Concert, Mayo 2023)")