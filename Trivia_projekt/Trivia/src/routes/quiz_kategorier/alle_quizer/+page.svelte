<script>
  const samfunnQuiz = [
    { navn: "Geografi", id: 22 },
    { navn: "Historie", id: 23 },
    { navn: "Politikk", id: 24 },
    { navn: "Kunst", id: 25 },
    { navn: "Dyr", id: 27 },
    { navn: "Mythologi", id: 20 },
    { navn: "Sport", id: 21 },
    { navn: "Brettspill", id: 16 },
    { navn: "Videospill", id: 15 },
    { navn: "Bøker", id: 10 },
    { navn: "Film", id: 11 },
    { navn: "Musikk", id: 12 },
    { navn: "Musikaler og teater", id: 13 },
    { navn: "TV", id: 14 },
    { navn: "Vitenskap og natur", id: 17 },
    { navn: "Datavitenskap", id: 18 },
    { navn: "Matematikk", id: 19 }
  ];
</script>

<main>
  <a href="/valg_side" class="pil-tilbake">⬅</a>
  <div class="container">
    <h1>Alle quizene</h1>
    <p>Velg en quiz:</p>

    <div class="quiz-valg">
      {#each samfunnQuiz as quiz}
        <a href={`/kategori/${quiz.id}`}>
          <button>{quiz.navn}</button>
        </a>
      {/each}
    </div>

    <div class="valg-knapper">
      <a href="/"><button class="tilbake-knapp">Tilbake til hovedmeny</button></a>
      <a href="/poeng_oversikt"><button class="highscore-knapp">Se highscores</button></a>
    </div>
  </div>
</main>

<style>
  :global(html, body) {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(to bottom right, #1e3a8a, #0f172a);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  main {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
  }

  .container {
    background-color: #0f172a;
    border: 8px solid white;
    border-radius: 10px;
    box-shadow: 0 0 30px white;
    padding: 2.5rem;
    max-width: 700px;
    width: 100%;
    text-align: center;
    color: white;
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
    margin-bottom: 2.5rem;
  }

  .quiz-valg a button {
    padding: 1rem 1.5rem;
    font-size: 1rem;
    background-color: #0070f3;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    min-width: 140px;
    transition: background-color 0.2s;
  }

  .quiz-valg a button:hover {
    background-color: #0059c1;
  }

  .valg-knapper {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
  }

  .tilbake-knapp {
    padding: 1rem 2rem;
    background-color: #ff0000d4;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .tilbake-knapp:hover {
    background-color: #b30000;
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
    padding: 1rem 2rem;
    background-color: #00ff08d8;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .highscore-knapp:hover {
    background-color: #00cc06;
  }
</style>
