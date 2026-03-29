const quiz = [
{
question: "Where was this photo taken?",
image: "images/photo1.jpg",
answers: ["Our first date", "Beach trip", "Birthday party"],
correct: 1
},

{
question: "Which trip was this?",
image: "images/photo2.jpg",
answers: ["Goa", "Mumbai", "Pune"],
correct: 0
},

{
question: "What was happening here?",
image: "images/photo3.jpg",
answers: ["Movie night", "Dinner date", "Festival"],
correct: 2
}
];

let currentQuestion = 0;
let score = 0;
let selectedAnswerIndex = null;

const questionEl = document.getElementById("question");
const imageEl = document.getElementById("question-image");
const answersEl = document.getElementById("answers");
const nextBtn = document.getElementById("next-btn");
const resultEl = document.getElementById("result");

function loadQuestion(){

    let q = quiz[currentQuestion];

    questionEl.textContent = q.question;
    imageEl.src = q.image;

    answersEl.innerHTML = "";
    selectedAnswerIndex = null;

    q.answers.forEach((answer,index)=>{
        let btn = document.createElement("button");
        btn.textContent = answer;

        btn.onclick = ()=>{
            selectedAnswerIndex = index;

            const allBtns = answersEl.querySelectorAll("button");
            allBtns.forEach((b, i)=>{
                b.classList.toggle("selected", i === index);
            });
        };

        answersEl.appendChild(btn);
    });
}

nextBtn.onclick = ()=>{
    const q = quiz[currentQuestion];

    if (selectedAnswerIndex !== null && selectedAnswerIndex === q.correct) {
        score++;
    }

    currentQuestion++;

    if(currentQuestion < quiz.length){
        loadQuestion();
    }
    else{
        questionEl.style.display = "none";
        imageEl.style.display = "none";
        answersEl.style.display = "none";
        nextBtn.style.display = "none";

        resultEl.innerHTML = "You scored " + score + "/" + quiz.length +
        "<br><br> You passed the girlfriend test 💖";
    }
};

loadQuestion();