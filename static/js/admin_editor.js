let noOfCharac = 50;
let contents = document.querySelectorAll(".content");
contents.forEach((content) => {
    //If text length is less that noOfCharac... then hide the read more button
    if (content.textContent.length < noOfCharac) {
        content.nextElementSibling.style.display = "none";
    } else {
        let displayText = content.textContent.slice(0, noOfCharac);
        let moreText = content.textContent.slice(noOfCharac);
        content.innerHTML = `${displayText}<span class="dots">...</span><span class="hide more">${moreText}</span>`;
    }
});

// Refresh page with form without warning
function readMore(btn) {
    let post = btn.parentElement;
    post.querySelector(".dots").classList.toggle("hide");
    post.querySelector(".more").classList.toggle("hide");
    btn.textContent == "View More" ? (btn.textContent = "View Less") : (btn.textContent = "View More");
}

// Password Toogle

function passwordToggle() {
  var x = document.getElementById("password1");
  var y = document.getElementById("password2");

  if (x.type === "password" && y.type == "password") {
    x.type = "text";
    y.type = "text";
  } else {
    x.type = "password";
    y.type = "password";
  }
}

if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}
