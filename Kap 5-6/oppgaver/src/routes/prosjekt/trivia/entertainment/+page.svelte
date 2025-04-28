<script>
    const underholdningKategorier = [
      { navn: "Bøker", id: 10 },
      { navn: "Film", id: 11 },
      { navn: "Musikk", id: 12 },
      { navn: "Musikaler og teater", id: 13 },
      { navn: "TV", id: 14 }
    ]
  </script>
  
  <main>
    <h1>Underholdning 🎭</h1>
    <p>Velg en quiz-kategori:</p>
  
    <ul>
      {#each underholdningKategorier as kategori}
        <li>
          <a href={`/prosjekt/trivia/kategori/${kategori.id}`}>
            {kategori.navn}
          </a>
        </li>
      {/each}
    </ul>
  
    <a href="/prosjekt/trivia">⬅ Tilbake til alle kategorier</a>
  </main>
  
  <style>
    main {
      padding: 2rem;
      max-width: 500px;
      margin: auto;
      font-family: Arial, sans-serif;
      text-align: center;
    }
  
    ul {
      list-style: none;
      padding: 0;
      margin: 1rem 0 2rem;
    }
  
    li {
      margin: 0.75rem 0;
    }
  
    a {
      text-decoration: none;
      color: #0070f3;
      font-weight: bold;
    }
  
    a:hover {
      text-decoration: underline;
    }
  </style>
  