<script>
  const hovedkategorier = [
    { navn: "Samfunn", sti: "samfunn" },
    { navn: "Sport og spill", sti: "sport og spill" },
    { navn: "Underholdning", sti: "underholdning" },
    { navn: "Vitenskap", sti: "vitenskap" },
    { navn: "Alle quizer", sti: "alle_quizer" }
  ]
</script>

<main>
  <a href="/" class="pil-tilbake">⬅</a>
  <div class="container">
    <h1>Velg en quizkategori</h1>
    <p>Trykk på en kategori for å se hvilke quizer som finnes</p>

    <div class="kategorier-container">
      <div class="kategori-firkant">
        {#each hovedkategorier.filter(k => k.sti !== "alle_quizer") as k}
          <a href={`/quiz_kategorier/${encodeURIComponent(k.sti)}`} class="kategori-knapp">
            {k.navn}
          </a>
        {/each}
      </div>

      <a href="/quiz_kategorier/alle_quizer" class="alle-knapp">Alle quizer</a>
    </div>

    <div class="valg-knapper">
      <a href="/"><button class="tilbake-knapp">Tilbake til hovedmeny</button></a>
      <a href="/poeng_oversikt"><button class="highscore-knapp">Se highscores</button></a>
    </div>
  </div>
</main>

<style>
:global(html, body) {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: auto;
  background: linear-gradient(to bottom right, #1e3a8a, #0f172a);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

main {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  text-align: center;
}

.container {
  background-color: #0f172a;
  color: white;
  border: 10px solid white;
  border-radius: 5px;
  box-shadow: 0 0 30px white;
  padding: 3rem 2rem;
  max-width: 500px;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

h1 {
  font-size: 2.2rem;
}

p {
  font-size: 1.2rem;
  color: #cbd5e1;
}

.kategorier-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.kategori-firkant {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.kategori-knapp,
.alle-knapp {
  padding: 1rem;
  color: white;
  font-weight: bold;
  text-decoration: none;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  transition: background-color 0.3s ease, transform 0.2s ease;
  text-align: center;
  min-width: 200px;
}

.kategori-knapp {
  background-color: #ff9800;
}
.kategori-knapp:hover {
  background-color: #e68900;
  transform: translateY(-2px);
}

.alle-knapp {
  background-color: #2196f3;
}
.alle-knapp:hover {
  background-color: #1976d2;
  transform: translateY(-2px);
}

.valg-knapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.highscore-knapp,
.tilbake-knapp {
  padding: 1rem 2rem;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.highscore-knapp {
  background-color: #00ff08d8;
}
.highscore-knapp:hover {
  background-color: #388e3c;
}

.tilbake-knapp {
  background-color: #ff0000d4;
}
.tilbake-knapp:hover {
  background-color: #b30000;
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
  }

  .pil-tilbake:hover {
    background-color: #081220;
    transform: scale(1.05);
  }
</style>