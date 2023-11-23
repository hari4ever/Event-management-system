var signup = document.getElementById('signuppageinjs'),
    data_in_db = JSON.parse(signup.textContent),
    classNodes = document.querySelectorAll('.form');
signup.textContent = '';


function doOperation(lis) {

    classNodes[0].value = lis['email'];
    classNodes[1].value = lis['username'];

    for (const o of lis['mistake']) {
        if (o == 'u') {
            classNodes[1].style.borderColor = 'red';
            classNodes[2].value = lis['password'];
            classNodes[3].value = lis['password'];
        } else if (o == 'p') {
            classNodes[3].style.borderColor = 'red';
            classNodes[4].style.borderColor = 'red';
            classNodes[4].value = '';
            classNodes[3].value = '';
        } else if (o == 'e') {
            classNodes[0].style.borderColor = 'red';
        } else if (o == 'ph') {
            classNodes[3].style.borderColor = 'red';
        }
    }
}

if (data_in_db['mistake'].length != 0) {
    doOperation(data_in_db);
} else
    for (var temp of classNodes) {
        temp.style.borderColor = 'aqua';
        temp.value = '';
    }