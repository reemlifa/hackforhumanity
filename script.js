document.getElementById('search-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const isRegistered = confirm("You need to sign up for Community Cleans before registering for an event. Would you like to sign up?");
    if (isRegistered) {
      alert("Redirecting to the sign-up page...");
      // Redirect to sign-up page logic (replace with the actual URL)
      window.location.href = "https://signup-page.com";
    }
  });