// custom.js

$(document).ready(function() {
    // Handle click event on overview button
    $('.overview-button').click(function(e) {
        e.preventDefault(); // Prevent default link behavior

        // Show the hi-container
        $('.hi-container , .hidden-container1').show();
    });
});
