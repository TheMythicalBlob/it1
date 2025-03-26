<script>
   let antall = $state(1);
   let laster = false;
   let kortstokk = $state([]);

   let trekkKort = async (a) => {
      laster = true;
      let data = await fetch(
         `http://deckofcardsapi.com/api/deck/new/draw/?count=${a}`,
      );

      let json = await data.json();

      laster = false;
      kortstokk = json.cards;
      console.log(kortstokk);
   };

   // Denne linjen gjør at vi kjører "trekkKort" på nytt når "antall" endrer seg:
   $effect(() => {
      trekkKort(antall);
   });

   let valoernavn = {
      ACE: "ESS",
      1: "1",
      2: "2",
      3: "3",
      4: "4",
      5: "5",
      6: "6",
      7: "7",
      8: "8",
      9: "9",
      10: "10",
      JACK: "KNEKT",
      QUEEN: "DAME",
      KING: "KONGE",
   }

   let sortnavn = {
      CLUBS: "KLØVER",
      DIAMONDS: "RUTER",
      HEARTS: "HJERTER",
      SPADES: "SPAR",
   }
   
</script>

<label>Antall: <input bind:value={antall} type="number" min="0" /></label>

{#if laster}Laster …{/if}

<h1>Kortstokk</h1>

{#each kortstokk as kort}
   <div>
      {JSON.stringify(kort)}
   </div>
{/each}
