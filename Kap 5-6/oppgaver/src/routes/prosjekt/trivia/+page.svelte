<script>
  import { onMount } from 'svelte';

  let questions = [];
  let currentQuestionIndex = 0;
  let score = 0;
  let selectedAnswer = '';
  let showFeedback = false;
  let showResult = false;
  let loading = true;
  let fetchFailed = false;

  function decode(str) {
    const txt = document.createElement("textarea");
    txt.innerHTML = str;
    return txt.value;
  }

  function shuffle(array) {
    return [...array].sort(() => Math.random() - 0.5);
  }

  onMount(async () => {
    try {
      const res = await fetch("https://opentdb.com/api.php?amount=10&category=19&difficulty=easy&type=multiple");
      const data = await res.json();
      questions = data.results.map(q => ({
        question: decode(q.question),
        correct: decode(q.correct_answer),
        answers: shuffle([decode(q.correct_answer), ...q.incorrect_answers.map(decode)])
      }));
    } catch (err) {
      console.error("Feil ved henting av spørsmål:", err);
      fetchFailed = true;
    } finally {
      loading = false;
    }
  });

  function handleAnswer(answer) {
    if (showFeedback) return;

    selectedAnswer = answer;
    showFeedback = true;

    if (answer === questions[currentQuestionIndex].correct) {
      score += 1;
    }

    setTimeout(() => {
      selectedAnswer = '';
      showFeedback = false;
      currentQuestionIndex++;

      if (currentQuestionIndex >= questions.length) {
        showResult = true;
        localStorage.setItem("lastScore", score);
      }
    }, 1500);
  }
</script>

{#if loading}
  <p>Laster spørsmål...</p>
{:else if fetchFailed}
  <p>⚠️ Klarte ikke å hente spørsmål fra API.</p>
{:else if showResult}
  <main>
    <h2>Resultat</h2>
    <p>Du fikk {score} av {questions.length} riktige!</p>
    <p>Sist lagrede score: {localStorage.getItem("lastScore")}</p>
    <a href="/">Prøv igjen</a>
  </main>
{:else if questions.length > 0}
  <main>
    <h2>Spørsmål {currentQuestionIndex + 1} av {questions.length}</h2>
    <p>{@html questions[currentQuestionIndex].question}</p>

    <ul>
      {#each questions[currentQuestionIndex].answers as answer}
        <li>
          <button
            class:selected={selectedAnswer === answer}
            on:click={() => handleAnswer(answer)}
            disabled={showFeedback}
            class:selectedCorrect={showFeedback && answer === questions[currentQuestionIndex].correct}
            class:selectedWrong={showFeedback && selectedAnswer === answer && answer !== questions[currentQuestionIndex].correct}
          >
            {answer}
          </button>
        </li>
      {/each}
    </ul>

    {#if showFeedback}
      <p>
        {selectedAnswer === questions[currentQuestionIndex].correct
          ? "✅ Riktig!"
          : `❌ Feil! Riktig svar var: ${questions[currentQuestionIndex].correct}`}
      </p>
    {/if}
  </main>
{/if}
