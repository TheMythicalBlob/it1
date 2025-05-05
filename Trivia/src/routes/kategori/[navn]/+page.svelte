<script>
  import { page } from '$app/stores'
  import { onMount } from 'svelte'

  let kategoriId = $page.params.navn
  let antall = 10
  let vanskelighetsgrad = "easy"
  let typeSvar = "multiple"
  let kategoriNavn = ""
  let feilmelding = ""
  let laster = true

  const maksPerKategori = {
  "10": { multiple: 50, boolean: 50 },  // Bøker
  "11": { multiple: 50, boolean: 50 },  // Film
  "12": { multiple: 50, boolean: 50 },  // Musikk
  "13": { multiple: 15, boolean: 15 },  // Musikaler og teater
  "14": { multiple: 50, boolean: 50 },  // TV
  "15": { multiple: 50, boolean: 50 },  // Videospill
  "16": { multiple: 50, boolean: 50 },  // Brettspill
  "17": { multiple: 50, boolean: 50 },  // Vitenskap og natur
  "18": { multiple: 50, boolean: 50 },  // Datavitenskap
  "19": { multiple: 20, boolean: 50 },  // Matematikk
  "20": { multiple: 15, boolean: 15 },  // Mythologi
  "21": { multiple: 50, boolean: 50 },  // Sport
  "22": { multiple: 50, boolean: 50 },  // Geografi
  "23": { multiple: 50, boolean: 50 },  // Historie
  "24": { multiple: 4,  boolean: 10 },  // Politikk
  "25": { multiple: 50, boolean: 50 },  // Kunst
  "26": { multiple: 15, boolean: 15 },  // Kjendiser
  "27": { multiple: 50, boolean: 50 },  // Dyr
  "28": { multiple: 15, boolean: 15 },  // Kjøretøy
  "29": { multiple: 15, boolean: 15 },  // Tegneserier
  "30": { multiple: 10, boolean: 10 },  // Gadgets
  "31": { multiple: 50, boolean: 50 },  // Anime og manga
  "32": { multiple: 50, boolean: 50 }   // Tegneserier og animasjoner
}

  onMount(async () => {
    try {
      const res = await fetch("https://opentdb.com/api_category.php")
      const data = await res.json()
      const kategori = data.trivia_categories.find(k => k.id.toString() === kategoriId)
      kategoriNavn = kategori?.name || `Kategori ${kategoriId}`
    } finally {
      laster = false
    }
  })

  const startQuiz = () => {
    const grenser = maksPerKategori[kategoriId]
    const maks = grenser ? grenser[typeSvar] : 50
    const valgtAntall = Math.min(antall, maks)

    const url = `/trivia_kategorier?amount=${valgtAntall}&category=${kategoriId}&difficulty=${vanskelighetsgrad}&type=${typeSvar}`
    window.location.href = url
  }

  $: {
    const grenser = maksPerKategori[kategoriId]
    const maks = grenser ? grenser[typeSvar] : 50
    if (antall > maks) {
      feilmelding = `⚠️ Maks ${maks} spørsmål for denne kategorien og typen. Antall er satt til ${maks}.`
      antall = maks
    } else {
      feilmelding = ""
    }
  }
</script>

<main>
  <button class="pil-tilbake" on:click={() => history.back()}>⬅</button>
  <div class="container">
    {#if laster}
      <p>Laster kategori…</p>
    {:else}
      <h1>{kategoriNavn}</h1>
      <label>
        Antall spørsmål:
        <input type="number" min="1" bind:value={antall} />
      </label>
      <label>
        Vanskelighetsgrad:
        <select bind:value={vanskelighetsgrad}>
          <option value="easy">Lett</option>
          <option value="medium">Middels</option>
          <option value="hard">Vanskelig</option>
        </select>
      </label>
      <label>
        Type spørsmål:
        <select bind:value={typeSvar}>
          <option value="multiple">Flervalg</option>
          <option value="boolean">Sant / Usant</option>
        </select>
      </label>
      {#if feilmelding}
        <p class="feilmelding">{feilmelding}</p>
      {/if}
      <button class="start-knapp" on:click={startQuiz}>Start quiz</button>
      <div class="valg-knapper">
        <a href="/"><button class="tilbake-knapp">Tilbake til hovedmeny</button></a>
        <a href="/poeng_oversikt"><button class="highscore-knapp">Se highscores</button></a>
      </div>
    {/if}
  </div>
</main>

<style>
  :global(body) {
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
    border-radius: 12px;
    box-shadow: 0 0 30px white;
    padding: 2rem;
    width: 100%;
    max-width: 500px;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    color: white;
    text-align: center;
  }

  h1 {
    margin-bottom: 0.5rem;
    font-size: 2rem;
  }

  label {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    font-weight: bold;
    gap: 0.3rem;
    text-align: left;
  }

  input, select {
    width: 100%;
    padding: 0.6rem;
    border-radius: 6px;
    border: none;
    font-size: 1rem;
  }

  .start-knapp,
  .tilbake-knapp,
  .highscore-knapp {
    padding: 0.8rem 1.6rem;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
  }

  .start-knapp {
    background-color: #0070f3;
    color: white;
  }

  .start-knapp:hover {
    background-color: #0059c1;
  }

  .tilbake-knapp {
    background-color: #ff0000d4;
    color: white;
  }

  .tilbake-knapp:hover {
    background-color: #b30000;
  }

  .highscore-knapp {
    background-color: #00ff08d8;
    color: white;
  }

  .highscore-knapp:hover {
    background-color: #388e3c;
  }

  .feilmelding {
    color: #f87171;
    background-color: #2b2b2b;
    padding: 0.8rem;
    border-radius: 8px;
  }

  .valg-knapper {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
    margin-top: 1.5rem;
  }

  .pil-tilbake {
    position: absolute;
    top: 1rem;
    left: 1rem;
    font-size: 1.5rem;
    background-color: #203565;
    color: white;
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

