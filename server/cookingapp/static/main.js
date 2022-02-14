function openModal(modalId) {
    modal = document.getElementById(modalId)
    modal.classList.remove('opacity-0')
    modal.classList.remove('h-0')
    modal.classList.remove('-mt-20')
}

function closeModal(modalId) {
    modal = document.getElementById(modalId)
    modal.classList.add('opacity-0')
    modal.classList.add('h-0')
    modal.classList.add('-mt-20')
}


// listener to radio button
var span = []
var radios = document.forms["recipeform"].elements["difficulty"]
for (var i=0, max=radios.length; i < max; i++) {
    
    radios[i].onclick = function() {
        for (var i=0, max=radios.length; i < max; i++) {
            span = document.getElementById(radios[i].id+"-checkbox");
            if (span.id == this.id+"-checkbox") {
                span.classList.add("bg-torange-500");
            } else {
                span.classList.remove("bg-torange-500");
            }
        }
    }
}