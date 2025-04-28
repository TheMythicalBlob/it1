<script>
    const kategorier = [
      { navn: "Matematikk", id: 19 },
      { navn: "Historie", id: 23 },
      { navn: "Datamaskin", id: 18 },
      { navn: "Geografi", id: 22 },
      { navn: "Filmer", id: 11 },
      { navn: "Videospill", id: 15 },
      { navn: "Dyr", id: 27},
      { navn: "Generell kunnskap", id: 9 },
      { navn: "Anime", id: 31 },
      { navn: "Mytologi", id: 20 },
      { navn: "Politikk", id: 24 }
    ];
  </script>
  
  <main>
    <h1>Velg kategori</h1>  
    <a href="/prosjekt/trivia/poeng_oversikt" class="stats-button">Se poengoversikt</a>
    <div class="grid">
      {#each kategorier as kat}
        <a href={`/prosjekt/trivia/kategori/${kat.id}`}>
          <button>{kat.navn}</button>
        </a>
      {/each}
    </div>
  </main>
  
  <style>
    main {
      padding: 1rem;
      text-align: center;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 1rem;
      margin-top: 2rem;
    }
    button {
      padding: 1rem;
      font-size: 1rem;
      border: none;
      border-radius: 10px;
      background-color: #6200ea;
      color: white;
      cursor: pointer;
      transition: 0.2s ease;
    }
    button:hover {
      background-color: #3700b3;
    }
    .stats-button {
      display: inline-block;
      margin-top: 1rem;
      padding: 0.75rem 1rem;
      background-color: #008c3e;
      color: white;
      border-radius: 6px;
      text-decoration: none;
      font-weight: bold;
      transition: background-color 0.2s;
    }
    .stats-button:hover {
      background-color: #006f32;
    }
  </style>
  