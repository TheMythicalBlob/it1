<script>
  import { page } from '$app/stores'
  import { onMount } from 'svelte'

  let kategoriId = $page.params.navn
  let antall = 10
  let vanskelighetsgrad = "easy"
  let typeSvar = "multiple"
  let kategoriNavn = ""

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
</script>


<main>
  <h1>{kategoriNavn}</h1>
  <p>Velg dine quiz-innstillinger:</p>

  <label>
    Antall spørsmål:
    <input type="number" min="1" max="50" bind:value={antall} />
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
</style>
