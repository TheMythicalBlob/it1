<script>
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  
  // Hent valgt kategori-id fra URL (f.eks. 19 for Matematikk)
  let categoryId = $page.params.navn;
  let amount = 10;
  let difficulty = "easy";
  let type = "multiple";
  let kategoriTekst = "";

onMount(async () => {
  try {
    const res = await fetch("https://opentdb.com/api_category.php");
    const data = await res.json();
    const kategori = data.trivia_categories.find(k => k.id.toString() === categoryId);
    kategoriTekst = kategori ? kategori.name : `Kategori ${categoryId}`;
  } catch {
    kategoriTekst = `Kategori ${categoryId}`;
  }
});


  function startQuiz() {
    const url = `/prosjekt/trivia/trivia_kategorier?amount=${amount}&category=${categoryId}&difficulty=${difficulty}&type=${type}`;
    window.location.href = url;
  }
</script>

<main>
  <h1>{kategoriTekst}</h1>
  <p>Velg dine quiz innstillinger:</p>

  <label>
    Antall spørsmål:
    <input type="number" min="1" max="50" bind:value={amount}>
  </label>

  <label>
    Vanskelighetsgrad:
    <select bind:value={difficulty}>
      <option value="easy">Lett</option>
      <option value="medium">Middels</option>
      <option value="hard">Vanskelig</option>
    </select>
  </label>

  <label>
    Type spørsmål:
    <select bind:value={type}>
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
    background-color: #fefefe;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
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
