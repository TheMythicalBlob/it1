<main>
  <div class="container">
    <h1>Velkommen til Trivia-nettsiden!</h1>
    <p>Hva vil du gjøre?</p>

    <div class="valg">
      <a href="/valg_side">
        <button class="quiz-knapp">Quizer</button>
      </a>
      <a href="/poeng_oversikt">
        <button class="score-knapp">Se highscores</button>
      </a>
    </div>
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
  }

  .container {
    background-color: rgba(0, 0, 0,);
    padding: 3rem 2rem;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
    text-align: center;
    width: 90%;
    max-width: 600px;
  }

  h1 {
    font-size: 2.2rem;
    margin-bottom: 1rem;
    color: #fff;
  }

  p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    color: #d1d5db;
  }

  .valg {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    justify-content: center;
  }

  a {
    text-decoration: none;
  }

  .quiz-knapp,
  .score-knapp {
    padding: 1rem 2rem;
    font-size: 1.1rem;
    border: none;
    border-radius: 10px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    transition: background-color 0.3s ease, transform 0.2s ease;
  }

  .quiz-knapp {
    background-color: #2563eb;
  }

  .quiz-knapp:hover {
    background-color: #1d4ed8;
    transform: translateY(-2px);
  }

  .score-knapp {
    background-color: #00ff08d8;
  }

  .score-knapp:hover {
    background-color: #388e3c;
    transform: translateY(-2px);
  }
</style>
