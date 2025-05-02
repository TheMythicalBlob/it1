<script>
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import { get } from 'svelte/store';

  const params = get(page).url.searchParams;
  const antall = +params.get("amount") || 10;
  const kategoriId = params.get("category");
  const vanskelighetsgrad = params.get("difficulty");
  const typeSvar = params.get("type");
  const scoreNokkel = `highscore-${kategoriId}-${vanskelighetsgrad}-${typeSvar}`;
  const maxNokkel = `maxscore-${kategoriId}-${vanskelighetsgrad}-${typeSvar}`;

  let valgtKategori = "", spørsmål = [], indeks = 0, poeng = 0, hoyestePoeng = 0;
  let valgtSvar = '', visTilbakemelding = false, visResultat = false, laster = true, error = null;

  const dekod = t => {
    const el = document.createElement("textarea");
    el.innerHTML = t;
    return el.value;
  };

  const stokk = arr => [...arr].sort(() => Math.random() - 0.5);

  onMount(async () => {
    try {
      const res = await fetch(`https://opentdb.com/api.php?amount=${antall}&category=${kategoriId}&difficulty=${vanskelighetsgrad}&type=${typeSvar}`);
      const data = await res.json();
      if (!data.results?.length) throw new Error("Ingen spørsmål funnet");

      const katRes = await fetch("https://opentdb.com/api_category.php");
      const katData = await katRes.json();
      valgtKategori = katData.trivia_categories.find(k => k.id == kategoriId)?.name || `Kategori ${kategoriId}`;

      spørsmål = data.results.map(q => {
        const riktig = dekod(q.correct_answer);
        const gale = q.incorrect_answers.map(dekod);
        return {
          spørsmåltekst: dekod(q.question),
          riktig,
          svaralternativer: q.type === "boolean" ? ["True", "False"] : stokk([riktig, ...gale])
        };
      });

      hoyestePoeng = +localStorage.getItem(scoreNokkel) || 0;
    } catch (e) {
      console.error("Feil:", e);
      error = e.message;
    } finally {
      laster = false;
    }
  });

  const svar = valg => {
    if (visTilbakemelding) return;
    valgtSvar = valg;
    visTilbakemelding = true;
    if (valg === spørsmål[indeks].riktig) poeng++;

    setTimeout(() => {
      valgtSvar = '';
      visTilbakemelding = false;
      indeks++;
      if (indeks >= spørsmål.length) {
        visResultat = true;

        const prosent = (poeng / spørsmål.length) * 100;
        const lagretPoeng = +localStorage.getItem(scoreNokkel) || 0;
        const lagretMaks = +localStorage.getItem(maxNokkel) || 0;
        const lagretProsent = lagretMaks ? (lagretPoeng / lagretMaks) * 100 : -1;

        if (lagretProsent === -1 || prosent > lagretProsent) {
          localStorage.setItem(scoreNokkel, poeng);
          localStorage.setItem(maxNokkel, spørsmål.length);
        }

        localStorage.setItem("lastScore", poeng);
      }
    }, 1200);
  };
</script>

{#if laster}
  <main><p>Laster spørsmål...</p></main>

{:else if error}
  <main>
    <p class="feilmelding">{error}</p>
    <a href={`/kategori/${kategoriId}`}><button>Gå tilbake og velg færre spørsmål</button></a>
  </main>

{:else if visResultat}
  <main>
    <h2>Resultat</h2>
    <b>Kategori: {valgtKategori}</b>
    <b>Du fikk {poeng} av {spørsmål.length} riktige</b><br><br>
    <b>Høyeste score: {hoyestePoeng}</b>
    <div class="result-buttons">
      <a href="/">Tilbake til hovedmeny</a>
      <a href="/poeng_oversikt">Se poengoversikt</a>
    </div>
  </main>

{:else}
  <main>
    <button class="pil-tilbake" on:click={() => history.back()}>⬅</button>
    <h2>{valgtKategori}</h2>
    <p>Spørsmål {indeks + 1} av {spørsmål.length}</p>
    <p>{@html spørsmål[indeks].spørsmåltekst}</p>

    <div class="answers">
      {#each spørsmål[indeks].svaralternativer as alt}
        <button
          class:selected={valgtSvar === alt}
          class:correct={visTilbakemelding && alt === spørsmål[indeks].riktig}
          class:wrong={visTilbakemelding && valgtSvar === alt && alt !== spørsmål[indeks].riktig}
          on:click={() => svar(alt)}
          disabled={visTilbakemelding}
        >
          {alt}
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
:global(body) {
  background: linear-gradient(to bottom right, #1e3a8a, #0f172a);
  margin: 0;
  padding: 0;
}

main {
  background-color: #0f172a;
  max-width: 700px;
  margin: auto;
  padding: 2rem;
  color: white;
  border: 8px solid white;
  border-radius: 10px;
  box-shadow: 0 0 25px white;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-align: center;
}

h2 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

p {
  margin: 0.5rem 0 1rem;
  font-size: 1.1rem;
}

.answers {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 2rem 0;
}

button {
  padding: 1rem;
  font-size: 1.1rem;
  border-radius: 10px;
  border: 2px solid transparent;
  background-color: #354969;
  color: white;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.1s ease;
}

button:hover {
  background-color: #334155;
  transform: scale(1.02);
}
  
button.correct {
  background-color: #22c55e;
  border-color: #16a34a;
}

button.wrong {
  background-color: #ef4444;
  border-color: #b91c1c;
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.9;
}

.feedback {
  margin-top: 1rem;
  font-weight: bold;
  font-size: 1.2rem;
  color: #facc15;
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

.feilmelding {
  background-color: #2b2b2b;
  padding: 1rem;
  border-radius: 8px;
  color: #f87171;
  margin-bottom: 1rem;
}

.pil-tilbake {
  position: absolute;
  top: 1rem;
  left: 1rem;
  font-size: 1.5rem;
  background-color: #203565;
  padding: 0.2rem 0.8rem;
  border: 2px solid white;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 0 10px white;
  color: white;
  transition: background-color 0.2s ease, transform 0.2s ease;
  z-index: 10;
}

.pil-tilbake:hover {
  background-color: #081220;
  transform: scale(1.05);
}
</style>
