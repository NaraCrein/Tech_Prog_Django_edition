function goToSign(flag) {
    if (flag){
        window.location.href = '../Profile/Profile.html';
    }
    window.location.href = '../Sign/SignIn.html';
}

const photoInput = document.querySelector('#photosInput');
const preview = document.querySelector('.preview');

photoInput.addEventListener('change', updateImageDisplay);

function updateImageDisplay() {

    while (preview.firstChild) {
        preview.removeChild(preview.firstChild);
    }

    const curFiles = photoInput.files;

    if (curFiles.length === 0) {
        const para = document.createElement('p');

        para.textContent = 'Пока не выбрано ни одного фото';

        preview.appendChild(para);
    } else {
        const list = document.createElement('ol');

        preview.appendChild(list);

        for (const file of curFiles) {
            const listItem = document.createElement('li');
            const para = document.createElement('p');

            para.textContent = '' + file.name + '';

            listItem.appendChild(para);

            list.appendChild(listItem);
        }
    }
}