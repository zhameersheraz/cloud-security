// mobile menu
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('nav ul');
if (toggle && menu) {
  toggle.addEventListener('click', () => menu.classList.toggle('open'));
}

// copy-to-clipboard
document.querySelectorAll('pre').forEach(pre => {
  const btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.textContent = 'copy';
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(pre.querySelector('code').innerText);
      btn.textContent = 'copied';
      setTimeout(() => btn.textContent = 'copy', 1500);
    } catch (e) { btn.textContent = 'failed'; }
  });
  pre.appendChild(btn);
});

// fade-in on scroll
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.cloud-card, h2, .note').forEach(el => {
  el.classList.add('fade-in');
  io.observe(el);
});

// small footer detail: year in copyright
const yr = document.getElementById('year');
if (yr) yr.textContent = new Date().getFullYear();

// mark current page in nav
const here = location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav a').forEach(a => {
  if (a.getAttribute('href') === here) a.classList.add('active');
});
