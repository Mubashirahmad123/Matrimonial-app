$(document).ready(function() {

    $('#logout-btn').on('click', function(e) {
      e.preventDefault();
      $.ajax({
        url: 'logout/',
        type: 'POST',
        headers: {
          'X-CSRFToken': csrfToken
        },
        success: function (response) {
          if (response.success){
            $('#logged-in').hide();
          }
        }
        

      });
    });
  });

//heading mouse move

var main = document.querySelector("#main");
var crsr = document.querySelector(".cursor");

main.addEventListener("mousemove", function (dets) {
    crsr.style.left = dets.x + "px";
    crsr.style.top = dets.y + "px";
});

main.addEventListener("mouseleave", function () {
    crsr.style.display = "none";
});

main.addEventListener("mouseenter", function () {
    crsr.style.display = "block"; // or "inline" depending on your cursor type
});

// ripple effect

function createRipple(event) {
    const ripple = document.createElement("div");
    ripple.className = "ripple";
    const rect = event.currentTarget.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    ripple.style.width = `${size}px`;
    ripple.style.height = `${size}px`;
    ripple.style.left = `${event.clientX - rect.left - size / 2}px`;
    ripple.style.top = `${event.clientY - rect.top - size / 2}px`;
    event.currentTarget.appendChild(ripple);
  }


//   smooth scrolling
// <!-- Add this script in your HTML file or include it in your existing JavaScript file -->

    document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();

                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    })

    // animate__slideInLeft


    document.addEventListener('DOMContentLoaded', function () {
        console.log('DOM fully loaded');
        document.querySelector('.introduction').classList.add('animate__animated', 'animate__slideInLeft');
        document.documentElement.style.setProperty('--animate-duration', '6s');

    });



    document.addEventListener('DOMContentLoaded', function () {
        console.log('DOM fully loaded');
        document.querySelector('.hero-section').classList.add('animate__animated', 'animate__slideInRight');
        document.documentElement.style.setProperty('--animate-duration', '6s');

    });
