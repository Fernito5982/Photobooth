const btnCerrar1 = document.querySelector('#cerrar1');
const fondo1 = document.querySelector('.filtro');
const btnComment = document.querySelector('#btnComment')
const windowPost1 = document.querySelector('#makeComment');
const textComment = document.querySelector('#comentario');
const ver = document.querySelector('#ver_mas');

ver.addEventListener('click',()=>{
    fondo1.classList.remove('oculto');
    windowPost1.classList.remove('oculto'); 
});

btnCerrar1.addEventListener('click',()=>{
    fondo1.classList.add('oculto');
    windowPost1.classList.add('oculto');
    console.log('Cerrado');
});

btnComment.addEventListener('click',()=>{
    fondo1.classList.remove('oculto');
    windowPost1.classList.remove('oculto');
});

textComment.addEventListener('click', ()=>{
    textComment.textContent = '';
});