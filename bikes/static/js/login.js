var n = document.getElementById('hee'),
    d = JSON.parse(n.textContent),
    classNodes = document.querySelectorAll('.form');
n.textContent = '';

function doOperation(lis) {

    classNodes[0].value = lis['username'];
    classNodes[1].value = lis['password'];

    if (lis['mistake'] == 'u')
        classNodes[0].style.borderColor = 'red';
    else if (lis['mistake'] == 'p')
        classNodes[1].style.borderColor = 'red';
}

if (d['mistake'].length != 0) {
    doOperation(d);
} else
    for (var temp of classNodes) {
        temp.style.borderColor = 'aqua';
        temp.value = '';
    }

    