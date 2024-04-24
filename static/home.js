// Define an array of image URLs
var images = ["ewaste1.jpg", "ewaste2.jpg", "ewaste3.jpg"]; // Add more image URLs as needed

// Initialize index and the image element
var index = 0;
var imgElement = document.getElementById("slideshow");

// Function to change the image every 2 seconds
function changeImage() {
    imgElement.src = "{% static 'images/" + images[index] + "' %}";
    index = (index + 1) % images.length; // Loop back to the beginning when reaching the end
}

// Call the function initially and set an interval to call it every 2 seconds
changeImage();
setInterval(changeImage, 2000);
