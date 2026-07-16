# BRIEF FREDMEL CONSULTING - Magic Patterns

**Projet :** Site vitrine cabinet de coaching  
**Client :** FREDMEL CONSULTING  
**Localisation :** Abomey-Calavi, Bénin  
**Slogan :** "L'Art de Réussir"

---

## 🎯 OBJECTIF BUSINESS

Générer des prises de contact qualifiées via 4 pôles d'expertise complémentaires.

---

## 🎨 CHARTE GRAPHIQUE STRICTE

### Palette de Couleurs (RESPECTER EXACTEMENT)

| Couleur | Code HEX | Usage |
|---------|----------|-------|
| Bleu Marine | `#0A2A4D` | Couleur principale |
| Bleu Acier | `#1E5C97` | Boutons, liens, actions |
| Bleu Ciel | `#4A90C4` | Accents, badges |
| Gris Ardoise | `#5A6B7D` | Texte secondaire |
| Blanc | `#FFFFFF` | Fond principal |

### Typographie
- **Titres** : Georgia, Times New Roman (serif)
- **Texte** : Arial, Helvetica (sans-serif)

### ⚠️ CONTRAINTES DESIGN
- ❌ **PAS de dégradés** (ni backgrounds, ni boutons, ni nulle part)
- ✅ Couleurs aplaties uniquement
- ✅ Design professionnel et sobre
- ✅ Style institutionnel mais accessible

---

## 📄 LISTE COMPLÈTE DES PAGES

### VERSION 1 (URGENT - 13 PAGES)

1. **Accueil** (`/`) - Action : "Prendre contact"
2. **Nos Pôles** (`/poles`) - Action : Choisir un pôle
3. **FREDMEL Leadership** (`/leadership`) - Action : "Discuter de mon accompagnement Leadership"
4. **FREDMEL Élite** (`/elite`) - Action : "Discuter de mon accompagnement Élite"
5. **FREDMEL Créativité** (`/creativite`) - Action : "Discuter de mon projet créatif"
6. **FREDMEL Business** (`/business`) - Action : "Discuter de mon projet d'entreprise"
7. **À Propos** (`/a-propos`) - Action : "Rencontrer l'équipe"
8. **Équipe** (`/equipe`) - Action : "Prendre rendez-vous"
9. **FAQ** (`/faq`) - Action : "Nous contacter"
10. **Contact** (`/contact`) - Action : Soumettre formulaire
11. **Prise de Rendez-vous** (`/rendez-vous`) - Action : Réserver créneau
12. **Mentions Légales** (`/mentions-legales`) - Pas d'action
13. **Politique de Confidentialité** (`/politique-confidentialite`) - Pas d'action

### VERSION 2 (FUTUR - 5 PAGES SUPPLÉMENTAIRES)

14. **Témoignages** (`/temoignages`) - Action : "Me faire accompagner aussi"
15. **Blog / Actualités** (`/blog`) - Action : S'abonner newsletter
16. **Article Blog** (`/blog/[slug]`) - Action : Partager / Contacter
17. **Espace Membre - Login** (`/espace-membre`) - Action : Se connecter
18. **Espace Membre - Dashboard** (`/espace-membre/dashboard`) - Action : Accéder contenu

**TOTAL : 18 pages (13 V1 + 5 V2)**

---

## 📐 RÈGLES DE DESIGN (WEB_DESIGN_MASTER_2026)

### Loi 1 : UNE SEULE MISSION PAR PAGE

**Chaque page = 1 objectif principal = 1 CTA dominant**

- Accueil → "Prendre contact"
- Page pôle → "Discuter de mon accompagnement [Pôle]"
- Contact → Remplir formulaire
- RDV → Réserver créneau

Les autres CTAs (secondaires) doivent être **visuellement moins dominants**.

### Loi 2 : Clarté en 5 Secondes

Chaque page doit répondre immédiatement :
- Où suis-je ?
- Que proposez-vous ?
- À qui cela s'adresse ?
- Quelle est l'action suivante ?

### Loi 3 : Blueprint du Hero

**Chaque Hero doit contenir :**
1. Badge/catégorie (optionnel)
2. Titre H1 clair
3. Sous-titre explicatif
4. CTA principal UNIQUE
5. CTA secondaire (optionnel, moins visible)
6. Preuve sociale (si disponible)

### Loi 4 : Les Mots Vendent

Le design facilite la lecture. Priorité absolue au contenu texte.

### Loi 5 : Art de la Retenue

Supprimer tout élément décoratif inutile. Le luxe = l'espace.

### Loi 6 : Performance

Site rapide = SEO + conversions. Images optimisées, code léger.

### Loi 7 : Système, pas Projet

Design system cohérent : composants réutilisables, tokens, cohérence absolue.

### Loi 8 : Hiérarchie Visuelle

Taille, contraste, couleur, espace, poids typographique = hiérarchie.

### Loi 9 : Confiance

Témoignages, FAQ, équipe, mentions légales, contact = indispensables.

### Loi 10 : Cohérence

Chaque page doit appartenir au même univers visuel.

### Loi 11 : Accessibilité

Contrastes WCAG AA, navigation clavier, alt images, HTML sémantique.

### Loi 12 : Charge Cognitive Minimale

Moins de choix = moins de fatigue = plus de conversions.

---

## 🎯 PRINCIPES UX (Laws of UX)

- **Loi de Hick** : Moins de choix = décision plus rapide
- **Loi de Fitts** : CTA gros et proche du flux naturel
- **Loi de Jakob** : Ne pas réinventer les conventions web
- **Loi de Miller** : Max 7 éléments de menu
- **Principe de Pareto** : 20% des fonctionnalités = 80% de la valeur
- **Peak-End Rule** : Soigner l'onboarding et les confirmations
- **Halo Effect** : Première impression = 50ms pour juger la qualité

---

## 📱 RESPONSIVE

- **Mobile-first ABSOLU** (priorité Bénin/Afrique de l'Ouest)
- Breakpoints : Mobile <768px, Tablet 768-1024px, Desktop >1024px
- Images responsives, lazy loading
- Tests sur vrais devices bas/moyen de gamme

---

## 🎨 COMPOSANTS À DESIGNER

### Navigation
- Header sticky, fond blanc
- Logo gauche, menu droite
- Hamburger sur mobile
- **1 CTA visible** dans header : "Prendre RDV"

### Boutons
- **Primaire** : Fond Bleu Acier `#1E5C97`, texte blanc, coins arrondis
- **Secondaire** : Border Bleu Marine, fond transparent
- **États** : default, hover, focus, active, disabled

### Cards
- Fond blanc, ombre légère
- Hover : élévation, pas de transformation complexe
- Structure : Icône + Titre + Description + Lien

### Formulaires
- Labels clairs au-dessus des champs
- Validation en temps réel
- Messages d'erreur contextuels
- Bouton submit explicite

### Footer
- Fond Bleu Marine `#0A2A4D`
- Texte blanc/gris clair
- 4 colonnes : Logo, Liens, Pôles, Contact

### Bouton WhatsApp Flottant
- Position fixe bas droite
- Fond vert `#25D366`
- Visible sur toutes les pages

---

## ✨ ANIMATIONS (SUBTILES UNIQUEMENT)

- Fade in au scroll (Intersection Observer)
- Hover cards : élévation shadow
- Hover boutons : légère élévation
- Transitions : 150-400ms ease-out
- **Respecter `prefers-reduced-motion`**

---

## 📝 CONTENU PAR PAGE (STRUCTURE MINIMALE)

### 1. Accueil
- Hero : "L'Art de Réussir Commence Ici" + CTA "Prendre contact"
- Présentation : 3-4 lignes sur FREDMEL
- 4 Pôles : Cards avec lien "En savoir plus"
- CTA Final : "Discutons de votre projet"

### 2. Nos Pôles
- Hero : "Nos 4 Pôles d'Expertise"
- 4 Cards détaillées (icône + titre + description + services + lien)
- Guide choix : 2 boxes d'aide

### 3-6. Pages Pôles (4 pages)
- Hero : Nom pôle + description mission
- Services : 4 cards services
- Bénéfices : Texte + liste à puces
- CTA : "Discuter de mon accompagnement [Pôle]"

### 7. À Propos
- Hero : "À Propos de FREDMEL CONSULTING"
- Histoire : Texte + image
- Mission/Vision/Valeurs : 3 cards
- CTA : "Rencontrer l'équipe"

### 8. Équipe
- Hero : "Notre Équipe"
- 6 cards membres (photo + nom + poste + bio)
- CTA : "Prendre rendez-vous"

### 9. FAQ
- Hero : "Questions Fréquentes"
- Accordéon 8 questions
- CTA : "Nous contacter"

### 10. Contact
- Hero : "Contactez-Nous"
- Formulaire (nom, email, message)
- Infos contact (adresse, email, WhatsApp)
- CTA : Bouton "Envoyer"

### 11. Prise de Rendez-vous
- Hero : "Réservez Votre Rendez-vous"
- Widget Calendly (placeholder)
- Infos pratiques
- CTA : Réserver créneau

### 12-13. Pages Légales
- Hero simple
- Contenu structuré lisible
- Pas de CTA

---

## 🚀 CONTRAINTES TECHNIQUES

- Framework : Bootstrap 5.3
- HTML sémantique
- Accessibilité WCAG AA
- Performance : <2s chargement
- SEO : meta tags, sitemap, structured data

---

## 📦 LIVRABLES ATTENDUS

**Magic Patterns doit créer :**

1. Designs haute-fidélité 13 pages V1 (Desktop + Mobile)
2. Composants réutilisables
3. Respect strict charte graphique
4. Hiérarchie typographique claire
5. Système d'espacements cohérent
6. États interactifs (hover, focus, etc.)
7. Version exportable HTML/CSS

---

## 🎯 DÉLÉGATION À MAGIC PATTERNS

**Magic Patterns a TOUTE liberté pour :**

- Créer les layouts de chaque page
- Choisir les compositions visuelles
- Définir les espacements précis
- Créer les animations subtiles
- Optimiser la hiérarchie visuelle
- Choisir les images/illustrations (placeholder)
- Créer un design premium et professionnel

**CONTRAINTES STRICTES :**
- Respecter la palette de couleurs exacte
- 1 CTA principal par page (visuellement dominant)
- Pas de dégradés
- Mobile-first
- Design sobre et institutionnel

---

## 📞 INFORMATIONS CLIENT

- Email : contact@fredmelconsulting.com
- Téléphone : +229 XX XX XX XX
- WhatsApp : +229 XX XX XX XX
- Adresse : Abomey-Calavi, Bénin

---

**MISSION : Créer un site vitrine professionnel, sobre et efficace qui génère des prises de contact qualifiées.** 🎯
