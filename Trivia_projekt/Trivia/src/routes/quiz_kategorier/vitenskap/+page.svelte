<script>
  const vitenskapQuiz = [
    { navn: "Vitenskap og natur", id: 17 },
    { navn: "Datavitenskap", id: 18 },
    { navn: "Matematikk", id: 19 }
  ];
</script>

<main>
  <a href="/valg_side" class="pil-tilbake">⬅</a>
  <div class="container">
    <h1>Vitenskap</h1>
    <p>Velg en quiz:</p>

    <div class="quiz-valg">
      {#each vitenskapQuiz as quiz}
        <a href={`/kategori/${quiz.id}`}>
          <button>{quiz.navn}</button>
        </a>
      {/each}
    </div>

    <div class="valg-knapper">
      <a href="/">
        <button class="tilbake-knapp">Tilbake til hovedmeny</button>
      </a>
      <a href="/poeng_oversikt">
        <button class="highscore-knapp">Se highscores</button>
      </a>
    </div>
  </div>
</main>

<style>
  :global(html, body) {
    height: 100%;
    margin: 0;
    background: linear-gradient(to bottom right, #1e3a8a, #0f172a);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  main {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: stretch;
    padding: 0;
  }

  .container {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background-color: #0f172a;
    border: 10px solid white;
    border-radius: 5px;
    box-shadow: 0 0 30px white;
    padding: 3rem 2rem;
    max-width: 500px;
    width: 100%;
    color: white;
    text-align: center;
  }

  h1 {
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
  }

  p {
    font-size: 1.2rem;
    color: #cbd5e1;
    margin-bottom: 2rem;
  }

  .quiz-valg {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
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

  .valg-knapper {
    display: flex;
    gap: 1rem;
    margin-top: 3rem;
    flex-wrap: wrap;
    justify-content: center;
  }

  .pil-tilbake {
    position: absolute;
    top:  1rem;
    left: 1rem;
    font-size: 1.5rem;
    text-decoration: none;
    color: white;
    background-color: #203565;
    padding: 0.2rem 0.8rem;
    border: 2px solid white;
    border-radius: 8px;
    cursor: pointer;
    box-shadow: 0 0 10px white;
    transition: background-color 0.2s ease, transform 0.2s ease;
    z-index: 10;
  }

  .pil-tilbake:hover {
    background-color: #081220;
    transform: scale(1.05);
  }

  .highscore-knapp {
    background-color: #00ff08d8;
  }

  .highscore-knapp:hover {
    background-color: #388e3c;
  }

  .tilbake-knapp {
    background-color: #ff0000d4;
  }

  .tilbake-knapp:hover {
    background-color: #757575;
  }
</style>
