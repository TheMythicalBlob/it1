<script>
    const vitenskapQuiz = [
      { navn: "Vitenskap og natur", id: 17 },
      { navn: "Datavitenskap", id: 18 },
      { navn: "Matematikk", id: 19 }
    ]
  </script>
  
  <main>
    <h1>Vitenskap</h1>
    <p>Velg en quiz:</p>
  
    <div class="quiz-valg">
      {#each vitenskapQuiz as quiz}
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
  