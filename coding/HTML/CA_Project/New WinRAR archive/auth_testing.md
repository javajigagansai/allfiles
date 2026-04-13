{
  "theme": {
    "archetype": "5 (Jewel & Luxury) + 4 (Swiss & High-Contrast)",
    "mode": "dark",
    "tone": "Professional, Authoritative, Premium, Trustworthy",
    "description": "A high-end corporate aesthetic tailored for a chartered accountant firm (Giri & Associates). Utilizes a deep midnight slate/navy base to establish authority and trust, paired with elegant champagne/gold accents for a premium touch. Employs crisp, minimalist geometric structures mixed with high-contrast typography."
  },
  "colors": {
    "background_base": "#0A0C10",
    "background_surface": "#13161D",
    "background_surface_elevated": "#1A1F2A",
    "primary_accent": "#D4AF37",
    "primary_accent_hover": "#F0C94F",
    "text_primary": "#F8FAFC",
    "text_secondary": "#94A3B8",
    "border_subtle": "rgba(255, 255, 255, 0.1)",
    "border_focus": "rgba(212, 175, 55, 0.5)",
    "status_success": "#22C55E",
    "status_error": "#EF4444"
  },
  "typography": {
    "heading_font": "Playfair Display",
    "body_font": "Work Sans",
    "rules": {
      "headings": "Use tracking-tight for sizes above text-3xl. For main hero, text-5xl to text-6xl clamp. Never center-align by default.",
      "body": "leading-relaxed. text-base or text-sm depending on density.",
      "labels": "Uppercase, tracking-[0.2em], text-xs, text-secondary color."
    }
  },
  "spacing_and_layout": {
    "padding": "Generous. Use p-8, p-12, p-16 for main sections. Use p-6 or p-8 inside bordered containers.",
    "grid": "Bento Grid (Tetris Mode) for Marketing features. Control Room Grid for Admin Dashboard.",
    "alignment": "Mobile-first. Left-align dense content. Optical alignment over mathematical."
  },
  "surfaces_and_effects": {
    "header": "Crystal Glassmorphism: bg-black/60, backdrop-blur-xl, border-b border-white/10.",
    "cards": "Neumorphic/Tactile variant: Solid background matching parent (or slightly elevated), 1px solid border-white/10, subtle drop shadow. Max border-radius 8px.",
    "hover_states": "Slight lift (-translate-y-1), border lightens, glow effect for primary buttons."
  },
  "components_strategy": {
    "marketing_pages": "Use pure HTML/Tailwind for structural layout (sections, hero, features) to allow asymmetric bento grids. Avoid wrapping everything in generic Shadcn cards.",
    "interactive_elements": "Use Shadcn customized components (Buttons, Inputs, Forms, Tables). Never use native inputs.",
    "admin_dashboard": "Cardless or subtle borders. Dense, technical grid. Shadcn tables and metrics."
  },
  "pages_and_features": {
    "home_marketing": {
      "hero_section": "Dark overlay on hero background (bg-black/60 to bg-black/80). Heavy, elegant typography. Primary CTA in gold. 'Tracing beam' or animated border on key stat widgets.",
      "services_carousel": "Bento grid layout or horizontal swipe. Use 'Living Texture' marquee for service lists if applicable.",
      "contact_section": "Large typography, structured grid for info, elegant form."
    },
    "client_portal": {
      "data_entry_form": "Shadcn Form, highly polished, left-aligned, generous spacing. File upload zone with dashed border, hover glow."
    },
    "admin_dashboard": {
      "layout": "Sidebar nav, dense data tables, minimal decorative elements. Focus on hierarchy and readability.",
      "service_management": "Shadcn Tables, Dialogs for editing. Status badges."
    }
  },
  "media_and_assets": {
    "icons": "lucide-react for standard UI, @phosphor-icons/react (Duotone) for marketing features. (yarn add @phosphor-icons/react)",
    "images": {
      "hero_background": {
        "url": "https://images.unsplash.com/photo-1764609289774-2b767bb4e6f5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1Nzh8MHwxfHNlYXJjaHwzfHxtb2Rlcm4lMjBvZmZpY2UlMjBidWlsZGluZyUyMGFyY2hpdGVjdHVyZSUyMGRhcmslMjBuaWdodHxlbnwwfHx8fDE3NzQ3NjIyNjV8MA&ixlib=rb-4.1.0&q=85",
        "alt": "Modern office building architecture dark night",
        "usage": "Hero section background with dark overlay."
      },
      "services_background": {
        "url": "https://images.pexels.com/photos/13156181/pexels-photo-13156181.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
        "alt": "Dark geometric background",
        "usage": "Subtle texture or background behind the services grid."
      },
      "about_team_meeting": {
        "url": "https://images.pexels.com/photos/8134173/pexels-photo-8134173.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
        "alt": "Professional team discussing projects",
        "usage": "About us or Contact section visual."
      }
    }
  },
  "accessibility_and_testing": {
    "testing": "All interactive elements MUST have data-testid (e.g., data-testid='hero-cta-button', data-testid='client-form-submit').",
    "accessibility": "Contrast ratios > 4.5:1. Explicit hover states on text (hover:text-white). Do not rely on color alone to convey status."
  },
  "instructions_to_main_agent": [
    "Do not build a generic template. Incorporate high contrast text and generous spacing.",
    "Use Playfair Display for headings and Work Sans for body. Configure these in Tailwind config.",
    "Marketing pages must use asymmetric layouts or bento grids. Do not center everything.",
    "Dashboard and admin pages must be functional, high density, utilizing custom shadcn tables and forms.",
    "Ensure the hero image is completely covered with a black/60 overlay for text readability.",
    "Apply the primary accent color (#D4AF37) strictly for interactive highlights and crucial CTAs, avoid overusing it."
  ]
}
