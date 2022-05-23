function check()
{
    if (document.getElementById('in').value == "")
    {
        alert("Введите имя пользователя")
        return
    }
    if (document.getElementById('first').value == "")
    {
        alert("Введите Пароль")
        return
    }

    if (document.getElementById('second').value == "")
    {
        alert("Подтвердите Пароль")
        return
    }

    if (document.querySelector('#first').value !== document.querySelector('#second').value ) {
        document.querySelector('.wrong').style.display = "block"
        document.querySelector('.block').style.height = "calc(580px + 20px)"
        return
    }
    else
    {
        document.querySelector('.wrong').style.display = "none"
        document.querySelector('.block').style.height = "580px"
        window.location.href = '/profile'
    }


}