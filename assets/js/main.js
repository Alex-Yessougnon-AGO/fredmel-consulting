/**
 * FREDMEL CONSULTING — Scripts principaux
 * Vanilla JS — design Éditorial Prestige
 */

'use strict';

const utils = {
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  },

  /** Préfixe relatif selon la page (racine vs /pages/) */
  basePath() {
    return window.location.pathname.includes('/pages/') ? '../' : '';
  }
};

/** Nav îlot + menu mobile plein écran */
const islandNav = {
  init() {
    const burger = document.getElementById('nav-burger');
    const panel = document.getElementById('nav-mobile');
    if (!burger || !panel) return;

    // Scrim cliquable pour fermer
    let scrim = document.querySelector('.nav-scrim');
    if (!scrim) {
      scrim = document.createElement('button');
      scrim.type = 'button';
      scrim.className = 'nav-scrim';
      scrim.setAttribute('aria-label', 'Fermer le menu');
      scrim.hidden = true;
      document.body.appendChild(scrim);
    }

    const openMenu = () => {
      burger.setAttribute('aria-expanded', 'true');
      burger.setAttribute('aria-label', 'Fermer le menu');
      panel.hidden = false;
      scrim.hidden = false;
      document.body.classList.add('nav-open');
      // Focus premier lien pour accessibilité
      const first = panel.querySelector('a');
      if (first) first.focus({ preventScroll: true });
    };

    const closeMenu = () => {
      burger.setAttribute('aria-expanded', 'false');
      burger.setAttribute('aria-label', 'Ouvrir le menu');
      panel.hidden = true;
      scrim.hidden = true;
      document.body.classList.remove('nav-open');
      burger.focus({ preventScroll: true });
    };

    const toggle = () => {
      const isOpen = burger.getAttribute('aria-expanded') === 'true';
      if (isOpen) closeMenu();
      else openMenu();
    };

    burger.addEventListener('click', (e) => {
      e.stopPropagation();
      toggle();
    });

    scrim.addEventListener('click', closeMenu);

    panel.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
        closeMenu();
      }
    });

    window.addEventListener(
      'resize',
      utils.debounce(() => {
        if (window.innerWidth >= 992) closeMenu();
      }, 100)
    );
  }
};

/** Bandeau cookies */
const cookieBanner = {
  storageKey: 'fredmel_cookie_consent',

  init() {
    // Ne pas afficher le bandeau sur la page cookies elle-même
    if (window.location.pathname.includes('/cookies.html')) return;

    try {
      if (localStorage.getItem(this.storageKey)) return;
    } catch (_) {
      /* private mode */
    }

    const base = utils.basePath();
    const banner = document.createElement('div');
    banner.className = 'cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Consentement aux cookies');
    banner.innerHTML = `
      <p>
        Nous utilisons des cookies techniques nécessaires au fonctionnement du site.
        En poursuivant, vous acceptez leur usage.
        <a href="${base}pages/cookies.html">En savoir plus</a>
      </p>
      <div class="cookie-banner-actions">
        <button type="button" class="btn-pill btn-pill--solid" data-cookie="accept">
          <span>Accepter</span>
          <span class="btn-pill-icon" aria-hidden="true">→</span>
        </button>
        <button type="button" class="btn-pill--ghost" data-cookie="essential">
          Essentiels uniquement
        </button>
      </div>
    `;

    document.body.appendChild(banner);

    banner.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-cookie]');
      if (!btn) return;
      const value = btn.getAttribute('data-cookie');
      try {
        localStorage.setItem(this.storageKey, value);
      } catch (_) {
        /* ignore */
      }
      banner.hidden = true;
      setTimeout(() => banner.remove(), 300);
    });
  }
};

/** Formulaire contact — validation légère côté client */
const contactForm = {
  init() {
    const form = document.getElementById('contactForm');
    if (!form) return;

    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const nom = form.querySelector('#nom');
      const email = form.querySelector('#email');
      const message = form.querySelector('#message');
      let valid = true;

      [nom, email, message].forEach((field) => {
        if (!field) return;
        if (!field.value.trim()) {
          field.style.borderColor = '#c0392b';
          valid = false;
        } else {
          field.style.borderColor = '';
        }
      });

      if (email && email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        email.style.borderColor = '#c0392b';
        valid = false;
      }

      if (!valid) return;

      const btn = form.querySelector('button[type="submit"]');
      const original = btn ? btn.innerHTML : '';
      if (btn) {
        btn.disabled = true;
        btn.innerHTML =
          '<span>Message enregistré (démo)</span><span class="btn-pill-icon" aria-hidden="true">✓</span>';
      }

      setTimeout(() => {
        form.reset();
        if (btn) {
          btn.disabled = false;
          btn.innerHTML = original;
        }
        alert(
          'Merci pour votre message. La soumission réelle sera branchée à la mise en ligne (email / CRM).'
        );
      }, 600);
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  islandNav.init();
  contactForm.init();
  cookieBanner.init();
});
