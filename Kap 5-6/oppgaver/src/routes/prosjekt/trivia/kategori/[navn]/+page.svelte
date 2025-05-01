<script>
  import { page } from '$app/stores'
  import { onMount } from 'svelte'

  let kategoriId = $page.params.navn
  let antall = 10
  let vanskelighetsgrad = "easy"
  let typeSvar = "multiple"
  let kategoriNavn = ""
  let feilmelding = ""

  // Hardkodet maks grenser (du kan endre selv hvis du vil senere)
  const maksPerKategori = {
    "24": { multiple: 4, boolean: 10 },  // Politikk
    "30": { multiple: 10, boolean: 10 }, // Gadgets
    "20": { multiple: 15, boolean: 15 }, // Mythologi
    "29": { multiple: 15, boolean: 15 }, // Tegneserier
    "28": { multiple: 15, boolean: 15 }, // Kjøretøy
    "13": { multiple: 15, boolean: 15 }, // Musikaler
    "26": { multiple: 15, boolean: 15 }, // Kjendiser
  }

  onMount(async () => {
    try {
      const res = await fetch("https://opentdb.com/api_category.php")
      const data = await res.json()
      const kategori = data.trivia_categories.find(k => k.id.toString() === kategoriId)
      kategoriNavn = kategori ? kategori.name : `Kategori ${kategoriId}`
    } catch {
      kategoriNavn = `Kategori ${kategoriId}`
    }
  })

  const startQuiz = () => {
    const url = `/prosjekt/trivia/trivia_kategorier?amount=${antall}&category=${kategoriId}&difficulty=${vanskelighetsgrad}&type=${typeSvar}`
    window.location.href = url
  }

  // Riktig maksgrenser basert på kategori og typeSvar
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
  <h1>{kategoriNavn}</h1>
  <p>Velg dine quiz-innstillinger:</p>

  <label>
    Antall spørsmål:
    <input type="number" min="1" max={typeSvar === "multiple" ? (maksPerKategori[kategoriId]?.multiple || 50) : (maksPerKategori[kategoriId]?.boolean || 50)} bind:value={antall} />
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

  <button on:click={startQuiz}>Start quiz</button>
</main>

<style>
  main {
    max-width: 500px;
    margin: auto;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  h1 {
    text-align: center;
    font-size: 1.5rem;
  }

  label {
    display: flex;
    flex-direction: column;
    font-weight: 500;
  }

  input, select {
    margin-top: 0.3rem;
    padding: 0.5rem;
    font-size: 1rem;
  }

  button {
    padding: 1rem;
    background-color: #0070f3;
    color: white;
    border: none;
    font-size: 1rem;
    border-radius: 8px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0059c1;
  }

  .feilmelding {
    color: #c9184a;
    font-weight: bold;
    background-color: #ffe5e9;
    padding: 0.75rem;
    border-radius: 8px;
    margin-top: -0.5rem;
  }
</style>
