<script>
  import { page } from '$app/stores'
  import { onMount } from 'svelte'

  let kategoriId   = $page.params.navn
  let antall       = 10
  let vanskelighetsgrad = "easy"
  let typeSvar     = "multiple"
  let kategoriNavn = ""
  let feilmelding  = ""
  let laster       = true

  const maksPerKategori = {
    "10": { multiple: 50, boolean: 50 },
    "11": { multiple: 50, boolean: 50 },
    "12": { multiple: 50, boolean: 50 },
    "13": { multiple: 15, boolean: 15 },
    "14": { multiple: 50, boolean: 50 },
    "15": { multiple: 50, boolean: 50 },
    "16": { multiple: 50, boolean: 50 },
    "17": { multiple: 50, boolean: 50 },
    "18": { multiple: 50, boolean: 50 },
    "19": { multiple: 20, boolean: 50 },
    "20": { multiple: 15, boolean: 15 },
    "21": { multiple: 50, boolean: 50 },
    "22": { multiple: 50, boolean: 50 },
    "23": { multiple: 50, boolean: 50 },
    "24": { multiple: 4,  boolean: 10 },
    "25": { multiple: 50, boolean: 50 },
    "26": { multiple: 15, boolean: 15 },
    "27": { multiple: 50, boolean: 50 },
    "28": { multiple: 15, boolean: 15 },
    "29": { multiple: 15, boolean: 15 },
    "30": { multiple: 10, boolean: 10 },
    "31": { multiple: 50, boolean: 50 },
    "32": { multiple: 50, boolean: 50 }
  }

  onMount(async () => {
    try {
      const res = await fetch("https://opentdb.com/api_category.php")
      const data = await res.json()
      const kategori = data.trivia_categories.find(k => k.id.toString() === kategoriId)
      kategoriNavn = kategori ? kategori.name : `Kategori ${kategoriId}`
    } catch (e) {
      kategoriNavn = `Kategori ${kategoriId}`
      console.error("Feil under lasting av kategori:", e)
    } finally {
      laster = false
    }
  })

  const startQuiz = () => {
    const url = `/trivia_kategorier?amount=${antall}&category=${kategoriId}&difficulty=${vanskelighetsgrad}&type=${typeSvar}`
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
  <div class="container">
    {#if laster}
      <p class="lastetekst">Laster kategori…</p>
    {:else}
      <h1>{kategoriNavn}</h1>
      <p>Velg dine quiz-innstillinger:</p>

      <label>
        Antall spørsmål:
        <input
          type="number"
          min="1"
          max={typeSvar === "multiple"
            ? (maksPerKategori[kategoriId]?.multiple || 50)
            : (maksPerKategori[kategoriId]?.boolean  || 50)}
          bind:value={antall}
        />
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

      <!-- Her kommer de to nye knappene: -->
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
    text-align: center;
    color: white;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }

  p {
    margin-bottom: 1rem;
    color: #cbd5e1;
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

  .start-knapp {
    padding: 1rem;
    font-size: 1rem;
    background-color: #0070f3;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
  }

  .start-knapp:hover {
    background-color: #0059c1;
  }

  .feilmelding {
    color: #f87171;
    background-color: #2b2b2b;
    padding: 0.8rem;
    border-radius: 8px;
  }

  .lastetekst {
    color: #ccc;
  }

  .valg-knapper {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;
  }

  .highscore-knapp {
    padding: 0.8rem 1.6rem;
    background-color: #00ff08d8;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
  }

  .highscore-knapp:hover {
    background-color: #388e3c;
  }

  .tilbake-knapp {
    padding: 0.8rem 1.6rem;
    background-color: #ff0000d4;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
  }

  .tilbake-knapp:hover {
    background-color: #757575;
  }
</style>
