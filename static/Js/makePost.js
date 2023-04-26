const picture = document.querySelector('#picture'); 
const btnCerrar = document.querySelector('#cerrar');
const btnBorrar = document.querySelector('#borrar');
const fondo = document.querySelector('.filtro');
const windowPost = document.querySelector('.makePost');
const BtnPost = document.querySelector('.btnPost')
const BtnCerrar2 = document.querySelector('.close');

// Cambiar la imagen
imagen.addEventListener('change',()=>{
    let imagen = document.querySelector('#imagen');
    let url = URL.createObjectURL(imagen.files[0]);

    picture.classList.remove('oculto');
    picture.src = url;
        
});

btnCerrar.addEventListener('click',()=>{
    fondo.classList.add('oculto');
    windowPost.classList.add('oculto');
    console.log('Cerrado');
});

btnBorrar.addEventListener('click',()=>{
    picture.classList.add('oculto');
    picture.src = ' ';

});

BtnPost.addEventListener('click',()=>{
    fondo.classList.remove('oculto');
    windowPost.classList.remove('oculto');
});

