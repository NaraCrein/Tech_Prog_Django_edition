function goToSign(flag) {
    if (flag){
        window.location.href = '../Profile/Profile.html';
    }
    window.location.href = '../Sign/SignIn.html';
}
function showContacts(){
    document.getElementById("show_txt").innerHTML="+79200000000";
}
function report(){
    document.getElementById("report_txt").innerHTML="Ваша жалоба принята на рассмотрение";
}
function lightStar(id_star){
    if (id_star>=1){
        document.getElementById("1").src="../images/Star_full.png"
    }if (id_star>=2){
        document.getElementById("2").src="../images/Star_full.png"
    }if (id_star>=3){
        document.getElementById("3").src="../images/Star_full.png"
    }if (id_star>=4){
        document.getElementById("4").src="../images/Star_full.png"
    }if (id_star===5){
        document.getElementById("5").src="../images/Star_full.png"
    }
}
function goBack(){
    document.getElementById("image_in_gallery").src="../images/chairs.png"
}
function goNext(){
    document.getElementById("image_in_gallery").src="../images/table.png"
}
