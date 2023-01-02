const circleProgress = document.querySelector(".circle-progress");
const numberOfBreaths = document.querySelector(".breath-input");
const start = document.querySelector(".start");
const instructions = document.querySelector(".instructions");
const breathsText = document.querySelector(".breaths-text");
let breathsLeft = 3;

//Getting selected breaths from user
numberOfBreaths.addEventListener("change", () => {
    breathsLeft = numberOfBreaths.value;
    breathsText.innerText = breathsLeft;
});

//Moviment of the circle while breathing
const growCircle = () => {
    circleProgress.classList.add("circle-grow");
    setTimeout(() => {
        circleProgress.classList.remove("circle-grow");
    }, 8000);
};

//Breathing instructions
const breathTextUpdate = () => {
    breathsLeft --;
    breathsText.innerText = breathsLeft;
    instructions.innerText = "Inhale";
    setTimeout(() => {
        instructions.innerText = "Hold Breath";
        setTimeout(() => {
            instructions.innerText = "Exhale";
        },4000);
    },4000);
};

//Breath App Function
const breathingApp = () => {
    const breathingAnimation = setInterval(() => {
        if (breathsLeft === 0) {
            clearInterval(breathingAnimation);
            instructions.innerText = "Breathing session completed. Click Start to begin another session!";
            start.classList.remove("start-inactive");
            breathsLeft = numberOfBreaths.value;
            breathsText.innerText = breathsLeft;
            return;
        }
        growCircle();
        breathTextUpdate();
    }, 12000);
};

//Start Breathing
start.addEventListener('click', () => {
    start.classList.add("button-inactive");
    instructions.innerText = "Get relaxed, and ready to begin breathing";
    setTimeout(() => {
        instructions.innerText = "Breathing is about to begin...";
        setTimeout(() => {
          breathingApp();
          growCircle();
          breathTextUpdate();
        },2000);
    },2000);
});