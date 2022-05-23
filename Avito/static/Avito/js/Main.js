function Detail()
{
    window.location.href = "/detail"
}

function Sign(flag)
{
    if (flag){
        window.location.href = '/profile';
    }
    else
        window.location.href = '/signin';
}

