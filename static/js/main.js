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