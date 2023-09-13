const red = document.querySelector('style')
// get the elements by its id
const red_header = document.querySelector('#red_header');


// Adds the class red to the header element when
//the user clicks on the tag with id red_header
red_header.addEventListener('click', () => {
    red_header.classList.add("red");
})