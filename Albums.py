import streamlit as st

st.title("Albums")

st.divider()
def red_divider(thickness=3):
    st.markdown(f'<hr style="border:{thickness}px solid red">', unsafe_allow_html=True)

st.write("Here is all discography of death grips")
st.header("1.-Exmilitary(2011)")
red_divider()
col1, col2 = st.columns(2)
col1.image("Exmilitary.WEBP")
col2.write("""
Exmilitary its the "first" release of the band and one of their best releases to date, this mixtape is what truly put Death Grips on the underground map sounding
raw aggressiv and untamed and it was released for free online, wich fits perfectly whit their DIY asthetic  and anti-industry standse.
Its a fusion of hardcore, hip-hop, Punk, Industrial noice and experimental sampling like in the song Spread Eagle Across the Block.
MC Ride´s vocals are intese: Screaming, ranting and rapping around edge that´s more primal than polished.
Some of the tracks that stand out are beware[1], tackyon[5], known for it[9] and Spread Eagle Across the Block[3] feel like pure power, its adrenaline in its purest feeling, lyrics
like "I fuck the music, I make it cum I fuck the music with my serpent tongue" makes MC Ride the vocalist and main face of the group look like he is defying
music standards, trying to project an image of rebellion.
This album is essential we need to understand the DNA of Death Grips

In my opinion this is a must hear, but if you are someone that its not so related with the hardcore, IDM, Electronic, Experimental music id recommend u better
go and listen to The Money Store (TMS) and then No Love Deep Web (NLDW), use it as an introduction ton their sound, trust me you'll thank us later.
""")
col1.write("Track List:")
col1.write("1.-Beware")
col1.write("2.-Guillotine")
col1.write("3.-Spread Eagle Cross the Block")
col1.write("4.-Lord of the Game")
col1.write("5.-Takyon (Death Yon)")
col1.write("6.-Klink")
col1.write("7.-Culture Shock")
col1.write("8.-Thru The Walls")
col1.write("9.-Known For It")
col1.write("10.-I Want it I Need It")
col1.write("11.-Blood Creepin")
st.audio("spread.mp3")
st.write("Song: Spread Eagle Across the Block")

st.header("2.-The Money Store(2012)")
red_divider()
col1, col2 = st.columns(2)
col1.image("moneys.jpg")
col2.write("""
The Money Store is their second release and debut album, a great introduction to Death Grips.
After Exmilitary gained traction, This was Death Grips´first major label debut and a major leap in production quality and exposure beeng more
structured than Exmilitary but it retains their chaos and confrontational sound.
Their sound is very experimental, explosive, creative sample, rare, aggresive beats and sints.
Some of the tracks that stand out are Get Got{1}, I've Seen Footage{2} being one of their most famous tracks and has something rhythmic, and Hacker{13} being a good ending i
nviting you to keep listening to their songs.
But it has something that grabs you like something new.  If don´t like it the first time lisening the album i recomend you lisent and a second time
because i known its dificult to like this kind of music but please give it a try .
""")
col2.image("Backmoneystore.JPG")
col1.write("Track List:")
col1.write("1.-Get Got")
col1.write("2.-The Fever")
col1.write("3.-Lost Boys")
col1.write("4.-Blackjack")
col1.write("5.-Hustle Bones")
col1.write("6.-I've Seen Footage")
col1.write("7.-Double Helix")
col1.write("8.-System Blower")
col1.write("9.-The Cage")
col1.write("10.-Punk Weight")
col1.write("11.-Fuck That")
col1.write("12.-Bitch Please")
col1.write("13.-Hacker")
st.audio("hacker.mp3")
st.write("Song: Hacker")

st.header("3.-No Love Deep Web(2012)")
red_divider()
col1, col2 = st.columns(2)
col1.image("Nolove.WEBP")
col2.write("""
No Love Deep Web is their third release beeng a diss album because Epic records didn´t want to release the album so they published it in the Deep Web, This is like a rapping
album(we fell it that way) because mc ride focuses on the letter and beeng like homemade samples and beats but its good at his way.
Some of the tracks that stand out are Whammy{7}, Vass Rattle Stars Out The Sky{12} because of the beat, No Love{3}.

""")
col2.image("Noloveback.WEBP")
col2.video("https://youtu.be/NOs51Lvhn64?si=ipBaj-h56uHR21vq")
col2.write("""
This is the first track of the album it has a high symbolic value, conveying a message that is transmitted throughout the album (We recommend searching for its meaning)
""")
col1.write("Track List:")
col1.write("1.-Come Up And Get Me")
col1.write("2.-Lil Boy")
col1.write("3.-No Love")
col1.write("4.-Black Dice")
col1.write("5.-World Of Dogs")
col1.write("6.-Lock Your Doors")
col1.write("7.-Whammy")
col1.write("8.-Hunger Games")
col1.write("9.-Deep Web")
col1.write("10.-Stockton")
col1.write("11.-Pop")
col1.write("12.-Vass Rattle Stars Out The Sky")
col1.write("13.-Artificial Death In The West")
st.audio("Lilboy.mp3")
st.write("Song: Lil Boy")

st.header("4.-Government Plates(2013)")
red_divider()
col1, col2 = st.columns(2)
col1.image("Government Plates.JPG")
col2.write("""Government Plates is one of the most unique releases in Death Grips' discography. Available for free online, this album represents a return to the band's most experimental and daring side,
moving away from the direct brutality of No Love Deep Web to delve into more psychedelic territory, full of abstract electronic layers and unconventional structures.
Here, the sound feels more ethereal and chaotic, as if Death Grips were less interested in creating traditional songs and more in constructing strange and hypnotic soundscapes.
What sets Government Plates apart from the band's other albums is the prominence of beats and electronic textures over MC Ride's vocals. His presence remains intense,
but on several tracks he is perceived more as an additional instrument than as the central axis of the music. This creates an atmosphere in which words, noises, and samples intertwine,
creating an almost surreal effect. The production by Zach Hill and Andy Morin shines with creativity, using unusual sounds and unpredictable structures that challenge the listener.
Among the most notable songs are Birds{5}, which mixes an unusual rhythm with enigmatic phrases repeated almost like a mantra; Feels Like a Wheel{6},
one of the most dynamic and vibrant pieces on the album; and “Whatever I Want (Fuck Who's Watching){11}, which perfectly reflects the band's defiant, anti-industry attitude.
Each track seems designed to disorient and surprise, playing with the familiar and the unknown, the aggressive and the hypnotic.
""")
col2.video("https://youtu.be/y2cQvZPX3OY?si=h_YvPGQvs2Ri7S8Y")
col2.image("bb.gif")
col1.write("Track List:")
col1.write("1.-You Might Think He Loves You For Your Money, But I Know What He Really Loves You For It's Your Brand New Leopard Skin Pillbox Hat")
col1.write("2.-Anne Bonny")
col1.write("3.-Two Heavens")
col1.write("4.-This Is Violence Now (Don´t Get Me Wrong)")
col1.write("5.-Birds")
col1.write("6.-Feels Like a Wheel")
col1.write("7.-I´m Overflow")
col1.write("8.-Big House")
col1.write("9.-Government Plates")
col1.write("10.-Bootleg (Don´t Need Yout Help)")
col1.write("11.-Whatever I Want (Fuck Who´s Watching)")
st.audio("Youmight.mp3")
st.write("Song: You Might Think He Loves You For Your Money, But I Know What He Really Loves You For...")

st.header("5.-The Powers That B(2015)")
red_divider()
col1, col2 = st.columns(2)
col1.image("Power.JPG")
col2.write("""
The Powers That B is perhaps Death Grips' most ambitious project. Divided into two albums—Niggas on the Moon (2014) and Jenny Death (2015)—
it serves as a dual exploration of what chaos means in their music. While the first volume focuses on extreme electronic experimentation, with a fragmented and almost unpredictable sound,
the second leans toward an intensity closer to rock and punk, with guitars, frenetic drums, and explosive energy. Together they form a contrast that perfectly represents the band's duality:
the cerebral and the visceral, the digital and the physical.
On Niggas on the Moon, Death Grips takes its more abstract side to the limit. The entire album uses samples of Björk's voice,
manipulated to the extreme to create a futuristic and disconcerting effect. The result is an album that sounds alien, full of broken percussion, oppressive atmospheres,
and an MC Ride who moves between the paranoid and the brutal. It's a work that demands patience and attention, because there are no concessions to the casual listener:
this is Death Grips at their most experimental and risky.
On the other hand, Jenny Death is the complete opposite: an explosion of raw energy featuring distorted guitars, heavy bass, and drums that sound like a hurricane.
Here, the band feels closer to hardcore punk and industrial metal, but without abandoning its experimental hip-hop essence. Songs like I Break Mirrors With My Face in the United States{2/1},
On GP{2/9}, and Centuries of Damn{2/8} are pure aggression, while songs like “Inanimate Sensation” show a more expansive side, with long instrumental passages that become hypnotic and monumental.
""")
col2.image("Nonthemoon.jpg")
col1.write("Track List (two Discs):")
col1.write("1.-Up My Sleeves")
col1.write("2.-Billy Not Really")
col1.write("3.-Black Quaterback")
col1.write("4.-Say Hey Kid")
col1.write("5.-Have a Sad Cum")
col1.write("6.-Fuck Me Out")
col1.write("7.-Voila")
col1.write("8.-Big Dipper")
col1.write("2 disc")
col1.write("1.-I Break Mirros With My Face In The United States")
col1.write("2.-Inanimate Sensation")
col1.write("3.-Turned Off")
col1.write("4.-Why a Bitch Gotta Lie")
col1.write("5.-PSS PSS")
col1.write("6.-The Powers That B")
col1.write("7.-Betond Alive")
col1.write("8.-Centuries of Damn")
col1.write("9.-On GP")
col1.write("10.-Death Grips 2.0")
st.audio("Blackquarterback.mp3")
st.write("Song: Black Quaterback")

st.header("6.-Bottomless Pit(2016)")
red_divider()
col1, col2 = st.columns(2)
col1.image("bottom.JPG")
col2.write("""
Bottomless Pit is one of the albums that best represents Death Grips' musical maturity. While earlier works such as Exmilitary and The Money Store had a more unpredictable and wild character,
this album manages to condense all that chaotic energy into a more direct and precise product.
It feels like a synthesis of everything the band had explored before: the fury of punk, industrial noise, aggressive hip-hop rhythms, and digital experimentation,
but with a much more polished and consistent production. It's an album that sounds like a perfectly oiled machine of sonic destruction.
Songs such as Giving Bad People Good Ideas{1}, Hot Head{2}, and “Spikes{3} stand out for their immediate power:
they are relentless bursts of energy that convey a chaotic feeling that the album attempts to convey.
""")
col2.image("bottomback.jpg")
col1.write("Track List:")
col1.write("1.-Giving Bad People Good Ideas")
col1.write("2.-Hot Head")
col1.write("3.-Spikes")
col1.write("4.-Warping")
col1.write("5.-Eh")
col1.write("6.-Bubbles Buried In This Jugle")
col1.write("7.-Trash")
col1.write("8.-Houdini")
col1.write("9.-BB poison")
col1.write("10.-Three Bedrooms In a Good Neighborhood")
col1.write("11.-Ring a Bell")
col1.write("12.-80808")
col1.write("13.-Bottomless Pit")
st.audio("Giving.mp3")
st.write("Song: Giving Bad People Good Ideas")

st.header("7.-Year Of The Snitch(2018)")
red_divider()
col1, col2 = st.columns(2)
col1.image("Yearof.JPG")
col2.write("""
Year of the Snitch is probably Death Grips' strangest and most experimental album. Unlike previous albums that felt more direct or charged with fury, here the band delves into much more chaotic territory,
full of sudden changes, fragmented ideas, and production that defies all expectations. This work sounds like a sonic collage that mixes elements of noise,
distorted electronica, psychedelic rock, and even nods to pop music, but all twisted under the dark and confrontational aesthetic that characterizes the group.
The most striking thing about the album is how it constantly plays with the listener's confusion. There is no clear structure in many of the tracks: some begin as if they were conventional songs
and suddenly break down into a whirlwind of noise, distorted voices, and broken rhythms. MC Ride maintains his visceral style, but here his interventions are even more unpredictable,
going from paranoid whispers to intense screams in a matter of seconds. This reinforces the feeling that Year of the Snitch is less a traditional album and more a sonic journey full of surprises.
Among the standout tracks are Black Paint{3}, with noisy guitars reminiscent of dirty punk; Linda's in Custody{4}, which is pure speed and tension; and “Death Grips Is Online{1},”
a track that seems to mock the internet and digital culture with a hypnotic and almost grotesque rhythm.
""")
col2.image("yearofthe.png")
col1.write("Track List:")
col1.write("1.-Death Grips Is Online")
col1.write("2.-Flies")
col1.write("3.-Black Paint")
col1.write("4.-Linda´s In Custody")
col1.write("5.-The Horn Section")
col1.write("6.-Hahaha")
col1.write("7.-Shitshow")
col1.write("8.-Streaky")
col1.write("9.-Dilemma")
col1.write("10.-Little Richard")
col1.write("11.-The Fear")
col1.write("12.-Outro")
col1.write("13.-Disappointed")
st.audio("Shitshow.mp3")
st.write("Song: Shitshow")