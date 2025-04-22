<script>
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { get } from 'svelte/store';

  const params = get(page).url.searchParams;
  const amount = params.get("amount") || "10";
  const category = params.get("category") || "19";
  const difficulty = params.get("difficulty") || "easy";
  const type = params.get("type") || "multiple";
  const scoreKey = `highscore-${category}-${difficulty}-${type}`;
  
  let valgtKategori = "";
  let questions = [];
  let index = 0;
  let score = 0;
  let highscore = 0;
  let selected = '';
  let feedback = false;
  let showResult = false;
  let loading = true;
  let error = false;


  const decode = (str) => {
    const el = document.createElement("textarea");
    el.innerHTML = str;
    return el.value;
  };

  const shuffle = (arr) => [...arr].sort(() => Math.random() - 0.5);

  onMount(async () => {
  try {
    const url = `https://opentdb.com/api.php?amount=${amount}&category=${category}&difficulty=${difficulty}&type=${type}`;
    const res = await fetch(url);
    const data = await res.json();

    // Hent kategori-navn fra API
    try {
      const katRes = await fetch("https://opentdb.com/api_category.php");
      const katData = await katRes.json();
      const kategori = katData.trivia_categories.find(k => k.id.toString() === category);
      valgtKategori = kategori ? kategori.name : `Kategori ${category}`;
    } catch (e) {
      valgtKategori = `Kategori ${category}`;
    }

    questions = data.results.map(q => ({
      question: decode(q.question),
      correct: decode(q.correct_answer),
      answers: shuffle([decode(q.correct_answer), ...q.incorrect_answers.map(decode)])
    }));

    const savedHighscore = localStorage.getItem(scoreKey);
    highscore = savedHighscore ? parseInt(savedHighscore) : 0;

  } catch {
    error = true;
  } finally {
    loading = false;
  }
});


  function answer(ans) {
    if (feedback) return;
    selected = ans;
    feedback = true;
    if (ans === questions[index].correct) score++;

    setTimeout(() => {
      selected = '';
      feedback = false;
      index++;
      if (index >= questions.length) {
        showResult = true;

        // Oppdater highscore hvis du har slått den
        if (score > highscore) {
          highscore = score;
          localStorage.setItem(scoreKey, score);
        }

        localStorage.setItem("lastScore", score);
      }

    }, 1200);
  }
</script>

{#if loading}
  <main><p>Laster spørsmål...</p></main>
{:else if error}
  <main><p>⚠️ Klarte ikke å hente spørsmål. Prøv igjen.</p></main>
{:else if showResult}
  <main>
    <h2>Resultat</h2>
    <p>Kategori: <strong>{valgtKategori}</strong></p>
    <p>Du fikk <strong>{score}</strong> av {questions.length} riktige</p>
    <p>Sist lagrede score: {localStorage.getItem("lastScore")}</p>
    <p>Høyeste score (for denne quizen): <strong>{highscore}</strong></p>    
    <div class="result-buttons">
      <a href="/prosjekt/trivia">Tilbake til hovedmeny</a>
      <a href="/prosjekt/trivia/poeng_oversikt">Se poengoversikt</a>
    </div>
    
  </main>
{:else if questions.length > 0}
  <main>
    <h2>{valgtKategori}</h2>
    <p>Spørsmål {index + 1} av {questions.length}</p>
    <p>{@html questions[index].question}</p>

    <div class="answers">
      {#each questions[index].answers as ans}
        <button
          class:selected={selected === ans}
          class:correct={feedback && ans === questions[index].correct}
          class:wrong={feedback && selected === ans && ans !== questions[index].correct}
          on:click={() => answer(ans)}
          disabled={feedback}
        >
          {ans}
        </button>
      {/each}
    </div>

    {#if feedback}
      <p class="feedback">
        {selected === questions[index].correct
          ? "✅ Riktig!"
          : `❌ Feil! Riktig svar var: ${questions[index].correct}`}
      </p>
    {/if}
  </main>
{/if}

<style>
  main {
    max-width: 600px;
    margin: auto;
    padding: 2rem;
    text-align: center;
  }

  .answers {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin: 1.5rem 0;
  }

  button {
    padding: 1rem;
    font-size: 1rem;
    border-radius: 8px;
    border: 2px solid transparent;
    background-color: #f0f0f0;
    cursor: pointer;
    transition: 0.2s;
  }

  button:hover {
    background-color: #e0e0e0;
  }

  button.correct {
    background-color: #c7f9cc;
    border-color: #2d6a4f;
  }

  button.wrong {
    background-color: #ffccd5;
    border-color: #c9184a;
  }

  button:disabled {
    cursor: not-allowed;
    opacity: 0.8;
  }

  .feedback {
    margin-top: 1rem;
    font-weight: bold;
  }
  .result-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 2rem;
}

.result-buttons a {
  background-color: #0070f3;
  color: white;
  padding: 1rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
}

.result-buttons a:hover {
  background-color: #0059c1;
}
</style>
