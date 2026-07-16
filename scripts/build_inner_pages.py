#!/usr/bin/env python3
"""Génère toutes les pages intérieures au design Éditorial Prestige."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"

WA = "https://wa.me/229XXXXXXXX"
EMAIL = "contact@fredmelconsulting.com"


def head(title: str, description: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <meta name="theme-color" content="#0A2A4D">
    <title>{title}</title>
    <link rel="icon" type="image/png" href="../assets/images/favicon.png">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="preconnect" href="https://cdn.jsdelivr.net">
</head>
<body class="page-inner">
    <a class="skip-link" href="#contenu-principal">Aller au contenu principal</a>
    <div class="grain" aria-hidden="true"></div>
"""


def nav(active: str) -> str:
    def cls(key: str) -> str:
        return ' class="is-active" aria-current="page"' if key == active else ""

    return f"""
    <header class="site-header">
        <div class="nav-island">
            <a class="nav-logo" href="../index.html">
                <span class="nav-logo-mark">F</span>
                <span class="nav-logo-text">FREDMEL</span>
            </a>
            <nav class="nav-desktop" aria-label="Navigation principale">
                <a href="../index.html">Accueil</a>
                <a href="poles.html"{cls("poles")}>Pôles</a>
                <a href="a-propos.html"{cls("a-propos")}>À propos</a>
                <a href="equipe.html"{cls("equipe")}>Équipe</a>
                <a href="faq.html"{cls("faq")}>FAQ</a>
            </nav>
            <div class="nav-actions">
                <a href="contact.html" class="btn-pill btn-pill--solid{" is-active" if active == "contact" else ""}">
                    <span>Prendre contact</span>
                    <span class="btn-pill-icon" aria-hidden="true">→</span>
                </a>
                <button type="button" class="nav-burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav-mobile" id="nav-burger">
                    <span></span><span></span><span></span>
                </button>
            </div>
        </div>
        <div class="nav-mobile" id="nav-mobile" hidden>
            <div class="nav-mobile-inner">
                <p class="nav-mobile-label">Menu</p>
                <nav aria-label="Menu mobile">
                    <a href="../index.html">Accueil</a>
                    <a href="poles.html">Nos Pôles</a>
                    <a href="leadership.html">Leadership</a>
                    <a href="elite.html">Élite</a>
                    <a href="creativite.html">Créativité</a>
                    <a href="business.html">Business</a>
                    <a href="a-propos.html">À propos</a>
                    <a href="equipe.html">Équipe</a>
                    <a href="faq.html">FAQ</a>
                    <a href="contact.html" class="nav-mobile-cta">
                        <span>Prendre contact</span>
                        <span aria-hidden="true">→</span>
                    </a>
                </nav>
                <div class="nav-mobile-meta">
                    <a href="cookies.html">Cookies</a>
                    ·
                    <a href="mentions-legales.html">Mentions légales</a>
                </div>
            </div>
        </div>
    </header>
"""


def footer() -> str:
    return f"""
    <footer class="ed-footer">
        <div class="ed-wrap">
            <div class="ed-footer-top">
                <div class="ed-footer-brand">
                    <p class="ed-footer-logo">FREDMEL CONSULTING</p>
                    <p class="ed-footer-tag">L’Art de Réussir</p>
                    <p class="ed-footer-loc">Abomey-Calavi, Bénin</p>
                </div>
                <div class="ed-footer-cols">
                    <div>
                        <p class="ed-footer-h">Explorer</p>
                        <ul>
                            <li><a href="poles.html">Nos Pôles</a></li>
                            <li><a href="a-propos.html">À propos</a></li>
                            <li><a href="equipe.html">Équipe</a></li>
                            <li><a href="faq.html">FAQ</a></li>
                        </ul>
                    </div>
                    <div>
                        <p class="ed-footer-h">Pôles</p>
                        <ul>
                            <li><a href="leadership.html">Leadership</a></li>
                            <li><a href="elite.html">Élite</a></li>
                            <li><a href="creativite.html">Créativité</a></li>
                            <li><a href="business.html">Business</a></li>
                        </ul>
                    </div>
                    <div>
                        <p class="ed-footer-h">Contact</p>
                        <ul>
                            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
                            <li><a href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
                            <li><a href="contact.html">Formulaire</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="ed-footer-bottom">
                <p>&copy; 2026 FREDMEL CONSULTING</p>
                <p>
                    <a href="mentions-legales.html">Mentions légales</a>
                    <span aria-hidden="true">·</span>
                    <a href="politique-confidentialite.html">Confidentialité</a>
                    <span aria-hidden="true">·</span>
                    <a href="cookies.html">Cookies</a>
                </p>
            </div>
        </div>
    </footer>

    <a href="{WA}" class="wa-fab" target="_blank" rel="noopener noreferrer" aria-label="Contactez-nous sur WhatsApp">
        <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M16 0c-8.837 0-16 7.163-16 16 0 2.825 0.737 5.607 2.137 8.048l-2.137 7.952 7.933-2.127c2.42 1.37 5.173 2.127 8.067 2.127 8.837 0 16-7.163 16-16s-7.163-16-16-16zM16 29.467c-2.482 0-4.908-0.646-7.07-1.87l-0.507-0.292-5.245 1.406 1.414-5.26-0.316-0.535c-1.347-2.271-2.059-4.871-2.059-7.515 0-8.101 6.599-14.7 14.7-14.7 8.101 0 14.7 6.599 14.7 14.7s-6.516 14.067-14.617 14.067zM21.983 19.217c-0.391-0.195-2.313-1.139-2.673-1.27-0.359-0.13-0.62-0.195-0.88 0.195s-1.010 1.27-1.238 1.531c-0.228 0.261-0.456 0.293-0.846 0.098-0.391-0.195-1.649-0.608-3.141-1.933-1.161-1.034-1.945-2.311-2.173-2.701-0.228-0.391-0.024-0.602 0.171-0.797 0.176-0.174 0.391-0.456 0.587-0.684 0.195-0.228 0.261-0.391 0.391-0.651 0.13-0.261 0.065-0.489-0.033-0.684s-0.88-2.119-1.206-2.902c-0.317-0.762-0.639-0.658-0.88-0.671-0.228-0.011-0.489-0.013-0.75-0.013s-0.684 0.098-1.043 0.489c-0.359 0.391-1.368 1.336-1.368 3.257s1.401 3.779 1.596 4.040c0.195 0.261 2.749 4.196 6.659 5.883 0.93 0.402 1.657 0.643 2.224 0.823 0.936 0.297 1.789 0.255 2.461 0.154 0.751-0.112 2.313-0.946 2.639-1.859 0.326-0.913 0.326-1.695 0.228-1.859-0.098-0.163-0.359-0.261-0.75-0.456z"/></svg>
    </a>
    <script src="../assets/js/main.js"></script>
</body>
</html>
"""


def cta_panel(title: str, text: str, primary_href: str = "contact.html", primary_label: str = "Prendre contact") -> str:
    return f"""
        <section class="ed-cta">
            <div class="ed-wrap">
                <div class="ed-cta-panel">
                    <div class="ed-cta-copy">
                        <span class="ed-kicker ed-kicker--on-dark">
                            <span class="ed-kicker-line" aria-hidden="true"></span>
                            Prochaine étape
                        </span>
                        <h2 class="ed-display ed-display--light">{title}</h2>
                        <p>{text}</p>
                    </div>
                    <div class="ed-cta-action">
                        <a href="{primary_href}" class="btn-pill btn-pill--light btn-pill--lg">
                            <span>{primary_label}</span>
                            <span class="btn-pill-icon" aria-hidden="true">→</span>
                        </a>
                        <p class="ed-cta-alt">ou <a href="rendez-vous.html">réserver un créneau</a></p>
                    </div>
                </div>
            </div>
        </section>
"""


def page_hero(kicker: str, title_html: str, lead: str, wide: bool = False) -> str:
    w = " pg-hero-inner--wide" if wide else ""
    return f"""
        <section class="pg-hero">
            <div class="ed-wrap">
                <div class="pg-hero-inner{w}">
                    <p class="ed-kicker">
                        <span class="ed-kicker-line" aria-hidden="true"></span>
                        {kicker}
                    </p>
                    <h1>{title_html}</h1>
                    <p class="pg-hero-lead">{lead}</p>
                </div>
            </div>
        </section>
"""


def wrap(title, desc, active, main_html) -> str:
    return head(title, desc) + nav(active) + f'\n    <main id="contenu-principal">\n{main_html}\n    </main>\n' + footer()


# ─── Content builders ───────────────────────────────────────────────

def poles_page() -> str:
    main = page_hero(
        "Nos expertises",
        "Quatre pôles.<br>Un seul standard&nbsp;: l’<em>exigence</em>.",
        "Identifiez le domaine qui correspond à votre besoin. Chaque pôle mène à un échange personnalisé.",
        wide=True,
    ) + """
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <ul class="ed-pole-list">
                    <li>
                        <a href="leadership.html" class="ed-pole-row">
                            <span class="ed-pole-num">01</span>
                            <span class="ed-pole-name">Leadership</span>
                            <span class="ed-pole-desc">Potentiel, confiance et posture de leader</span>
                            <span class="ed-pole-go" aria-hidden="true">→</span>
                        </a>
                    </li>
                    <li>
                        <a href="elite.html" class="ed-pole-row">
                            <span class="ed-pole-num">02</span>
                            <span class="ed-pole-name">Élite</span>
                            <span class="ed-pole-desc">Image pro &amp; personal branding au féminin</span>
                            <span class="ed-pole-go" aria-hidden="true">→</span>
                        </a>
                    </li>
                    <li>
                        <a href="creativite.html" class="ed-pole-row">
                            <span class="ed-pole-num">03</span>
                            <span class="ed-pole-name">Créativité</span>
                            <span class="ed-pole-desc">Identité visuelle et créations sur mesure</span>
                            <span class="ed-pole-go" aria-hidden="true">→</span>
                        </a>
                    </li>
                    <li>
                        <a href="business.html" class="ed-pole-row">
                            <span class="ed-pole-num">04</span>
                            <span class="ed-pole-name">Business</span>
                            <span class="ed-pole-desc">De l’idée entrepreneuriale au lancement</span>
                            <span class="ed-pole-go" aria-hidden="true">→</span>
                        </a>
                    </li>
                </ul>
            </div>
        </section>

        <section class="pg-section">
            <div class="ed-wrap">
                <header class="ed-section-head">
                    <div class="ed-section-head-left">
                        <span class="ed-index">En détail</span>
                        <h2>Ce que chaque pôle vous apporte</h2>
                    </div>
                    <p class="ed-section-head-right">
                        Une approche globale et complémentaire — choisissez un point d’entrée, ou combinez plusieurs expertises.
                    </p>
                </header>

                <div class="pg-grid-2">
                    <article class="pg-card">
                        <span class="pg-card-num">01 — Leadership</span>
                        <h3>FREDMEL Leadership</h3>
                        <p>Développez votre potentiel, gagnez en confiance et affirmez votre posture de leader, dans la vie professionnelle comme personnelle.</p>
                        <ul class="pg-check-list" style="margin-top:1.25rem">
                            <li>Coaching individuel de développement personnel</li>
                            <li>Accompagnement à la confiance en soi</li>
                            <li>Ateliers de développement du leadership</li>
                            <li>Suivi personnalisé selon vos objectifs</li>
                        </ul>
                        <p style="margin-top:1.25rem"><a href="leadership.html" class="ed-text-link ed-text-link--dark">En savoir plus <span aria-hidden="true">→</span></a></p>
                    </article>
                    <article class="pg-card">
                        <span class="pg-card-num">02 — Élite</span>
                        <h3>FREDMEL Élite</h3>
                        <p>Pour les femmes qui veulent une image professionnelle forte et un personal branding authentique, aligné avec leurs ambitions.</p>
                        <ul class="pg-check-list" style="margin-top:1.25rem">
                            <li>Personal branding féminin</li>
                            <li>Prise de parole et présence</li>
                            <li>Stratégie de visibilité</li>
                            <li>Suivi individuel adapté</li>
                        </ul>
                        <p style="margin-top:1.25rem"><a href="elite.html" class="ed-text-link ed-text-link--dark">En savoir plus <span aria-hidden="true">→</span></a></p>
                    </article>
                    <article class="pg-card">
                        <span class="pg-card-num">03 — Créativité</span>
                        <h3>FREDMEL Créativité</h3>
                        <p>Donnez forme à vos idées avec des créations graphiques et des tableaux personnalisés qui portent votre identité.</p>
                        <ul class="pg-check-list" style="margin-top:1.25rem">
                            <li>Créations graphiques sur mesure</li>
                            <li>Tableaux et pièces uniques</li>
                            <li>Identité visuelle</li>
                            <li>Accompagnement créatif</li>
                        </ul>
                        <p style="margin-top:1.25rem"><a href="creativite.html" class="ed-text-link ed-text-link--dark">En savoir plus <span aria-hidden="true">→</span></a></p>
                    </article>
                    <article class="pg-card">
                        <span class="pg-card-num">04 — Business</span>
                        <h3>FREDMEL Business</h3>
                        <p>Transformez un projet entrepreneurial en réalité structurée — de l’idée au lancement, étape par étape.</p>
                        <ul class="pg-check-list" style="margin-top:1.25rem">
                            <li>Structuration de projet</li>
                            <li>Accompagnement à la création</li>
                            <li>Outils et méthodes business</li>
                            <li>Suivi jusqu’au lancement</li>
                        </ul>
                        <p style="margin-top:1.25rem"><a href="business.html" class="ed-text-link ed-text-link--dark">En savoir plus <span aria-hidden="true">→</span></a></p>
                    </article>
                </div>
            </div>
        </section>
""" + cta_panel(
        "Vous ne savez pas<br>par où <em>commencer</em>&nbsp;?",
        "Parlez-nous de votre situation. Nous vous orientons vers le pôle le plus adapté — sans engagement.",
    )
    return wrap(
        "Nos Pôles d’Expertise | FREDMEL CONSULTING",
        "Découvrez les 4 pôles FREDMEL : Leadership, Élite, Créativité et Business.",
        "poles",
        main,
    )


def pole_detail(
    filename_key: str,
    nav_active: str,
    num: str,
    name: str,
    title_em: str,
    lead: str,
    services: list[tuple[str, str]],
    benefits_title: str,
    benefits_intro: str,
    benefits: list[str],
    cta_title: str,
    img: str,
) -> str:
    cards = ""
    for i, (t, d) in enumerate(services, 1):
        cards += f"""
                    <article class="pg-card">
                        <span class="pg-card-num">{i:02d}</span>
                        <h3>{t}</h3>
                        <p>{d}</p>
                    </article>"""

    benefits_li = "".join(f"<li><strong>{b.split(' — ')[0]}</strong> — {b.split(' — ')[1] if ' — ' in b else b}</li>" if " — " in b else f"<li>{b}</li>" for b in benefits)
    # Simpler benefits
    benefits_li = ""
    for b in benefits:
        benefits_li += f"<li>{b}</li>"

    main = page_hero(
        f"Pôle {num} · {name}",
        f"FREDMEL <em>{title_em}</em>",
        lead,
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <header class="ed-section-head">
                    <div class="ed-section-head-left">
                        <span class="ed-index">Services</span>
                        <h2>Ce que nous proposons</h2>
                    </div>
                </header>
                <div class="pg-grid-2">{cards}
                </div>
            </div>
        </section>

        <section class="pg-section">
            <div class="ed-wrap">
                <div class="pg-grid-split">
                    <div>
                        <span class="ed-index">Bénéfices</span>
                        <h2 class="ed-display" style="margin-bottom:1.25rem">{benefits_title}</h2>
                        <p style="color:var(--ink-soft);margin-bottom:1.5rem">{benefits_intro}</p>
                        <ul class="pg-check-list">{benefits_li}
                        </ul>
                        <p style="margin-top:1.75rem">
                            <a href="poles.html" class="ed-text-link ed-text-link--dark">← Tous les pôles</a>
                        </p>
                    </div>
                    <figure class="pg-media">
                        <div class="ed-frame">
                            <div class="ed-frame-inner">
                                <img src="../assets/images/{img}" alt="FREDMEL {name}" width="1024" height="1024" loading="lazy" decoding="async">
                            </div>
                        </div>
                    </figure>
                </div>
            </div>
        </section>
""" + cta_panel(cta_title, "Contactez-nous pour discuter de votre situation et découvrir l’accompagnement adapté.")
    return wrap(
        f"FREDMEL {name} | FREDMEL CONSULTING",
        lead,
        nav_active,
        main,
    )


def a_propos() -> str:
    main = page_hero(
        "Le cabinet",
        "À propos de<br>FREDMEL <em>Consulting</em>",
        "Un cabinet dédié à l’excellence, l’écoute et l’accompagnement sur mesure, basé à Abomey-Calavi.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <div class="pg-grid-split">
                    <figure class="pg-media">
                        <div class="ed-frame">
                            <div class="ed-frame-inner">
                                <img src="../assets/images/10-objectifs-vision.png" alt="Vision FREDMEL CONSULTING" width="1024" height="1024" loading="lazy">
                            </div>
                        </div>
                    </figure>
                    <div>
                        <span class="ed-index">Notre histoire</span>
                        <h2 class="ed-display" style="margin-bottom:1.25rem">Révélateur de <em>potentiel</em></h2>
                        <p style="color:var(--ink-soft)">Basé à Abomey-Calavi, FREDMEL CONSULTING est né d’une conviction : chaque personne et chaque entreprise possède un potentiel unique qui mérite d’être révélé et développé.</p>
                        <p style="color:var(--ink-soft)">Notre cabinet s’est construit autour de quatre domaines d’expertise complémentaires, permettant un accompagnement global et cohérent, quelle que soit votre situation.</p>
                        <p style="color:var(--ink-soft);margin-bottom:0">Aujourd’hui, nous accompagnons des professionnels, des entrepreneurs et des porteurs de projets avec une approche humaine et personnalisée.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="pg-section">
            <div class="ed-wrap">
                <header class="ed-section-head ed-section-head--center">
                    <span class="ed-index">Fondations</span>
                    <h2>Mission, vision &amp; valeurs</h2>
                </header>
                <div class="pg-grid-3">
                    <article class="pg-card">
                        <span class="pg-card-num">I</span>
                        <h3>Mission</h3>
                        <p>Accompagner chaque personne et chaque entreprise dans la réalisation de son plein potentiel, à travers un accompagnement humain, structuré et sur mesure.</p>
                    </article>
                    <article class="pg-card">
                        <span class="pg-card-num">II</span>
                        <h3>Vision</h3>
                        <p>Faire de FREDMEL CONSULTING une référence en coaching, développement personnel et accompagnement entrepreneurial en Afrique de l’Ouest.</p>
                    </article>
                    <article class="pg-card">
                        <span class="pg-card-num">III</span>
                        <h3>Valeurs</h3>
                        <p>Excellence, écoute, engagement, créativité — quatre principes qui guident chacun de nos accompagnements.</p>
                    </article>
                </div>
            </div>
        </section>

        <section class="pg-section" style="padding-top:0">
            <div class="ed-wrap">
                <header class="ed-section-head">
                    <div class="ed-section-head-left">
                        <span class="ed-index">Piliers</span>
                        <h2>Ce qui guide notre travail</h2>
                    </div>
                </header>
                <div class="pg-grid-2">
                    <article class="pg-card"><span class="pg-card-num">01</span><h3>Excellence</h3><p>Méthodes éprouvées et exigence de qualité constante dans chaque accompagnement.</p></article>
                    <article class="pg-card"><span class="pg-card-num">02</span><h3>Écoute</h3><p>Chaque parcours commence par une écoute attentive de vos besoins et objectifs.</p></article>
                    <article class="pg-card"><span class="pg-card-num">03</span><h3>Engagement</h3><p>Un suivi personnalisé et un soutien constant dans la durée.</p></article>
                    <article class="pg-card"><span class="pg-card-num">04</span><h3>Créativité</h3><p>Des solutions innovantes, pensées pour votre situation unique.</p></article>
                </div>
            </div>
        </section>
""" + cta_panel(
        "Envie d’en savoir<br>plus sur <em>nous</em>&nbsp;?",
        "Échangeons sur votre projet — ou découvrez l’équipe qui vous accompagnera.",
    )
    return wrap(
        "À Propos | FREDMEL CONSULTING",
        "Histoire, mission, vision et valeurs de FREDMEL CONSULTING à Abomey-Calavi.",
        "a-propos",
        main,
    )


def equipe() -> str:
    members = [
        ("F", "[Nom du Fondateur]", "Fondateur & Directeur", "Direction stratégique et vision du cabinet."),
        ("L", "[Nom Responsable]", "Responsable Leadership", "Coaching et développement du potentiel."),
        ("É", "[Nom Responsable]", "Responsable Élite", "Personal branding et image professionnelle."),
        ("C", "[Nom Responsable]", "Responsable Créativité", "Graphisme et identité visuelle."),
        ("B", "[Nom Responsable]", "Responsable Business", "Accompagnement entrepreneurial."),
        ("+", "[Nom Coach]", "Coach & Consultant", "Accompagnement transversal selon le besoin."),
    ]
    cards = ""
    for mark, name, role, bio in members:
        cards += f"""
                    <article class="pg-team-card">
                        <div class="pg-avatar" aria-hidden="true">{mark}</div>
                        <h3>{name}</h3>
                        <p class="pg-team-role">{role}</p>
                        <p>{bio}</p>
                    </article>"""

    main = page_hero(
        "Les personnes",
        "Notre <em>équipe</em>",
        "Des professionnels engagés autour de quatre pôles — une force dans la complémentarité des expertises.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <div class="pg-notice">
                    <strong>Note :</strong> les profils ci-dessous sont des placeholders. Noms, photos et biographies réelles seront fournis par le client avant mise en ligne.
                </div>
                <div class="pg-grid-3">{cards}
                </div>
            </div>
        </section>

        <section class="pg-section">
            <div class="ed-wrap">
                <header class="ed-section-head ed-section-head--center">
                    <span class="ed-index">Culture</span>
                    <h2>Ce qui nous unit</h2>
                </header>
                <div class="pg-grid-3">
                    <article class="pg-card"><span class="pg-card-num">I</span><h3>Passion</h3><p>Nous sommes passionnés par l’accompagnement et le développement humain.</p></article>
                    <article class="pg-card"><span class="pg-card-num">II</span><h3>Exigence</h3><p>Chaque séance vise un progrès concret, mesurable et durable.</p></article>
                    <article class="pg-card"><span class="pg-card-num">III</span><h3>Proximité</h3><p>Une relation de confiance, ancrée à Abomey-Calavi et ouverte au distanciel.</p></article>
                </div>
            </div>
        </section>
""" + cta_panel(
        "Rencontrez-nous<br>autour d’un <em>projet</em>",
        "Prenez contact pour un premier échange avec l’équipe FREDMEL.",
    )
    return wrap(
        "Équipe | FREDMEL CONSULTING",
        "Présentation de l’équipe FREDMEL CONSULTING à Abomey-Calavi.",
        "equipe",
        main,
    )


def faq() -> str:
    items = [
        (
            "Comment se déroule un premier contact ?",
            "Vous pouvez nous contacter via le formulaire ou WhatsApp. Nous échangeons pour comprendre votre besoin et vous orienter vers le pôle le plus adapté. Ce premier échange est gratuit et sans engagement.",
        ),
        (
            "Comment savoir quel pôle correspond à mon besoin ?",
            "Consultez la présentation de nos 4 pôles. Si vous hésitez, contactez-nous : nous vous orienterons selon votre situation et vos objectifs.",
        ),
        (
            "Les accompagnements sont-ils individuels ou en groupe ?",
            "Cela dépend du pôle et du type d’accompagnement. Contactez-nous pour connaître les modalités précises selon votre besoin.",
        ),
        (
            "Dans quelle zone intervenez-vous ?",
            "Nous sommes basés à Abomey-Calavi et accompagnons principalement au Bénin. Certains services peuvent être proposés à distance.",
        ),
        (
            "Quels sont vos tarifs ?",
            "Nos tarifs varient selon le type d’accompagnement. Contactez-nous pour un devis personnalisé adapté à votre projet.",
        ),
        (
            "Sous quel délai me répondez-vous ?",
            "Nous faisons notre maximum pour répondre rapidement. Pour une réponse plus immédiate, privilégiez WhatsApp.",
        ),
        (
            "Puis-je bénéficier de plusieurs services en même temps ?",
            "Oui. Nos 4 pôles sont complémentaires. Par exemple, un entrepreneur peut combiner Business et Leadership.",
        ),
        (
            "Comment se déroule un accompagnement type ?",
            """Un parcours type suit plusieurs étapes :
                <ol>
                    <li><strong>Premier contact</strong> — comprendre votre besoin</li>
                    <li><strong>Diagnostic</strong> — situation et objectifs</li>
                    <li><strong>Plan d’action</strong> — parcours adapté</li>
                    <li><strong>Accompagnement</strong> — sessions selon le rythme convenu</li>
                    <li><strong>Suivi</strong> — évaluation et ajustements</li>
                </ol>""",
        ),
    ]
    faq_html = ""
    for i, (q, a) in enumerate(items):
        open_attr = " open" if i == 0 else ""
        faq_html += f"""
                    <details{open_attr}>
                        <summary>{q}</summary>
                        <div class="pg-faq-body"><p>{a}</p></div>
                    </details>"""

    main = page_hero(
        "FAQ",
        "Questions <em>fréquentes</em>",
        "Des réponses claires pour lever les dernières hésitations avant de nous contacter.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap" style="max-width:720px">
                <div class="pg-faq">{faq_html}
                </div>
            </div>
        </section>
""" + cta_panel(
        "Vous avez d’autres<br><em>questions</em>&nbsp;?",
        "Notre équipe est à votre écoute pour vous guider vers la solution la plus adaptée.",
    )
    return wrap(
        "FAQ | FREDMEL CONSULTING",
        "Questions fréquentes sur les services FREDMEL CONSULTING.",
        "faq",
        main,
    )


def contact() -> str:
    main = page_hero(
        "Contact",
        "Parlons de<br>votre <em>projet</em>",
        "Une question, une envie d’en savoir plus ? Écrivez-nous — nous vous répondons rapidement.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <div class="pg-grid-split">
                    <div class="pg-block">
                        <h2>Envoyez un message</h2>
                        <form class="pg-form" id="contactForm" novalidate>
                            <div class="field">
                                <label for="nom">Nom complet <span class="req">*</span></label>
                                <input type="text" id="nom" name="nom" required placeholder="Votre nom" autocomplete="name">
                            </div>
                            <div class="field">
                                <label for="email">Adresse email <span class="req">*</span></label>
                                <input type="email" id="email" name="email" required placeholder="votre@email.com" autocomplete="email">
                            </div>
                            <div class="field">
                                <label for="telephone">Téléphone (optionnel)</label>
                                <input type="tel" id="telephone" name="telephone" placeholder="+229 XX XX XX XX" autocomplete="tel">
                            </div>
                            <div class="field">
                                <label for="pole">Pôle concerné (optionnel)</label>
                                <select id="pole" name="pole">
                                    <option value="">Choisissez un pôle…</option>
                                    <option value="leadership">FREDMEL Leadership</option>
                                    <option value="elite">FREDMEL Élite</option>
                                    <option value="creativite">FREDMEL Créativité</option>
                                    <option value="business">FREDMEL Business</option>
                                    <option value="autre">Autre / Non spécifié</option>
                                </select>
                            </div>
                            <div class="field">
                                <label for="message">Votre message <span class="req">*</span></label>
                                <textarea id="message" name="message" required placeholder="Décrivez votre besoin ou votre question…"></textarea>
                            </div>
                            <button type="submit" class="btn-pill btn-pill--solid btn-pill--lg" style="width:100%;justify-content:space-between">
                                <span>Envoyer le message</span>
                                <span class="btn-pill-icon" aria-hidden="true">→</span>
                            </button>
                        </form>
                    </div>
                    <div>
                        <div class="pg-block">
                            <h2>Coordonnées</h2>
                            <ul class="pg-info-list">
                                <li>
                                    <span class="label">Adresse</span>
                                    Abomey-Calavi, Bénin
                                </li>
                                <li>
                                    <span class="label">Email</span>
                                    <a href="mailto:{EMAIL}">{EMAIL}</a>
                                </li>
                                <li>
                                    <span class="label">WhatsApp</span>
                                    <a href="{WA}" target="_blank" rel="noopener noreferrer">+229 XX XX XX XX</a>
                                </li>
                                <li>
                                    <span class="label">Horaires</span>
                                    Lundi – Vendredi · 8h00 – 18h00
                                </li>
                            </ul>
                        </div>
                        <div class="pg-block" style="margin-top:1.25rem">
                            <h2>Réserver un créneau</h2>
                            <p style="color:var(--ink-soft);margin-bottom:1.25rem">Vous préférez choisir directement un horaire pour un premier échange&nbsp;?</p>
                            <a href="rendez-vous.html" class="btn-pill btn-pill--solid">
                                <span>Prendre rendez-vous</span>
                                <span class="btn-pill-icon" aria-hidden="true">→</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="pg-section">
            <div class="ed-wrap">
                <div class="pg-placeholder">
                    <div>
                        <strong>Abomey-Calavi, Bénin</strong>
                        Carte interactive à intégrer (Google Maps / OpenStreetMap)
                    </div>
                </div>
            </div>
        </section>
"""
    return wrap(
        "Contact | FREDMEL CONSULTING",
        "Contactez FREDMEL CONSULTING à Abomey-Calavi — formulaire, email, WhatsApp.",
        "contact",
        main,
    )


def rdv() -> str:
    main = page_hero(
        "Rendez-vous",
        "Réservez votre<br><em>premier échange</em>",
        "Choisissez un créneau pour discuter de votre projet. Premier échange gratuit et sans engagement.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <div class="pg-grid-split">
                    <div class="pg-block">
                        <h2>Planifier un rendez-vous</h2>
                        <div class="pg-notice">
                            <strong>Configuration requise :</strong> intégrer un outil de réservation (Calendly, Acuity, etc.) une fois choisi avec le client.
                        </div>
                        <div class="pg-placeholder" style="min-height:420px">
                            <div>
                                <strong>Widget de réservation</strong>
                                Le calendrier en ligne sera intégré ici.<br>
                                Options : Calendly · Acuity · SimplyBook.me
                            </div>
                        </div>
                    </div>
                    <div class="pg-block">
                        <h2>Informations pratiques</h2>
                        <ul class="pg-info-list">
                            <li>
                                <span class="label">Durée</span>
                                Premier échange : <strong>30 minutes</strong>
                            </li>
                            <li>
                                <span class="label">Format</span>
                                Visioconférence · Présentiel à Abomey-Calavi · Téléphone
                            </li>
                            <li>
                                <span class="label">Engagement</span>
                                Gratuit et sans engagement — pour clarifier votre besoin
                            </li>
                        </ul>
                        <p style="margin-top:1.5rem;color:var(--ink-soft)">Vous préférez écrire d’abord&nbsp;?</p>
                        <a href="contact.html" class="ed-text-link ed-text-link--dark">Utiliser le formulaire de contact <span aria-hidden="true">→</span></a>
                    </div>
                </div>
            </div>
        </section>
""" + cta_panel(
        "Pas de créneau<br>qui vous <em>convient</em>&nbsp;?",
        "Contactez-nous directement — nous trouverons un moment ensemble.",
        primary_href="contact.html",
    )
    return wrap(
        "Prise de Rendez-vous | FREDMEL CONSULTING",
        "Réservez un créneau avec FREDMEL CONSULTING pour un premier échange.",
        "contact",
        main,
    )


def mentions() -> str:
    main = page_hero(
        "Légal",
        "Mentions <em>légales</em>",
        "Informations légales et réglementaires relatives au site FREDMEL CONSULTING.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <div class="pg-prose">
                    <div class="pg-note">
                        <strong>Note :</strong> les mentions entre crochets sont à compléter par le client (RCCM, NIF, hébergeur, etc.) avant mise en ligne.
                    </div>

                    <h2>1. Éditeur du site</h2>
                    <p><strong>Raison sociale :</strong> [À COMPLÉTER]</p>
                    <p><strong>Forme juridique :</strong> [À COMPLÉTER]</p>
                    <p><strong>Capital social :</strong> [À COMPLÉTER] FCFA</p>
                    <p><strong>Siège social :</strong> Abomey-Calavi, Bénin</p>
                    <p><strong>RCCM :</strong> [À COMPLÉTER]</p>
                    <p><strong>NIF :</strong> [À COMPLÉTER]</p>
                    <p><strong>Email :</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
                    <p><strong>Téléphone :</strong> +229 [À COMPLÉTER]</p>
                    <p><strong>Directeur de publication :</strong> [À COMPLÉTER]</p>

                    <h2>2. Hébergement</h2>
                    <p><strong>Hébergeur :</strong> [À COMPLÉTER]</p>
                    <p><strong>Adresse :</strong> [À COMPLÉTER]</p>
                    <p><strong>Contact :</strong> [À COMPLÉTER]</p>

                    <h2>3. Propriété intellectuelle</h2>
                    <p>L’ensemble des contenus présents sur le site (textes, images, graphismes, logo, etc.) est la propriété exclusive de FREDMEL CONSULTING, sauf mention contraire. Toute reproduction non autorisée est interdite.</p>

                    <h2>4. Protection des données personnelles</h2>
                    <p>FREDMEL CONSULTING s’engage à respecter la réglementation applicable, notamment la loi béninoise relative à la protection des données à caractère personnel et le cadre de l’APDP.</p>
                    <p>Pour plus d’informations, consultez notre <a href="politique-confidentialite.html">Politique de confidentialité</a>.</p>

                    <h2>5. Cookies</h2>
                    <p>Le site peut utiliser des cookies techniques nécessaires au bon fonctionnement. Vous pouvez modifier vos préférences dans les paramètres de votre navigateur.</p>

                    <h2>6. Responsabilité</h2>
                    <p>FREDMEL CONSULTING s’efforce de fournir des informations exactes et disponibles. Toutefois, la responsabilité du cabinet ne saurait être engagée pour d’éventuelles erreurs ou indisponibilités.</p>

                    <h2>7. Liens hypertextes</h2>
                    <p>Le site peut contenir des liens vers d’autres sites. FREDMEL CONSULTING n’exerce aucun contrôle sur ces sites et décline toute responsabilité quant à leur contenu.</p>

                    <h2>8. Droit applicable</h2>
                    <p>Le présent site est soumis au droit béninois. En cas de litige, les tribunaux compétents du Bénin seront saisis.</p>
                </div>
            </div>
        </section>
"""
    return wrap(
        "Mentions Légales | FREDMEL CONSULTING",
        "Mentions légales du site FREDMEL CONSULTING.",
        "",
        main,
    )


def confidentialite() -> str:
    main = page_hero(
        "Confidentialité",
        "Politique de<br><em>confidentialité</em>",
        "Comment FREDMEL CONSULTING collecte, utilise et protège vos données personnelles.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <div class="pg-prose">
                    <div class="pg-note">
                        Document de base conforme aux principes APDP / protection des données. À faire valider par le client avant publication.
                    </div>

                    <h2>1. Responsable du traitement</h2>
                    <p>FREDMEL CONSULTING, Abomey-Calavi, Bénin — <a href="mailto:{EMAIL}">{EMAIL}</a></p>

                    <h2>2. Données collectées</h2>
                    <p>Nous pouvons collecter : nom, email, téléphone, message, pôle d’intérêt, et données techniques de navigation (logs, cookies techniques).</p>

                    <h2>3. Finalités</h2>
                    <ul>
                        <li>Répondre à vos demandes de contact ou de rendez-vous</li>
                        <li>Assurer le suivi de l’accompagnement</li>
                        <li>Améliorer le site et la sécurité</li>
                    </ul>

                    <h2>4. Base légale</h2>
                    <p>Consentement (formulaires) et intérêt légitime (sécurité, amélioration du service).</p>

                    <h2>5. Destinataires</h2>
                    <p>Vos données sont destinées à FREDMEL CONSULTING. Elles ne sont pas vendues à des tiers. Des prestataires techniques (hébergeur, outil de RDV) peuvent y accéder strictement pour le service.</p>

                    <h2>6. Durée de conservation</h2>
                    <p>Les données de contact sont conservées le temps nécessaire au traitement de votre demande, puis archivées ou supprimées selon les obligations légales applicables.</p>

                    <h2>7. Vos droits</h2>
                    <p>Vous disposez d’un droit d’accès, de rectification, de suppression et d’opposition. Pour les exercer : <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

                    <h2>8. Sécurité</h2>
                    <p>Nous mettons en œuvre des mesures techniques et organisationnelles raisonnables pour protéger vos données.</p>

                    <h2>9. Cookies</h2>
                    <p>Pour le détail des cookies utilisés, consultez notre <a href="cookies.html">Politique de cookies</a>.</p>

                    <h2>10. Contact</h2>
                    <p>Pour toute question relative à cette politique : <a href="mailto:{EMAIL}">{EMAIL}</a> ou via la <a href="contact.html">page Contact</a>.</p>
                </div>
            </div>
        </section>
"""
    return wrap(
        "Politique de Confidentialité | FREDMEL CONSULTING",
        "Politique de confidentialité et protection des données FREDMEL CONSULTING.",
        "",
        main,
    )


def cookies() -> str:
    main = page_hero(
        "Cookies",
        "Politique de<br><em>cookies</em>",
        "Quels cookies nous utilisons, pourquoi, et comment gérer vos préférences.",
    ) + f"""
        <section class="pg-section pg-section--tight">
            <div class="ed-wrap">
                <div class="pg-prose">
                    <div class="pg-note">
                        Cette page complète les mentions légales et la politique de confidentialité. À adapter si des outils analytics ou marketing sont ajoutés plus tard.
                    </div>

                    <h2>1. Qu’est-ce qu’un cookie&nbsp;?</h2>
                    <p>Un cookie est un petit fichier déposé sur votre appareil lors de la visite d’un site. Il permet de mémoriser des informations relatives à votre navigation.</p>

                    <h2>2. Cookies que nous utilisons</h2>
                    <h3 style="font-size:1.1rem;margin-top:1.25rem">Cookies strictement nécessaires</h3>
                    <p>Ces cookies sont indispensables au fonctionnement du site. Ils ne peuvent pas être désactivés via le bandeau, car le site ne fonctionnerait pas correctement sans eux.</p>
                    <ul>
                        <li><strong>Consentement cookies</strong> — mémorise votre choix (accepter / essentiels) dans le stockage local du navigateur</li>
                        <li><strong>Cookies techniques</strong> — éventuels cookies de session liés à la sécurité ou à l’affichage</li>
                    </ul>

                    <h3 style="font-size:1.1rem;margin-top:1.25rem">Cookies optionnels</h3>
                    <p>À ce jour, FREDMEL CONSULTING n’utilise pas de cookies publicitaires ni de trackers marketing. Si des outils d’analyse (ex. statistiques de fréquentation) sont ajoutés ultérieurement, cette page sera mise à jour et un nouveau consentement pourra être demandé.</p>

                    <h2>3. Finalités</h2>
                    <ul>
                        <li>Assurer le bon fonctionnement du site</li>
                        <li>Mémoriser vos préférences de consentement</li>
                        <li>Sécuriser la navigation</li>
                    </ul>

                    <h2>4. Durée de conservation</h2>
                    <p>Le choix de consentement est conservé dans votre navigateur jusqu’à ce que vous le supprimiez (localStorage) ou vidiez les données du site. Les cookies techniques de session expirent à la fermeture du navigateur ou selon une durée limitée.</p>

                    <h2>5. Gérer vos cookies</h2>
                    <p>Vous pouvez&nbsp;:</p>
                    <ul>
                        <li>Choisir «&nbsp;Essentiels uniquement&nbsp;» ou «&nbsp;Accepter&nbsp;» via le bandeau affiché à la première visite</li>
                        <li>Supprimer les cookies et le stockage local depuis les paramètres de votre navigateur</li>
                        <li>Configurer votre navigateur pour bloquer certains cookies (cela peut limiter certaines fonctionnalités)</li>
                    </ul>

                    <h2>6. Vos droits</h2>
                    <p>Pour toute question relative aux cookies ou à vos données personnelles, contactez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a>. Voir aussi la <a href="politique-confidentialite.html">Politique de confidentialité</a> et les <a href="mentions-legales.html">Mentions légales</a>.</p>

                    <h2>7. Mise à jour</h2>
                    <p>Cette politique peut être mise à jour pour refléter l’évolution du site ou de la réglementation. Dernière mise à jour indicative : juillet 2026.</p>
                </div>
            </div>
        </section>
"""
    return wrap(
        "Politique de Cookies | FREDMEL CONSULTING",
        "Politique de cookies du site FREDMEL CONSULTING — types, finalités et gestion des préférences.",
        "",
        main,
    )


def main() -> None:
    pages = {
        "poles.html": poles_page(),
        "leadership.html": pole_detail(
            "leadership",
            "poles",
            "01",
            "Leadership",
            "Leadership",
            "Accompagnement pour développer votre potentiel, gagner en confiance et affirmer votre posture de leader.",
            [
                ("Coaching individuel", "Accompagnement personnalisé pour développer votre potentiel unique et atteindre vos objectifs."),
                ("Confiance en soi", "Renforcement de l’estime personnelle et d’une confiance solide face aux défis."),
                ("Ateliers leadership", "Sessions pratiques pour inspirer, motiver et piloter avec clarté."),
                ("Suivi personnalisé", "Accompagnement continu adapté à votre rythme et à vos objectifs."),
            ],
            "Développez votre leadership",
            "Notre approche repose sur l’écoute, l’analyse de vos forces et l’identification des leviers de progression.",
            [
                "<strong>Affirmez votre posture de leader</strong> dans votre environnement professionnel",
                "<strong>Développez votre intelligence émotionnelle</strong> et vos compétences relationnelles",
                "<strong>Renforcez votre confiance</strong> pour prendre des décisions importantes",
                "<strong>Atteignez vos objectifs</strong> avec une stratégie claire et personnalisée",
            ],
            "Prêt à développer<br>votre <em>leadership</em>&nbsp;?",
            "03-services-coaching-individuel.png",
        ),
        "elite.html": pole_detail(
            "elite",
            "poles",
            "02",
            "Élite",
            "Élite",
            "Pour les femmes qui souhaitent construire une image professionnelle forte et un personal branding aligné avec leurs ambitions.",
            [
                ("Personal branding féminin", "Une image professionnelle authentique qui reflète vos valeurs et votre expertise."),
                ("Prise de parole", "Affirmez votre présence et communiquez avec assurance."),
                ("Stratégie de visibilité", "Faites reconnaître votre expertise dans votre domaine."),
                ("Suivi individuel adapté", "Un accompagnement qui respecte votre parcours unique."),
            ],
            "Affirmez votre singularité",
            "FREDMEL Élite est conçu pour accompagner les femmes dans leur développement professionnel et la construction d’une image qui leur ressemble.",
            [
                "<strong>Construisez votre marque personnelle</strong> avec authenticité et cohérence",
                "<strong>Développez votre posture professionnelle</strong> et votre impact en public",
                "<strong>Augmentez votre visibilité</strong> et faites reconnaître votre expertise",
                "<strong>Alignez image et ambitions</strong> sur le long terme",
            ],
            "Prête à affirmer<br>votre <em>image</em>&nbsp;?",
            "05-equipe-portrait.png",
        ),
        "creativite.html": pole_detail(
            "creativite",
            "poles",
            "03",
            "Créativité",
            "Créativité",
            "Des créations graphiques et des tableaux personnalisés qui donnent vie à vos idées et à votre identité visuelle.",
            [
                ("Créations graphiques", "Supports visuels sur mesure pour vos projets et votre communication."),
                ("Tableaux personnalisés", "Pièces uniques qui incarnent votre univers et vos valeurs."),
                ("Identité visuelle", "Cohérence et impact pour votre marque personnelle ou professionnelle."),
                ("Accompagnement créatif", "De l’intention à la réalisation, avec une direction artistique claire."),
            ],
            "Donnez forme à vos idées",
            "FREDMEL Créativité transforme l’intention en réalisation tangible, avec soin et exigence.",
            [
                "<strong>Exprimez votre identité</strong> à travers des créations uniques",
                "<strong>Valorisez votre image</strong> avec une direction visuelle cohérente",
                "<strong>Concrétisez un projet créatif</strong> de A à Z",
                "<strong>Différenciez-vous</strong> par un style affirmé",
            ],
            "Un projet créatif<br>en <em>tête</em>&nbsp;?",
            "09-ressources-blog.png",
        ),
        "business.html": pole_detail(
            "business",
            "poles",
            "04",
            "Business",
            "Business",
            "Un accompagnement structuré pour transformer votre projet entrepreneurial en réalité — de l’idée au lancement.",
            [
                ("Structuration de projet", "Clarifiez votre offre, votre marché et votre modèle."),
                ("Création d’entreprise", "De l’idée aux premières étapes concrètes de lancement."),
                ("Outils & méthodes", "Des outils actionnables pour piloter votre progression."),
                ("Suivi entrepreneurial", "Un accompagnement régulier jusqu’à l’autonomie."),
            ],
            "Passez de l’idée à l’action",
            "FREDMEL Business vous aide à structurer, prioriser et avancer avec méthode.",
            [
                "<strong>Clarifiez votre projet</strong> et vos priorités",
                "<strong>Structurez votre offre</strong> et votre positionnement",
                "<strong>Évitez les erreurs classiques</strong> de démarrage",
                "<strong>Avancez avec un plan clair</strong> et un suivi régulier",
            ],
            "Prêt à lancer<br>votre <em>projet</em>&nbsp;?",
            "04-services-coaching-equipe.png",
        ),
        "a-propos.html": a_propos(),
        "equipe.html": equipe(),
        "faq.html": faq(),
        "contact.html": contact(),
        "rendez-vous.html": rdv(),
        "mentions-legales.html": mentions(),
        "politique-confidentialite.html": confidentialite(),
        "cookies.html": cookies(),
    }

    for name, html in pages.items():
        path = PAGES / name
        path.write_text(html, encoding="utf-8")
        print(f"✓ {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
