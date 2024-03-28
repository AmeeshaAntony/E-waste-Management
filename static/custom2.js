document.addEventListener("DOMContentLoaded", function() {
    var container = document.querySelector(".scrolling");

    container.addEventListener("wheel", function(event) {
        container.scrollLeft += event.deltaY;
        event.preventDefault();
    });
});
