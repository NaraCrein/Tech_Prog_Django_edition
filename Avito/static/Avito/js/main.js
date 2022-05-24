function Detail(id)
{
        window.open(`/detail?q=${id}`);
}

function Sign(flag)
{
    if (flag){
        window.location.href = '/profile';
    }
    else
        window.location.href = '/signin';
}

