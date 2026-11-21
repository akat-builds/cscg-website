B = "https://www.carolinasportsconsultinggroup.com"
S = "https://cdn.sanity.io/images/k8nixw64/production/"

APPLY_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScF7aFVsTs0aodlqPWvOBaBjPoM5bUePfno7vSBe51YHzsrYA/viewform"
LINKEDIN = "https://www.linkedin.com/company/carolinascg/"
INSTAGRAM = "https://www.instagram.com/carolina_sports_consulting/"

IMG = {
    "hero": B + "/_next/static/media/kenan-bell-tower-view.7b1a0d6e.webp",
    "boxseats": B + "/images/kenan-box-seats.webp",
    "logo_blue": B + "/logos/Main%20Logo%20Blue.png",
    "logo_white": B + "/logos/Main%20Logo%20White.png",
    "logo_horiz_white": B + "/_next/static/media/White%20Horizontal.b39a1238.png",
    "founders": B + "/_next/static/media/CSCGFounders.3e35d0ee.avif",
    "event": B + "/_next/static/media/CSCGEvent.9f60ae0d.webp",
    "profdev": B + "/_next/static/media/12.1.25%20CSCG%20-06.4c081d2c.webp",
    "services1": B + "/images/12.1.25%20CSCG%20-18.webp",
    "services2": B + "/images/CmuK1iZQ.webp",
    "apply1": B + "/images/12.1.25%20CSCG%20-10.webp",
    "apply2": B + "/images/12.1.25%20CSCG%20-3.webp",
}

STATS = [("45", "+", "Consultants"), ("15", "+", "Clients served"), ("2024", "", "Founded Fall")]

FOUNDERS_LETTER = [
    "Welcome to the official website of the Carolina Sports Consulting Group! We appreciate you taking the time to learn more about our organization. CSCG is a 45-member, rapidly growing, student-run consulting group at the University of North Carolina at Chapel Hill dedicated to helping sports properties, brands, and organizations tackle their biggest challenges through strategic, data-driven insights.",
    "Our members come from a wide range of majors and backgrounds, bringing together creativity, professionalism, and entrepreneurial energy to deliver real impact. We have partnered with organizations such as the PGA TOUR, Under Armour, DAZN, the LPGA, and UNC Athletics, among many others, giving students the opportunity to work directly on projects that shape the future of sports business.",
    "CSCG has defined our college experience. It has challenged us to lead, to grow, and to think bigger, and none of that would be possible without the dedication and drive of our members. They are the heartbeat of this group: doers, problem solvers, and innovators who come together to create something meaningful both for our clients and our community. If you are interested in joining CSCG, we recruit each Fall and Spring semester through the link on our website. We encourage you to stay connected and reach out with any questions.",
]

MISSION = [
    ("Student Development", "Provide incredible hands-on development opportunities for UNC students to help them develop business strategy skills and set them up for internships and full-time roles."),
    ("Client Excellence", "Support world-class clients in the sports property and brands space with strategic insights from diverse perspectives in order to drive results."),
]

EXPERTISE = [
    ("Business Strategy", "Developing growth-focused strategies that drive revenue, enhance fan engagement, and position your brand for long-term success in the sports industry.", "event"),
    ("Data Analysis", "Leveraging advanced analytics and data-driven insights to uncover trends, optimize performance, and make informed decisions that maximize impact.", "services1"),
    ("Custom Research", "Conducting tailored research to address your unique challenges, providing proprietary insights that give you a competitive edge in the marketplace.", "services2"),
]

ALUMNI_LOGOS = [
    ("NBA.png", "NBA"), ("nike.png", "Nike"), ("mckinsey.png", "McKinsey"), ("EY.png", "EY"),
    ("KPMG.png", "KPMG"), ("wasserman.avif", "Wasserman"), ("octagon.png", "Octagon"), ("CAA.png", "CAA"),
    ("playfly.png", "Playfly"), ("Truist.png", "Truist"), ("DeutscheBank.png", "Deutsche Bank"),
    ("P%26G.png", "Procter & Gamble"), ("HoulihanLokey.svg", "Houlihan Lokey"), ("AMBSE.png", "AMBSE"),
    ("ESPN.png", "ESPN"), ("BOA.png", "Bank of America"), ("BNP_Paribas.png", "BNP Paribas"),
    ("BCG.png", "Boston Consulting Group"), ("Capital_One.png", "Capital One"), ("Huron.png", "Huron"),
]
ALUMNI_LOGOS = [(B + "/images/alumni_logos/" + f, a) for f, a in ALUMNI_LOGOS]
ABOUT_LOGOS = ALUMNI_LOGOS[:15]  # the About page shows the first 15

CLIENT_LOGOS = [
    ("charsports.png", "Charlotte Sports Foundation"), ("pga.png", "PGA TOUR"), ("pirates.png", "Pittsburgh Pirates"),
    ("ramsclub.png", "Rams Club"), ("SMU.png", "SMU"), ("Under_armour_logo.svg", "Under Armour"),
    ("DAZN.webp", "DAZN"), ("LPGA.webp", "LPGA"), ("UNC.png", "UNC"), ("UTSA.webp", "UTSA"),
]
CLIENT_LOGOS = [(B + "/images/logos/" + f, a) for f, a in CLIENT_LOGOS]

TESTIMONIALS = [
    (B + "/images/logos/pga.png", "PGA Tour logo", "PGA TOUR", "It was our pleasure to work with a fantastic group of enthusiastic students dedicated to delivering fresh, actionable, insights on marketing PGA TOUR, Fan-Forward experiences to younger audiences."),
    (B + "/images/logos/pirates.png", "Pittsburgh Pirates logo", "Pittsburgh Pirates", "The work the team did added insight into the psychology of the demographic we're aimed to tap into. Additionally, the group went above and beyond our expectations in the research aspect."),
    (B + "/images/logos/UNC.png", "Carolina Football logo", "Carolina Football", "Outstanding work in all ways!"),
]

ADVISORS = [
    ("Anna (McGraw) Miller", "Director of Corporate Strategy, NFL", "Anna is a 2015 graduate of UNC Kenan-Flagler, and current Director of Corporate Strategy at the National Football League (NFL). Before the NFL, Anna has spent time working at Target, the WWE, and Warner Brothers.", "/images/AnnaHeadshot.webp", "https://www.linkedin.com/in/anna-mcgraw-miller-54824298/"),
    ("Tony Mayhoff", "Vice President of Corporate Partnerships, Baltimore Orioles", "Tony is an MBA graduate of UNC's Kenan-Flagler Business School, and has spent years in various media and marketing roles. After spending multiple years with Junior Motorsports, where he climbed the ladder to be CCO and Senior Vice President, Tony has now moved into baseball to work with the Orioles.", "/images/Tony_Mayhoff.webp", "https://www.linkedin.com/in/tony-mayhoff/"),
    ("Ryan Meyer", "Senior Director Of Ticketing, PGA TOUR Events", "Ryan is a graduate of UNC with both undergraduate and graduate degrees, and is currently the Senior Director of Ticketing PGA Tour Events at the PGA Tour. Before the PGA Tour, Ryan had worked with numerous organizations in the ticketing department including UNC Athletics, International Speedway Corporation, and Stubhub.", "/images/Ryan_Meyer.webp", "https://www.linkedin.com/in/jamesryanmeyer/"),
    ("Rick Hart", "Senior Advisor, Altius Sports Partners", "Rick is a 1994 graduate from UNC and currently a Senior Advisor for Altius Sports Partners. Rick spent multiple years at UNC, Oklahoma University, and UT Chattanooga before spending 13 years as the Athletic Director of SMU.", "/images/Rick_Hart.webp", "https://www.linkedin.com/in/rick-l-hart/"),
    ("Laura Fellwock", "Director, Tournament Services, HNS Sports Group", "Laura is a 2016 graduate of UNC and the current Director of Tournament Services at HNS Sports Group. Before HNS Sports Group Laura has spent time in the golf space at AJGA, the PGA Tour, and Constellation Furyk and Friends.", "/images/Laura_Fellwock.webp", "https://www.linkedin.com/in/laura-fellwock-84483984/"),
    ("Colin Smith", "President, Racing America, RTA Media", "Colin is a 1994 graduate of UNC and the current President of Race Team Alliance. Before Race Team Alliance Colin spent time at Raycom Sports, Nascar, and Motorsport Network.", "/images/Colin_Smith.webp", "https://www.linkedin.com/in/colincfsmith/"),
    ("Scott Warfield", "VP of Gaming, PGA TOUR", "Scott is a graduate from UNC, a member of 2021 Sports Business Journal's 40 under 40, and the current VP of Gaming at the PGA Tour. Before the PGA Tour Scott climbed his way up Nascar eventually becoming a Managing Director of Gaming.", "/images/Scott_Warfield.webp", "https://www.linkedin.com/in/scott-warfield-59058912/"),
    ("Clint Gwaltney", "Sr. Associate Athletic Director, UNC Athletics", "Clint is a former UNC football player, a 1992 UNC graduate, and the current Senior Athletic Director for Operations at UNC. Clint spent two years with Andersen Consulting before getting his masters in sports administration from Ohio University. Since then Clint has climbed the ladder at UNC Athletics starting as a ticket office intern and now as a Senior Athletic Director.", "/images/Clint_Gwaltney.webp", "https://www.linkedin.com/in/clint-gwaltney-8202158/"),
]
ADVISORS = [(n, t, b, B + i, l) for n, t, b, i, l in ADVISORS]

# (name, role, major, year, image id, linkedin)
EXEC = [
    ("Dylan Gigler", "President", "Business Administration", "Sophomore", "59b47165fbfaf8b21fc36fd17ec1a4ac0f473f2f-2704x3380.jpg", "https://www.linkedin.com/in/dylan-gigler/"),
    ("Meaghan Leary", "CEO", "Business Administration", "Sophomore", "13f201adf317fd83fe2a99fe20ddff88b1c13164-7008x4672.webp", "https://www.linkedin.com/in/meaghan-leary0319/"),
    ("Sidney Griffin", "Director of Projects", "Sports Administration", "Junior", "24be125bc5faf73689bae06202ef911e3ff1f974-1730x1730.jpg", "https://www.linkedin.com/in/sidneyagriffin/"),
    ("Max Haber", "Director of Legal and Financial", "Business Administration & Public Policy", "Sophomore", "e68f4d0d672dfd3d2c46e118282de5ba0042d078-488x562.png", "https://www.linkedin.com/in/max-haber/"),
    ("Ty Fitch", "Director of Recruitment", "Business Administration & Economics", "Sophomore", "cc8067831ef40f5ceaa9484fe2e87a43119dd912-1365x2048.jpg", "https://www.linkedin.com/in/tyfitch/"),
    ("Sydnie Rice", "Director of Marketing", "Business Administration & Journalism", "Junior", "29be31ab8c1056851bf0f170171feb84122d23d1-3183x3979.jpg", "https://www.linkedin.com/in/sydnie-rice/"),
]

CDP_INTRO = "The Consultant Development Program at Carolina Sports Consulting Group (CSCG) introduces new members to the fundamentals of sports consulting and helps them develop as future business leaders. Members engage in mock projects, group presentations, and networking events to strengthen strategic thinking, problem solving, teamwork, and client management. This experience provides a strong foundation for work within CSCG and prepares our consultants to become business leaders of the future."

CDP = [
    ("Alexander Panas", "Analyst", "Business Administration & Public Policy", "Freshman", "262d50d1aca1f3bc96b0aa5283f68bee52a2bb98-3183x3979.jpg", "https://www.linkedin.com/in/alexander-panas-50713126a/"),
    ("Jackson Matz", "Consultant", "Neuroscience & Global Health", "Freshman", "bfb5f49409d021f3243f5d2501f5ddba4c3b7c33-2657x3321.jpg", "https://www.linkedin.com/in/jackson-matz/"),
    ("Fatimah Naraghi", "Consultant", "Business Administration", "Freshman", "18881b6977b30dfd9eba79408e09f1d3ae962a5d-3932x4915.jpg", "https://www.linkedin.com/in/fatimahnaraghi/"),
    ("Aran Jaiman", "Consultant", "Economics & Computer Science", "Freshman", "c19c386766e5b338515b9e3ca52ffc4d4f297986-3252x4065.jpg", "https://www.linkedin.com/in/aranjaiman/"),
    ("Henry Steckman", "Consultant", "Business Administration", "Freshman", "9d26f26d826ed3a16f76ed938975cdd7d3e3f6bf-3164x3955.jpg", "https://www.linkedin.com/in/henry-steckman-aa7a3b373/"),
    ("Kyle Wei", "Consultant", "Business Administration & Data Science", "Freshman", "58a2bec3919f47cc93861e5b73a2ca3207553e38-2773x4160.jpg", "https://www.linkedin.com/in/kyle-wei-44708a372/"),
    ("Aidan Dobrosielski", "Consultant", "Business Administration & Economics", "Freshman", "f9e7dcc27d87b7e94ac4d4938047def2c6fd30ab-3264x4928.jpg", "https://www.linkedin.com/in/adobro/"),
    ("Jamie Le", "Consultant", "Business Administration & Management", "Freshman", "6c34fd19c06e8f6e0c23bcb84b64dbb70af834f6-3366x4207.jpg", "https://www.linkedin.com/in/jamie-n-le/"),
    ("Valerie Foust", "Consultant", "Sport Administration & Media and Journalism", "Freshman", "7942db51e2e9e0367e03e15a5da36dc7f47bc733-3895x4869.jpg", "https://www.linkedin.com/in/val-faust/"),
    ("Aaron George", "Consultant", "Business Administration & Finance", "Freshman", "d0d8a464bafe01243bd37640605f55ed01723489-1570x1430.jpg", "https://www.linkedin.com/in/aaron-george-8102b5378/"),
]

PROJECTS = [
    ("ESPN", "0867c0a12951c8451bf5f811a0fbb572afd5d8e0-1947x600.png", [
        ("Graham Guilfoyle", "Project Manager", "Business Administration & Global Studies", "Junior", "b73b7a1a00f07192fddf86d7c3cf6189f99cd4c7-3978x4973.jpg", "https://www.linkedin.com/in/grahamguilfoyle/"),
        ("Mallory Barakat", "Consultant", "Sports Administration", "Junior", "6db26bd3eff06431ef59b4eb9c8e063bf9c3a4ee-913x1239.png", "https://www.linkedin.com/in/mallorybarakat/"),
        ("Landis Haynes", "Consultant", "Economics & Data Science", "Junior", "656ab968f87d5e00143ca5fd85f65b6628c53ef4-1179x1484.jpg", "https://www.linkedin.com/in/landis-haynes/"),
        ("Tess Calabria", "Consultant", "Undecided", "Sophomore", "9bee01141d77c2df1831d14ffc057a39a9bf4cf4-399x400.jpg", "https://www.linkedin.com/in/tesscalabria/"),
        ("James Butlin", "Consultant", "Business Administration", "Freshman", "c35607eca98cdd8e53470dbc25d730a0ffd0099b-3200x4000.jpg", "https://www.linkedin.com/in/jamesabutlin/"),
        ("Anya Yajnik", "Consultant", "Data Analytics & Economics", "Junior", "f7d3ef36276886812caac633b9a26e4fc75476cf-2957x3696.jpg", "https://www.linkedin.com/in/anya-yajnik/"),
        ("Dylan Clark", "Consultant", "Business Administration", "Sophomore", "b086d45897c841728330cd580bccc9f13bbe922d-3986x4982.jpg", "https://www.linkedin.com/in/dylanclark-/"),
    ]),
    ("Joe Gibbs Racing", "9e1638536684bb2620d08ea0b99058a66f69fa8d-1024x1024.png", [
        ("Devin Buckler", "Project Manager", "Business Administration & Statistics", "Junior", "728685161eaa3f3e2b1b8b141588ebc063574544-4630x5787.webp", "https://www.linkedin.com/in/devin-buckler/"),
        ("Max Haber", "Director of Legal and Financial", "Business Administration & Public Policy", "Sophomore", "e68f4d0d672dfd3d2c46e118282de5ba0042d078-488x562.png", "https://www.linkedin.com/in/max-haber/"),
        ("Rhea Bakshi", "Consultant", "Economics & Data Science", "Sophomore", "6efa7a75abea6a7385d22417b0e1f0f2a9a65793-3143x3929.jpg", "https://www.linkedin.com/in/rheabakshi/"),
        ("Matt Rossitch", "Consultant", "Business Administration & Chemistry", "Junior", "812ff827e1721444de95c631a7a88d7f9f21e4e0-400x400.jpg", "https://www.linkedin.com/in/matt-rossitch/"),
        ("Andrew Stone", "Analyst", "Business Administration", "Freshman", "f3f0257a28db1c481678e65d4c8e103252f98b72-3011x3764.jpg", "https://www.linkedin.com/in/andrew-stone1/"),
        ("Paeton Brown", "Consultant", "Sports Administration & Economics", "Sophomore", "ccb59bc515abcfd38613c51cabc39d2fa5f44e4a-3970x4963.jpg", "https://www.linkedin.com/in/paeton/"),
        ("Jackson Crawford", "Consultant", "Business Administration & Economics", "Sophomore", "dab2d373f268b45c63b122fa6012cd03386ab609-3983x4979.jpg", "https://www.linkedin.com/in/jacksoncrawf/"),
        ("Vikas Nandakumar", "Consultant", "Business Administration & Statistics", "Sophomore", "f528357ff9c62e00bd1bf1d1001e27ab4b786ebc-400x400.jpg", "https://www.linkedin.com/in/vikas-nandakumar/"),
    ]),
    ("Nike", "88792ea5685f1206b49100b777c9ab9d1679b63b-1024x1024.png", [
        ("Neha Jumani", "Project Manager", "Data Science", "Sophomore", "ef0afba9cc7671c67cb0d6373bf669d64cee30b0-3694x4617.jpg", "https://www.linkedin.com/in/neha-jumani/"),
        ("Levi Graham", "Consultant", "Business Administration", "Sophomore", "e8b9743f4dbd01eb072eab666efcbc8ffa576146-1397x1563.webp", "https://www.linkedin.com/in/levi-graham1/"),
        ("Aidan Dobson", "Consultant", "Business Administration", "Junior", "0cedf595eedceef99603ab3c37e7bc6e7a6ed457-3801x4751.jpg", "https://www.linkedin.com/in/aidan-dobson/"),
        ("Ryan Le", "Analyst", "Undecided", "Freshman", "87d2eefc409ed18715380c6393904f70ae01e836-2870x3588.jpg", "https://www.linkedin.com/in/ryan-le-0a1997380/"),
        ("Katie Dennison", "Analyst", "Business Administration & Sports Administration", "Freshman", "d565474108aaf34888b355033b35505720e19815-2740x3425.jpg", "https://www.linkedin.com/in/katie-dennison-80751a340/"),
        ("Frank Kaplan", "Consultant", "Chemistry & Biology", "Sophomore", "f9619394bde4c1d023556136edcc09e0972e5470-3696x4620.jpg", "https://www.linkedin.com/in/frank-kaplan-686027274/"),
        ("Anna Schmedes", "Consultant", "Sports Administration & Data Science", "Senior", "6a2033f57ec76ef3ac430ce9ff006133c2179f34-1067x1600.jpg", "https://www.linkedin.com/in/anna-schmedes-090960292/"),
        ("Jaeger Ouanounou", "Consultant", "Business Administration", "Sophomore", "65930981f2c770e4da1d38b24e755c0221701638-400x400.jpg", "https://www.linkedin.com/in/jaegero/"),
    ]),
    ("Peter Millar", "b32d692d1914518ee3d0aa7f10120008705c3eac-601x600.png", [
        ("Caroline Crews", "Project Manager", "Business Administration", "Junior", "35a6356f0982dc3d411610d8107ef85783978d85-3200x4000.jpg", "https://www.linkedin.com/in/caroline-crews/"),
        ("Mathias Reinartz", "Consultant", "Biology", "Junior", "99c15cb291e9c053e150bc303012c32a9f9c4df0-4724x4724.jpg", "https://www.linkedin.com/in/thomas-reinartz/"),
        ("Ria Shah", "Consultant", "Sports Administration & Management and Society", "Senior", "2faadaf0b275d84a2485f063f8c03bcd654bc8a9-4672x7008.jpg", "https://www.linkedin.com/in/riarshah04/"),
        ("Ty Fitch", "Director of Recruitment", "Business Administration & Economics", "Sophomore", "cc8067831ef40f5ceaa9484fe2e87a43119dd912-1365x2048.jpg", "https://www.linkedin.com/in/tyfitch/"),
        ("Connor Markwell", "Consultant", "Business Administration & Economics", "Sophomore", "3cf8d01cbf0c8cd2f91b07ec28baa552b05812a9-1330x1290.jpg", "https://www.linkedin.com/in/connor-markwell/"),
        ("Vanessa Convers", "Consultant", "Business Administration & Data Science", "Sophomore", "fb193b3776ec9ab15d252cac5db7a13276efbebf-400x400.jpg", "https://www.linkedin.com/in/vconversocampo/"),
        ("Vraj Parikh", "Consultant", "Health Policy and Management & Statistics", "Junior", "6b300648538231973660691c4cbfc2928150350c-1056x1074.png", "https://www.linkedin.com/in/vraj-parikh2027/"),
        ("Helen Sands", "Consultant", "Business Administration", "Sophomore", "e40531a160155641df556e842843981d7c36194d-2888x3610.jpg", "https://www.linkedin.com/in/hdsands05/"),
    ]),
]

CASE_STUDY = {
    "slug": "industry-spotlight-sports-media-and-broadcasting",
    "title": "Industry Spotlight: Sports Media & Broadcasting",
    "date": "March 26, 2026",
    "short_date": "3/26/2026",
    "cover": S + "a5b6bf9ef7d9579df63d4b6f9005712d9291ddd6-3420x1114.png",
    "slides": [S + x for x in [
        "88b965b385e1a43dd797b7fe94a5cd3cbdddbda0-3360x2138.png",
        "5be76ee5cc3d46dacaa7f2f5f03495e42a35f3f9-3294x2136.png",
        "1aa06b1ff692ff254552a9af56258bde7ad02b85-3294x2136.png",
        "1bcf948dd271c4e50738d9102a5cd07c9eb63731-3294x2136.png",
        "5f5e818d626284d255a246a2dfda51beb7d9a373-3294x2136.png",
        "7b165c57803cdc760abceca5fcb1f663119fa526-3294x2078.png",
        "f721457d544a406adf2a74a200ddd878b1d6ab43-3294x2136.png",
        "568988b84b2e7f12b547409f7cde60e35882bb4e-3294x2136.png",
        "191fdb71c8c4be8ae5d005139499593a4278667d-3294x2136.png",
        "b302d5ed91dbf9c45d25a2f7ad6c6b0e869a9fd1-3294x2136.png",
        "506bb5a824d40c316f0dc93c513e61c7e76eecbe-3294x2136.png",
    ]],
}

SERVICES_INTRO = [
    "We partner with sports properties, brands, and rights-holders to design growth-minded strategies, build engaging virtual and live experiences, and deliver data-driven insights that drive revenue and fan engagement. Our services include brand strategy, sponsorship and partnership analysis, experiential and ticketing strategies, proprietary research, and customized consulting engagements tailored to your objectives.",
]
SERVICES_TAG = "Let us help you convert insights into impact."
WHY_US = "We specialize in analyzing and engaging the 18-24 year old demographic — how they attend, watch, and engage with sports, media, teams, and leagues. Using quantitative research, behavioral analysis, and experiential testing, we design strategies that reach young fans where they are and convert short-term attention into long-term loyalty."
WHY_US_TAG = "Let us show you how to win the next generation of fans."
SERVICES = ["Brand Growth Strategies", "Media Marketing and Online Engagement", "Fan Experience and In-person Engagement",
            "Partnership and Sponsorship Analysis", "Strategic Initiatives", "Ticketing Strategies",
            "Data and Economic Analysis", "Proprietary Research", "Custom Consulting"]

APPLY_WHY = "We're committed to collaboration, growth, inclusion, mentorship, and providing real-world experiences that prepare students for professional success."
APPLY_STEPS = [
    ("Application", "A brief questionnaire to get to know you, your skills, and your experiences."),
    ("Video Interview", "An opportunity for you to provide context surrounding your skills and experience."),
    ("Interview", "A one-on-one interview consisting of behavioral and technical sections."),
]
FAQ = [
    ("What does the application process look like?", "There will be a preliminary application, followed by a group or individual case, and finally an individual interview."),
    ("What are we looking for in applications?", "Curious, hardworking people who have made quantifiable impact."),
    ("What majors and qualifications is CSCG looking for?", "We welcome candidates from all academic backgrounds and value diverse skill sets including creativity, analytics, and communication."),
    ("Additional questions", "If you have a specific question not covered here, please contact us via the Contact page."),
]
