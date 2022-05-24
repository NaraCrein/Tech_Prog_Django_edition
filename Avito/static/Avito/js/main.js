function Detail(id)
{

        window.location.href = `/detail/${id}`


}

function Sign(flag)
{
    if (flag){
        window.location.href = '/profile';
    }
    else
        window.location.href = '/signin';
}

