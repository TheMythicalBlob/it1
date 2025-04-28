  <main>
    <h1>Velkommen til Trivia quiz nettside ting</h1>
    <p>Hva vil du gjøre</p>
  
    <div class="valg">
      <a href="/prosjekt/trivia/valg_side">
        <button>Start quiz</button>
      </a>
      <a href="/prosjekt/trivia/poeng_oversikt">
        <button>Se poengoversikt</button>
      </a>
    </div>
  </main>
  
  <style>
    main {
      text-align: center;
      padding: 3rem;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
  
    h1 {
      font-size: 2rem;
      margin-bottom: 1rem;
    }
  
    p {
      font-size: 1.2rem;
      margin-bottom: 2rem;
    }
  
    .valg {
      display: flex;
      justify-content: center;
      gap: 2rem;
      flex-wrap: wrap;
    }
  
    a {
      text-decoration: none;
    }
  
    button {
      padding: 1rem 2rem;
      font-size: 1.1rem;
      border: none;
      border-radius: 8px;
      background-color: #0070f3;
      color: white;
      cursor: pointer;
      transition: background-color 0.2s;
    }
  
    button:hover {
      background-color: #0059c1;
    }
  </style>
  