<script>
  import { page } from '$app/stores'
  import { onMount } from 'svelte'
  import { get } from 'svelte/store'

  const parametere = get(page).url.searchParams
  const antall = parametere.get("amount")
  const kategoriId = parametere.get("category")
  const vanskelighetsgrad = parametere.get("difficulty")
  const typeSvar = parametere.get("type")
  const scoreNokkel = `highscore-${kategoriId}-${vanskelighetsgrad}-${typeSvar}`

  let valgtKategori = ""
  let spørsmål = []
  let indeks = 0
  let poeng = 0
  let hoyestePoeng = 0
  let valgtSvar = ''
  let visTilbakemelding = false
  let visResultat = false
  let laster = true

  const dekod = (tekst) => {
    const el = document.createElement("textarea")
    el.innerHTML = tekst
    return el.value
  }

  const stokk = (arr) => [...arr].sort(() => Math.random() - 0.5)

  onMount(async () => {
  try {
    const url = `https://opentdb.com/api.php?amount=${antall}&category=${kategoriId}&difficulty=${vanskelighetsgrad}&type=${typeSvar}`
    const res = await fetch(url)
    const data = await res.json()

    if (!data.results || data.results.length === 0) {
      error = true
      return
    }

    const katRes = await fetch("https://opentdb.com/api_category.php")
    const katData = await katRes.json()
    const kategori = katData.trivia_categories.find(k => k.id.toString() === kategoriId)
    valgtKategori = kategori?.name

    spørsmål = data.results.map(q => {
      const riktig = dekod(q.correct_answer)
      const gale = q.incorrect_answers.map(dekod)
      const svaralternativer = q.type === "boolean"
        ? stokk(["True", "False"])
        : stokk([riktig, ...gale])

      return {
        spørsmåltekst: dekod(q.question),
        riktig,
        svaralternativer
      }
    })

    const lagret = localStorage.getItem(scoreNokkel)
    hoyestePoeng = lagret ? parseInt(lagret) : 0

  } catch (e) {
    console.error("Feil under lasting av quiz:", e)
    error = true
  } finally {
    laster = false
  }
})

  const svar = (valg) => {
    if (visTilbakemelding) return
    valgtSvar = valg
    visTilbakemelding = true
    if (valg === spørsmål[indeks].riktig) poeng++

    setTimeout(() => {
      valgtSvar = ''
      visTilbakemelding = false
      indeks++
      if (indeks >= spørsmål.length) {
        visResultat = true
        if (poeng > hoyestePoeng) {
          hoyestePoeng = poeng
          localStorage.setItem(scoreNokkel, poeng)
        }
        localStorage.setItem("lastScore", poeng)
      }
    }, 1200)
  }
</script>

{#if laster}
  <main><p>Laster spørsmål...</p></main>
{:else if visResultat}
  <main>
    <h2>Resultat</h2>
    <b>Kategori: {valgtKategori}</b>
    <b>Du fikk {poeng} av {spørsmål.length} riktige</b> <br> <br> <br>
    <b>Høyeste score (for denne quizen): {hoyestePoeng}</b>    
    <div class="result-buttons">
      <a href="/">Tilbake til hovedmeny</a>
      <a href="/poeng_oversikt">Se poengoversikt</a>
    </div>
  </main>
{:else if spørsmål.length > 0}
  <main>
    <h2>{valgtKategori}</h2>
    <p>Spørsmål {indeks + 1} av {spørsmål.length}</p>
    <p>{@html spørsmål[indeks].spørsmåltekst}</p>
  
    <div class="answers">
      {#each spørsmål[indeks].svaralternativer as alternativ}
        <button
          class:selected={valgtSvar === alternativ}
          class:correct={visTilbakemelding && alternativ === spørsmål[indeks].riktig}
          class:wrong={visTilbakemelding && valgtSvar === alternativ && alternativ !== spørsmål[indeks].riktig}
          on:click={() => svar(alternativ)}
          disabled={visTilbakemelding}
        >
          {alternativ}
        </button>
      {/each}
    </div>

    {#if visTilbakemelding}
      <p class="feedback">
        {valgtSvar === spørsmål[indeks].riktig
          ? "✅ Riktig!"
          : `❌ Feil! Riktig svar var: ${spørsmål[indeks].riktig}`}
      </p>
    {/if}
  </main>
{/if}

<style>
  main {
    max-width: 600px;
    margin: auto;
    padding: 2rem;
    text-align: center;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  }

  .answers {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin: 1.5rem 0;
  }

  button {
    padding: 1rem;
    font-size: 1rem;
    border-radius: 8px;
    border: 2px solid transparent;
    background-color: #f0f0f0;
    cursor: pointer;
    transition: 0.2s;
  }

  button:hover {
    background-color: #e0e0e0;
  }

  button.correct {
    background-color: #c7f9cc;
    border-color: #2d6a4f;
  }

  button.wrong {
    background-color: #ffccd5;
    border-color: #c9184a;
  }

  button:disabled {
    cursor: not-allowed;
    opacity: 0.8;
  }

  .feedback {
    margin-top: 1rem;
    font-weight: bold;
  }
  .result-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 2rem;
}

.result-buttons a {
  background-color: #0070f3;
  color: white;
  padding: 1rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
}

.result-buttons a:hover {
  background-color: #0059c1;
}
</style>
