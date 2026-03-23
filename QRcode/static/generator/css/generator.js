const counterInput = document.querySelector('.input-counter')
const btnPlus = document.querySelector('.btn-plus')
const btnMinus = document.querySelector('.btn-minus')

let count = parseInt(counterInput.value) || 0

// Update input and count variable, prevent negatives and non-numbers
function updateCounter(newCount) {
  if (isNaN(newCount) || newCount < 0) {
    newCount = 0
  }
  count = newCount
  counterInput.value = count
}

function increment() {
  updateCounter(count + 1)
}

function decrement() {
  updateCounter(count - 1)
}

// Button click listeners
btnPlus.addEventListener('click', increment)
btnMinus.addEventListener('click', decrement)

// Keyboard support for arrow keys
document.addEventListener('keydown', event => {
  if (event.key === 'ArrowUp') {
    increment()
  } else if (event.key === 'ArrowDown') {
    decrement()
  }
})

// Listen for manual changes in the input
counterInput.addEventListener('input', () => {
  let manualValue = parseInt(counterInput.value)
  if (isNaN(manualValue) || manualValue < 0) {
    manualValue = 0 // Reset to 0 if invalid or negative
  }
  count = manualValue
  counterInput.value = count // Correct the displayed value if needed
})
