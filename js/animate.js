window.addEventListener('load', () => {
    const modal = document.getElementById('popupModal');
    modal.classList.remove('hidden');
  });
  
  document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    const data = {
      name: document.getElementById('name').value.trim(),
      email: document.getElementById('email').value.trim(),
      phone: document.getElementById('phone').value.trim(),
      message: document.getElementById('message').value.trim()
    };
  
    console.log('Form submitted:', data);
  
    // Optional: integrate with Flask backend
    /*
    fetch('http://127.0.0.1:5000/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => alert("Submitted Successfully!"))
    .catch(error => console.error("Error:", error));
    */
  });
  
  function closeForm() {
    document.getElementById('popupModal').classList.add('hidden');
  }
  