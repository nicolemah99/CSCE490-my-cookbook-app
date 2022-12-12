if (document.querySelector('form') != undefined) {

    const form = document.querySelector("form")

    form.addEventListener('submit', e => {
        if (!form.checkValidity()) {
            e.preventDefault()
        }
        form.classList.add('was-validated')
    })
}

document.addEventListener('DOMContentLoaded', function () {

    update_counters();
    
    if (document.querySelector('#averageRating') != undefined){
        const averageRating = document.querySelector('#averageRating');
        const recipe_id = averageRating.dataset.recipe_id;
        console.log(`recipeID:${recipe_id}`);

        fetch(`/api/rating?recipe_id=${recipe_id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.avg)
            addRatingStars(data.avg);
        })
        .catch(error => {
            console.log("*** api/rating error **", response.json());
        })

    }
    if (document.querySelector('.ratings') != undefined){
        const ratingBlock = document.querySelector(".ratings");
            var rating = ratingBlock.dataset.rating;
            for (let i = 0; i < rating; i++) {
                var star = document.createElement('i');
                star.className = "bi bi-star-fill";
                ratingBlock.appendChild(star);
        }
        
    }
    if (document.querySelector('.toggle_saved') != undefined) {

        document.querySelectorAll('.toggle_saved').forEach(button => {
            const recipe_id = parseInt(button.dataset.recipe_id);

            fetch(`/api/saved?recipe_id=${recipe_id}`)
                .then(response => response.json())
                .then(data => {
                    update_button_display(button, data.in_cookbook);
                })
                .catch(error => {
                    console.log("*** api/saved error **", response.json());
                })

            button.onclick = function () {

                const recipe_id = this.dataset.recipe_id;
                console.log(`Toggle saved for recipe id=${recipe_id}`);
                fetch(`/api/toggle?recipe_id=${recipe_id}`)
                    .then(response => response.json())
                    .then(data => {
                        update_button_display(this, data.in_cookbook);
                        update_innerHTML('#ms', data['my_saves'])
                    })
                    .catch(error => {
                        console.log("*** api/toggle error **", error);
                    })
            }
        })
    }

});
function addRatingStars(rating){
    const ratingDiv = document.querySelector('#averageRating');
    
    for (let i = 0; i < rating; i++) {
        var star = document.createElement('i');
                star.className = "bi bi-star-fill";
                ratingDiv.appendChild(star);
      }

};

function addInstructionElement() {
    const element = document.getElementById("instructionList");
    var IG = document.createElement('div');
    var IGT = document.createElement('div');
    var I1 = document.createElement('input');
    IG.className = "input-group";
    IGT.className = 'input-group-text';
    I1.name = "instructions";
    I1.className = 'form-control';
    I1.type = 'text';
    I1.placeholder = 'Add Instruction';
    IG.append(IGT);
    IG.append(I1);

    element.append(IG);
}

function addIngredientElement() {
    const element = document.getElementById("ingredientList");
    var IG = document.createElement('div');
    var IGT = document.createElement('div');
    var I1 = document.createElement('input');
    var I2 = document.createElement('input');
    var I3 = document.createElement('select');
    var O1 = document.createElement('option');
    var O2 = document.createElement('option');
    var O3 = document.createElement('option');
    var O4 = document.createElement('option');
    var O5 = document.createElement('option');
    var O6 = document.createElement('option');
    var O7 = document.createElement('option');
    IG.className = "input-group";
    IGT.className = 'input-group-text';
    I1.className = 'form-control';
    I1.name = "ingredients";
    I2.className = 'form-control';
    I2.name = "ingredients";
    I3.className = 'form-control custom-select';
    I3.name = "ingredients";
    I1.type = 'text';
    I2.type = 'number';
    I1.placeholder = 'Ingredient';
    I2.placeholder = 'Quantity';
    O1.selected;
    O1.innerHTML = 'Choose a Unit';
    O2.value = 'C';
    O2.innerHTML = 'Cup';
    O3.value = 'OZ';
    O3.innerHTML = 'Ounce';
    O4.value = 'LB';
    O4.innerHTML = 'Pound';
    O5.value = 'TB';
    O5.innerHTML = 'Tablespoon';
    O6.value = 'TS';
    O6.innerHTML = 'Teaspoon';
    O7.innerHTML = 'Not Applicable';
    O7.value = 'NA';
    I3.appendChild(O1);
    I3.appendChild(O7);
    I3.appendChild(O2);
    I3.appendChild(O3);
    I3.appendChild(O4);
    I3.appendChild(O5);
    I3.appendChild(O6);
    IG.append(IGT);
    IG.append(I2);
    IG.append(I3);
    IG.append(I1);

    element.append(IG);
}

function clearForm() {
    var form = document.getElementById('recipeSubmit');
    form.submit();
    form.reset();
}

function update_button_display(button, saved) {
    console.log(`update_button-display: ${button} ${saved}`);
    let filename = button.src;
    if (saved) {
        filename = filename.replace("hollow", "filled");
    } else {
        filename = filename.replace("filled", "hollow");
    }
    button.src = filename;
}


function update_innerHTML(element_id, value) {
    if (document.querySelector(element_id) != undefined) {
        document.querySelector(element_id).innerHTML = value;
    }
}

function update_counters() {
    fetch("/api/counters")
    .then(response => response.json())
    .then(data => {
        update_innerHTML('#mr', data['my_recipes'])
        update_innerHTML('#ms', data['my_saves'])
    })
    .catch(error => {
        console.log('**** api/counters error **', error);
    });
}


const myTextArea = document.getElementById('my-textarea');
const remainingCharsText = document.getElementById('my-textarea-remaining-chars');
const MAX_CHARS = 250;

myTextArea.addEventListener('input', () => {
    const remaining = MAX_CHARS - myTextArea.value.length;
    const color = remaining < MAX_CHARS * 0.1 ? 'red' : null
    remainingCharsText.textContent = `${remaining} characters remaining`;
    remainingCharsText.style.color = color;
});

const oneStar = document.getElementById('oneStar');
const twoStar= document.getElementById('twoStar');
const threeStar = document.getElementById('threeStar');
const fourStar = document.getElementById('fourStar');
const fiveStar = document.getElementById('fiveStar');
const rating = document.getElementById('rating');

oneStar.addEventListener('mouseover',oneStarOn);
function oneStarOn(){
    oneStar.className = 'bi bi-star-fill';
}

twoStar.addEventListener('mouseover',twoStarOn);
function twoStarOn(){
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
}

threeStar.addEventListener('mouseover',threeStarOn);

function threeStarOn(){
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
    threeStar.className = 'bi bi-star-fill';
};

fourStar.addEventListener('mouseover',fourStarOn);
function fourStarOn(){
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
    threeStar.className = 'bi bi-star-fill';
    fourStar.className = 'bi bi-star-fill';
};

fiveStar.addEventListener('mouseover',fiveStarOn);
function fiveStarOn(){
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
    threeStar.className = 'bi bi-star-fill';
    fourStar.className = 'bi bi-star-fill';
    fiveStar.className = 'bi bi-star-fill';
};

oneStar.addEventListener('mouseleave',oneStarLeave);
function oneStarLeave(){
    oneStar.className = 'bi bi-star';
}

twoStar.addEventListener('mouseleave',twoStarLeave);
function twoStarLeave(){
    oneStar.className = 'bi bi-star';
    twoStar.className = 'bi bi-star';
};

threeStar.addEventListener('mouseleave',threeStarLeave);
function threeStarLeave(){
    oneStar.className = 'bi bi-star';
    twoStar.className = 'bi bi-star';
    threeStar.className = 'bi bi-star';
};

fourStar.addEventListener('mouseleave',fourStarLeave);

function fourStarLeave(){
    oneStar.className = 'bi bi-star';
    twoStar.className = 'bi bi-star';
    threeStar.className = 'bi bi-star';
    fourStar.className = 'bi bi-star';
};

fiveStar.addEventListener('mouseleave',fiveStarLeave);

function fiveStarLeave(){
    oneStar.className = 'bi bi-star';
    twoStar.className = 'bi bi-star';
    threeStar.className = 'bi bi-star';
    fourStar.className = 'bi bi-star';
    fiveStar.className = 'bi bi-star';
}

oneStar.addEventListener('click',() => {
    oneStar.className = 'bi bi-star-fill';
    rating.value = 1;
    oneStar.removeEventListener('mouseleave',oneStarLeave);
    twoStar.removeEventListener('mouseleave',twoStarLeave);
    threeStar.removeEventListener('mouseleave',threeStarLeave);
    fourStar.removeEventListener('mouseleave',fourStarLeave);
    fiveStar.removeEventListener('mouseleave',fiveStarLeave);
    oneStar.removeEventListener('mouseover',oneStarOn);
    twoStar.removeEventListener('mouseover',twoStarOn);
    threeStar.removeEventListener('mouseover',threeStarOn);
    fourStar.removeEventListener('mouseover',fourStarOn);
    fiveStar.removeEventListener('mouseover',fiveStarOn);
    twoStar.className = 'bi bi-star';
    threeStar.className = 'bi bi-star';
    fourStar.className = 'bi bi-star';
    fiveStar.className = 'bi bi-star';
});

twoStar.addEventListener('click',() => {
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
    rating.value = 2;
    oneStar.removeEventListener('mouseleave',oneStarLeave);
    twoStar.removeEventListener('mouseleave',twoStarLeave);
    threeStar.removeEventListener('mouseleave',threeStarLeave);
    fourStar.removeEventListener('mouseleave',fourStarLeave);
    fiveStar.removeEventListener('mouseleave',fiveStarLeave);
    oneStar.removeEventListener('mouseover',oneStarOn);
    twoStar.removeEventListener('mouseover',twoStarOn);
    threeStar.removeEventListener('mouseover',threeStarOn);
    fourStar.removeEventListener('mouseover',fourStarOn);
    fiveStar.removeEventListener('mouseover',fiveStarOn);
    threeStar.className = 'bi bi-star';
    fourStar.className = 'bi bi-star';
    fiveStar.className = 'bi bi-star';

});

threeStar.addEventListener('click',() => {
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
    threeStar.className = 'bi bi-star-fill';
    rating.value = 3;
    oneStar.removeEventListener('mouseleave',oneStarLeave);
    twoStar.removeEventListener('mouseleave',twoStarLeave);
    threeStar.removeEventListener('mouseleave',threeStarLeave);
    fourStar.removeEventListener('mouseleave',fourStarLeave);
    fiveStar.removeEventListener('mouseleave',fiveStarLeave);
    oneStar.removeEventListener('mouseover',oneStarOn);
    twoStar.removeEventListener('mouseover',twoStarOn);
    threeStar.removeEventListener('mouseover',threeStarOn);
    fourStar.removeEventListener('mouseover',fourStarOn);
    fiveStar.removeEventListener('mouseover',fiveStarOn);

    fourStar.className = 'bi bi-star';
    fiveStar.className = 'bi bi-star';
});

fourStar.addEventListener('click',() => {
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
    threeStar.className = 'bi bi-star-fill';
    fourStar.className = 'bi bi-star-fill';
    rating.value = 4;
    oneStar.removeEventListener('mouseleave',oneStarLeave);
    twoStar.removeEventListener('mouseleave',twoStarLeave);
    threeStar.removeEventListener('mouseleave',threeStarLeave);
    fourStar.removeEventListener('mouseleave',fourStarLeave);
    fiveStar.removeEventListener('mouseleave',fiveStarLeave);
    oneStar.removeEventListener('mouseover',oneStarOn);
    twoStar.removeEventListener('mouseover',twoStarOn);
    threeStar.removeEventListener('mouseover',threeStarOn);
    fourStar.removeEventListener('mouseover',fourStarOn);
    fiveStar.removeEventListener('mouseover',fiveStarOn);
    fiveStar.className = 'bi bi-star';
});

fiveStar.addEventListener('click',() => {
    oneStar.className = 'bi bi-star-fill';
    twoStar.className = 'bi bi-star-fill';
    threeStar.className = 'bi bi-star-fill';
    fourStar.className = 'bi bi-star-fill';
    fiveStar.className = 'bi bi-star-fill';
    rating.value = 5;
    oneStar.removeEventListener('mouseleave',oneStarLeave);
    twoStar.removeEventListener('mouseleave',twoStarLeave);
    threeStar.removeEventListener('mouseleave',threeStarLeave);
    fourStar.removeEventListener('mouseleave',fourStarLeave);
    fiveStar.removeEventListener('mouseleave',fiveStarLeave);
    oneStar.removeEventListener('mouseover',oneStarOn);
    twoStar.removeEventListener('mouseover',twoStarOn);
    threeStar.removeEventListener('mouseover',threeStarOn);
    fourStar.removeEventListener('mouseover',fourStarOn);
    fiveStar.removeEventListener('mouseover',fiveStarOn);
});
