var check = document.querySelector(".btcheck");
check.addEventListener('click',idioma);

function idioma(){
/*  console.log(check.checked);
*/
  let id=check.checked;

 // alert(id);

   if (id){
    location.href="../home";
  }else{
    location.href="../index";
  }


}
