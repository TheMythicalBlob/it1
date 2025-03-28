<script>
   let antall = $state(1);
   let laster = false;
   let kortstokk = $state([]);

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
   };

   let sortnavn = {
      CLUBS: "KLØVER",
      DIAMONDS: "RUTER",
      HEARTS: "HJERTER",
      SPADES: "SPAR",
   };

   let trekkKort = async (a) => {
      laster = true;
      let data = await fetch(
         `https://deckofcardsapi.com/api/deck/new/draw/?count=${a}`
      );

      let json = await data.json();

      laster = false;
      kortstokk = json.cards;
   };

   // Denne linjen gjør at vi kjører "trekkKort" på nytt når "antall" endrer seg:
   $effect(() => {
      trekkKort(antall);
   });
</script>

<label>Antall: <input bind:value={antall} type="number" min="1" /></label>

{#if laster}
   <p>Laster …</p>
{/if} 

<h1>Kortstokk</h1>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
   {#each kortstokk as kort}
      <div style="text-align: center;">
         <p>{valoernavn[kort.value] || kort.value}  {sortnavn[kort.suit] || kort.suit}</p>
         <img src={kort.image} alt="{kort.value} of {kort.suit}" width="100" height="140" />
      </div>
   {/each}
</div>
