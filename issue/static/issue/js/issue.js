const updateModal = document.getElementById("updateIssue");
updateModal.addEventListener("show.bs.modal", (event) => {
  // Button that triggered the modal
  const button = event.relatedTarget;
  // Extract info from data-bs-* attributes
  const pk = button.getAttribute("data-bs-issuepk");
    fetch(`/issue/update/${pk}`)
        .then(response => response.text())
        .then(html => setForm(html))
        .catch(err => console.warn(err));
    
    
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  function setForm(html) {
      const modalBody = updateModal.querySelector("#updateIssue .modal-body");
      modalBody.innerHTML = html;
  }

});
