<script>
    // @ts-nocheck
  
    let elever = [
      { fornavn: "Abbas", etternavn: "Ahmadi", klasse: "2STE" },
      { fornavn: "Abdalla", etternavn: "Mohamed-Sharif", klasse: "2STB" },
      { fornavn: "Ahad", etternavn: "Sajid", klasse: "2STB" },
      { fornavn: "Ali", etternavn: "Gondal", klasse: "3STE" },
      { fornavn: "Arsam", etternavn: "Nasar", klasse: "2STB" },
      { fornavn: "Birk", etternavn: "Eilertsen", klasse: "3STB" },
      { fornavn: "Henry", etternavn: "Tran", klasse: "2STE" },
      { fornavn: "Leon", etternavn: "Almli", klasse: "3STE" },
      { fornavn: "Margrethe", etternavn: "Gøthesen", klasse: "2STC" },
      { fornavn: "Martin", etternavn: "Farahi", klasse: "3STA" },
      { fornavn: "Martin", etternavn: "Larsen", klasse: "2STC" },
      { fornavn: "Philip", etternavn: "Schytt", klasse: "2STD" },
      { fornavn: "Rehman", etternavn: "Shah", klasse: "2STB" },
      { fornavn: "Sergei", etternavn: "Titov", klasse: "3STE" },
      { fornavn: "Simen", etternavn: "Mathiesen", klasse: "3STB" },
      { fornavn: "Sondre", etternavn: "Arnesen", klasse: "3STC" },
      { fornavn: "Tymofii", etternavn: "Chernata", klasse: "3STE" },
    ];
  
    // Setter alle elever til å være tilstede
    for (let elev of elever) {
      elev.tilstede = Math.random() < 0.75;
    }
  
    // Reaktiv variabel som teller antall tilstede
    let antall_tilstede = elever.filter((a) => a.tilstede).length;
  
    // Lytterfunksjon for å endre tilstedeværelese for elev
    const byttTilstede = (elev) => {
      // hvordan endrer vi verdien til tilstede for elev?
    };
  </script>
  
  <h2>Informasjonsteknologi 1</h2>
  <h3>Tilstede: {antall_tilstede} elever</h3>
  <table>
    <thead>
      <tr>
        <th>Fornavn</th>
        <th>Etternavn</th>
        <th>Klasse</th>
      </tr>
    </thead>
    <tbody>
      {#each elever as elev}
        <tr
          on:click={() => {
            // Hva skal stå her for at tilstede hos eleven skal endres?
            
          }}
        >
          <!-- Hvilken verdi for attributten class når en elev er tilstede? -->
          <!-- Hva gjør det med utseendet til raden? -->
          <td class={elev.tilstede ? "tilstede" : ""}>{elev.fornavn}</td>
          <td class={elev.tilstede ? "tilstede" : ""}>{elev.etternavn}</td>
          <td class="klasse {elev.tilstede ? 'tilstede' : ''}">{elev.klasse}</td>
        </tr>
      {/each}
    </tbody>
  </table>
  
  <style>
    table {
      border-collapse: collapse;
      border: black 2px solid;
    }
    thead tr {
      background-color: lightgreen;
    }
    tbody tr:nth-child(even) {
      background-color: lightgreen;
    }
    td,
    th {
      width: 7em;
      border: black 1px solid;
      padding: 0.2em;
    }
    tr:hover {
      cursor: pointer;
    }
  
    .klasse {
      text-align: center;
    }
  
    .tilstede {
      color: skyblue;
    }
  </style>
  
   