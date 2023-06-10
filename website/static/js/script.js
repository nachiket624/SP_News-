const hamburger = document.querySelector(".hamburger")
const navList = document.querySelector(".nav-list")

hamburger.addEventListener('click', () =>{
navList.classList.toggle('show')
});

var widths = [0, 500, 850];

function resizeFn() {
if (window.innerWidth>=widths[0] && window.innerWidth<widths[1]) {
    hamburger.addEventListener('click', () =>{
        navList.classList.toggle('show')
        });
} 
else {
    
}
}
window.onresize = resizeFn;
resizeFn();