# Premature-stop cases for manual tagging

Model `gemini-3.8-flash`. Each case: the agent said SUFFICIENT while at least one gold paragraph was not yet retrieved. Read the evidence, decide why it stopped, and write one cause per case in `tags.csv`.

Causes:
- `parametric`: answer comes from the model's own memory, not from the evidence shown
- `bridge-missed`: the first-hop evidence is there but the second-hop (bridge) paragraph is missing and the model did not notice
- `distractor`: a retrieved non-gold paragraph was taken as the evidence
- `partial-answer`: part of the answer is supported, a required piece is not
- `ambiguous`: the question or gold answer is ambiguous or the gold label looks wrong
- `other`: write why in notes

## hotpotqa: 84 premature stops of 500 questions, 25 sampled

### hotpotqa-01 `5ac160605542994ab5c67d02` (stopped at step 1, stated probability 0.95)

**Question:** Who coached the Indians and was the first Native American to win a gold metal his home country?

**Gold answer:** Jim Thorpe  |  **Model answer:** Jim Thorpe  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Jim Thorpe**: James Francis Thorpe (Sac and Fox (Sauk): "Wa-Tho-Huk", translated as "Bright Path"; May 22 or 28, 1887March 28, 1953) was an American athlete and Olympic gold medalist. A member of the Sac and Fox Nation, Thorpe became the first Native American to win a gold medal for his home country. Considered one of the most versatile athletes of modern sports
2. **Thomas L. Sloan**: Thomas L. Sloan (1863–1940) was the first Native American lawyer to argue before the U.S. Supreme Court, and with his partner Hiram Chase, formed the first Native American law firm in the United States. Sloan was a founder and leader of the Society of American Indians (1911–1923), the first national American Indian rights organization run by and fo
3. **Hiram Chase**: Hiram Chase (Hiram John Hatu Mi Chase) (September 9, 1861 – December 3, 1928), was one of the first Native American Lawyers to argue before the U.S. Supreme Court, and with his partner Thomas L. Sloan, formed the first Native American law firm in the United States. Chase was a leader of the Society of American Indians, the first national American I

**Gold paragraphs NOT retrieved:**

- **Eagle Feather**: Beamus Pierce aka Eagle Feather was a professional football player who played in the National Football League during the 1922 and 1923 seasons. He played college football at the Carlisle Indian School, located in Carlisle, Pennsylvania, before joining the NFL's Oorang Indians. The Indians were a team based in LaRue, Ohio, composed only of Native Am

### hotpotqa-02 `5adc094a55429947ff1738c0` (stopped at step 2, stated probability 1.0)

**Question:** American Blues included the drummer from which American rock band?

**Gold answer:** ZZ Top  |  **Model answer:** ZZ Top  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **Slash's Blues Ball**: Slash's Blues Ball was an American blues rock band that formed in Los Angeles, California in 1996. The band, which comprised lead guitarist Slash, lead vocalist Teddy "Big Bag Zig Zag" Andreadis, bassist Johnny Griparic, drummer Alvino Bennet, rhythm guitarist Bobby Schneck and saxophonist Dave McLaurin, toured as a cover band for two years followi
2. **The Muggs**: The Muggs is an American blues rock band from Detroit, Michigan. Formed in February 2000 by guitarist Danny Methric, bassist Tony DeNardo and drummer Matt Rost. They were ranked in December 2008 on the "100 Hot Unsigned Band" list by "Music Connection". They won several awards including the Best Blues Artist and the Best Rock Band for 2007.
3. **Mabel Greer's Toyshop**: Mabel Greer's Toyshop are an English progressive rock (initially as psychedelic rock) band formed in London, active from 1966 to 1968 that was the precursor to the rock band Yes. Their music was marked by a combination of psychedelic, American blues and classically influenced arrangements with poetic lyrics. Members included Chris Squire, Peter Ban
4. [GOLD] **Frank Beard (musician)**: Frank Lee Beard (born June 11, 1949) is the drummer in the American rock band ZZ Top. Beard was formerly with the bands The Cellar Dwellers, who originally were a three-piece band, The Hustlers, The Warlocks, and American Blues before starting to play and record with Billy Gibbons and Dusty Hill as ZZ Top.
5. **Five Horse Johnson**: Five Horse Johnson is an American blues rock band from Toledo, Ohio, formed in 1995. They have toured with such popular groups as Clutch and Halfway to Gone. The band combines hard rock, blues and other influences into a blend of stoner rock/blues music they call their own. Their second to latest album "The Mystery Spot" featured many special guest
6. **Chris Robinson Brotherhood**: Chris Robinson Brotherhood is an American blues rock band formed in 2011 by Black Crowes singer Chris Robinson while The Black Crowes were on hiatus. The band has released four studio albums: "Big Moon Ritual", "The Magic Door", "Phosphorescent Harvest", and "Any Way You Love, We Know How You Feel". The band consists of Robinson, guitarist Neal Cas

**Gold paragraphs NOT retrieved:**

- **American Blues**: American Blues were an American 1960s Texas-based garage rock band, who played a psychedelic style of blues rock music influenced by the 13th Floor Elevators. They are most notable for including two future members of the band ZZ Top in their ranks, Dusty Hill and Frank Beard. From 1966 to 1968, they played the Dallas-Fort Worth-Houston circuit and 

### hotpotqa-03 `5a7736bc554299373536021b` (stopped at step 1, stated probability 0.95)

**Question:** What composer with an Italian libretto was born 4 March 1678?

**Gold answer:** Antonio Lucio Vivaldi  |  **Model answer:** Antonio Vivaldi  |  EM 0, F1 0.80

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Antonio Vivaldi**: Antonio Lucio Vivaldi (] ; 4 March 1678 – 28 July 1741) was an Italian Baroque composer, virtuoso violinist, teacher and cleric. Born in Venice, he is recognized as one of the greatest Baroque composers, and his influence during his lifetime was widespread across Europe. He composed many instrumental concertos, for the violin and a variety of other
2. **Jacques Hardel**: Jacques Hardel (died March 1678) was a French composer and harpsichordist.
3. **Zanetto**: Zanetto is an opera in one act by Pietro Mascagni to an Italian libretto by Giovanni Targioni-Tozzetti and Guido Menasci. It received its first performance on 2 March 1896 at the Liceo Musicale Rossini in Pesaro. Only 40 minutes long and with cast of two singers, "Zanetto" was originally described by its composer as a "scena lirica" (lyric scene) r

**Gold paragraphs NOT retrieved:**

- **Dorilla in Tempe**: Dorilla in Tempe is a melodramma eroico pastorale in three acts by composer Antonio Vivaldi with an Italian libretto by Antonio Maria Lucchini. The opera premiered at the Teatro San Angelo in Venice on 9 November 1726. Vivaldi later revised the opera numerous times for several difference performances throughout the second half of his career.

### hotpotqa-04 `5ab3c48755429969a97a81b8` (stopped at step 1, stated probability 1.0)

**Question:** What cuisine is described as a cultural blending of Mediterranean influences (such as those created by Italian and Spanish populations)?

**Gold answer:** Argentine cuisine  |  **Model answer:** Argentine cuisine  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Argentine cuisine**: Argentine cuisine is described as a cultural blending of Mediterranean influences (such as those created by Italian and Spanish populations) with and very small inflows (mainly in border areas), Indigenous, within the wide scope of agricultural products that are abundant in the country. Argentine annual consumption of beef has averaged 100 kg (220 
2. **Phuket cuisine**: In the past, Phuket was one of Thailand’s commercial ports which traded with other countries. These cultural influences are reflected in the cuisine and local foods. Phuket cuisine and local food (Baba Peranakan food) is the combination of many cultural food habits, whether they be Chinese, Malay or Thai. Some Phuket local food tastes sweet, such a
3. **Croatian cuisine**: Croatian cuisine is heterogeneous and is known as a cuisine of the regions, since every region of Croatia has its own distinct culinary tradition. Its roots date back to ancient times. The differences in the selection of foodstuffs and forms of cooking are most notable between those in mainland and those in coastal regions. Mainland cuisine is more

**Gold paragraphs NOT retrieved:**

- **Tourism in Argentina**: Argentina is provided with a vast territory and a huge variety of climates and microclimates ranging from tundra and polar in the south to the tropical climate in the north, through a vast expanse of temperate climate and natural wonders like the Aconcagua, the highest mountain in the world outside the Himalayas, the widest river and estuary of the

### hotpotqa-05 `5ae16bce5542997b2ef7d1e8` (stopped at step 1, stated probability 0.85)

**Question:** When is the election held for the position former policy director Krishanti "Krish" Vignarajah is running in?

**Gold answer:** November 6, 2018  |  **Model answer:** 2018  |  EM 0, F1 0.50

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Krishanti Vignarajah**: Krishanti "Krish" Vignarajah is the former policy director for United States First Lady Michelle Obama, and a declared Democratic candidate for Maryland's 2018 governor's race on August 9, 2017.
2. **Director of Policy Planning**: The Director of Policy Planning is the United States Department of State official in charge of the Department's internal think tank, the Policy Planning Staff. In the Department, the Director of Policy Planning has a rank equivalent to Assistant Secretary. The position has traditionally been held by many members of the U.S. foreign policy establish
3. **Jennifer Branstetter**: Jennifer Branstetter served as the Secretary of Planning and Policy for the administration of former Pennsylvania Governor Tom Corbett. In that position, she was part of the Governor's "senior staff." As Secretary of Planning and Policy, she manages policy development for the Governor's Office, including energy policy. She also served as the policy

**Gold paragraphs NOT retrieved:**

- **Maryland gubernatorial election, 2018**: The 2018 Maryland gubernatorial election will take place on November 6, 2018, to elect the Governor of Maryland. The Republican and Democratic primaries will be held on June 26, 2018.

### hotpotqa-06 `5adff34555429942ec259baa` (stopped at step 1, stated probability 0.85)

**Question:** Robert Bobby Noble's third football engagement was with a association station where?

**Gold answer:** Bury, Greater Manchester, England  |  **Model answer:** Bury  |  EM 0, F1 0.40

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **Bobby Noble (academic)**: Bobby Noble, aka Jean Bobby Noble or J. Bobby Noble, is a professor at York University in Toronto, Ontario, Canada. He is the author of the books "Masculinities Without Men? " and "Sons of the Movement" and is one of the foremost scholars of transgender studies in North America.
2. [GOLD] **Bobby Noble (footballer, born 1949)**: Robert "Bobby" Noble (25 May 1949 – May 2005), born in Gosforth, Newcastle upon Tyne, was an English professional footballer. He started his career as a central defender for Newcastle United (although he made no senior appearances), going on loan to Barrow before moving on to Bury, then returned to Barrow on a permanent deal. This was followed by m
3. **Masculinities Without Men?**: Masculinities without Men? is a book by Jean Bobby Noble.

**Gold paragraphs NOT retrieved:**

- **Bury F.C.**: Bury Football Club is a professional association football club based in Bury, Greater Manchester, England. The team compete in League One, the third tier of the English football league system.

### hotpotqa-07 `5ac2610f55429951e9e68593` (stopped at step 1, stated probability 1.0)

**Question:** which  Indian businessman and politician owns Mabula Game Reserve 

**Gold answer:** Vijay Vittal Mallya  |  **Model answer:** Vijay Mallya  |  EM 0, F1 0.80

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Mabula Game Reserve**: Mabula Game Reserve is a private game reserve situated in the Limpopo province of South Africa. It is about 12000 ha in area and is about 47 km from Bela Bela (Warmbaths). The current owner of Mabula Game Reserve is the Indian businessman and liquor baron Vijay Mallya.
2. **Thornybush Game Reserve**: Thornybush Game Reserve, is a private game reserve, near Hoedspruit, in the Limpopo province of South Africa. It borders the Kapama Game Reserve and is located close to the Timbavati Game Reserve and the Kruger Park. The Reserve's surface area is approximately 11.000 Ha of mainly open savannah.
3. **Falgore Game Reserve**: Falgore Game Reserve is protected ecosystem designated mainly for games protection in southern Kano State of northern Nigeria. This game reserve is located about 150 kilometers away from Kano city. It lies in Tudun Wada, Doguwa and Sumaila local government areas. It extends to the boundary line between Kano, Kaduna and Bauchi states respectively. I

**Gold paragraphs NOT retrieved:**

- **Vijay Mallya**: Vijay Vittal Mallya (born 18 December 1955) is an Indian businessman and politician who is the subject of an extradition effort to try to force his return from the U.K. to India to face charges of financial crimes. The son of businessman Vittal Mallya, he is the ex-chairman of United Spirits Ltd, the largest spirits company in India and continues t

### hotpotqa-08 `5ab78edc5542995dae37e95c` (stopped at step 1, stated probability 0.95)

**Question:** Where is the school that Tyler Kalinoski went to located?

**Gold answer:** located in Olathe, Kansas  |  **Model answer:** Kansas  |  EM 0, F1 0.40

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Tyler Kalinoski**: Tyler Kalinoski (born December 19, 1992) is an American basketball player for Antwerp Giants in the Belgian League. Kalinoski was a McDonald’s All-American nominee as a senior at Olathe East High School in Kansas and completed his college career for the Davidson Wildcats. He was named Atlantic 10 Conference Men's Basketball Player of the Year in 20
2. **Tyler Consolidated High School**: Tyler Consolidated High School (TCHS) is a public secondary school in Sistersville, West Virginia, United States. It is part of the Tyler County Schools district and is located at 1993 Silver Knight Drive. The school was formed in 1993 when students from Sistersville High School and Tyler County High School consolidated to form one county high scho
3. **Woodville High School (Texas)**: Woodville High School is a public high school located in the city of Woodville, Texas in Tyler County, United States and classified as a 3A school by the UIL. It is a part of the Woodville Independent School District located in central Tyler County. In 2015, the school was rated "Met Standard" by the Texas Education Agency.

**Gold paragraphs NOT retrieved:**

- **Olathe East High School**: Olathe East High School is a public high school located in Olathe, Kansas, United States, serving students in grades 9-12. Olathe East is the largest of four public high schools in Olathe. Olathe East is a member of the Kansas State High School Activities Association and offers a variety of sports programs. Athletic teams compete in the 6A division

### hotpotqa-09 `5adeda67554299728e26c7db` (stopped at step 1, stated probability 0.95)

**Question:** Are Water dropwort and Costus both in the family Apiaceae?

**Gold answer:** no  |  **Model answer:** no  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Water dropwort**: The water dropworts, Oenanthe , are a genus of plants in the family Apiaceae. Most of the species grow in damp ground, in marshes or in water.
2. **Costus osae**: Costus osae is a rare member of the Costus family. One of many rare tropical plants in the Costus family, "Costus osae" is a species native to Costa Rica described in 1997 . It has also been reported from Colombia.
3. **Oxypolis filiformis**: Oxypolis filiformis is a species of flowering plant in the carrot family known by the common names water cowbane and water dropwort. It grows in swamps, freshwater wetlands, and along the borders of ponds in the southeastern United States, as far north as Delaware, as well as the northern Bahamian pineyards of the Bahamas.

**Gold paragraphs NOT retrieved:**

- **Costus**: Costus is a group of perennial herbaceous plants in the family (Costaceae) described by Linnaeus as a genus in 1753. It was formerly known as "Hellenia" after the Finish botanist Carl Niclas von Hellens. It is widespread through tropical and subtropical regions of Asia, Africa, and the Americas.

### hotpotqa-10 `5abcf70b55429959677d6b7e` (stopped at step 1, stated probability 0.95)

**Question:** Wrinkles is a song that was recorded by what American country and Christian country band that was founded in 1982?

**Gold answer:** Diamond Rio  |  **Model answer:** Diamond Rio  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Wrinkles (song)**: "Wrinkles" is a song written by Neil Thrasher and Ronny Scaife, and recorded by American country music group Diamond Rio. It was released in July 2003 as the third single from the album "Completely". The song reached number 16 on the "Billboard" Hot Country Singles & Tracks chart.
2. **Thy Will**: "Thy Will" is a Christian country song recorded by American singer and songwriter Hillary Scott for her collaborative album with the Scott Family, "Love Remains" (2016). Scott co-wrote the faith-affirming song with Bernie Herms and Emily Weisband. It was released April 22, 2016 as the lead single from the record and impacted Christian and country r
3. **Country Boy (Ricky Skaggs song)**: "Country Boy" is a song written by Tony Colton, Albert Lee, and Ray Smith of the British band Heads Hands & Feet, and recorded by American country music artist Ricky Skaggs. It was released in February 1985 as the second single and title track from the album "Country Boy". The song was Ricky Skaggs' ninth number-one country hit. The single went to 

**Gold paragraphs NOT retrieved:**

- **Diamond Rio**: Diamond Rio is an American country and Christian country music band. The band was founded in 1982 as an attraction for the Opryland USA theme park in Nashville, Tennessee, and was originally known as the Grizzly River Boys, then the Tennessee River Boys. It was founded by Matt Davenport, Danny Gregg, and Ty Herndon, the last of whom became a solo a

### hotpotqa-11 `5a87100655429960ec39b71e` (stopped at step 1, stated probability 1.0)

**Question:** Which British Indian novelist and essayist did Anthony Burgess address in a lengthy letter?

**Gold answer:** Salman Rushdie  |  **Model answer:** Salman Rushdie  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **An Essay on Censorship**: An Essay on Censorship is a lengthy letter, in verse, by Anthony Burgess addressed to his fellow novelist Salman Rushdie. Published in the wake of the 1989 Iranian "fatwa" against Rushdie and the Bradford book-burnings that followed, Burgess's letter has been compared to the "Essay on Man" of Alexander Pope.
2. **Anthony Burgess: A Life**: Anthony Burgess: A Life is the title of a biography of the novelist and critic Anthony Burgess (1917-93) by Roger Lewis.
3. **Anthony Burgess Center**: The Anthony Burgess Center of the University of Angers, France, exists to honor the memory of the 20th-century English novelist Anthony Burgess. It houses a collection of books, manuscripts, scores, and other items belonging to Burgess donated by his second wife Liana, and these can be inspected and studied by visitors and scholars. The Center publ

**Gold paragraphs NOT retrieved:**

- **Salman Rushdie**: Sir Ahmed Salman Rushdie, FRSL ( ; Kashmiri: अहमद सलमान रुशदी , ; born 19 June 1947) is a British Indian novelist and essayist. His second novel, "Midnight's Children" (1981), won the Booker Prize in 1981 and was deemed to be "the best novel of all winners" on two separate occasions, marking the 25th and the 40th anniversary of the prize. Much of h

### hotpotqa-12 `5ae13e205542997b2ef7d157` (stopped at step 1, stated probability 0.85)

**Question:** The 43d Air Mobility Operations Group is stationed at which largest military installation?

**Gold answer:** Fort Bragg  |  **Model answer:** Fort Bragg  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **721st Air Mobility Operations Group**: The 721st Air Mobility Operations Group is a United States Air Force (USAF) unit assigned to the 521st Air Mobility Operations Wing, stationed at Ramstein Air Base, Germany.
2. [GOLD] **43d Air Mobility Operations Group**: The 43d Air Mobility Operations Group is an active duty air mobility unit at Pope Field, Fort Bragg, North Carolina (formerly Pope AFB), and is part of the Air Mobility Command (AMC) USAF Expeditionary Center. The unit is composed of five squadrons, including one of the only two active Air Force aeromedical evacuation squadrons based in the United 
3. **43d Aeromedical Evacuation Squadron**: The 43d Aeromedical Evacuation Squadron (43 AES) is a unit of the United States Air Force. It is part of the 43d Air Mobility Operations Group at Pope Army Air Field, North Carolina. It is a component of Eighteenth Air Force and Air Mobility Command of the United States Air Force, and is part of the air force component of United States Transportati

**Gold paragraphs NOT retrieved:**

- **Fort Bragg**: Fort Bragg, North Carolina, is a military installation of the United States Army and is the largest military installation in the world (by population) with more than 50,000 active duty personnel. The installation is located within Cumberland, Hoke, Harnett and Moore counties. The installation borders the towns of Fayetteville, Spring Lake and South

### hotpotqa-13 `5a7ecae055429934daa2fc6a` (stopped at step 1, stated probability 0.98)

**Question:** Are Nathalie Sarraute and Anchee Min both writers?

**Gold answer:** yes  |  **Model answer:** Yes  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Nathalie Sarraute**: Nathalie Sarraute (] ; July 18, 1900 – October 19, 1999) was a French lawyer and writer.
2. **Lucette Finas**: Lucette Finas (born July 13, 1921) is a French author and essayist, part of the structuralist movement. She has published several articles relating interviews with French scholars and philosophers in the 1970s, like writers Nathalie Sarraute, philosopher and historian Michel Foucault or philosopher Jacques Derrida.
3. **Katherine (Min novel)**: Katherine (ISBN  ) is the first novel by Anchee Min. It was published by Riverside Books in 1995.

**Gold paragraphs NOT retrieved:**

- **Anchee Min**: Anchee Min or Min Anqi (; born January 14, 1957 in Shanghai, China) is a Chinese-American author who lives in San Francisco and Shanghai. Min has published two memoirs, "Red Azalea" and "", and six historical novels. Her fiction emphasizes strong female characters, such as Jiang Qing, the wife of chairman Mao Zedong, and Empress Dowager Cixi, the l

### hotpotqa-14 `5ab5e9865542992aa134a3db` (stopped at step 1, stated probability 0.95)

**Question:** What type of beliefs does Mount Ida and Rhea have in common?

**Gold answer:** Greek mythology  |  **Model answer:** Greek mythology  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Mount Ida**: In Greek mythology, two sacred mountains are called Mount Ida, the "Mountain of the Goddess": Mount Ida in Crete; and Mount Ida in the ancient Troad region of western Anatolia (in modern-day Turkey) which was also known as the "Phrygian Ida" in classical antiquity and is the mountain that is mentioned in the Iliad of Homer and the Aeneid of Virgil.
2. **Mount Ida High School**: Mount Ida High School is a public six-year high school located in Mount Ida, Arkansas, United States. Mount Ida is one of three public high schools in Montgomery County and the only high school of the Mount Ida School District. For 2010–11, the school enrollment was 256 students occupying grades 7 through 12.
3. **Mount Ida (community), Wisconsin**: Mount Ida is an unincorporated community located in the town of Mount Ida in Grant County, Wisconsin, United States. It is located along U.S. Route 18.

**Gold paragraphs NOT retrieved:**

- **Rhea (mythology)**: Rhea ( ; Greek: Ῥέα , ] ) is a character in Greek mythology, the Titaness daughter of the earth goddess Gaia and the sky god Uranus, and sister and wife to Cronus. In early traditions, she is known as "the mother of gods" and therefore is strongly associated with Gaia and Cybele, who have similar functions. The classical Greeks saw her as the mothe

### hotpotqa-15 `5ae3b1ba5542992f92d82343` (stopped at step 1, stated probability 1.0)

**Question:** Which university did the third pick by the Philadelphia 76ers in the 2014 NBA draft attend before he was drafted?

**Gold answer:** University of Kansas  |  **Model answer:** University of Kansas  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Joel Embiid**: Joel Hans Embiid ( ; born 16 March 1994) is a Cameroonian professional basketball player for the Philadelphia 76ers of the National Basketball Association (NBA). After one year of college basketball at the University of Kansas, he was drafted with the third overall pick in the 2014 NBA draft by the 76ers. He has nicknamed himself "The Process" in r
2. **Ben Simmons**: Benjamin David Simmons (born 20 July 1996) is an Australian professional basketball player for the Philadelphia 76ers of the National Basketball Association (NBA). A versatile forward from Melbourne, Simmons attended Box Hill Senior Secondary College before moving to the United States to attend Montverde Academy in Montverde, Florida. He played one
3. **Glenn Robinson III**: Glenn Alan Robinson III (born January 8, 1994) is an American professional basketball player for the Indiana Pacers of the National Basketball Association (NBA). Robinson played college basketball for the Michigan Wolverines for two years. He was an All-State high school basketball player for Lake Central High School in St. John, Indiana. After his

**Gold paragraphs NOT retrieved:**

- **2015–16 Philadelphia 76ers season**: The 2015–16 Philadelphia 76ers season was the 77th season of the franchise in the National Basketball Association (NBA). It was also the second straight season that Joel Embiid, their third pick in the 2014 NBA draft, would not suit up for the 76ers due to a leg injury. Philadelphia broke the record for the longest losing streak in American profess

### hotpotqa-16 `5a7b413a5542992d025e67c4` (stopped at step 1, stated probability 0.99)

**Question:** What sport do Straight Blast Gym - Ireland and John Kavanagh have in common?

**Gold answer:** martial arts  |  **Model answer:** Mixed martial arts  |  EM 0, F1 0.80

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Straight Blast Gym - Ireland**: Straight Blast Gym Ireland is a mixed martial arts academy and professional team based in Dublin, Ireland. It is run by John Kavanagh, and is part of Straight Blast Gym International. The team has produced several Ultimate Fighting Championship (UFC) fighters, including UFC Lightweight champion Conor McGregor.
2. **Matt Thornton (martial artist)**: Matt Thornton (born March 25, 1969) is a martial arts athlete, trainer, and founder of Straight Blast Gym International, an association of over 35 gyms worldwide engaged in training athletes in Brazilian jiu-jitsu, boxing and mixed martial arts.
3. **Geasa (band)**: Geasa is a Celtic metal band originating from Dublin, Ireland. Formed by Fergal Purcell and John Kavanagh in 1993 the band combines traditional Celtic music with black metal to form Celtic black metal. They have released one demo album, one EP, and three full-length albums.

**Gold paragraphs NOT retrieved:**

- **John Kavanagh (martial artist)**: John Raymond Kavanagh (born January 18, 1977) is an Irish martial arts coach, brazilian jiu-jitsu practitioner and former professional mixed martial artist. His students include fighters such as Conor McGregor and Gunnar Nelson.

### hotpotqa-17 `5a90503755429916514e7470` (stopped at step 2, stated probability 0.95)

**Question:** What title did the Queen of the United Kingdom of Great Britain and Ireland give to Jeremiah Meyer?

**Gold answer:** Painter in Miniatures  |  **Model answer:** Painter in Miniatures  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **United Kingdom of Great Britain and Ireland**: The United Kingdom of Great Britain and Ireland was established as a sovereign state on 1 January 1801 by the Acts of Union 1800, which merged the kingdoms of Great Britain and Ireland. The growing desire for an Irish Republic led to the Irish War of Independence, which resulted in Ireland seceding from the Union and forming the Irish Free State in
2. **List of British monarchs**: There have been 12 monarchs of the Kingdom of Great Britain and the United Kingdom (see Monarchy of the United Kingdom) since the merger of the Kingdom of England and the Kingdom of Scotland on 1 May 1707. England and Scotland had been in personal union under the House of Stuart since 24 March 1603. On 1 January 1801, Great Britain merged with the 
3. **Irish migration to Great Britain**: Irish migration to Great Britain has occurred from the earliest recorded history to the present. There has been a continuous movement of people between the islands of Ireland and Great Britain due to their proximity. This tide has ebbed and flowed in response to politics, economics and social conditions of both places. Ireland was a feudal Lordship
4. [GOLD] **Jeremiah Meyer**: Jeremiah Meyer {'1': ", '2': ", '3': ", '4': "} (born "Jeremias Majer"; 18 January 1735 – 20 January 1789) was an 18th-century English miniature painter. He was Painter in Miniatures to Queen Charlotte, Painter in Enamels to King George III and was one of the founder members of the Royal Academy.
5. **Confessions of a Teenage Drama Queen (soundtrack)**: Confessions of a Teenage Drama Queen is the soundtrack album for the 2004 American teen comedy film: "Confessions of a Teenage Drama Queen", released on February 17, 2004. The film's lead actress Lindsay Lohan recorded four songs written for the film, including "Drama Queen (That Girl)", that was released as a promotional single in January of that 
6. **RuPaul's Drag Race**: RuPaul's Drag Race is an American reality competition television series produced by World of Wonder for Logo TV and, beginning with the ninth season, VH1. The show documents RuPaul in the search for "America's next drag superstar." RuPaul plays the role of host, mentor, and head judge for this series, as contestants are given different challenges e

**Gold paragraphs NOT retrieved:**

- **Charlotte of Mecklenburg-Strelitz**: Charlotte of Mecklenburg-Strelitz (Sophia Charlotte; 19 May 1744 – 17 November 1818) was by marriage to King George III the Queen of Great Britain and Ireland from her wedding in 1761 until the union of the two kingdoms in 1801, after which she was Queen of the United Kingdom of Great Britain and Ireland until her death in 1818. She was also the El

### hotpotqa-18 `5a7fb1e55542995d8a8ddef7` (stopped at step 1, stated probability 0.95)

**Question:** Which documentary film premiered first, Grizzly Man or Pray the Devil Back to Hell?

**Gold answer:** Grizzly Man  |  **Model answer:** Grizzly Man  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Pray the Devil Back to Hell**: Pray the Devil Back to Hell is a documentary film directed by Gini Reticker and produced by Abigail Disney. The film premiered at the 2008 Tribeca Film Festival, where it won the award for Best Documentary. The film had its theatrical release in New York City on November 7, 2008.
2. **Grizzly Man (soundtrack)**: Grizzly Man is the soundtrack album from the documentary "Grizzly Man", produced by Richard Thompson and released in 2005.
3. **Coyotes (song)**: Coyotes is an American Western song written by Bob McDill and closely associated with cowboy singer Don Edwards. It appears on Edwards' 1993 album "Goin' Back to Texas", and was featured on the soundtrack of the 2005 documentary film "Grizzly Man".

**Gold paragraphs NOT retrieved:**

- **Grizzly Man**: Grizzly Man is a 2005 American documentary film by German director Werner Herzog. It chronicles the life and death of bear enthusiast Timothy Treadwell. The film includes some of Treadwell's own footage of his interactions with grizzly bears before 2003, and of interviews with people who knew, or were involved with Treadwell, as well as professiona

### hotpotqa-19 `5ab7b3cc55429928e1fe3893` (stopped at step 2, stated probability 0.95)

**Question:** Are both Microcachrys and Protea endemic to the same continent ?

**Gold answer:** no  |  **Model answer:** No  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **Protea neriifolia**: Protea neriifolia, also known as oleanderleaf protea, is a flowering plant that is endemic to South Africa.
2. **Protea Hotels by Marriott**: Protea Hotels by Marriott is a leading South African hotel brand headquartered in Cape Town. The brand has more than 10,000 rooms in the African continent. As of April 2016, it is the largest hotel company on the continent, with over 100 managed and franchised properties in 8 African countries.
3. **Protea nitida**: Protea nitida (commonly called Wagon tree, Waboom or Blousuikerbos) is a large, slow-growing "Protea" endemic to South Africa. It is one of the few Proteas that grow into trees, and the only one that has usable timber.
4. **List of birds of South America**: This is a list of the bird species recorded in South America. South America is the "Bird Continent": It hosts 3379 species, more than any other. (Much larger Eurasia is second with 3232.) Colombia's list alone numbers more than 1800 species. Of the continent's species, 2304 are endemic, significantly more than Eurasia's 2018. Nine entire families, 
5. [GOLD] **Microcachrys**: Microcachrys tetragona (Creeping Pine or Creeping Strawberry Pine) is a species of dioecious conifer belonging to the podocarp family (Podocarpaceae). It is the sole species of the genus Microcachrys. The plant is endemic to western Tasmania, where it is a low shrub growing to 1 m tall at high altitudes. Its leaves are scale-like, arranged (unusual
6. **Diselma**: Diselma archeri (Dwarf Pine) or (Cheshunt pine) is a species of plant of the family Cupressaceae and the sole species in the genus Diselma. It is endemic to the alpine regions of Tasmania's southwest and Central Highlands, on the western coast ranges and Lake St. Clair. It is a monotypic genus restricted to high altitude rainforest and moist alpine

**Gold paragraphs NOT retrieved:**

- **Protea**: Protea is both the botanical name and the English common name of a genus of South African flowering plants, sometimes also called sugarbushes (Afrikaans: suikerbos). In local tradition, the Protea flower represents change and hope.

### hotpotqa-20 `5ae1f79f5542997283cd2302` (stopped at step 1, stated probability 1.0)

**Question:** "When a Woman Loves" is the first single by singer R. Kelly from his eleventh studio album named what?

**Gold answer:** "Love Letter"  |  **Model answer:** Love Letter  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **When a Woman Loves (song)**: "When a Woman Loves" is the first single by singer R. Kelly from his eleventh studio album "Love Letter". The song peaked at #93 on the "Billboard" Hot 100; and it was promoted with a music video directed by Kelly and Jeremy Rall. In 2011 R. Kelly was nominated for a Grammy Award for Best Traditional R&B Performance, but lost.
2. **Platinum (Snoop Dogg song)**: Platinum is a song by American rapper Snoop Dogg, released as the third promotional single from his eleventh studio album Doggumentary. The song features guest vocals from R&B singer R. Kelly, and is produced by American producer Lex Luger.
3. **A Woman's Threat**: "A Woman's Threat" is a single by American R&B singer R. Kelly from his fourth solo studio album and second sequel to 12 Play, TP-2. com. It's the fifth and last single on that album and a six-minute music video has been made for the song. The song charted at number 15 on the US bubbling under charts, 35 on the R&B/Hip Hop charts and below 50 on tw

**Gold paragraphs NOT retrieved:**

- **R. Kelly**: Robert Sylvester Kelly (born January 8, 1967), known professionally as R. Kelly, is an American singer, songwriter, record producer, and former professional basketball player. A native of Chicago, Illinois, Kelly began performing during the late 1980s and debuted in 1992 with the group Public Announcement. In 1993, Kelly went solo with the album "1

### hotpotqa-21 `5a7a030c5542996a35c17077` (stopped at step 1, stated probability 0.95)

**Question:** J.B. Scotts located on this 11 mile stretch in Albany New York and is also known by this name in Schenectady County?

**Gold answer:** State Street  |  **Model answer:** State Street  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Central Avenue (Albany, New York)**: Central Avenue, in Albany, New York, is an 11-mile (5 km) stretch in Albany County, of the 16-mile Albany-Schenectady Turnpike, which runs from Lark Street in the city of Albany, westward through the towns of Colonie, New York and Niskayuna, New York, to the city of Schenectady, New York. In the city of Albany it is called Central Avenue, in Coloni
2. **Schenectady County, New York**: Schenectady County ( ) is a county located in the U.S. state of New York. As of the 2010 census, the population was 154,727. The county seat is Schenectady. The name is from a Mohawk language word meaning "on the other side of the pine lands," a term that originally applied to Albany.
3. **Schenectady, New York**: Schenectady ( ) is a city in Schenectady County, New York, United States, of which it is the county seat. As of the 2010 census, the city had a population of 66,135. The name "Schenectady" is derived from a Mohawk word "skahnéhtati" meaning "beyond the pines". The city was founded on the south side of the Mohawk River by Dutch colonists in the 17th

**Gold paragraphs NOT retrieved:**

- **J.B. Scott's**: J.B. Scott's was a nightclub located on Central Avenue in Albany, New York. Its capacity was approximately 700. It was open from 1979 to 1982 when it burned down. Its performers included U2, John Mellencamp, Bryan Adams, Thin Lizzy, Pat Benatar and Iggy Pop. In 1985 club owner Douglas Jacobs opened another nightclub in Albany named J.B.'s Theatre.

### hotpotqa-22 `5add7a335542992200553b37` (stopped at step 1, stated probability 1.0)

**Question:** Which genus of plant is named after a person, Amesiella or Cucurbita?

**Gold answer:** Amesiella  |  **Model answer:** Amesiella  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Amesiella**: Amesiella is a genus of orchids endemic to the Island of Luzon, in the Philippines. The genus is named for Oakes Ames (1874-1950), founder of the orchid herbarium at Harvard University.
2. **Cucurbita palmeri**: Cucurbita palmeri is a plant species of the genus "Cucurbita". It is native to the Pacific coast of northwestern Mexico to Nicaragua. It is closely related to "Cucurbita argyrosperma" and "Cucurbita sororia".
3. **Cucurbita sororia**: Cucurbita sororia is a plant species of the genus "Cucurbita", sometimes considered to be a subspecies of "Cucurbita argyrosperma", "C. a." subsp. "sororia". It ranges from northern Mexico to Nicaragua, mostly along the Pacific coast. This species was originally considered closely related to "Cucurbita texana" but "C. sororia" was later shown to be

**Gold paragraphs NOT retrieved:**

- **Cucurbita**: Cucurbita (Latin for gourd) is a genus of herbaceous vines in the gourd family, Cucurbitaceae, also known as cucurbits, native to the Andes and Mesoamerica. Five species are grown worldwide for their edible fruit, variously known as squash, pumpkin, or gourd depending on species, variety, and local parlance, and for their seeds. First cultivated in

### hotpotqa-23 `5adccdd55542992c1e3a2408` (stopped at step 1, stated probability 1.0)

**Question:** Meaning "reddish water" in Hawaiian, which location was Butch Van Artsdalen known for surfing 25-foot waves at?

**Gold answer:** Waimea Bay  |  **Model answer:** Waimea Bay  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Butch Van Artsdalen**: Charles M. Van Artsdalen (January 31, 1941 – July 18, 1979) was a legendary surfer. He moved to La Jolla, California, from his birthplace of Norfolk, Virginia, at age 14. Van Artsdalen is best known as a pioneer of surfing 25-foot waves at such North Shore locations as Waimea Bay and Sunset Beach; and tube riding in Hawaii during the early 1960-197
2. **Waimea**: Waimea is a common name in Hawaii and New Zealand. In Hawaiian, it means reddish water, but in Maori it has no meaning. It may refer to:
3. **Mister Pipeline**: Mister Pipeline is a title given to masters of the waves at the North Shore's Pipeline. It was first given to Butch Van Artsdalen, and is passed on from generation to generation, by consensus. Other holders of the title have included sometime actor Gerry Lopez and bodyboarding legend Mike Stewart.

**Gold paragraphs NOT retrieved:**

- **Waimea Bay, Hawaii**: Waimea Bay is located in Haleiwa on the North Shore of O'ahu in the Hawaiian Islands at the mouth of the Waimea River. Waimea Valley extends behind Waimea Bay. "Waimea" means "reddish water" in Hawaiian.

### hotpotqa-24 `5abae3205542996cc5e49edc` (stopped at step 1, stated probability 1.0)

**Question:** What award did the writer of Never Let Me Go novel win in 1989?

**Gold answer:** Man Booker Prize for Fiction  |  **Model answer:** Booker Prize  |  EM 0, F1 0.57

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Never Let Me Go (novel)**: Never Let Me Go is a 2005 dystopian science fiction novel by Japanese-born British author Kazuo Ishiguro. It was shortlisted for the 2005 Booker Prize (an award Ishiguro had previously won in 1989 for "The Remains of the Day"), for the 2006 Arthur C. Clarke Award and for the 2005 National Book Critics Circle Award. " Time" magazine named it the bes
2. **Never Let Me Go (2010 film)**: Never Let Me Go is a 2010 British dystopian romantic drama film based on Kazuo Ishiguro's 2005 novel of the same name. The film was directed by Mark Romanek from a screenplay by Alex Garland. "Never Let Me Go" is set in an alternative history and centres on Kathy, Ruth and Tommy portrayed by Carey Mulligan, Keira Knightley and Andrew Garfield respe
3. **Never Let Me Go (Johnny Ace song)**: "Never Let Me Go" is a blues ballad song by American R&B/blues singer Johnny Ace, written by Joseph Scott and released in 1954 under Duke Records. The song is featured on the albums "My Songs" and "Memorial". "Never Let Me Go" was one of his eighth consecutive top ten R&B hits in a row, including "My Song", "Cross My Heart," "Please Forgive Me," "T

**Gold paragraphs NOT retrieved:**

- **The Remains of the Day**: The Remains of the Day is a 1989 novel by British writer Kazuo Ishiguro. The work was awarded the Man Booker Prize for Fiction in 1989. A film adaptation of the novel, made in 1993 and starring Anthony Hopkins and Emma Thompson, was nominated for eight Academy Awards.

### hotpotqa-25 `5a8268215542995ce29dccfb` (stopped at step 1, stated probability 1.0)

**Question:** What other country does the league that Taylor Eric Kemp played in represents the sport's highest level besides the United States?

**Gold answer:** Canada  |  **Model answer:** Canada  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Taylor Kemp**: Taylor Eric Kemp (born July 23, 1990) is an American soccer player currently playing for D.C. United in Major League Soccer.
2. **Carlos Carmona**: Carlos Emilio Carmona Tello (born February 21, 1987) is a Chilean professional footballer who plays for Atlanta United as a midfielder in the Major League Soccer (MLS) men's professional soccer league, sanctioned by U.S. Soccer, that represents the sport's highest level in both the United States and Canada.
3. **National Women's Soccer League**: The National Women's Soccer League (NWSL) is a professional women's soccer league, run by the United States Soccer Federation. At the top of the United States league system, it represents the sport's highest level in the United States. The NWSL was established in 2012 as a successor to Women's Professional Soccer (2007–2012) which was the successor

**Gold paragraphs NOT retrieved:**

- **Major League Soccer**: Major League Soccer (MLS) is a men's professional soccer league, sanctioned by U.S. Soccer, that represents the sport's highest level in both the United States and Canada. MLS constitutes one of the major professional sports leagues of the United States and Canada. The league comprises 22 teams—19 in the U.S. and 3 in Canada. The MLS regular season

## musique: 104 premature stops of 500 questions, 25 sampled

### musique-01 `3hop1__465684_160545_34754` (stopped at step 3, stated probability 0.95)

**Question:** What does the US believe caused the country where Bodindecha was born to help Japan?

**Gold answer:** blackmail  |  **Model answer:** Japanese blackmail  |  EM 0, F1 0.67

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Bodindecha**: Chao Phraya Bodindecha (, , 1777–1849), personal name Sing Sinhaseni (), was one of the most prominent political and military figures of the early Bangkok Rattanakosin Kingdom. Bodindecha was both a top military general () and Chief Minister in charge of civilian affairs as the "Akkhra Maha Senabodi" () of the "Samuha Nayok" ) during the reign of K
2. **American Chamber of Commerce Japan**: The American Chamber of Commerce Japan (ACCJ) is a non-profit business organization consisting mainly of executives from American companies. Currently, the ACCJ has members that represent over 1,000 companies with offices located in Tokyo, Nagoya and Osaka. Working closely with the governments of the United States and Japan, business organizations 
3. **Phishing**: It is estimated that between May 2004 and May 2005, approximately 1.2 million computer users in the United States suffered losses caused by phishing, totaling approximately US$929 million. United States businesses lose an estimated US$2 billion per year as their clients become victims.
4. **Pacific War**: The Axis states which assisted Japan included the authoritarian government of Thailand in World War II, which quickly formed a temporary alliance with the Japanese in 1941, as the Japanese forces were already invading the peninsula of southern Thailand. The Phayap Army sent troops to invade and occupy northeastern Burma, which was former Thai terri
5. **Military history of the United States during World War II**: The military history of the United States in World War II covers the war against Germany, Italy, Japan and starting with the 7 December 1941 attack on Pearl Harbor. During the first two years of World War II, the United States had maintained formal neutrality as made officially in the Quarantine Speech delivered by U.S. President Franklin D. Roosev
6. **Imperialism**: During the First Sino-Japanese War in 1894, Japan absorbed Taiwan. As a result of the Russo-Japanese War in 1905, Japan took part of Sakhalin Island from Russia. Korea was annexed in 1910. During World War I, Japan took German-leased territories in China’s Shandong Province, as well as the Mariana, Caroline, and Marshall Islands. In 1918, Japan occ
7. **Battle of Palembang**: The Battle of Palembang was a battle of the Pacific theatre of World War II. It occurred near Palembang, on Sumatra, on 13–15 February 1942. The Royal Dutch Shell oil refineries at nearby Pladju (or Pladjoe) were the major objectives for the Empire of Japan in the Pacific War, because of an oil embargo imposed on Japan by the United States, the Net
8. **USS Jason (AR-8)**: USS "Jason" (AR-8) was the fourth of the Vulcan class repair ship of the United States Navy in service from 1944 to 1995, serving in World War II, Korea, Vietnam, and the Gulf War. At the time of her decommissioning, "Jason" was (with the exception of ) the oldest ship in continual commission in the United States Navy, and the final ship in continu
9. [GOLD] **Pacific War**: The official policy of the U.S. Government is that Thailand was not an ally of the Axis, and that the United States was not at war with Thailand. The policy of the U.S. Government ever since 1945 has been to treat Thailand not as a former enemy, but rather as a country which had been forced into certain actions by Japanese blackmail, before being o

**Gold paragraphs NOT retrieved:**

- **Bang Bon District**: Bang Bon (Thai: บางบอน, pronounced [bāːŋ bɔ̄ːn]) is one of the 50 districts (khet) of Bangkok, Thailand. Its neighbours, clockwise from north, are Bang Khae, Phasi Charoen, Chom Thong, and Bang Khun Thian districts of Bangkok, Mueang Samut Sakhon District and Krathum Baen District of Samut Sakhon Province, and Nong Khaem District of Bangkok.

### musique-02 `4hop2__103790_14670_8987_8529` (stopped at step 2, stated probability 0.95)

**Question:** A country's military branch, the equivalent of which in the US contains the Air Defense Artillery, was unprepared for the invasion of Ivo Werner's country. When was the word "Slavs" used in the national anthem of the unprepared country?

**Gold answer:** 1943–1992  |  **Model answer:** 1943–1992 (and 1992–2003)  |  EM 0, F1 0.50

**Gold paragraphs:** 4, retrieved 3

**Evidence the agent had:**

1. [GOLD] **Ivo Werner**: Ivo Werner (born 19 August 1960) is a former professional tennis player originally from Czechoslovakia who competed for both his native country as well as West Germany. Werner, who is now a tennis coach, immigrated to West Germany in 1982 and got citizenship two years later.
2. [GOLD] **Slavs**: The word "Slavs" was used in the national anthem of the Slovak Republic (1939–1945), Yugoslavia (1943–1992) and the Federal Republic of Yugoslavia (1992–2003), later Serbia and Montenegro (2003–2006).
3. **America (My Country, 'Tis of Thee)**: ``My Country, 'Tis of Thee '', also known as`` America'', is an American patriotic song, whose lyrics were written by Samuel Francis Smith. The melody used is the same as that of the national anthem of the United Kingdom, ``God Save the Queen '', arranged by Thomas Arne. The song served as one of the de facto national anthems of the United States (
4. **Warsaw Pact**: The multi-national Communist armed forces' sole joint action was the Warsaw Pact invasion of Czechoslovakia in August 1968. All member countries, with the exception of the Socialist Republic of Romania and the People's Republic of Albania participated in the invasion.
5. [GOLD] **Josip Broz Tito**: In 1968, Tito offered Czechoslovak leader Alexander Dubček to fly to Prague on three hours notice if Dubček needed help in facing down the Soviets. In April 1969, Tito removed generals Ivan Gošnjak and Rade Hamović in the aftermath of the invasion of Czechoslovakia due to the unpreparedness of the Yugoslav army to respond to a similar invasion of Y
6. **Czechoslovakia**: Several accomplished professional tennis players including Ivan Lendl, Jan Kodeš, Miloslav Mečíř, Hana Mandlíková, Martina Hingis, Martina Navratilova, Jana Novotna, Petra Kvitová and Daniela Hantuchová were born in Czechoslovakia.

**Gold paragraphs NOT retrieved:**

- **United States Army**: Currently, the army is divided into the Regular Army, the Army Reserve, and the Army National Guard. The army is also divided into major branches such as Air Defense Artillery, Infantry, Aviation, Signal Corps, Corps of Engineers, and Armor. Before 1903 members of the National Guard were considered state soldiers unless federalized (i.e., activated

### musique-03 `3hop1__536452_15840_36014` (stopped at step 1, stated probability 1.0)

**Question:** What was Nintendo's limit on games per developer per year on the platform with a three letter abbreviation, that had the game Pinball Quest?

**Gold answer:** five  |  **Model answer:** five games per year  |  EM 0, F1 0.40

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Pinball Quest**: Pinball Quest is the name of a Nintendo Entertainment System video game developed by TOSE and published by Jaleco in 1990. The game is based on the popular arcade game pinball. The role playing aspect of the game makes it unique from other pinball based video games.
2. [GOLD] **Super Nintendo Entertainment System**: During the NES era, Nintendo maintained exclusive control over titles released for the system—the company had to approve every game, each third-party developer could only release up to five games per year (but some third parties got around this by using different names, for example Konami's "Ultra Games" brand), those games could not be released on
3. **The Quest Trio**: The Quest Trio is a video game for the Nintendo DS. It was published by Activision in 2008. The "Trio" part of the game's name refers to the 3 selectable games: Jewel Quest II: Jewel Quest Expeditions, Jewel Quest Solitaire, and Mah Jong Quest Expeditions.

**Gold paragraphs NOT retrieved:**

- **Nintendo Entertainment System**: The Nintendo Entertainment System (also abbreviated as NES) is an 8-bit home video game console that was developed and manufactured by Nintendo. It was initially released in Japan as the Family Computer (Japanese: ファミリーコンピュータ, Hepburn: Famirī Konpyūta?) (also known by the portmanteau abbreviation Famicom (ファミコン, Famikon?) and abbreviated as FC) on 

### musique-04 `2hop__24661_66233` (stopped at step 2, stated probability 0.95)

**Question:** When does the new season of the Carolina Hurricanes' league start?

**Gold answer:** October 3, 2018  |  **Model answer:** October 3, 2018  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **North Carolina**: North Carolina is home to three major league sports franchises: the Carolina Panthers of the National Football League and the Charlotte Hornets of the National Basketball Association are based in Charlotte, while the Raleigh-based Carolina Hurricanes play in the National Hockey League. The Panthers and Hurricanes are the only two major professional
2. **Adam Burt**: Burt played four seasons for the Ontario Hockey League's North Bay Centennials before joining the Whalers organization. He made his NHL debut for Hartford in the 1988–89 season, and he remained with the franchise through its transformation into the Carolina Hurricanes in 1997. Burt parted ways with the Hurricanes on March 6, 1999, when he was trade
3. **Brett Pesce**: Brett Pesce (born November 15, 1994) is an American professional ice hockey defenseman currently playing for the Carolina Hurricanes of the National Hockey League (NHL). He was drafted 66th overall by the Hurricanes in the 2013 NHL Entry Draft.
4. **2018–19 NHL season**: The 2018 -- 19 NHL season is the 102nd season of operation (101st season of play) of the National Hockey League. 31 teams are competing in an 82 - game regular season. The regular season began on October 3, 2018, and will end on April 6, 2019. The 2019 Stanley Cup playoffs will begin a few days afterwards, with the Stanley Cup Finals held in late M
5. **NHL on ABC**: The NHL on ABC is the branding formerly used for broadcasts of National Hockey League (NHL) games televised on the American Broadcasting Company (ABC) in the United States. The network first broadcast NHL games during the 1992–93 season under a time-buy agreement with ESPN; ABC resumed regular season game telecasts on February 6, 2000, as part of a
6. [GOLD] **2018–19 NHL season**: The 2018 -- 19 NHL season will be the 102nd season of operation (101st season of play) of the National Hockey League. 31 teams will be competing in an 82 - game regular season. The regular season is scheduled to begin on October 3, 2018, and will end on April 6, 2019. The 2019 Stanley Cup playoffs will then begin a few days afterwards, with the Sta

**Gold paragraphs NOT retrieved:**

- **North Carolina**: In Raleigh many tourists visit the Capital, African American Cultural Complex, Contemporary Art Museum of Raleigh, Gregg Museum of Art & Design at NCSU, Haywood Hall House & Gardens, Marbles Kids Museum, North Carolina Museum of Art, North Carolina Museum of History, North Carolina Museum of Natural Sciences, North Carolina Sports Hall of Fame, Ral

### musique-05 `2hop__771477_149987` (stopped at step 1, stated probability 0.95)

**Question:** Which mythological tradition has the group of heroes that includes Aegialeus?

**Gold answer:** Greek mythology  |  **Model answer:** Greek mythology  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Aegialeus (King of Argos)**: Aegialeus was identified as one of the Epigoni, who avenged their fathers' disastrous attack on the city of Thebes by retaking the city, by both Pausanias and Hellanikos. While his father was the only one of the Seven Against Thebes who did not die in the battle, Aegialeus was the only one of the leaders of the Epigoni who was killed when they reto
2. **The Heroes (1980 film)**: The Heroes, also known as The Shaolin Heroes, is a 1980 Hong Kong martial arts film directed by Wu Ma and Pao Hsueh Li and starring Ti Lung, Shih Szu and Danny Lee.
3. **The Death of Procris**: The Death of Procris, A Satyr mourning over a Nymph or simply A Mythological Subject are names given to an unsigned, undated panel painting in the National Gallery in London, United Kingdom, securely attributed to Piero di Cosimo (who never signed his works). Its date is uncertain, and its subject has been a matter of dispute. The name "The Death o

**Gold paragraphs NOT retrieved:**

- **Epigoni**: In Greek mythology, Epigoni (; from , meaning "offspring") are the sons of the Argive heroes who had fought and been killed in the first Theban war, the subject of the "Thebaid", in which Polynices and six allies (the Seven Against Thebes) attacked Thebes because Polynices' brother, Eteocles, refused to give up the throne as promised. The second Th

### musique-06 `3hop1__857_846_7794` (stopped at step 2, stated probability 1.0)

**Question:** In 2010, what was the population of the city where the Yongle emperor greeted the person to whom the edict was addressed?

**Gold answer:** 8.005 million  |  **Model answer:** 8.005 million  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Sino-Tibetan relations during the Ming dynasty**: The Information Office of the State Council of the PRC preserves an edict of the Zhengtong Emperor (r. 1435–1449) addressed to the Karmapa in 1445, written after the latter's agent had brought holy relics to the Ming court. Zhengtong had the following message delivered to the Great Treasure Prince of Dharma, the Karmapa:
2. **Sino-Tibetan relations during the Ming dynasty**: In his usurpation of the throne from the Jianwen Emperor (r. 1398–1402), the Yongle Emperor was aided by the Buddhist monk Yao Guangxiao, and like his father, the Hongwu Emperor, the Yongle Emperor was "well-disposed towards Buddhism", claims Rossabi. On March 10, 1403, the Yongle Emperor invited Deshin Shekpa, 5th Karmapa Lama (1384–1415), to his 
3. **Sino-Tibetan relations during the Ming dynasty**: Throughout the following month, the Yongle Emperor and his court showered the Karmapa with presents. At Linggu Temple in Nanjing, he presided over the religious ceremonies for the Yongle Emperor's deceased parents, while twenty-two days of his stay were marked by religious miracles that were recorded in five languages on a gigantic scroll that bore
4. [GOLD] **Nanjing**: According to the Sixth China Census, the total population of the City of Nanjing reached 8.005 million in 2010. The statistics in 2011 estimated the total population to be 8.11 million. The birth rate was 8.86 percent and the death rate was 6.88 percent. The urban area had a population of 6.47 million people. The sex ratio of the city population wa
5. **Nanjing**: Nanjing ( listen; Chinese: 南京, "Southern Capital") is the city situated in the heartland of lower Yangtze River region in China, which has long been a major centre of culture, education, research, politics, economy, transport networks and tourism. It is the capital city of Jiangsu province of People's Republic of China and the second largest city i
6. **Dashengguan Yangtze River Bridge**: The Dashengguan Yangtze River Bridge () crosses the Yangtze River in Nanjing, Jiangsu. Construction of the bridge started in 2006 and it was completed in 2010. The bridge has two main spans of it is one of the largest arch bridges in the world. It carries six tracks: two for the Beijing–Shanghai High-Speed Railway (opened on 30 June 2011), two for 

**Gold paragraphs NOT retrieved:**

- **Sino-Tibetan relations during the Ming dynasty**: During his travels beginning in 1403, Deshin Shekpa was induced by further exhortations by the Ming court to visit Nanjing by April 10, 1407. Norbu writes that the Yongle Emperor, following the tradition of Mongol emperors and their reverence for the Sakya lamas, showed an enormous amount of deference towards Deshin Shekpa. The Yongle Emperor came 

### musique-07 `3hop1__836699_15840_36014` (stopped at step 1, stated probability 1.0)

**Question:** What was Nintendo's limit on games per developer per year on the platform of Nightshade?

**Gold answer:** five  |  **Model answer:** Five games per year  |  EM 0, F1 0.40

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Super Nintendo Entertainment System**: During the NES era, Nintendo maintained exclusive control over titles released for the system—the company had to approve every game, each third-party developer could only release up to five games per year (but some third parties got around this by using different names, for example Konami's "Ultra Games" brand), those games could not be released on
2. [GOLD] **Nightshade (1992 video game)**: Nightshade Part 1: The Claws of Sutekh is an action-adventure video game released in 1992 for the Nintendo Entertainment System. It was developed by Beam Software and published by Ultra Games. The game was meant to be the first part in a series, but no sequels were ever made; however, it served as the basis for Beam Software's 1993 game ""Shadowrun
3. **Nintendo Entertainment System**: Nintendo was not as restrictive as Sega, which did not permit third-party publishing until Mediagenic in late summer 1988. Nintendo's intention, however, was to reserve a large part of NES game revenue for itself. Nintendo required that they be the sole manufacturer of all cartridges, and that the publisher had to pay in full before the cartridges 

**Gold paragraphs NOT retrieved:**

- **Nintendo Entertainment System**: The Nintendo Entertainment System (also abbreviated as NES) is an 8-bit home video game console that was developed and manufactured by Nintendo. It was initially released in Japan as the Family Computer (Japanese: ファミリーコンピュータ, Hepburn: Famirī Konpyūta?) (also known by the portmanteau abbreviation Famicom (ファミコン, Famikon?) and abbreviated as FC) on 

### musique-08 `3hop1__516535_834494_33939` (stopped at step 1, stated probability 0.95)

**Question:** In 1900, what was the population of the city in the same county as Allen?

**Gold answer:** 7,531  |  **Model answer:** 7,531  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Allen, Arizona**: Allen, also known as Allen City is a ghost town in Pima County in southern Arizona. It was founded fifty miles southeast of Ajo, c. 1880. By 1886, the post office closed and the town has been abandoned since.
2. [GOLD] **Tucson, Arizona**: By 1900, 7,531 people lived in the city. The population increased gradually to 13,913 in 1910. At about this time, the U.S. Veterans Administration had begun construction on the present Veterans Hospital. Many veterans who had been gassed in World War I and were in need of respiratory therapy began coming to Tucson after the war, due to the clean d
3. **Cross City, Florida**: Cross City is a town in Dixie County, Florida, United States. The population was 1,728 at the 2010 census. It is the county seat of Dixie County.

**Gold paragraphs NOT retrieved:**

- **Pima County Natural Resources, Parks and Recreation**: Pima County Natural Resources, Parks and Recreation is the agency within Pima County, Arizona that manages the natural resources, parks, and recreation offerings within Pima County including Tucson, AZ.

### musique-09 `3hop1__139862_2053_52946` (stopped at step 2, stated probability 0.95)

**Question:** When is Celebrity Big Brother coming to the network which, along with ABC and the network which broadcasted Highway to Heaven, is the other major broadcaster based in NY?

**Gold answer:** February 7, 2018  |  **Model answer:** February 7, 2018  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. **Celebrity Big Brother (American TV series)**: Celebrity Big Brother, also known as Big Brother: Celebrity Edition, is a spin - off series of the American reality television series Big Brother. This season aired during the winter of the 2017 -- 18 network television season on CBS and was the second U.S. Big Brother season to air outside the usual summer television season, the first being Big Br
2. [GOLD] **Celebrity Big Brother (American TV series)**: Celebrity Big Brother also known as Big Brother: Celebrity Edition is a spin - off series of the American reality television series Big Brother. This season will air during the winter of the 2017 -- 18 network television season on CBS and will be the second U.S. Big Brother season to air outside the usual summer television season, the first being B
3. **Celebrity Big Brother (American TV series)**: The main television coverage of Celebrity Big Brother was screened on CBS during the winter of the 2017 -- 18 network television season. CBS decided to schedule the spin - off during the February 2018 sweeps period to counterprogram NBC's coverage of the 2018 Winter Olympics. Episodes aired on Sundays, Mondays, Wednesdays, and Fridays with two spec
4. [GOLD] **Highway to Heaven**: Highway to Heaven is an American television drama series that ran on NBC from 1984 to 1989. The series aired for five seasons, running a total of 111 episodes. The series starred Michael Landon as Jonathan Smith, and Victor French—-Landon's co-star from "Little House on the Prairie"-—as Mark Gordon. Jonathan is an angel who has been stripped of his
5. **DXAQ-AM**: DXAQ (1404 kHz Davao City) Kingdom Radio was a flagship AM station of ACQ-Kingdom Broadcasting Network in the Philippines. The station's studio is located along Philippine-Japan Friendship Highway, Catitipan in Davao City.
6. **Arkansas Highway 242**: Arkansas Highway 242 (AR 242, Hwy. 242) is an east–west state highway in Phillips County, Arkansas. The route of runs from Highway 44 near Helena-West Helena north through the city and through the St. Francis National Forest to Highway 1 near Lexa. A segment of the route is part of the Mississippi River Trail, essentially a bicycle-friendly version

**Gold paragraphs NOT retrieved:**

- **New York City**: The television industry developed in New York and is a significant employer in the city's economy. The three major American broadcast networks are all headquartered in New York: ABC, CBS, and NBC. Many cable networks are based in the city as well, including MTV, Fox News, HBO, Showtime, Bravo, Food Network, AMC, and Comedy Central. The City of New 

### musique-10 `3hop1__831162_831637_91775` (stopped at step 2, stated probability 1.0)

**Question:** What does SEAL stand for in the military group that is part of the military branch that operates USS Dour?

**Gold answer:** Sea, Air, and Land  |  **Model answer:** Sea, Air, and Land  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **USS Dour (AM-223)**: USS "Dour" (AM-223) was an built for the United States Navy during World War II. She was awarded three battle stars for service in the Pacific during World War II. She was decommissioned in March 1947 and placed in reserve. While she remained in reserve, "Dour" was reclassified as MSF-223 in February 1955 but never reactivated. In October 1962, she
2. **Marian reforms**: The Marian reforms of 107 BC were a group of military reforms initiated by Gaius Marius, a statesman and general of the Roman Republic.
3. **Military budget of the United States**: The military budget is the portion of the discretionary United States federal budget allocated to the Department of Defense, or more broadly, the portion of the budget that goes to any military - related expenditures. The military budget pays the salaries, training, and health care of uniformed and civilian personnel, maintains arms, equipment and 
4. [GOLD] **United States Navy SEALs**: The United States Navy's ``Sea, Air, and Land ''Teams, commonly abbreviated as the Navy SEALs, are the U.S. Navy's primary special operations force and a component of the Naval Special Warfare Command. Among the SEALs' main functions are conducting small - unit maritime military operations that originate from, and return to, a river, ocean, swamp, 
5. **United States Navy SEALs**: The Navy needed to determine its role within the special operations arena. In March 1961, Admiral Arleigh Burke, the Chief of Naval Operations, recommended the establishment of guerrilla and counter-guerrilla units. These units would be able to operate from sea, air or land. This was the beginning of the Navy SEALs. All SEALs came from the Navy's U
6. **Rudy Boesch**: Boesch was born and raised in Rochester, New York, and enlisted in the United States Navy at age 17. He became a Underwater Demolition Team (UDT) Frogman in 1951, serving on two UDT Teams. He was chosen as one of the first SEALs, becoming Chief of the Boat of newly created SEAL Team TWO in 1962. Starting in 1968 and 1970, Boesch completed two comba

**Gold paragraphs NOT retrieved:**

- **List of destroyer classes of the United States Navy**: The first major warship produced by the U.S. Navy after World War II (and in the Cold War) were "frigates"—the ships were originally designated destroyer leaders but reclassified in 1975 as guided missile cruisers (except the became guided missile destroyers). These grew out of the last all-gun destroyers of the 1950s. In the middle 1970s the s ent

### musique-11 `3hop1__157177_625046_613900` (stopped at step 4, stated probability 0.85)

**Question:** The city where the river that Merchants Bridge crosses over is the capital of which county?

**Gold answer:** Ottawa County  |  **Model answer:** Ramsey County  |  EM 0, F1 0.50

**Gold paragraphs:** 3, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Merchants Bridge**: The Merchants Bridge, officially the Merchants Memorial Mississippi Rail Bridge, is a rail bridge crossing the Mississippi River between St. Louis, Missouri, and Venice, Illinois. The bridge is owned by the Terminal Railroad Association of St. Louis. It opened in May 1889 and crossed the river north of the Eads Bridge.
2. **Diehls Covered Bridge**: The Diehls Covered Bridge, also known as Turner's Bridge, is a historic wooden covered bridge located at Harrison Township in Bedford County, Pennsylvania. It is a , Burr Truss bridge with a shallow gable roof, constructed in 1892. It crosses the Raystown Branch Juniata River. It is one of 15 historic covered bridges in Bedford County.
3. **Southampton**: The River Test runs along the western border of the city, separating it from the New Forest. There are bridges over the Test from Southampton, including the road and rail bridges at Redbridge in the south and the M27 motorway to the north. The River Itchen runs through the middle of the city and is bridged in several places. The northernmost bridge
4. **Saint Paul, Minnesota**: Saint Paul (abbreviated St. Paul) is the capital and second-most populous city of the U.S. state of Minnesota. As of 2016, the city's estimated population was 304,442. Saint Paul is the county seat of Ramsey County, the smallest and most densely populated county in Minnesota. The city lies mostly on the east bank of the Mississippi River in the are
5. **Saint Paul, Minnesota**: Saint Paul (abbreviated St. Paul) is the capital and second-most populous city of the U.S. state of Minnesota. As of 2017, the city's estimated population was 309,180. Saint Paul is the county seat of Ramsey County, the smallest and most densely populated county in Minnesota. The city lies mostly on the east bank of the Mississippi River in the are
6. **Savannah, Georgia**: Savannah (/ səˈvænə /) is the oldest city in the U.S. state of Georgia and is the county seat of Chatham County. Established in 1733 on the Savannah River, the city of Savannah became the British colonial capital of the Province of Georgia and later the first state capital of Georgia. A strategic port city in the American Revolution and during the 
7. **Beckwith, Ontario**: Beckwith is a township in eastern Ontario, Canada. It is located in Lanark County on the Mississippi River. It is located within Canada's National Capital Region.
8. **Mississippi River**: The Mississippi River is the chief river of the second - largest drainage system on the North American continent, second only to the Hudson Bay drainage system. Flowing entirely in the United States (although its drainage basin reaches into Canada), it rises in northern Minnesota and meanders slowly southwards for 2,320 miles (3,730 km) to the Miss
9. **New Albin, Iowa**: New Albin is a city in Iowa Township, Allamakee County, Iowa, United States. It is the farthest northeast town in Iowa, located on the Mississippi River and the Minnesota border. The population was 522 at the 2010 census.
10. **Minneapolis**: Minneapolis lies on both banks of the Mississippi River, just north of the river's confluence with the Minnesota River, and adjoins Saint Paul, the state's capital. The city is abundantly rich in water, with 13 lakes, wetlands, the Mississippi River, creeks and waterfalls; many connected by parkways in the Chain of Lakes and the Grand Rounds Nation
11. **Apies River**: The Apies River is a river that flows through the city of Pretoria, South Africa. Its source is located just south of the city (south of Erasmus Park) and it flows northward until it drains into the Pienaars River.
12. **Changji**: Changji is a county-level city situated about west of the regional capital, Ürümqi in northern Xinjiang, China, and has about 390,000 inhabitants. It is the seat of Changji Hui Autonomous Prefecture. At the northeast corner of the modern city are the walls and other archaeological remains of the Tang dynasty city, usually referred to as Ancient Cha

**Gold paragraphs NOT retrieved:**

- **I-35W Mississippi River bridge**: The I-35W Mississippi River bridge (officially known as Bridge 9340) was an eight-lane, steel truss arch bridge that carried Interstate 35W across the Saint Anthony Falls of the Mississippi River in Minneapolis, Minnesota, United States. The bridge opened in 1967 and was Minnesota's third busiest, carrying 140,000 vehicles daily. It had a catastrop
- **Minneapolis, Kansas**: Minneapolis is a city in and the county seat of Ottawa County, Kansas, United States. As of the 2010 census, the city population was 2,032.

### musique-12 `3hop2__25177_19506_23299` (stopped at step 1, stated probability 0.95)

**Question:** After the period which limited the supply of shellac; Białystok, Przemyśl were returned to what country along with the region they had been given in the Treaty of Schönbrunn?

**Gold answer:** Polish state  |  **Model answer:** Poland  |  EM 0, F1 0.00

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Molotov–Ribbentrop Pact**: Of the territories of Poland annexed by the Soviet Union between 1939 and 1940, the region around Białystok and a minor part of Galicia east of the San river around Przemyśl were returned to the Polish state at the end of World War II. Of all other territories annexed by the USSR in 1939–40, the ones detached from Finland (Karelia, Petsamo), Estoni
2. **Gmina Supraśl**: Gmina Supraśl is an urban-rural gmina (administrative district) in Białystok County, Podlaskie Voivodeship, in north-eastern Poland. Its seat is the town of Supraśl, which lies approximately north-east of the regional capital Białystok.
3. [GOLD] **Napoleon**: The resulting Treaty of Schönbrunn in October 1809 was the harshest that France had imposed on Austria in recent memory. Metternich and Archduke Charles had the preservation of the Habsburg Empire as their fundamental goal, and to this end they succeeded by making Napoleon seek more modest goals in return for promises of friendship between the two 

**Gold paragraphs NOT retrieved:**

- **Phonograph record**: Vinyl's lower surface noise level than shellac was not forgotten, nor was its durability. In the late 1930s, radio commercials and pre-recorded radio programs being sent to disc jockeys started being stamped in vinyl, so they would not break in the mail. In the mid-1940s, special DJ copies of records started being made of vinyl also, for the same r

### musique-13 `2hop__668407_683671` (stopped at step 1, stated probability 0.95)

**Question:** Who is the father of Empress Wang's husband?

**Gold answer:** Yang Xingmi  |  **Model answer:** Emperor Xiaowu  |  EM 0, F1 0.00

**Gold paragraphs:** 2, retrieved 0

**Evidence the agent had:**

1. **Empress Dowager Xu**: Empress Dowager Xu (徐太后, personal name unknown) (died 926), honored as Empress Dowager Shunsheng (順聖太后) during the reign of her son Wang Yan (né Wang Zongyan), known as Consort Xu with the imperial consort rank "Xianfei" (徐賢妃) during the reign of her husband Wang Jian, was an empress dowager of the Chinese Five Dynasties and Ten Kingdoms period sta
2. **Empress Gou**: Empress Gou (苟皇后, personal name unknown) was an empress of the Chinese/Di state Former Qin. Her husband was Fu Jiān, who created her empress in 355 after seizing the throne from his violent and cruel cousin Fu Sheng even though he claimed only the title of "Heavenly Prince" ("Tian Wang").
3. **Wang Shen'ai**: Wang Shen'ai was the daughter of the official Wang Xianzhi, the son of the famed official and calligrapher Wang Xizhi. Her mother Princess Xin'an was the daughter of Emperor Jianwen, making her and her husband cousins. In 396, while he was still crown prince under his father Emperor Xiaowu, they married, and she became crown empress. She was 12, an

**Gold paragraphs NOT retrieved:**

- **Empress Dowager Wang (Rui)**: Empress Dowager Wang (王太后, personal name unknown) (died 928) was a concubine of the late-Tang Dynasty warlord Yang Xingmi and the mother of his son Yang Pu, the final ruler and the only emperor of the Wu state founded upon the territory that Yang Xingmi took. During Yang Pu's reign as emperor, she was honored as empress dowager.
- **Empress Wang (Yang Pu)**: Empress Wang (王皇后, personal name unknown), known as Empress Rang (讓皇后, "empress of the emperor who yielded") during Southern Tang, was the wife and empress of Yang Pu (Emperor Rui), the final ruler of the Chinese Five Dynasties and Ten Kingdoms period state Wu. As he was the only ruler who claimed the title of emperor, she was the only person to ca

### musique-14 `3hop1__857_846_7701` (stopped at step 2, stated probability 0.85)

**Question:** When did the city where the Yongle emperor greeted the person to whom the edict was addressed become the Chinese national capital?

**Gold answer:** Jin dynasty  |  **Model answer:** Jin dynasty  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Sino-Tibetan relations during the Ming dynasty**: The Information Office of the State Council of the PRC preserves an edict of the Zhengtong Emperor (r. 1435–1449) addressed to the Karmapa in 1445, written after the latter's agent had brought holy relics to the Ming court. Zhengtong had the following message delivered to the Great Treasure Prince of Dharma, the Karmapa:
2. **Sino-Tibetan relations during the Ming dynasty**: In his usurpation of the throne from the Jianwen Emperor (r. 1398–1402), the Yongle Emperor was aided by the Buddhist monk Yao Guangxiao, and like his father, the Hongwu Emperor, the Yongle Emperor was "well-disposed towards Buddhism", claims Rossabi. On March 10, 1403, the Yongle Emperor invited Deshin Shekpa, 5th Karmapa Lama (1384–1415), to his 
3. **Sino-Tibetan relations during the Ming dynasty**: Throughout the following month, the Yongle Emperor and his court showered the Karmapa with presents. At Linggu Temple in Nanjing, he presided over the religious ceremonies for the Yongle Emperor's deceased parents, while twenty-two days of his stay were marked by religious miracles that were recorded in five languages on a gigantic scroll that bore
4. [GOLD] **Nanjing**: Nanjing ( listen; Chinese: 南京, "Southern Capital") is the city situated in the heartland of lower Yangtze River region in China, which has long been a major centre of culture, education, research, politics, economy, transport networks and tourism. It is the capital city of Jiangsu province of People's Republic of China and the second largest city i
5. **Nanjing**: Over two centuries after the removal of the capital to Beijing, Nanjing was destined to become the capital of a Ming emperor one more time. After the fall of Beijing to Li Zicheng's rebel forces and then to the Manchu-led Qing dynasty in the spring of 1644, the Ming prince Zhu Yousong was enthroned in Nanjing in June 1644 as the Hongguang Emperor. 
6. **Nanjing**: The Xinhai Revolution led to the founding of the Republic of China in January 1912 with Sun Yat-sen as the first provisional president and Nanking was selected as its new capital. However, the Qing Empire controlled large regions to the north, so revolutionaries asked Yuan Shikai to replace Sun as president in exchange for the abdication of Puyi, t

**Gold paragraphs NOT retrieved:**

- **Sino-Tibetan relations during the Ming dynasty**: During his travels beginning in 1403, Deshin Shekpa was induced by further exhortations by the Ming court to visit Nanjing by April 10, 1407. Norbu writes that the Yongle Emperor, following the tradition of Mongol emperors and their reverence for the Sakya lamas, showed an enormous amount of deference towards Deshin Shekpa. The Yongle Emperor came 

### musique-15 `2hop__417937_158105` (stopped at step 1, stated probability 0.85)

**Question:** Which two features were played up by the author of Business @ the Speed of Thought?

**Gold answer:** ease of use and enhanced support for Plug and Play  |  **Model answer:** digital infrastructures and information networks  |  EM 0, F1 0.13

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Business @ the Speed of Thought**: Business @ the Speed of Thought is a book written by Bill Gates and Collins Hemingway in 1999. It discusses how business and technology are integrated, and explains how digital infrastructures and information networks can help someone get an edge on the competition.
2. **Alfred North Whitehead**: Whitehead has had some influence on philosophy of business administration and organizational theory. This has led in part to a focus on identifying and investigating the effect of temporal events (as opposed to static things) within organizations through an “organization studies” discourse that accommodates a variety of 'weak' and 'strong' process 
3. **Psyb0t**: Psyb0t or Network Bluepill is a computer worm discovered in January 2009. It is thought to be unique in that it can infect routers and high-speed modems.

**Gold paragraphs NOT retrieved:**

- **Windows 98**: The release of Windows 98 was preceded by a notable press demonstration at COMDEX in April 1998. Microsoft CEO Bill Gates was highlighting the operating system's ease of use and enhanced support for Plug and Play (PnP). However, when presentation assistant Chris Capossela hot plugged a USB scanner in, the operating system crashed, displaying a Blue

### musique-16 `2hop__88149_807969` (stopped at step 1, stated probability 0.85)

**Question:** The all time top goal scorer in premier league in one season is a member of what team?

**Gold answer:** Egypt national football team  |  **Model answer:** Newcastle United and Blackburn Rovers  |  EM 0, F1 0.00

**Gold paragraphs:** 2, retrieved 0

**Evidence the agent had:**

1. **Premier League**: The Golden Boot is awarded to the top Premier League scorer at the end of each season. Former Blackburn Rovers and Newcastle United striker Alan Shearer holds the record for most Premier League goals with 260. Twenty-four players have reached the 100-goal mark. Since the first Premier League season in 1992–93, 14 different players from 10 different
2. **List of Wigan Warriors players**: Wigan Warriors is an English professional rugby league club based in Wigan, Greater Manchester. Formed in 1872, the club was a founding member of the Northern Rugby Football Union in 1895, and competed in the inaugural season of the Northern Union's league championship. Since then, more than 1,100 players have appeared for the club's first team. Ji
3. **Assi Tubi**: Assi Tubi (, born 27 January 1972) is an Israeli footballer. He was the Israeli Premier League top scorer in the 1999–2000 season with 27 goals.

**Gold paragraphs NOT retrieved:**

- **Premier League records and statistics**: Most goals in a season (38 games): 32, Mohamed Salah (Liverpool, 2017 -- 18) Most games scored in during a Premier League season: 24, Mohamed Salah (Liverpool, 2017 -- 18) Most Premier League goals in a calendar year: 39, Harry Kane (Tottenham Hotspur, 2017) Number of teams scored against in a season: 17, joint record: 20 - team league: Ian Wright 
- **Ahmed Salah Hosny**: Ahmed Salah Mohammed Hosny Hassan (born 11 July 1979) is a footballer from Egypt who played for VfB Stuttgart and the Egypt national football team. Recently, Hosny turned to art since he has worked with Amr Diab and Mohamed Hamaki in composing songs in their music albums, and most recently he has played a role (Fu'ad Hareedy) in the Egyptian series

### musique-17 `4hop1__525129_315334_131926_13165` (stopped at step 5, stated probability 0.9)

**Question:** What treaty ceded territory to the US extending west to body of water by the city where the Lots More Blues, Rags and Hollers performer was formed?

**Gold answer:** Treaty of Paris  |  **Model answer:** Treaty of Paris (1783)  |  EM 0, F1 0.86

**Gold paragraphs:** 4, retrieved 2

**Evidence the agent had:**

1. [GOLD] **Lots More Blues, Rags and Hollers**: Lots More Blues, Rags and Hollers is an album by the blues trio Koerner, Ray & Glover, released in 1964.
2. **Two Mile Square Reservation**: The Two Mile Square Reservation or Two Mile Square Reserve was a tract of land in Ohio ceded by Native Americans to the United States of America in the Treaty of Greenville in 1795. It was subsequently surveyed in a manner different from surrounding land, and lots sold to settlers.
3. **Adams–Onís Treaty**: The Adams -- Onís Treaty of 1819, also known as the Transcontinental Treaty, the Florida Purchase Treaty, or the Florida Treaty, was a treaty between the United States and Spain in 1819 that ceded Florida to the U.S. and defined the boundary between the U.S. and New Spain. It settled a standing border dispute between the two countries and was consi
4. [GOLD] **Koerner, Ray & Glover**: Koerner, Ray & Glover was a loose-knit group of three blues musicians from Minneapolis, Minnesota: "Spider" John Koerner on guitar and vocals, Dave "Snaker" Ray on guitar and vocals, and Tony "Little Sun" Glover on harmonica. They were notable figures of the revival of folk music and blues in the 1960s.
5. **Robert Ray Hamilton**: Robert Ray Hamilton graduated from Columbia College and Columbia Law School. He was admitted to the bar, and practiced law in New York City.
6. **American Idol**: 23-year-old Candice Glover won the season with Kree Harrison taking the runner-up spot. Glover is the first female to win American Idol since Jordin Sparks. Glover released "I Am Beautiful" as a single while Harrison released "All Cried Out" immediately after the show. Glover sold poorly with her debut album, and this is also the first season that 
7. **French and Indian War**: The outcome was one of the most significant developments in a century of Anglo - French conflict. France ceded to Great Britain its territory east of the Mississippi. It ceded French Louisiana west of the Mississippi River (including New Orleans) to its ally Spain in compensation for Spain's loss to Britain of Florida. (Spain had ceded Florida to B
8. **History of Canada**: With the end of the Seven Years' War and the signing of the Treaty of Paris (1763), France ceded almost all of its remaining territory in mainland North America, except for fishing rights off Newfoundland and the two small islands of Saint Pierre and Miquelon where its fishermen could dry their fish. France had already secretly ceded its vast Louis
9. **Louisiana Purchase**: A dispute soon arose between Spain and the United States regarding the extent of Louisiana. The territory's boundaries had not been defined in the 1762 Treaty of Fontainebleau that ceded it from France to Spain, nor in the 1801 Third Treaty of San Ildefonso ceding it back to France, nor the 1803 Louisiana Purchase agreement ceding it to the United 
10. **American Revolutionary War**: Date April 19, 1775 -- September 3, 1783 (8 years, 4 months and 15 days) Ratification effective: May 12, 1784 (9 years and 23 days) Location Eastern North America, Caribbean Sea, Indian subcontinent, Africa, the Atlantic Ocean, and the Indian Ocean Result Allied victory: Peace of Paris British recognition of American independence End of the First B
11. **American Indian Wars**: When the British made peace with the Americans in the Treaty of Paris (1783), they ceded a vast amount of Native American territory (without the consent of the indigenous peoples) to the United States. The United States treated the Native Americans who had fought with the British as enemy allies, a conquered people who had lost their land. The fede
12. **Missouri**: Missouri is landlocked and borders eight different states as does its neighbor, Tennessee. No state in the U.S. touches more than eight. Missouri is bounded by Iowa on the north; by Illinois, Kentucky, and Tennessee across the Mississippi River on the east; on the south by Arkansas; and by Oklahoma, Kansas, and Nebraska (the last across the Missour
13. **Río Rico, Tamaulipas**: Río Rico is a town located along the Rio Grande river in the Mexican state of Tamaulipas. It is notable for its partial occupation of the Horcón Tract, a piece of land ceded by the United States to Mexico in 1977 under the terms of the Boundary Treaty of 1970.
14. **Mississippi River**: The Mississippi River is the chief river of the second - largest drainage system on the North American continent, second only to the Hudson Bay drainage system. Flowing entirely in the United States (although its drainage basin reaches into Canada), it rises in northern Minnesota and meanders slowly southwards for 2,320 miles (3,730 km) to the Miss
15. **Pawnee River**: The Pawnee River is a river in southwestern Kansas in the United States, about long. It is a tributary of the Arkansas River, which in turn is a branch of the Mississippi River.

**Gold paragraphs NOT retrieved:**

- **Military history of the United States**: In the Treaty of Paris after the Revolution, the British had ceded the lands between the Appalachian Mountains and the Mississippi River to the United States, without consulting the Shawnee, Cherokee, Choctaw and other smaller tribes who lived there. Because many of the tribes had fought as allies of the British, the United States compelled tribal 
- **Minneapolis**: Minneapolis lies on both banks of the Mississippi River, just north of the river's confluence with the Minnesota River, and adjoins Saint Paul, the state's capital. The city is abundantly rich in water, with 13 lakes, wetlands, the Mississippi River, creeks and waterfalls; many connected by parkways in the Chain of Lakes and the Grand Rounds Nation

### musique-18 `2hop__3131_3300` (stopped at step 1, stated probability 0.95)

**Question:** Which season was the runner up of the third season of American Idol on?

**Gold answer:** season three  |  **Model answer:** Season 3  |  EM 0, F1 0.50

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **American Idol**: 23-year-old Candice Glover won the season with Kree Harrison taking the runner-up spot. Glover is the first female to win American Idol since Jordin Sparks. Glover released "I Am Beautiful" as a single while Harrison released "All Cried Out" immediately after the show. Glover sold poorly with her debut album, and this is also the first season that 
2. [GOLD] **American Idol**: Phillips became the winner, beating Sanchez. Prior to the announcement of the winner, season five finalist Ace Young proposed marriage to season three runner-up Diana DeGarmo on stage – which she accepted.
3. **American Idol (season 16)**: The sixteenth season of American Idol premiered on March 11, 2018, on the ABC television network. It is the show's first season to air on ABC, after 15 years on Fox. Ryan Seacrest continued his role as the show's host, while Katy Perry, Luke Bryan, and Lionel Richie joined as judges. Maddie Poppe from Clarksville, Iowa won the season on May 21, 201

**Gold paragraphs NOT retrieved:**

- **American Idol**: The performance of "Summertime" by Barrino, later known simply as "Fantasia", at Top 8 was widely praised, and Simon Cowell considered it as his favorite Idol moment in the nine seasons he was on the show. Fantasia and Diana DeGarmo were the last two finalists, and Fantasia was crowned as the winner. Fantasia released as her coronation single "I Be

### musique-19 `3hop2__90098_76623_10557` (stopped at step 3, stated probability 0.95)

**Question:** What was the language from which the last name Sylvester originated during the era of the person crowned emperor of the west in 800 CE later known as?

**Gold answer:** Medieval Latin  |  **Model answer:** Medieval Latin  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. **History of India**: Classical India refers to the period when much of the Indian subcontinent was reunited under the Gupta Empire (c. 320–550 CE). This period has been called the Golden Age of India and was marked by extensive achievements in science, technology, engineering, art, dialectic, literature, logic, mathematics, astronomy, religion, and philosophy that crys
2. **Empress Wang (Yang Pu)**: Empress Wang (王皇后, personal name unknown), known as Empress Rang (讓皇后, "empress of the emperor who yielded") during Southern Tang, was the wife and empress of Yang Pu (Emperor Rui), the final ruler of the Chinese Five Dynasties and Ten Kingdoms period state Wu. As he was the only ruler who claimed the title of emperor, she was the only person to ca
3. **Holy Roman Empire**: In 768 Pepin's son Charlemagne became King of the Franks and began an extensive expansion of the realm. He eventually incorporated the territories of present - day France, Germany, northern Italy, and beyond, linking the Frankish kingdom with Papal lands. On Christmas Day of 800, Pope Leo III crowned Charlemagne emperor, restoring the title in the 
4. [GOLD] **Sylvester**: Sylvester is a name derived from the Latin adjective silvestris meaning ``wooded ''or`` wild'', which derives from the noun silva meaning ``woodland ''. Classical Latin spells this with i. In Classical Latin y represented a separate sound distinct from i, not a native Latin sound but one used in transcriptions of foreign words. After the Classical 
5. **Estonian language**: The return of Soviet immigrants to their countries of origin has brought the proportion of Estonians in Estonia back above 70%. And again as in Latvia, today many of the remnant non-Estonians in Estonia have adopted the Estonian language; about 40% at the 2000 census.
6. **Jews**: Genetic studies on Jews show that most Jews worldwide bear a common genetic heritage which originates in the Middle East, and that they bear their strongest resemblance to the peoples of the Fertile Crescent. The genetic composition of different Jewish groups shows that Jews share a common genetic pool dating back 4,000 years, as a marker of their 
7. [GOLD] **Middle Ages**: Charlemagne's court in Aachen was the centre of the cultural revival sometimes referred to as the "Carolingian Renaissance". Literacy increased, as did development in the arts, architecture and jurisprudence, as well as liturgical and scriptural studies. The English monk Alcuin (d. 804) was invited to Aachen and brought the education available in t
8. **Roman numerals**: The number zero does not have its own Roman numeral, but the word nulla (the Latin word meaning ``none '') was used by medieval scholars in lieu of 0. Dionysius Exiguus was known to use nulla alongside Roman numerals in 525. About 725, Bede or one of his colleagues used the letter N, the initial of nulla or of nihil (the Latin word for`` nothing'')
9. **Charlemagne**: Charlemagne (/ ˈʃɑːrlɪmeɪn /) or Charles the Great (2 April 742 -- 28 January 814), numbered Charles I, was King of the Franks from 768, King of the Lombards from 774 and Emperor of the Romans from 800. He united much of Europe during the early Middle Ages. He was the first recognised emperor in western Europe since the fall of the Western Roman Em

**Gold paragraphs NOT retrieved:**

- **Charlemagne**: Charlemagne (/ ˈʃɑːrləmeɪn /) or Charles the Great (2 April 742 -- 28 January 814), numbered Charles I, was King of the Franks from 768, King of the Lombards from 774, and Holy Roman Emperor from 800. He united much of western and central Europe during the early Middle Ages. He was the first recognized emperor to rule from western Europe since the 

### musique-20 `2hop__75169_92673` (stopped at step 2, stated probability 0.95)

**Question:** Where is the starting meridian for the longitude system on the world map?

**Gold answer:** latitude 90 ° North  |  **Model answer:** Greenwich meridian (Greenwich)  |  EM 0, F1 0.00

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. **Prime meridian**: A prime meridian is a meridian (a line of longitude) in a geographic coordinate system at which longitude is defined to be 0 °. Together, a prime meridian and its antimeridian (the 180th meridian in a 360 ° - system) form a great circle. This great circle divides the sphere, e.g., Earth, into two hemispheres. If one uses directions of East and West
2. [GOLD] **Prime meridian**: On Earth, starting at the North Pole and heading south to the South Pole, the IERS Reference Meridian (as of 2016) passes through:
3. **Meridian (geography)**: A (geographical) meridian (or line of longitude) is the half of an imaginary great circle on the Earth's surface, terminated by the North Pole and the South Pole, connecting points of equal longitude. The position of a point along the meridian is given by its latitude indicating how many degrees north or south of the Equator the point is. Each meri
4. **Greenwich Mean Time**: As the United Kingdom grew into an advanced maritime nation, British mariners kept at least one chronometer on GMT to calculate their longitude from the Greenwich meridian, which was by convention considered to have longitude zero degrees, internationally adopted in the International Meridian Conference of 1884. Synchronisation of the chronometer o
5. **Choctaw meridian**: The Choctaw meridian is a meridian that governs the surveys in most of central Mississippi, USA. It begins on the Choctaw baseline, latitude 31° 54' 40" north, longitude 90° 14' 45" west from Greenwich and runs north to the south boundary of the Chickasaw cession, at latitude 34° 19' 40" north.
6. **Airy-0**: Airy-0 is a crater on Mars whose location defined the position of the prime meridian of that planet. It is about across and lies within the larger crater Airy in the region Sinus Meridiani. The IAU Working Group on Cartographic Coordinates and Rotational Elements has now recommended setting the longitude of the Viking 1 lander (47°.95137 west) as t

**Gold paragraphs NOT retrieved:**

- **North Pole**: The North Pole is the northernmost point on the Earth, lying diametrically opposite the South Pole. It defines geodetic latitude 90 ° North, as well as the direction of true north. At the North Pole all directions point south; all lines of longitude converge there, so its longitude can be defined as any degree value. Along tight latitude circles, c

### musique-21 `3hop1__9285_5188_23307` (stopped at step 2, stated probability 0.85)

**Question:** What month did the Tripartite discussions begin between Britain, France, and the country where, despite being headquartered in the nation called the nobilities commonwealth, the top-ranking Warsaw Pact operatives originated?

**Gold answer:** mid-June  |  **Model answer:** June  |  EM 0, F1 0.00

**Gold paragraphs:** 3, retrieved 1

**Evidence the agent had:**

1. **Warsaw Pact**: While the Warsaw Pact was established as a balance of power or counterweight to NATO, there was no direct confrontation between them. Instead, the conflict was fought on an ideological basis. Both NATO and the Warsaw Pact led to the expansion of military forces and their integration into the respective blocs. The Warsaw Pact's largest military enga
2. **Warsaw Pact**: In 1956, following the declaration of the Imre Nagy government of withdrawal of Hungary from the Warsaw Pact, Soviet troops entered the country and removed the government. Soviet forces crushed the nationwide revolt, leading to the death of an estimated 2,500 Hungarian citizens.
3. **Australia at the 2018 Commonwealth Games**: Being the host nation, Australia sent a contingent of 474 athletes, participating in all of the 18 sports staged. Though only 469 competed. This was the highest number of athletes to represent Australia in a Commonwealth Games ever, eclipsing their previous record of 417 athletes at the 2014 Glasgow Commonwealth Games. Hockey athlete Mark Knowles w
4. [GOLD] **Molotov–Ribbentrop Pact**: By the end of May, drafts were formally presented. In mid-June, the main Tripartite negotiations started. The discussion was focused on potential guarantees to central and east European countries should a German aggression arise. The USSR proposed to consider that a political turn towards Germany by the Baltic states would constitute an "indirect a
5. **Oblasts of the Soviet Union**: The oblasts of the Soviet Union were second-level entities of the Soviet Union, and first-level entities of the republics of the Soviet Union.
6. **Soviet Union**: With the rise of strong nationalist and separatist movements inside the union republics, Gorbachev tried to avert a dissolution of the Soviet Union in the post-Cold War era. A March 1991 referendum, boycotted by some republics, resulted in a majority of participating citizens voting in favor of preserving the union as a renewed federation. Gorbache

**Gold paragraphs NOT retrieved:**

- **Szlachta**: The Polish nobility enjoyed many rights that were not available to the noble classes of other countries and, typically, each new monarch conceded them further privileges. Those privileges became the basis of the Golden Liberty in the Polish–Lithuanian Commonwealth. Despite having a king, Poland was called the nobility's Commonwealth because the kin
- **Warsaw Pact**: The Warsaw Treaty's organization was two-fold: the Political Consultative Committee handled political matters, and the Combined Command of Pact Armed Forces controlled the assigned multi-national forces, with headquarters in Warsaw, Poland. Furthermore, the Supreme Commander of the Unified Armed Forces of the Warsaw Treaty Organization which comman

### musique-22 `3hop2__76623_90098_10557` (stopped at step 4, stated probability 1.0)

**Question:** What was the version of the language the last name Sylvester comes from, used in the era of the individual crowned Emperor of the West in 800 CE, later called?

**Gold answer:** Medieval Latin  |  **Model answer:** Medieval Latin  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. **Holy Roman Empire**: In 768 Pepin's son Charlemagne became King of the Franks and began an extensive expansion of the realm. He eventually incorporated the territories of present - day France, Germany, northern Italy, and beyond, linking the Frankish kingdom with Papal lands. On Christmas Day of 800, Pope Leo III crowned Charlemagne emperor, restoring the title in the 
2. **Holy Roman Emperor**: Emperor of the Holy Roman Empire Romanorum Imperator Imperial Double - headed Reichsadler used by the Habsburg emperors of the early modern period Last in Office Francis II 5 July 1792 -- 6 August 1806 Details Style His Imperial Majesty First monarch Charlemagne Last monarch Francis II Formation 25 December 800 Abolition 6 August 1806 Appointer see
3. **History of India**: Classical India refers to the period when much of the Indian subcontinent was reunited under the Gupta Empire (c. 320–550 CE). This period has been called the Golden Age of India and was marked by extensive achievements in science, technology, engineering, art, dialectic, literature, logic, mathematics, astronomy, religion, and philosophy that crys
4. [GOLD] **Middle Ages**: Charlemagne's court in Aachen was the centre of the cultural revival sometimes referred to as the "Carolingian Renaissance". Literacy increased, as did development in the arts, architecture and jurisprudence, as well as liturgical and scriptural studies. The English monk Alcuin (d. 804) was invited to Aachen and brought the education available in t
5. **Auctor**: Auctor is Latin for author or originator. The term is used in Scholasticism for a "renowned scholar", and in biological taxonomy for the scientist describing a species or other taxon. The term is widely replaced by author in English-language works.
6. **Charlemagne**: Charlemagne (/ ˈʃɑːrlɪmeɪn /) or Charles the Great (2 April 742 -- 28 January 814), numbered Charles I, was King of the Franks from 768, King of the Lombards from 774 and Emperor of the Romans from 800. He united much of Europe during the early Middle Ages. He was the first recognised emperor in western Europe since the fall of the Western Roman Em
7. **Táng (surname)**: Tang (; Chinese: 唐, mandarin Pinyin: "Táng"; Japanese: 唐/とう/から; Korean: 당/唐; Cantonese : Tong; old Chinese read Dang), is a Chinese surname. The three languages also have the surname with the same character but different pronunciation/romanization. In Korean, it is usually romanized also as Dang. In Japanese, the surname is often romanized as To. I
8. **Estonian language**: The return of Soviet immigrants to their countries of origin has brought the proportion of Estonians in Estonia back above 70%. And again as in Latvia, today many of the remnant non-Estonians in Estonia have adopted the Estonian language; about 40% at the 2000 census.
9. **Walker (surname)**: Walker is a German surname derived from either a fuller, from the Middle High German walker, meaning ``a fuller of cloth '', or an officer whose duty consisted of walking or inspecting a certain part of a forest. The surname`` Walker'' was first found in Germany where records of the name date back to the thirteenth century. In 1253, Sigelo dictus W
10. **Jews**: Genetic studies on Jews show that most Jews worldwide bear a common genetic heritage which originates in the Middle East, and that they bear their strongest resemblance to the peoples of the Fertile Crescent. The genetic composition of different Jewish groups shows that Jews share a common genetic pool dating back 4,000 years, as a marker of their 
11. [GOLD] **Sylvester**: Sylvester is a name derived from the Latin adjective silvestris meaning ``wooded ''or`` wild'', which derives from the noun silva meaning ``woodland ''. Classical Latin spells this with i. In Classical Latin y represented a separate sound distinct from i, not a native Latin sound but one used in transcriptions of foreign words. After the Classical 
12. **Madagascar**: The Malagasy language is of Malayo-Polynesian origin and is generally spoken throughout the island. The numerous dialects of Malagasy, which are generally mutually intelligible, can be clustered under one of two subgroups: eastern Malagasy, spoken along the eastern forests and highlands including the Merina dialect of Antananarivo, and western Mala

**Gold paragraphs NOT retrieved:**

- **Charlemagne**: Charlemagne (/ ˈʃɑːrləmeɪn /) or Charles the Great (2 April 742 -- 28 January 814), numbered Charles I, was King of the Franks from 768, King of the Lombards from 774, and Holy Roman Emperor from 800. He united much of western and central Europe during the early Middle Ages. He was the first recognized emperor to rule from western Europe since the 

### musique-23 `2hop__423972_540249` (stopped at step 1, stated probability 1.0)

**Question:** Who was the sibling of Nannina de' Medici?

**Gold answer:** Giuliano de' Medici  |  **Model answer:** Lorenzo de' Medici  |  EM 0, F1 0.67

**Gold paragraphs:** 2, retrieved 1

**Evidence the agent had:**

1. [GOLD] **Nannina de' Medici**: Nannina de' Medici (14 February 1448 – 14 May 1493), born Lucrezia de' Medici, was the second daughter of Piero di Cosimo de' Medici and Lucrezia Tornabuoni. She was thus the elder sister of Lorenzo de' Medici. She married Bernardo Rucellai. Her father's name was Piero, so she is sometimes known as Lucrezia di Piero de' Medici.
2. **Portrait of Ippolito de' Medici**: The Portrait of Ippolito de' Medici is a 1532-33 portrait of Ippolito de' Medici by Titian, now in the Palazzo Pitti.
3. **Pietro de' Medici**: Don Pietro de' Medici (3 June 1554 – 25 April 1604) was the youngest son of Cosimo I de' Medici, Grand Duke of Tuscany and Eleonora di Toledo.

**Gold paragraphs NOT retrieved:**

- **Giuliano de' Medici**: Giuliano de' Medici (25 March 1453 – 26 April 1478) was the second son of Piero de' Medici (the Gouty) and Lucrezia Tornabuoni. As co-ruler of Florence, with his brother Lorenzo the Magnificent, he complemented his brother's image as the "patron of the arts" with his own image as the handsome, sporting, "golden boy."

### musique-24 `3hop1__140786_2053_52946` (stopped at step 1, stated probability 0.95)

**Question:** When is Celebrity Big Brother coming to the broadcast company that, along with the network of Just Men!?, and ABC, is one of the major broadcasters based in New York?

**Gold answer:** February 7, 2018  |  **Model answer:** February 7, 2018  |  EM 1, F1 1.00  <- correct without all gold evidence

**Gold paragraphs:** 3, retrieved 2

**Evidence the agent had:**

1. **Celebrity Big Brother (American TV series)**: Celebrity Big Brother, also known as Big Brother: Celebrity Edition, is a spin - off series of the American reality television series Big Brother. This season aired during the winter of the 2017 -- 18 network television season on CBS and was the second U.S. Big Brother season to air outside the usual summer television season, the first being Big Br
2. [GOLD] **New York City**: The television industry developed in New York and is a significant employer in the city's economy. The three major American broadcast networks are all headquartered in New York: ABC, CBS, and NBC. Many cable networks are based in the city as well, including MTV, Fox News, HBO, Showtime, Bravo, Food Network, AMC, and Comedy Central. The City of New 
3. [GOLD] **Celebrity Big Brother (American TV series)**: Celebrity Big Brother also known as Big Brother: Celebrity Edition is a spin - off series of the American reality television series Big Brother. This season will air during the winter of the 2017 -- 18 network television season on CBS and will be the second U.S. Big Brother season to air outside the usual summer television season, the first being B

**Gold paragraphs NOT retrieved:**

- **Just Men!**: Just Men! is an American game show that aired on NBC Daytime from January 3 to April 1, 1983. The show starred Betty White, who won an Emmy award for her work on the show, with Steve Day announcing.

### musique-25 `4hop1__391525_49925_13759_736921` (stopped at step 2, stated probability 0.95)

**Question:** Where is the district that the person who wanted to reform and address John Kodwo Amissah's religion preached a sermon on Marian devotion before his death located?

**Gold answer:** Saxony-Anhalt  |  **Model answer:** Saxony-Anhalt, Germany  |  EM 0, F1 0.67

**Gold paragraphs:** 4, retrieved 3

**Evidence the agent had:**

1. [GOLD] **John Kodwo Amissah**: John Kodwo Amissah (November 27, 1922 – September 22, 1991) was a Ghanaian prelate of the Catholic Church who served as Archbishop of Cape Coast from 1959 until his death.
2. [GOLD] **Mary, mother of Jesus**: Despite Martin Luther's harsh polemics against his Roman Catholic opponents over issues concerning Mary and the saints, theologians appear to agree that Luther adhered to the Marian decrees of the ecumenical councils and dogmas of the church. He held fast to the belief that Mary was a perpetual virgin and the Theotokos or Mother of God. Special att
3. **A River Runs Through It (film)**: Soon after the fishing excursion, Norman is again contacted by the police. They tell him that Paul has been found beaten to death in an alley, and that all the bones in his right hand have also been broken. Norman goes home and tells his parents the sad news. The story then jumps ahead a few years to a sermon being given by John with Mrs. Maclean, 
4. [GOLD] **Wittenberg (district)**: Wittenberg is a district () in the east of Saxony-Anhalt, Germany. Neighboring districts are (from west clockwise) Anhalt-Bitterfeld, the district-free city of Dessau-Roßlau, the districts of Potsdam-Mittelmark, Teltow-Fläming and Elbe-Elster in Brandenburg, and the district of Nordsachsen in the Free State of Saxony.
5. **Pegangsaan, Menteng**: Pegangsaan is an administrative village in the Menteng district of Indonesia. It has a postal code of 10320. This administrative village is also known as the location of the house where the Proclamation of Indonesian Independence was read.
6. **Bülach District**: Bülach District ("Bezirk Bülach") is one of 12 districts of the Canton of Zürich in Switzerland, with some 117,000 inhabitants the third largest in the canton. Its administrative capital is Bülach, the largest municipality is Kloten, the location of Zurich Airport. It includes the Rafzerfeld north of the Rhine, with Rafz, Wil, Hüntwangen and Waster

**Gold paragraphs NOT retrieved:**

- **Reformation**: Although there had been significant earlier attempts to reform the Catholic Church before Luther -- such as those of Jan Hus, Peter Waldo, and John Wycliffe -- Martin Luther is widely acknowledged to have started the Reformation with the Ninety - five Theses. Luther began by criticising the sale of indulgences, insisting that the Pope had no author
