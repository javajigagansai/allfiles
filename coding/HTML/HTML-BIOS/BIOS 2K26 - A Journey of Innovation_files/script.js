document.addEventListener("DOMContentLoaded", () => {
  // --- 1. Custom Elegant Cursor ---
  const cursor = document.querySelector(".cursor");
  const cursorFollower = document.querySelector(".cursor-follower");
  // Only initialize mouse events if it's not a touch device
  if (window.matchMedia("(pointer: fine)").matches) {
    document.addEventListener("mousemove", (e) => {
      cursor.style.left = e.clientX + "px";
      cursor.style.top = e.clientY + "px";

      cursorFollower.style.left = e.clientX + "px";
      cursorFollower.style.top = e.clientY + "px";
    });
    // Hover effects on interactive elements
    const interactiveSelectors =
      "a, button, .interactive-card, .interactive-bento, .hover-reveal, .interactive-badge, .interactive-glass, .interactive-contact, .interactive-pane, .scroll-btn";
    const interactiveElements = document.querySelectorAll(interactiveSelectors);

    interactiveElements.forEach((el) => {
      el.addEventListener("mouseenter", () => {
        cursor.style.backgroundColor = "transparent";

        cursorFollower.style.transform = "translate(-50%, -50%) scale(1.5)";
        cursorFollower.style.borderColor = "rgba(255, 255, 255, 0.3)";
        cursorFollower.style.background = "rgba(255, 255, 255, 0.05)";
      });

      el.addEventListener("mouseleave", () => {
        cursor.style.backgroundColor = "var(--text-primary)";

        cursorFollower.style.transform = "translate(-50%, -50%) scale(1)";
        cursorFollower.style.borderColor = "var(--glass-border)";
        cursorFollower.style.background = "rgba(255,255,255,0.01)";
      });
    });
  }

  // --- 2. Horizontal Scrolling for Gauntlet (Mouse Wheel) ---
  const scrollSections = document.querySelectorAll(".narrative");

  scrollSections.forEach((section) => {
    const scrollContainer = section.querySelector(".horizontal-scroll");
    if (!scrollContainer) return;

    if (window.matchMedia("(pointer: fine)").matches) {
      scrollContainer.addEventListener("wheel", (evt) => {
        // Check if user is scrolling mostly horizontally vs vertically
        // To allow normal page scroll if they hit the edge, but for simplicity here we assume scroll shift
        evt.preventDefault();
        scrollContainer.scrollLeft += evt.deltaY;
      });
    }

    const scrollLeftBtn = section.querySelector(".scroll-btn[aria-label='Scroll left'], #scroll-left");
    const scrollRightBtn = section.querySelector(".scroll-btn[aria-label='Scroll right'], #scroll-right");

    if (scrollLeftBtn && scrollRightBtn) {
      const scrollAmount = 350; // approximate width of one card + gap

      scrollLeftBtn.addEventListener("click", () => {
        scrollContainer.scrollBy({ left: -scrollAmount, behavior: "smooth" });
      });

      scrollRightBtn.addEventListener("click", () => {
        scrollContainer.scrollBy({ left: scrollAmount, behavior: "smooth" });
      });
    }
  });

  // --- 3. Fade-up Intersection Observer Component ---
  const fadeElements = document.querySelectorAll(".fade-up");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
        }
      });
    },
    {
      root: null,
      rootMargin: "0px",
      threshold: 0.15,
    },
  );
  fadeElements.forEach((el) => observer.observe(el));
  // --- 4. Smooth scrolling for Anchor Links ---
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href");
      if (targetId === "#") return;
      const target = document.querySelector(targetId);
      if (target) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });
  // --- 5. Navbar Hide/Show on Scroll Strategy ---
  let lastScrollY = window.scrollY;
  const nav = document.querySelector(".premium-nav");

  window.addEventListener(
    "scroll",
    () => {
      if (window.scrollY > 100 && window.scrollY > lastScrollY) {
        nav.style.transform = "translateY(-150%)";
      } else {
        nav.style.transform = "translateY(0)";
      }
      lastScrollY = window.scrollY;
    },
    { passive: true },
  );

  // --- 6. Parallax Effect for floating elements in Hero ---
  const parallaxElements = document.querySelectorAll(".parallax");

  if (window.matchMedia("(pointer: fine)").matches) {
    document.addEventListener("mousemove", (e) => {
      const windowWidth = window.innerWidth;
      const windowHeight = window.innerHeight;

      const mouseX = e.clientX;
      const mouseY = e.clientY;

      parallaxElements.forEach((el) => {
        const speed = parseFloat(el.getAttribute("data-speed")) || 1;
        const x = ((windowWidth / 2 - mouseX) * speed) / 100;
        const y = ((windowHeight / 2 - mouseY) * speed) / 100;

        el.style.transform = `translate(${x}px, ${y}px)`;
      });
    });
  }
  // --- 7. Theme Toggle Logic ---
  const themeToggleBtn = document.getElementById("theme-toggle");
  const htmlElement = document.documentElement;

  // Check for saved theme priority
  const savedTheme = localStorage.getItem("bios-theme");
  if (savedTheme) {
    htmlElement.setAttribute("data-theme", savedTheme);
  } else {
    // Default to dark, or check OS preference
    const prefersLight = window.matchMedia(
      "(prefers-color-scheme: light)",
    ).matches;
    if (prefersLight) {
      htmlElement.setAttribute("data-theme", "light");
    }
  }

  themeToggleBtn.addEventListener("click", () => {
    const currentTheme = htmlElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    htmlElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("bios-theme", newTheme);
  });
  // --- 8. Dynamic Countdown Timer ---
  // The event is set dynamically to March 27 of the current tracking year.
  let targetYear = new Date().getFullYear();
  let countDownDate = new Date(`March 27, ${targetYear} 09:00:00`).getTime();

  // If we happen to be past March 27th of the current year, track towards the next year so it doesn't just sit at 00.
  if (countDownDate < new Date().getTime() && new Date().getMonth() > 2) {
    targetYear++;
    countDownDate = new Date(`March 27, ${targetYear} 09:00:00`).getTime();
  }
  const daysEl = document.getElementById("days");
  const hoursEl = document.getElementById("hours");
  const minutesEl = document.getElementById("minutes");

  if (daysEl && hoursEl && minutesEl) {
    const updateCountdown = () => {
      const now = new Date().getTime();
      const distance = countDownDate - now;
      if (distance < 0) {
        daysEl.innerText = "00";
        hoursEl.innerText = "00";
        minutesEl.innerText = "00";
        return;
      }
      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor(
        (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60),
      );
      const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      daysEl.innerText = days.toString().padStart(2, "0");
      hoursEl.innerText = hours.toString().padStart(2, "0");
      minutesEl.innerText = minutes.toString().padStart(2, "0");
    };
    updateCountdown();
    setInterval(updateCountdown, 60000); // Updated every minute since seconds aren't tracked visually
  }
});
