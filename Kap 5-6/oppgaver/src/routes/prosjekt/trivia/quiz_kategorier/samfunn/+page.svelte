<script>
    const samfunnQuiz = [
      { navn: "Geografi", id: 22 },
      { navn: "Historie", id: 23 },
      { navn: "Politikk", id: 24 },
      { navn: "Kunst", id: 25 },
      { navn: "Dyr", id: 27 },
      { navn: "Mythologi", id: 20 }
    ]
  </script>
  
  <main>
    <h1>Samfunn og annet</h1>
    <p>Velg en quiz:</p>
  
    <div class="quiz-valg">
      {#each samfunnQuiz as quiz}
        <a href={`/prosjekt/trivia/kategori/${quiz.id}`}>
          <button>{quiz.navn}</button>
        </a>
      {/each}
    </div>
  
    <a href="/prosjekt/trivia">⬅ Tilbake</a>
  </main>
  
<style>
  main {
    text-align: center;
    padding: 2rem;
  }
  .quiz-valg {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
    margin-top: 2rem;
  }
  button {
    padding: 1rem 2rem;
    font-size: 1rem;
    background-color: #0070f3;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
  }
  button:hover {
    background-color: #0059c1;
  }
  a {
    display: block;
    margin-top: 2rem;
    font-weight: bold;
    color: #0070f3;
  }
</style>
  