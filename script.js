// mobile menu toggle
const toggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('nav ul');
if (toggle && menu) {
  toggle.addEventListener('click', () => menu.classList.toggle('open'));
}

// copy-to-clipboard for code blocks
document.querySelectorAll('pre').forEach(pre => {
  const btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.textContent = 'copy';
  btn.addEventListener('click', async () => {
    const code = pre.querySelector('code');
    try {
      await navigator.clipboard.writeText(code.innerText);
      btn.textContent = 'copied';
      setTimeout(() => btn.textContent = 'copy', 1500);
    } catch (e) { btn.textContent = 'failed'; }
  });
  pre.appendChild(btn);
});
