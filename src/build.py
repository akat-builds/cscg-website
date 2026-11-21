import os, shutil, json, html
from data import *

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "..", "dist")
e = html.escape

# ---------- icons ----------
I = {
    "chev": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5"/></svg>',
    "right": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>',
    "left": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M13 8H3M7 4 3 8l4 4"/></svg>',
    "crumb": '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m4.5 2.5 3.5 3.5-3.5 3.5"/></svg>',
    "ext": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6 3H3v10h10v-3M9 3h4v4M13 3 7 9"/></svg>',
    "plus": '<svg viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 1v12M1 7h12"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 5l14 14M19 5 5 19"/></svg>',
    "li": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4v11H3zM9.5 9.75h3.8v1.5h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1v5.45h-4v-4.83c0-1.15-.02-2.63-1.6-2.63-1.6 0-1.85 1.25-1.85 2.55v4.91h-4z"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
}
SVC_ICONS = [  # simple line icons, one per service
    '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    '<path d="M3 10c3-4 15-4 18 0v6c-3 4-15 4-18 0z"/><path d="M3 10c3 4 15 4 18 0"/>',
    '<path d="M8 12l3 3 5-6"/><circle cx="12" cy="12" r="9"/>',
    '<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>',
    '<path d="M3 8a2 2 0 0 0 0 4v4h18v-4a2 2 0 0 1 0-4V4H3z"/><path d="M14 4v12"/>',
    '<path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/>',
    '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
    '<path d="M4 6h16M4 12h10M4 18h7"/><circle cx="18" cy="16" r="3"/>',
]

def sanity(img_id, w=640, h=800):
    return f"{S}{img_id}?w={w}&auto=format"

def sanity_logo(img_id, w=300):
    return f"{S}{img_id}?w={w}&auto=format"

NAV_TEAM = [("Board of Advisors", "/team/advisors/", "Industry leaders guiding CSCG"),
            ("Executive Board", "/team/executives/", "The students running the group"),
            ("Consultant Development Program", "/team/cdp/", "Where new members start"),
            ("Project Teams", "/team/projects/", "Current client engagements"),
            ("Alumni", "/team/alumni/", "Where our members go next")]
NAV_WORK = [("Case Studies", "/work/case-studies/", "Published research and spotlights"),
            ("Services", "/work/services/", "What we do for clients"),
            ("Clients", "/work/clients/", "Who we've worked with")]

def dd(items, cur):
    return "".join(f'<a href="{u}"{" aria-current=\"page\"" if u == cur else ""}><strong>{e(t)}</strong><small>{e(d)}</small></a>' for t, u, d in items)

def header(cur):
    team_on = cur.startswith("/team/")
    work_on = cur.startswith("/work/")
    ac = lambda u: ' aria-current="page"' if u == cur else ""
    return f'''
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <div class="pill">
      <a class="brand" href="/" aria-label="Carolina Sports Consulting Group home">
        <img class="logo-light" src="{IMG['logo_white']}" alt="" width="34" height="34">
        <img class="logo-dark" src="{IMG['logo_blue']}" alt="" width="34" height="34">
        <span>Carolina Sports Consulting Group</span>
      </a>
      <ul class="nav">
        <li><a class="nav-link" href="/about/"{ac("/about/")}>About Us</a></li>
        <li class="has-menu"><button class="nav-link{" is-section" if team_on else ""}" aria-expanded="false" aria-haspopup="true">Our Team {I['chev']}</button>
          <div class="dropdown">{dd(NAV_TEAM, cur)}</div></li>
        <li class="has-menu"><button class="nav-link{" is-section" if work_on else ""}" aria-expanded="false" aria-haspopup="true">Our Work {I['chev']}</button>
          <div class="dropdown">{dd(NAV_WORK, cur)}</div></li>
      </ul>
    </div>
    <div class="pill header-cta">
      <a class="nav-link" href="/contact/"{ac("/contact/")}>Contact Us</a>
      <a class="btn btn-primary" href="/apply/">Apply</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">{I['menu']}</button>
    </div>
  </div>
</header>
<div class="mobile-menu" role="dialog" aria-label="Site menu">
  <button class="close" aria-label="Close menu">{I['close']}</button>
  <a href="/">Home</a>
  <a href="/about/">About Us</a>
  <h3>Our Team</h3>{"".join(f'<a href="{u}">{e(t)}</a>' for t, u, _ in NAV_TEAM)}
  <h3>Our Work</h3>{"".join(f'<a href="{u}">{e(t)}</a>' for t, u, _ in NAV_WORK)}
  <h3>Get in touch</h3><a href="/contact/">Contact Us</a>
  <a class="btn btn-primary" href="/apply/">Apply to CSCG</a>
</div>'''

FOOTER = f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a href="/" aria-label="Home"><img src="{IMG['logo_horiz_white']}" alt="CSCG"></a>
        <p>A student-run sports consulting group at the University of North Carolina at Chapel Hill.</p>
      </div>
      <div><h3>Our Team</h3><ul>{"".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u, _ in NAV_TEAM)}</ul></div>
      <div><h3>Our Work</h3><ul>{"".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u, _ in NAV_WORK)}</ul></div>
      <div><h3>CSCG</h3><ul><li><a href="/about/">About Us</a></li><li><a href="/apply/">Apply</a></li><li><a href="/contact/">Contact Us</a></li></ul></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Carolina Sports Consulting Group</span>
      <div class="footer-social">
        <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{I['li']}</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{I['ig']}</a>
      </div>
    </div>
  </div>
</footer>'''

def page(path, title, desc, body):
    full_title = "Carolina Sports Consulting Group" if path == "/" else f"{title} | Carolina Sports Consulting Group"
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{IMG['hero']}">
<meta name="theme-color" content="#081A2F">
<link rel="icon" href="{IMG['logo_blue']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
{header(path)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="/main.js" defer></script>
</body>
</html>'''
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(doc)

def page_hero(crumbs, title, lede="", extra="", img=None):
    cr = ""
    for i, (t, u) in enumerate(crumbs):
        cr += (f'<a href="{u}">{e(t)}</a>' if u else f'<span>{e(t)}</span>') + (I["crumb"] if i < len(crumbs) - 1 else "")
    return f'''
<section class="page-hero on-dark">
  <div class="bg"><img src="{img or IMG['boxseats']}" alt="Kenan Stadium box seats"></div>
  <div class="wrap">
    <nav class="crumb" aria-label="Breadcrumb">{cr}</nav>
    <h1>{title}</h1>
    {f'<p class="lede">{lede}</p>' if lede else ""}
    {extra}
  </div>
</section>'''

def subnav(items, cur):
    return '<nav class="subnav" aria-label="Section pages">' + "".join(
        f'<a href="{u}"{" aria-current=\"page\"" if u == cur else ""}>{e(t)}</a>' for t, u, _ in items) + "</nav>"

def person(p, lead_roles=("Project Manager",)):
    name, role, major, year, img, li = p
    lead = role in lead_roles
    return f'''
<article class="person">
  <div class="ph"><img src="{sanity(img)}" alt="{e(name)}" loading="lazy" width="640" height="800"></div>
  <div class="info">
    <h3>{e(name)}</h3>
    <div class="role">{e(role)}</div>
    <div class="major">{e(major)}</div>
    <div class="meta">
      <span class="tag">{e(year)}</span>
      <a class="li-btn" href="{li}" target="_blank" rel="noopener" aria-label="{e(name)} on LinkedIn">{I['li']}</a>
    </div>
  </div>
</article>'''

def marquee(logos):
    imgs = "".join(f'<img src="{u}" alt="{e(a)}" loading="lazy">' for u, a in logos)
    dup = "".join(f'<img src="{u}" alt="" aria-hidden="true" loading="lazy">' for u, a in logos)
    return f'<div class="marquee"><div class="marquee-track">{imgs}{dup}</div></div>'

def logo_wall(logos):
    return '<div class="logo-wall">' + "".join(f'<div class="logo-tile"><img src="{u}" alt="{e(a)}" loading="lazy"></div>' for u, a in logos) + '</div>'

def cta(title, muted, lede):
    return f'''
<section class="section bg-mist">
  <div class="wrap">
    <div class="cta-band">
      <div class="row">
        <div>
          <h2 class="h-section">{title} <span class="muted" style="color:var(--carolina)">{muted}</span></h2>
          <p class="lede" style="color:#B9C9DD">{lede}</p>
        </div>
        <div class="actions">
          <a class="btn btn-primary" href="{APPLY_FORM}" target="_blank" rel="noopener">Start your application</a>
          <a class="btn btn-ghost" href="/contact/">Contact us</a>
        </div>
      </div>
    </div>
  </div>
</section>'''

# =========================================================
# HOME
# =========================================================
chips = [
    ("live", "ESPN", "Active project team", "top:24%;right:22%", 0.5, True),
    ("live", "Nike", "Active project team", "top:40%;right:8%", 0.65, False),
    ("live", "Joe Gibbs Racing", "Active project team", "top:58%;right:20%", 0.8, False),
    ("live", "Peter Millar", "Active project team", "top:74%;right:10%", 0.95, False),
    ("", "PGA TOUR", "Past client", "top:16%;right:6%", 1.1, False),
    ("", "Kenan Stadium", "Chapel Hill, NC", "top:82%;right:26%", 1.25, False),
]
chip_html = "".join(
    f'<div class="chip{" keep" if keep else ""}" style="{pos};animation-delay:{d}s,{d + .7}s"><i class="dot {cls}"></i><div><strong>{e(t)}</strong><span>{e(s)}</span></div></div>'
    for cls, t, s, pos, d, keep in chips)

home = f'''
<section class="hero on-dark">
  <div class="hero-bg"><img src="{IMG['hero']}" alt="Kenan Stadium and the Bell Tower" fetchpriority="high"></div>
  <div class="chips" aria-hidden="true"><div class="wrap" style="position:relative;height:100%">{chip_html}</div></div>
  <div class="wrap">
    <div class="hero-copy">
      <div class="badge"><i class="dot live"></i>Student-run consulting at UNC Chapel Hill</div>
      <h1 class="h-display"><span class="line">Carolina Sports Consulting Group.</span><span class="line muted">Strategic Insights to Boost Your Game.</span></h1>
      <p class="lede">We help sports properties, brands, and organizations tackle their biggest challenges through strategic, data-driven insights.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/apply/">Apply to CSCG</a>
        <a class="btn btn-ghost" href="/work/case-studies/">See our work</a>
      </div>
    </div>
  </div>
</section>

<div class="logo-strip">
  <div class="wrap">
    <p>Trusted by the properties and brands behind the game</p>
    {marquee(CLIENT_LOGOS)}
  </div>
</div>

<section class="section bg-mist">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><div class="num"><span data-count="45">45</span><sup>+</sup></div><div class="label">Consultants</div></div>
      <div class="stat"><div class="num"><span data-count="15">15</span><sup>+</sup></div><div class="label">Clients Served</div></div>
      <div class="stat"><div class="num"><span class="pre">Fall</span><span data-count="2024" data-from="2000">2024</span></div><div class="label">Founded</div></div>
    </div>
  </div>
</section>

<section class="section tight bg-mist">
  <div class="wrap split top wide-left">
    <div class="letter">
      <h2 class="h-section">A message from <span class="muted">our founders.</span></h2>
      <div style="margin-top:32px">{"".join(f"<p>{e(p)}</p>" for p in FOUNDERS_LETTER)}</div>
      <div class="signature">
        <img src="{IMG['logo_blue']}" alt="">
        <div><strong>Trevor Lan, Riley Snow, &amp; Corson Schweizer</strong><span>Founders, Carolina Sports Consulting Group</span></div>
      </div>
    </div>
    <div class="photo sticky"><img src="{IMG['founders']}" alt="CSCG Founders: Trevor Lan, Riley Snow, and Corson Schweizer" loading="lazy"></div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="section-head"><h2 class="h-section">Our Mission. <span class="muted">Two commitments drive everything we do.</span></h2></div>
    <div class="grid-2">
      {"".join(f'<div class="card mission-card bg-mist"><span class="n" aria-hidden="true">{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(MISSION))}
    </div>
  </div>
</section>

<section class="section bg-mist">
  <div class="wrap">
    <div class="section-head"><h2 class="h-section">Our Expertise. <span class="muted">Strategy, data, and research for the sports world.</span></h2></div>
    <div class="tabset" data-tabset>
      <div class="tablist" role="tablist" aria-label="Our expertise">
        {"".join(f'<button class="tab-btn" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="exp-{i}" id="exp-tab-{i}"><strong>{e(t)}</strong><span class="desc"><span>{e(d)}</span></span><i class="bar"></i></button>' for i, (t, d, _) in enumerate(EXPERTISE))}
      </div>
      <div class="tab-panels">
        {"".join(f'<div class="tab-panel{" active" if i == 0 else ""}" role="tabpanel" id="exp-{i}" aria-labelledby="exp-tab-{i}"><img src="{IMG[k]}" alt="" loading="lazy"><div class="cap"><strong>{e(t)}</strong><span>CSCG consultants at work</span></div></div>' for i, (t, d, k) in enumerate(EXPERTISE))}
      </div>
    </div>
  </div>
</section>
''' + cta("Recruiting every Fall and Spring.", "Come build with us.", "Students from every major are welcome. See what the process looks like, or jump straight into the application.")

page("/", "Home", "Carolina Sports Consulting Group is a student-run consulting group at UNC Chapel Hill serving sports properties, brands, and talent.", home)

# =========================================================
# ABOUT
# =========================================================
about = page_hero([("Home", "/"), ("About Us", None)], "About Us",
    "A student-run consulting group that specializes in properties, brands and talents in the sports world.") + f'''
<section class="section bg-mist">
  <div class="wrap split">
    <div class="photo" style="aspect-ratio:5/4"><img src="{IMG['event']}" alt="Our team hard at work" loading="lazy"></div>
    <div>
      <h2 class="h-section">Creative and Innovative <span class="muted">Solutions.</span></h2>
      <p class="lede">Carolina Sports Consulting Group is a student-run consulting group that specializes in properties, brands and talents in the sports world. We offer strategic guidance, analysis and research to help our clients succeed. CSCG provides valuable hands-on professional development skills to UNC students.</p>
    </div>
  </div>
</section>
<section class="section tight bg-mist">
  <div class="wrap split">
    <div>
      <h2 class="h-section">Professional Development <span class="muted">for UNC Students.</span></h2>
      <p class="lede">As a team of young and innovative consultants, we are dedicated to helping our clients navigate the challenging and ever-evolving sports industry. Contact us today and let us help you achieve your goals!</p>
      <div style="margin-top:28px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" href="/contact/">Contact us</a><a class="btn btn-outline" href="/team/executives/">Meet the team</a></div>
    </div>
    <div class="photo" style="aspect-ratio:5/4"><img src="{IMG['profdev']}" alt="professionalDevelopment" loading="lazy"></div>
  </div>
</section>
<section class="section bg-white">
  <div class="wrap">
    <div class="section-head"><h2 class="h-section">Where Our Alumni &amp; <span class="muted">Members Have Worked.</span></h2></div>
    {logo_wall(ABOUT_LOGOS)}
  </div>
</section>
''' + cta("Want to join CSCG?", "Applications open each semester.", "We recruit each Fall and Spring semester.")
page("/about/", "About Us", "Learn about Carolina Sports Consulting Group, a student-run sports consulting group at UNC Chapel Hill.", about)

# =========================================================
# TEAM: ADVISORS
# =========================================================
adv_cards = "".join(f'''
<article class="advisor">
  <div class="ph"><img src="{img}" alt="{e(n)}" loading="lazy"></div>
  <div>
    <div class="top"><div><h3>{e(n)}</h3><div class="role">{e(t)}</div></div>
      <a class="li-btn" href="{li}" target="_blank" rel="noopener" aria-label="Open {e(n)}'s LinkedIn">{I['li']}</a></div>
    <p>{e(b)}</p>
  </div>
</article>''' for n, t, b, img, li in ADVISORS)
page("/team/advisors/", "Board of Advisors", "CSCG's Board of Advisors: UNC alumni leading across the NFL, PGA TOUR, MLB, and college athletics.",
     page_hero([("Home", "/"), ("Our Team", None), ("Board of Advisors", None)], "Board of Advisors", extra=subnav(NAV_TEAM, "/team/advisors/")) +
     f'<section class="section bg-mist"><div class="wrap"><div class="grid-2 advisors">{adv_cards}</div></div></section>')

# =========================================================
# TEAM: EXEC
# =========================================================
page("/team/executives/", "Executive Board", "Meet the CSCG Executive Board.",
     page_hero([("Home", "/"), ("Our Team", None), ("Executive Board", None)], "Executive Board", extra=subnav(NAV_TEAM, "/team/executives/")) +
     f'<section class="section bg-mist"><div class="wrap"><div class="grid-3">{"".join(person(p) for p in EXEC)}</div></div></section>')

# =========================================================
# TEAM: CDP
# =========================================================
page("/team/cdp/", "Consultant Development Program", "The CSCG Consultant Development Program introduces new members to the fundamentals of sports consulting.",
     page_hero([("Home", "/"), ("Our Team", None), ("Consultant Development Program", None)], "Consultant Development Program",
               lede=e(CDP_INTRO), extra=subnav(NAV_TEAM, "/team/cdp/")) +
     f'<section class="section bg-mist"><div class="wrap"><div class="grid-4">{"".join(person(p) for p in CDP)}</div></div></section>')

# =========================================================
# TEAM: PROJECTS
# =========================================================
def slug(s): return s.lower().replace(" ", "-")
tabs = "".join(f'''<button class="team-tab" role="tab" data-target="{slug(c)}" aria-controls="{slug(c)}" aria-selected="false">
  <span class="lg"><img src="{sanity_logo(logo)}" alt=""></span><span><strong>{e(c)}</strong><span>{len(m)} members</span></span></button>''' for c, logo, m in PROJECTS)
panels = "".join(f'''<div class="team-panel" role="tabpanel" id="{slug(c)}">
  <div class="team-panel-head"><img src="{sanity_logo(logo, 400)}" alt="{e(c)} logo"><h2 class="sr-only">{e(c)}</h2></div>
  <div class="grid-4">{"".join(person(p) for p in m)}</div></div>''' for c, logo, m in PROJECTS)
page("/team/projects/", "Project Teams", "CSCG's current project teams for ESPN, Joe Gibbs Racing, Nike, and Peter Millar.",
     page_hero([("Home", "/"), ("Our Team", None), ("Project Teams", None)], "Project Teams", extra=subnav(NAV_TEAM, "/team/projects/")) +
     f'<section class="section bg-mist"><div class="wrap" data-teams><div class="team-tabs" role="tablist" aria-label="Project teams">{tabs}</div>{panels}</div></section>')

# =========================================================
# TEAM: ALUMNI
# =========================================================
page("/team/alumni/", "Our Alumni", "Where CSCG alumni work.",
     page_hero([("Home", "/"), ("Our Team", None), ("Alumni", None)], "Our Alumni", extra=subnav(NAV_TEAM, "/team/alumni/")) + f'''
<section class="section bg-mist"><div class="wrap">
  <div class="section-head"><h2 class="h-section">Where Our <span class="muted">Alumni Work.</span></h2>
  <p class="lede">Our alumni have gone on to build impactful careers across leading companies from Fortune 500s to innovative startups in sports, finance, and beyond.</p></div>
  {logo_wall(ALUMNI_LOGOS)}
</div></section>''')

# =========================================================
# WORK: CASE STUDIES
# =========================================================
cs = CASE_STUDY
cs_url = f"/work/case-studies/{cs['slug']}/"
page("/work/case-studies/", "Case Studies", "Case studies and industry spotlights from Carolina Sports Consulting Group.",
     page_hero([("Home", "/"), ("Our Work", None), ("Case Studies", None)], "Case Studies", extra=subnav(NAV_WORK, "/work/case-studies/")) + f'''
<section class="section bg-mist"><div class="wrap">
  <a class="case-card" href="{cs_url}">
    <div class="cover"><img src="{cs['cover']}?w=1200&auto=format" alt="{e(cs['title'])}" loading="lazy"></div>
    <div class="body"><span class="date">{cs['short_date']}</span><h2>{e(cs['title'])}</h2><span class="more">Read the case study {I['right']}</span></div>
  </a>
</div></section>''')

thumbs = "".join(f'<button aria-label="Go to slide {i + 1}" aria-current="{"true" if i == 0 else "false"}"><img src="{s}?w=240&auto=format" alt="" loading="lazy"></button>' for i, s in enumerate(cs["slides"]))
page(cs_url, cs["title"], "CSCG Industry Spotlight on sports media and broadcasting.",
     page_hero([("Home", "/"), ("Case Studies", "/work/case-studies/"), ("Industry Spotlight", None)], e(cs["title"]),
               lede=f"Published: {cs['date']}") + f'''
<section class="section bg-mist"><div class="wrap">
  <div style="margin-bottom:24px"><a class="btn btn-outline" href="/work/case-studies/">{I['left']} Back to Case Studies</a></div>
  <div class="viewer" data-viewer data-slides='{json.dumps(cs["slides"])}'>
    <div class="viewer-stage"><img src="{cs['slides'][0]}?w=1800&auto=format" alt="Slide 1 of {len(cs['slides'])}"></div>
    <div class="viewer-bar">
      <div class="count"><span data-cur>1</span> <span>/ {len(cs['slides'])}</span></div>
      <div class="ctrls">
        <button data-prev aria-label="Previous slide">{I['left']}</button>
        <button data-next aria-label="Next slide">{I['right']}</button>
        <a data-open href="{cs['slides'][0]}" target="_blank" rel="noopener" aria-label="Open slide full size">{I['ext']}</a>
      </div>
    </div>
    <div class="thumbs">{thumbs}</div>
  </div>
</div></section>''')

# =========================================================
# WORK: SERVICES
# =========================================================
svc = "".join(f'<div class="service"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SVC_ICONS[i]}</svg></span><h3>{e(s)}</h3></div>' for i, s in enumerate(SERVICES))
page("/work/services/", "Our Services", "Brand strategy, sponsorship analysis, fan experience, ticketing, research, and custom consulting for sports properties and brands.",
     page_hero([("Home", "/"), ("Our Work", None), ("Services", None)], "Our Services", extra=subnav(NAV_WORK, "/work/services/")) + f'''
<section class="section bg-mist"><div class="wrap split">
  <div>
    <h2 class="h-section">Carolina Sports <span class="muted">Consulting Group.</span></h2>
    {"".join(f'<p class="lede">{e(p)}</p>' for p in SERVICES_INTRO)}
    <p class="tagline">{e(SERVICES_TAG)}</p>
  </div>
  <div class="stack-photos">
    <div class="photo"><img src="{IMG['services1']}" alt="Carolina Sports Consulting Group" loading="lazy"></div>
    <div class="photo"><img src="{IMG['services2']}" alt="Carolina Sports Consulting Group engaging fans" loading="lazy"></div>
  </div>
</div></section>
<section class="section on-dark"><div class="wrap why-grid">
  <h2 class="h-section">Why us</h2>
  <div><p class="why">{e(WHY_US)}</p><p class="tagline" style="margin-top:24px">{e(WHY_US_TAG)}</p></div>
</div></section>
<section class="section bg-mist"><div class="wrap">
  <div class="section-head"><h2 class="h-section">Services <span class="muted">We Offer.</span></h2></div>
  <div class="grid-3">{svc}</div>
</div></section>''' + f'''
<section class="section tight bg-mist"><div class="wrap"><div class="cta-band"><div class="row">
  <div><h2 class="h-section">Have a challenge for us? <span class="muted" style="color:var(--carolina)">Let's talk.</span></h2></div>
  <div class="actions"><a class="btn btn-primary" href="/contact/">Contact us</a><a class="btn btn-ghost" href="/work/clients/">See past clients</a></div>
</div></div></div></section>''')

# =========================================================
# WORK: CLIENTS
# =========================================================
quotes = "".join(f'''<div class="quote{" active" if i == 0 else ""}">
  <div class="q-logo"><img src="{u}" alt="{e(a)}" loading="lazy"></div>
  <div><blockquote>&ldquo;{e(q)}&rdquo;</blockquote><cite>{e(n)}</cite></div></div>''' for i, (u, a, n, q) in enumerate(TESTIMONIALS))
page("/work/clients/", "Our Past Clients", "Past clients of Carolina Sports Consulting Group, including the PGA TOUR, Under Armour, DAZN, the LPGA, and UNC Athletics.",
     page_hero([("Home", "/"), ("Our Work", None), ("Clients", None)], "Our Past Clients", extra=subnav(NAV_WORK, "/work/clients/")) + f'''
<section class="section bg-mist"><div class="wrap">
  <h2 class="sr-only">Client logos</h2>
  {logo_wall(CLIENT_LOGOS)}
</div></section>
<section class="section on-dark"><div class="wrap">
  <div class="section-head"><h2 class="h-section">What clients <span class="muted">say.</span></h2></div>
  <div class="quotes" data-quotes>
    {quotes}
    <div class="quote-nav"><button data-prev aria-label="Previous testimonial">{I['left']}</button><button data-next aria-label="Next testimonial">{I['right']}</button>
      <div class="quote-dots" aria-hidden="true">{"".join("<span></span>" for _ in TESTIMONIALS)}</div></div>
  </div>
</div></section>''')

# =========================================================
# CONTACT
# =========================================================
page("/contact/", "Contact Us", "Get in touch with Carolina Sports Consulting Group.",
     page_hero([("Home", "/"), ("Contact Us", None)], "Contact Us") + f'''
<section class="section bg-mist"><div class="wrap split top">
  <div>
    <h2 class="h-section">Let's work <span class="muted">together.</span></h2>
    <p class="lede">Questions about a project or about joining CSCG? Send us a message or reach us on social.</p>
    <div class="social-links">
      <a class="social-link" href="{LINKEDIN}" target="_blank" rel="noopener"><span class="ic">{I['li']}</span><span>LinkedIn<small>Carolina Sports Consulting Group</small></span></a>
      <a class="social-link" href="{INSTAGRAM}" target="_blank" rel="noopener"><span class="ic">{I['ig']}</span><span>Instagram<small>@carolina_sports_consulting</small></span></a>
    </div>
  </div>
  <form class="form-card" data-contact novalidate>
    <div class="fields">
      <div class="field"><label for="fn">First Name</label><input id="fn" name="first" autocomplete="given-name"></div>
      <div class="field"><label for="ln">Last Name</label><input id="ln" name="last" autocomplete="family-name"></div>
      <div class="field"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email"></div>
      <div class="field"><label for="ph">Phone</label><input id="ph" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field full"><label for="msg">Message</label><textarea id="msg" name="message"></textarea></div>
    </div>
    <div style="margin-top:20px"><button class="btn btn-primary" type="submit">Submit</button></div>
    <p class="form-note" role="status">This form isn't connected yet. For now, message us on <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a> or <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>.</p>
  </form>
</div></section>''')

# =========================================================
# APPLY
# =========================================================
steps = "".join(f'<div class="step"><div class="num">{i + 1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(APPLY_STEPS))
faq = "".join(f'<details><summary>{e(q)}<span class="pm">{I["plus"]}</span></summary><p>{e(a).replace("Contact page", "<a href=\"/contact/\">Contact page</a>")}</p></details>' for q, a in FAQ)
page("/apply/", "Apply", "Apply to join Carolina Sports Consulting Group. We recruit each Fall and Spring semester.",
     page_hero([("Home", "/"), ("Apply", None)], "Apply", lede="We recruit each Fall and Spring semester.",
               extra=f'<div class="actions"><a class="btn btn-primary" href="{APPLY_FORM}" target="_blank" rel="noopener">Start your application {I["ext"]}</a><a class="btn btn-ghost" href="#faq">Read the FAQ</a></div>') + f'''
<section class="section bg-mist"><div class="wrap split">
  <div>
    <h2 class="h-section">Why <span class="muted">CSCG.</span></h2>
    <p class="lede">{e(APPLY_WHY)}</p>
  </div>
  <div class="stack-photos">
    <div class="photo"><img src="{IMG['apply1']}" alt="Program image" loading="lazy"></div>
    <div class="photo"><img src="{IMG['apply2']}" alt="Case interview" loading="lazy"></div>
  </div>
</div></section>
<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2 class="h-section">How the process <span class="muted">works.</span></h2></div>
  <div class="steps">{steps}</div>
  <div style="margin-top:40px"><a class="btn btn-primary" href="{APPLY_FORM}" target="_blank" rel="noopener">Start your application {I["ext"]}</a></div>
</div></section>
<section class="section bg-mist" id="faq"><div class="wrap split top">
  <h2 class="h-section">Application <span class="muted">FAQ.</span></h2>
  <div class="faq">{faq}</div>
</div></section>''')

# ---------- static assets ----------
for f in ("styles.css", "main.js"):
    shutil.copy(os.path.join(ROOT, f), os.path.join(OUT, f))
with open(os.path.join(OUT, "404.html"), "w") as f:
    f.write('<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/"><title>Redirecting</title><a href="/">Go home</a>')
print("built")
