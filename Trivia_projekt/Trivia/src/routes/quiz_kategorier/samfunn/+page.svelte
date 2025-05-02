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
    <a href="/valg_side" class="pil-tilbake">⬅</a>
    <div class="container">
      <h1>Samfunn og annet</h1>
      <p>Velg en quiz:</p>
  
      <div class="quiz-valg">
        {#each samfunnQuiz as quiz}
          <a href={`/kategori/${quiz.id}`}>
            <button>{quiz.navn}</button>
          </a>
        {/each}
      </div> <br>
  
      <div class="valg-knapper">
      <a href="/">
        <button class="tilbake-knapp">Tilbake til hovedmeny</button>
      </a>
        <a href="/poeng_oversikt">
          <button class="highscore-knapp">Se highscores</button>
        </a>
    </div>
  </main>
  
  
<style>
  :global(body) {
    margin: 0;
    padding: 0;
    background: linear-gradient(to bottom right, #1e3a8a, #0f172a);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: white;
  }

  main {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
  }

  .container {
    background-color: rgba(15, 23, 42, 0.9);
    padding: 2rem;
    border: 6px solid white;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.4);
    max-width: 500px;
    width: 100%;
    text-align: center;
  }

  h1 {
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
  }

  p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    color: #cbd5e1;
  }

  .quiz-valg {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    justify-content: center;
    margin-top: 1rem;
  }

  button {
    padding: 1rem 2rem;
    font-size: 1.1rem;
    background-color: #0070f3;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    transition: background-color 0.3s ease, transform 0.2s ease;
  }

  button:hover {
    background-color: #0059c1;
    transform: translateY(-2px);
  }
  .valg-knapper {
    display: flex;
    gap: 1rem;
    margin-top: 3rem;
    flex-wrap: wrap;
    justify-content: center;
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
      background-color: #388e3c;
  }

  a {
    display: block;
    margin-top: 2.5rem;
    font-weight: bold;
    color: #4fc3f7;
    text-align: center;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  </style>
  