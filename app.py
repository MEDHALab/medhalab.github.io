from flask import Flask, render_template


app = Flask(__name__)


SITE = {
    "group_name": "MEDHA Lab",
    "pi_name": "Punit Kumar",
    "pi_title": "Assistant Professor, School of Mechanical and Aerospace Engineering",
    "institution": "Nanyang Technological University, Singapore",
    "pi_email": "punitkumar@ntu.edu.sg",
    "address": "MAE, Nanyang Technological University, 50 Nanyang Ave, Singapore 639798",
    "scholar_link": "https://scholar.google.com/citations?user=fh5Z0eYAAAAJ&hl=en",
    "ntu_profile_link": "https://dr.ntu.edu.sg/entities/person/b1a3df3b-c7ff-4ebb-afab-c8ab2c13f5a4",
}


NEWS = [
    {
        "date": "2026-08-20",
        "title": "We welcome Dr. Tiffany Wu as our Postdoctoral Researcher",
        "summary": "Dr. Tiffany Wu joins MEDHA Lab from Northwestern University after completing a year of postdoctoral research, bringing valuable research experience in advanced alloy design, additive manufacturing, and materials characterization."
    },
    {
        "date": "2026-08-10",
        "title": "We welcome our first two PhD students, Gurharinder Singh and Fahad Mohammed",
        "summary": "MEDHA Lab welcomes its first two PhD students, Gurharinder Singh from IIT Delhi and Fahad Mohammed from the University of Bristol. We look forward to their enthusiasm for learning, exploring new ideas, and contributing to the development of next-generation materials."
    },
    {
        "date": "2026-07-06",
        "title": "Punit Kumar received National Research Foundation Fellowship",
        "summary": "Professor Punit Kumar has received the National Research Foundation Fellowship (NRFF), supporting a research programme focused on designing damage-tolerant materials for extreme environments."
    },
    {
        "date": "2025-09-01",
        "title": "Group launched at NTU!",
        "summary": "Here we go, MEDHA Lab has started investigating materials."
    },
]


RESEARCH_AREAS = [
    {
        "title": "Structural materials for extreme temperatures (4 K–2273 K)",
        "desc": "Placeholders for your theme description and representative projects."
    },
    {
        "title": "Resilient functional materials under coupled fields",
        "desc": "Electro-thermo-mechanical coupling, flexible electronics, harsh environments."
    },
]


# NOTE: photo paths are relative to the /static folder (used with url_for).
TEAM = {
    "pi": {
        "name": SITE["pi_name"],
        "title": f"{SITE['pi_title']}, {SITE['institution']}",
        "email": SITE["pi_email"],
        "office": "N3-02-C71",
        "photo": "img/punit sir.jpg",
        "bio": "Dr. Punit Kumar is an Assistant Professor in the School of Mechanical and Aerospace Engineering at Nanyang Technological University (NTU), Singapore, where he leads MEDHA Lab — Materials for Extremes by Designing Hierarchical structures using AI. His research integrates advanced manufacturing, fracture mechanics, and physics-informed AI to design damage-tolerant materials for extreme environments. Before joining NTU, he was a Project Scientist at the University of California, Berkeley, and an affiliated Scientist at Lawrence Berkeley National Laboratory. He earned his Ph.D. in Materials Engineering from the Indian Institute of Science, Bangalore. Dr. Kumar received the Singapore National Research Foundation (NRF) Fellowship in 2026 and was named among MIT Technology Review’s Innovators Under 35 Asia Pacific the same year. His earlier recognitions include the Acta Student Award (2019) and inclusion in the Stanford/Elsevier list of the world’s top 2% of scientists."
    },

    "members": {

        "Postdoctoral Researchers": [
            {
                "name": "Tiffany Wu",
                "role": "Postdoctoral Researcher",
                "topic": "Research area",
                "email": "tiffany.wu@ntu.edu.sg",
                "photo": "img/Tiffany.jpg",
                "bio": [
                    "Tiffany Wu is Taiwanese, born in the US, and grew up in China. She earned her B.S. in Engineering Physics from the University of Illinois Urbana-Champaign in 2019, during which she completed an exchange research program at Kyushu University's I2CNER in 2018. She went on to receive her Ph.D. in Materials Science and Engineering from Northwestern University in 2024, under the supervision of Prof. David Dunand.",

                    "Her doctoral research focused on developing creep-resistant Al-Ce based eutectic alloys through casting and additive manufacturing using laser powder-bed fusion. As part of this work, she conducted exchange research at Oak Ridge National Laboratory in 2022–23 on additive alloys. She then completed a year of postdoctoral research within the same group, focusing on high-throughput material design and testing of gradient materials, including superalloys, with an emphasis on creep and oxidation behavior.",

                    "She has since joined MEDHA Lab, continuing her work on cast and additive alloys while expanding into new areas, including refractory medium-entropy alloys studied at both much higher and lower temperatures, and fracture behavior."
                ],
                "hobbies": "A fan of Japanese anime and likes to draw fan art."
            }
        ],

        "PhD Students": [
            {
                "name": "Gurharinder Singh",
                "role": "PhD Student",
                "topic": "Research area",
                "email": "SI0001ER@e.ntu.edu.sg",
                "photo": "img/Gurharinder.jpg",
                "bio": [
                    "Gurharinder Singh was born and brought up in Delhi, India. He earned his B.Tech. in Material Science and Engineering, with a Minor in Quantum Technologies from the Department of Physics, at Indian Institute of Technology, Delhi, India (2025).",

                    "Following this, he worked under Prof. K. B. Balasubramanian on layered sputtered superconducting films, in research funded by ISRO (2026).",

                    "He has since joined MEDHA Lab, where he is working on refractory high entropy alloys and soft material systems manufactured through additive manufacturing, with a focus on their fracture behavior."
                ],
                "hobbies": "Music and games."
            },

            {
                "name": "Fahad Mohammed",
                "role": "PhD Student",
                "topic": "Research area",
                "email": "FAHAD002@e.ntu.edu.sg",
                "photo": "img/Fahad.jpg",
                "bio": [
                    "Fahad Mohammed graduated his B.Tech in Metallurgical and Materials Engineering from the National Institute of Technology, Andhra Pradesh, India (2021–2025), where he conducted heat treatment processes, metallographic analysis, and mechanical testing of materials.",

                    "He went on to pursue his master's in Advanced Composites at the University of Bristol, United Kingdom (2025–2026), where his research with GKN Aerospace focused on defect-driven failure in bonded composite joints using FEA, and he contributed to publications and conferences with TU Delft, Netherlands, and the University of the West of England, UK.",

                    "His work combines finite element modelling, experimental validation, and data-driven AI/ML to understand material behavior and fracture mechanics, and he continues this work at MEDHA Lab."
                ],
                "hobbies": "Sports and walking."
            }
        ],

        "MSc Students": [
            {
                "name": "Chan Yuet Yan",
                "role": "MSc Student",
                "topic": "Research area",
                "email": "YUETYAN001@e.ntu.edu.sg",
                "photo": "img/Serena.jpg"
            }
        ],

        "Undergraduate Students": [
            {
                "name": "Keith Tor Jun Yu",
                "role": "Undergraduate Student",
                "topic": "Research area",
                "email": "KTOR001@e.ntu.edu.sg",
                "photo": "img/Keith.jpg"
            },

            {
                "name": "Saranretnam S/O Chelvaretnam",
                "role": "Undergraduate Student",
                "topic": "Research area",
                "email": "SARA0084@e.ntu.edu.sg",
                "photo": "img/Saran.jpg"
            },

            {
                "name": "Shekhar Rajat",
                "role": "Undergraduate Student",
                "topic": "Research area",
                "email": "RAJAT004@e.ntu.edu.sg",
                "photo": "img/Rajat.jpg"
            },

            {
                "name": "Porwal Dhriti Dhiraj Kumar",
                "role": "Undergraduate Student",
                "topic": "Research area",
                "email": "DHRITI002@e.ntu.edu.sg",
                "photo": "img/Dhriti.jpg"
            }
        ]

    }
}


PUBLICATIONS = [
    {
        "authors": "P. Kumar, D. Cook, W. Wang, P. Borges, A. M. Minor, M. Asta, R. O. Ritchie*",
        "title": "Fracture behavior of high-entropy alloys: Resistance to fracture from strain hardening and softening",
        "journal": "Matter",
        "details": "8-4 (2025)",
        "doi": "https://doi.org/10.1016/j.matt.2025.102042",
    },
    {
        "authors": "D. H. Cook#, P. Kumar#*, C. H. Belcher, M. Payne, P. Borges, W. Wang, F. Walsh, A. Devaraj, M. Zhang, M. Asta, A. M. Minor, D. Apelian, E. J. Lavernia, R. O. Ritchie*",
        "title": "Kink bands promote exceptional fracture resistance in a NbTaTiHf refractory medium-entropy alloy",
        "journal": "Science",
        "details": "384, 178–184 (2024)",
        "doi": "https://www.science.org/doi/10.1126/science.adn2428",
    },
    {
        "authors": "P. Kumar, H. Sheng, D. H. Cook, K. Chen, U. Ramamurty, X. Tan, R. O. Ritchie*",
        "title": "A strong fracture-resistant high-entropy alloy with nano-bridged honeycomb microstructure: A critical role of 3D printing in promoting strength without compromising toughness",
        "journal": "Nature Communications",
        "details": "15(1) (2024), 841",
        "doi": "https://doi.org/10.1038/s41467-024-45178-2",
    },
    {
        "authors": "P. Kumar, M. Michalek, D. H. Cook, H. Sheng, K. B. Lau, P. Wang, M. Zhang, A. M. Minor, U. Ramamurty, R. O. Ritchie*",
        "title": "On the strength and fracture toughness of an additive manufactured CrCoNi medium-entropy alloy",
        "journal": "Acta Materialia",
        "details": "258 (2023), 119249",
        "doi": "https://doi.org/10.1016/j.actamat.2023.119249",
    },
    {
        "authors": "P. Kumar, X. Gou, D. H. Cook, N. J. Morrison, M. I. Payne, W. Wang, M. Zhang, M. Asta, A. M. Minor, R. Cao, Y. Li, R. O. Ritchie*",
        "title": "Degradation of the mechanical properties of NbMoTaW refractory high-entropy alloy in tension",
        "journal": "Acta Materialia",
        "details": "279, 120297 (2024)",
        "doi": "https://doi.org/10.1016/j.actamat.2024.120297",
    },
    {
        "authors": "P. Kumar, S. J. Kim, Q. Yu, J. Ell, M. Zhang, Y. Yang, J. Y. Kim, H. Park, A. M. Minor, E. S. Park, R. O. Ritchie*",
        "title": "Compressive vs. tensile yield and fracture toughness behavior of a body-centered cubic refractory high-entropy superalloy Al0.5Nb1.25Ta1.25TiZr at temperatures from ambient to 1200°C",
        "journal": "Acta Materialia",
        "details": "245 (2023), 118620",
        "doi": "https://doi.org/10.1016/j.actamat.2022.118620",
    },
    {
        "authors": "X. Xu#, P. Kumar#, R. Cao, Q. Ye, Y. Chu, Y. Tian, Y. Li*, R. O. Ritchie*",
        "title": "Exceptional cryogenic-to-ambient impact toughness of a low carbon micro-alloyed steel with a multi-heterogeneous structure",
        "journal": "Acta Materialia",
        "details": "274, 120019 (2024)",
        "doi": "https://doi.org/10.1016/j.actamat.2024.120019",
    },
    {
        "authors": "S Huang*, P. Kumar, W. Y. Yeong, R. L. Narayan, U. Ramamurty",
        "title": "Fracture Behavior of Laser Powder Bed Fusion Fabricated Ti41Nb via In-situ Alloying",
        "journal": "Acta Materialia",
        "details": "225 (2021), 117593",
        "doi": "https://doi.org/10.1016/j.actamat.2021.117593",
    },
    {
        "authors": "T.H. Becker, P. Kumar, U. Ramamurty*",
        "title": "Fracture and fatigue in additively manufactured metals",
        "journal": "Acta Materialia",
        "details": "219 (2021), 117240",
        "doi": "https://doi.org/10.1016/j.actamat.2021.117240",
    },
    {
        "authors": "P. Kumar, R. Jayaraj, J. Suryawanshi, U.R. Satwik, J. McKinnell, U. Ramamurty*",
        "title": "Fatigue strength of additively manufactured 316L austenitic stainless steel",
        "journal": "Acta Materialia",
        "details": "199 (2020), 225–239",
        "doi": "https://doi.org/10.1016/j.actamat.2020.08.033",
    },
    {
        "authors": "P. Kumar, U. Ramamurty*",
        "title": "Microstructural optimization through heat treatment for enhancing the fracture toughness and fatigue crack growth resistance of selective laser melted Ti–6Al–4V alloy",
        "journal": "Acta Materialia",
        "details": "169 (2019), 45–59",
        "doi": "https://doi.org/10.1016/j.actamat.2019.03.003",
    },
    {
        "authors": "P. Kumar, O. Prakash, U. Ramamurty*",
        "title": "Micro-and meso-structures and their influence on mechanical properties of selectively laser melted Ti-6Al-4V",
        "journal": "Acta Materialia",
        "details": "154 (2018), 246–260",
        "doi": "https://doi.org/10.1016/j.actamat.2018.05.044",
    },
]


@app.context_processor
def inject_site():
    return dict(**SITE)


# Trailing slashes so each page is exported as <page>/index.html
@app.get("/")
def home():
    return render_template("home.html", news=NEWS)


@app.get("/research/")
def research():
    return render_template("research.html", research_areas=RESEARCH_AREAS)


@app.get("/team/")
def team():
    return render_template("team.html", team=TEAM)


@app.get("/publications/")
def publications():
    return render_template("publications.html", publications=PUBLICATIONS)


@app.get("/news/")
def news():
    return render_template("news.html", news=NEWS)


@app.get("/opportunities/")
def opportunities():
    return render_template("opportunities.html")


@app.get("/teaching/")
def teaching():
    return render_template("teaching.html")


@app.get("/gallery/")
def gallery():
    return render_template("gallery.html")


@app.get("/contact/")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
