document.querySelectorAll('.task-list li').forEach(item => {
    item.addEventListener('dragstart', dragStart);
});

document.querySelectorAll('.matrix .col').forEach(col => {
    col.addEventListener('dragover', ev => ev.preventDefault());
    col.addEventListener('drop', drop);
});

function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.dataset.task);
}

function drop(e) {
    e.preventDefault();
    const taskId = e.dataTransfer.getData('text/plain');
    const category = this.dataset.category;
    fetch(`/tasks/${taskId}/update-category/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: `category=${category}`
    }).then(() => location.reload());
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.querySelectorAll('#tmt .start-timer').forEach(btn => {
    btn.addEventListener('click', function () {
        const timerSpan = this.nextElementSibling;
        let time = 120;
        timerSpan.textContent = format(time);
        const interval = setInterval(() => {
            time--;
            timerSpan.textContent = format(time);
            if (time <= 0) {
                clearInterval(interval);
            }
        }, 1000);
    });
});

function format(time) {
    const m = String(Math.floor(time / 60)).padStart(2, '0');
    const s = String(time % 60).padStart(2, '0');
    return `${m}:${s}`;
}
