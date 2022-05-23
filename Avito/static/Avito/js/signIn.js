function signi()
{
    if (document.getElementById('in').value == "")
    {
        alert("Введите имя пользователя")
        return
    }
    if (document.getElementById('pass').value == "")
    {
        alert("Введите Пароль")
        return
    }

        window.location.href = '/profile'
}