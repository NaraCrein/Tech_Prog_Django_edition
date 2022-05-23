function Sign(flag)
{
    if (flag){
        window.location.href = '/profile';
    }
    else
        window.location.href = '/signin';
}

function Contacts(){
    document.getElementById("show_txt").innerHTML="+79200000000";
}

function Star(id_star){

    for (let i = 1; i <= id_star; i++)
    {
        document.getElementById(i).src="../static/Avito/imgs/Star_full.png"
    }
    for (let i = id_star + 1; i < 6; i++)
         document.getElementById(i).src="../static/Avito/imgs/Star.png"
}
function Back(){
    document.getElementById("image_in_gallery").src="../static/Avito/imgs/chairs.png"
}
function Next(){
    document.getElementById("image_in_gallery").src="{{Ad.image}}"
}
