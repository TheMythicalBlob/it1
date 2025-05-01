<script>
  const hovedkategorier = [
    { navn: "Samfunn", sti: "samfunn" },
    { navn: "Sport og spill", sti: "sport og spill" },
    { navn: "Underholdning", sti: "underholdning" },
    { navn: "Vitenskap", sti: "vitenskap" },
    { navn: "Alle quizer", sti: "alle_quizer" }
  ];
</script>

<main>
    <div class="container">
      <h1>Velg en quizkategori</h1>
      <p>Trykk på en kategori for å se hvilke quizer som finnes</p>
  
      <div class="kategorier-container">
        <div class="kategori-firkant">
          {#each hovedkategorier as kategori (kategori.sti)}
            {#if kategori.sti !== "alle_quizer"}
              <a href={`/quiz_kategorier/${kategori.sti.replace(/\s/g, "%20")}`} class="kategori-knapp">
                {kategori.navn}
              </a>
            {/if}
          {/each}
        </div>
  
        <a href="/quiz_kategorier/alle_quizer" class="alle-knapp">
          Alle quizer
        </a>
      </div>
  
      <div class="valg-knapper">
        <a href="/">
          <button class="tilbake-knapp">Tilbake til hovedmeny</button>
        </a>
        <a href="/poeng_oversikt">
          <button class="highscore-knapp">Se highscores</button>
        </a>

      </div>
    </div>
  </main>

<style>
:global(html, body) {
  height: 100%;
  margin: 0;
  padding: 0;
  background: linear-gradient(to bottom right, #1e3a8a, #0f172a);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  overflow: auto;
}

main {
  min-height: 100vh;
  display: flex;
  text-align: center;
  justify-content: center;
  align-items: stretch;
  padding: 0;
}

.container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: #0f172a;
  border: 10px solid white;
  border-radius: 5px;
  box-shadow: 0 0 30px white;
  padding: 3rem 2rem;
  max-width: 500px;
  width: 100%;
}


h1 {
  font-size: 2.2rem;
  color: white;
  margin-bottom: 0.5rem;
}

p {
  font-size: 1.2rem;
  color: #cbd5e1;
  margin-bottom: 2rem;
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

.kategori-knapp {
  padding: 1rem;
  background-color: #ff9800;
  color: white;
  border-radius: 10px;
  text-decoration: none;
  font-weight: bold;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  transition: background-color 0.3s ease, transform 0.2s ease;
  text-align: center;
  min-width: 200px;
}

.kategori-knapp:hover {
  background-color: #e68900;
  transform: translateY(-2px);
}

.alle-knapp {
  padding: 1rem 2rem;
  background-color: #2196f3;
  color: white;
  border-radius: 10px;
  font-weight: bold;
  text-decoration: none;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.alle-knapp:hover {
  background-color: #1976d2;
  transform: translateY(-2px);
}

.valg-knapper {
  display: flex;
  gap: 1rem;
  margin-top: 3rem;
  flex-wrap: wrap;
  justify-content: center;
}

.highscore-knapp {
  padding: 1rem 2rem;
  background-color: #00ff08d8;
  color: white;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.highscore-knapp:hover {
  background-color: #388e3c;
}

.tilbake-knapp {
  padding: 1rem 2rem;
  background-color: #ff0000d4;
  color: white;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.tilbake-knapp:hover {
  background-color: #b30000;
}
</style>