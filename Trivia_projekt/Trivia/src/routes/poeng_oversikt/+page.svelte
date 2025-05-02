<script>
  import { onMount } from 'svelte'

  let highscores = []
  let kategorier = []

  // Hent highscores og kategori-navn
  onMount(async () => {
    try {
      const res = await fetch("https://opentdb.com/api_category.php")
      const data = await res.json()
      for (const kat of data.trivia_categories) {
        kategorier[kat.id.toString()] = kat.name
      }

      oppdaterHighscores()
    } catch (error) {
      console.error("Klarte ikke å hente poengoversikt:", error)
    }
  })

  const oppdaterHighscores = () => {
    const temp = []
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i)
      if (key && key.startsWith("highscore-")) {
        const [_, category, difficulty, type] = key.split("-")
        const score = parseInt(localStorage.getItem(key))
        const max = parseInt(localStorage.getItem(`maxscore-${category}-${difficulty}-${type}`)) || 10
        const prosent = (score / max) * 100

        temp.push({
          key,
          kategori: kategorier[category] || `Kategori ${category}`,
          difficulty,
          type,
          score,
          max,
          prosent
        })
      }
    }
    highscores = temp.sort((a, b) => b.prosent - a.prosent)
  }

  const slettHighscore = (key) => {
    localStorage.removeItem(key)
    const parts = key.split("-")
    const maxKey = `maxscore-${parts[1]}-${parts[2]}-${parts[3]}`
    localStorage.removeItem(maxKey)
    oppdaterHighscores()
  }

  const slettAlle = () => {
  const nøkler = []

  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i)
    if (key?.startsWith("highscore-") || key?.startsWith("maxscore-")) {
      nøkler.push(key)
    }
  }

  for (const key of nøkler) {
    localStorage.removeItem(key)
  }

  oppdaterHighscores();
}
</script>

<main>
  <button class="pil-tilbake" on:click={() => history.back()}>⬅</button>
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
              <td>{h.score} / {h.max}</td>
              <td><button class="slett" on:click={() => slettHighscore(h.key)}>🗑</button></td>
            </tr>
          {/each}
        </tbody>
      </table>
    {:else}
      <p>Ingen lagrede highscores ennå.</p>
    {/if}

    <div class="valg-knapper">
      <a href="/"><button class="hovedmeny-knapp">Tilbake til hovedmeny</button></a>
      <button class="slett-alle" on:click={slettAlle}>Slett alle</button>
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

  .slett, .slett-alle {
    background-color: #c9184a;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
    border-radius: 5px;
  }

  .slett:hover, .slett-alle:hover {
    background-color: #a0113b;
  }

  .valg-knapper {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .hovedmeny-knapp {
    padding: 0.8rem 1.2rem;
    background-color: #00ff08d8;
    border: none;
    color: white;
    border-radius: 8px;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
  }

  .hovedmeny-knapp:hover {
    background-color: #00cc00;
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
</style>
