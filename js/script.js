function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskDate = document.getElementById('taskDate');
    const taskList = document.getElementById('taskList');

    const taskText = taskInput.value.trim();
    const date = taskDate.value;

    if (taskText === '' || date === '') {
        alert("Please enter a task and date!");
        return;
    }

    const li = document.createElement('li');
    li.innerHTML = `
        <span>${taskText} - <strong>${date}</strong></span>
        <button class="delete-btn" onclick="this.parentElement.remove()">Delete</button>
    `;

    taskList.appendChild(li);

    taskInput.value = '';
    taskDate.value = '';
}
