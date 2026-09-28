console.log("MEDHA site loaded");

document.querySelectorAll('.team-member-about-trigger').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const wrapper = btn.closest('.team-member-about');
    document.querySelectorAll('.team-member-about.bio-open').forEach(el => {
      if (el !== wrapper) el.classList.remove('bio-open');
    });
    wrapper.classList.toggle('bio-open');
  });
});

// Tap anywhere else closes any open bio
document.addEventListener('click', (e) => {
  if (!e.target.closest('.team-member-about')) {
    document.querySelectorAll('.team-member-about.bio-open').forEach(el => el.classList.remove('bio-open'));
  }
});
// Hero slideshow: change photo every 3 seconds
(function () {
  const slides = document.querySelectorAll('.hero-slide');
  if (slides.length < 2) return;

  let current = 0;
  setInterval(() => {
    slides[current].classList.remove('active');
    current = (current + 1) % slides.length;
    slides[current].classList.add('active');
  }, 3000);
})();
