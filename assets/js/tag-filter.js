document.addEventListener('DOMContentLoaded', function () {
  const buttons = document.querySelectorAll('.tag-btn');
  const items = document.querySelectorAll('[data-tags]');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const tag = btn.dataset.tag;

      items.forEach(item => {
        const tags = item.dataset.tags.split(',');
        item.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
      });
    });
  });
});
