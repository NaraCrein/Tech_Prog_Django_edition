function reset()
{
    if (document.querySelector('#first').value !== document.querySelector('#second').value)
    {
        alert("Пароли не совпадают")
        return
    }

    if (document.getElementById('first').value == "")
    {
        alert("Введите пароль")
        return
    }
    alert("Пароль успешно изменен")
    window.location.href = '../Profile/Profile.html'
}