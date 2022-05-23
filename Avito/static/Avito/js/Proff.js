 function Thereturn()
{
    window.location.href = '/';
}

function Change()
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

function CreateNote()
{
    window.location.href = '/add'
}