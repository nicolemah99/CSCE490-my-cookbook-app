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
            console.log(button)
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

function lightbox(){
    const imageInstance = basicLightbox.create(document.querySelector('#image'))
    document.querySelector('img.image').onclick = imageInstance.show
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
