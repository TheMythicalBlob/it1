<script>
  import { onMount } from 'svelte';

  let highscores = [];
  let kategorier = {}; // maps category id -> name

  onMount(async () => {
    try {
      // Hent kategorier
      const res = await fetch("https://opentdb.com/api_category.php");
      const data = await res.json();
      for (const kat of data.trivia_categories) {
        kategorier[kat.id.toString()] = kat.name; // sikre key er string
      }

      // Hent highscores fra localStorage
      const tempScores = [];
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith("highscore-")) {
          const parts = key.split("-");
          const category = parts[1];
          const difficulty = parts[2];
          const type = parts[3];
          const score = parseInt(localStorage.getItem(key));

          tempScores.push({
            kategori: kategorier[category] || `Kategori ${category}`,
            category,
            difficulty,
            type,
            score
          });
        }
      }

      highscores = tempScores;
    } catch (e) {
      console.error("Klarte ikke å hente poengoversikt:", e);
    }
  });
</script>

<main>
  <h1>Poengoversikt</h1>

  {#if highscores.length > 0}
    <table>
      <thead>
        <tr>
          <th>Kategori</th>
          <th>Vanskelighetsgrad</th>
          <th>Type</th>
          <th>Poeng</th>
        </tr>
      </thead>
      <tbody>
        {#each highscores as h}
          <tr>
            <td>{h.kategori}</td>
            <td>{h.difficulty}</td>
            <td>{h.type === "multiple" ? "Flervalg" : "Sant/Usant"}</td>
            <td>{h.score}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  {:else}
    <p>Ingen lagrede highscores ennå.</p>
  {/if}

  <a href="/prosjekt/trivia">← Tilbake til meny</a>
</main>

<style>
  main {
    max-width: 800px;
    margin: auto;
    padding: 2rem;
  }

  h1 {
    text-align: center;
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
  }

  th {
    background-color: #f0f0f0;
  }

  a {
    display: block;
    text-align: center;
    text-decoration: none;
    font-weight: bold;
    margin-top: 1rem;
    color: #0070f3;
  }

  a:hover {
    text-decoration: underline;
  }
</style>
