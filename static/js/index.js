const counterButton = document.querySelector('.counterBtn')
const counter = document.querySelector('.counter')

counterButton.addEventListener('click', () => counter.textContent = Number(counter.textContent) + 1)