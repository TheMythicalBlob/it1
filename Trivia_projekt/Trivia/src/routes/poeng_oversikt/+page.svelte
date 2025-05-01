<script>
  import { onMount } from 'svelte';

  let highscores = [];
  let kategorier = [];

  // Hent highscores og kategori-navn
  onMount(async () => {
    try {
      const res = await fetch("https://opentdb.com/api_category.php");
      const data = await res.json();
      for (const kat of data.trivia_categories) {
        kategorier[kat.id.toString()] = kat.name;
      }

      oppdaterHighscores();
    } catch (error) {
      console.error("Klarte ikke å hente poengoversikt:", error);
    }
  });

  function oppdaterHighscores() {
    const temp = [];
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key && key.startsWith("highscore-")) {
        const [_, category, difficulty, type] = key.split("-");
        const score = parseInt(localStorage.getItem(key));

        temp.push({
          key,
          kategori: kategorier[category] || `Kategori ${category}`,
          difficulty,
          type,
          score
        });
      }
    }
    highscores = temp.sort((a, b) => b.score - a.score);
  }

  function slettHighscore(key) {
    localStorage.removeItem(key);
    oppdaterHighscores();
  }
</script>

<main>
  <div class="container">
    <h1>Highscore oversikt</h1>

    {#if highscores.length > 0}
      <table>
        <thead>
          <tr>
            <th>Kategori</th>
            <th>Vanskelighetsgrad</th>
            <th>Type</th>
            <th>Poeng</th>
            <th>Slett</th>
          </tr>
        </thead>
        <tbody>
          {#each highscores as h}
            <tr>
              <td>{h.kategori}</td>
              <td>{h.difficulty}</td>
              <td>{h.type === "multiple" ? "Flervalg" : "Sant/Usant"}</td>
              <td>{h.score}</td>
              <td>
                <button class="slett" on:click={() => slettHighscore(h.key)}>🗑</button>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    {:else}
      <p>Ingen lagrede highscores ennå.</p>
    {/if}

    <div class="valg-knapper">
      <a href="/">
        <button class="tilbake-knapp">Tilbake til hovedmeny</button>
      </a>
    </div>
  </div>
</main>

<style>
  main {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 3rem 1rem;
    min-height: 100vh;
  }

  .container {
    background-color: #0f172a;
    border: 10px solid white;
    border-radius: 5px;
    box-shadow: 0 0 30px white;
    padding: 2rem;
    width: 100%;
    max-width: 800px;
    color: white;
    text-align: center;
  }

  h1 {
    margin-bottom: 2rem;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 2rem;
  }

  th, td {
    border: 1px solid #ccc;
    padding: 0.8rem;
    text-align: center;
    background-color: #1e293b;
  }

  th {
    background-color: #334155;
  }

  .slett {
    background-color: #c9184a;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
    border-radius: 5px;
  }

  .slett:hover {
    background-color: #a0113b;
  }

  .valg-knapper {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
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
    background-color: #b30000 ;
  }
</style>
