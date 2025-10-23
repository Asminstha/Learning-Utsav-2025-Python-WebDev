(function(){
  // Theme toggle using localStorage
  const toggle = document.getElementById('themeToggle');
  const body = document.body;
  const label = document.getElementById('themeLabel');
  const theme = localStorage.getItem('theme') || 'light';
  if(theme === 'dark'){
    body.classList.add('dark-mode');
    toggle.checked = true;
    label.textContent = '☀️';
  } else {
    body.classList.remove('dark-mode');
    toggle.checked = false;
    label.textContent = '🌙';
  }

  toggle && toggle.addEventListener('change', function(e){
    if(e.target.checked){
      body.classList.add('dark-mode');
      localStorage.setItem('theme','dark');
      label.textContent = '☀️';
    } else {
      body.classList.remove('dark-mode');
      localStorage.setItem('theme','light');
      label.textContent = '🌙';
    }
  });

})();
