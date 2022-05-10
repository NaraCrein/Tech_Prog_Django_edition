 function returns()
{
    window.location.href = '../Main/main.html';
}

function change()
{
    if (document.querySelector('#change').value === "Редактировать")
    {
        document.querySelector('#change').value = "Сохранить"
        document.querySelector('.inp').disabled = ""
        document.querySelector('#inp1').disabled = ""
    }
    else if (document.querySelector('#change').value === "Сохранить")
    {
        document.querySelector('#change').value = "Редактировать"
        document.querySelector('.inp').disabled = "disabled"
        document.querySelector('#inp1').disabled = "disabled"
    }
}

function createNote()
{
    window.location.href = '../Add/add.html'
}