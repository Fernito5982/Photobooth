const imagen = document.querySelector('.user');
const input = document.querySelector('#avatar');

console.log(imagen);
console.log(input);

input.addEventListener('change',()=>{
    imagen.src = URL.createObjectURL(input.files[0]);
});