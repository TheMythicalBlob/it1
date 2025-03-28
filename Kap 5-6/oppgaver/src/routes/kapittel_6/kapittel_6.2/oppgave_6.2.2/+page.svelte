<script>
	let skurker_liste = [
		["Pingvinen", "Lynvingen"],
		["B-Gjengen", "Onkel Skrue"],
		["Lex Luthor", "Supermann"],
	];

	let skurker_obj = [
		{ navn: "Pingvinen", fiende: "Lynvingen" },
		{ navn: "B-Gjengen", fiende: "Onkel Skrue" },
		{ navn: "Lex Luthor", fiende: "Supermann" },
	];

	// Sorter etter navn
	skurker_obj.sort((a, b)=>a.navn.localeCompare(b.navn))

</script>

{#each skurker_liste as skurk}
	<article>
		<h1>{skurk[0]}</h1>
		<p>Fiende: {skurk[1]}</p>
	</article>
{/each}

{#each skurker_obj as skurk}
	<article>
		<h1>{skurk.navn}</h1>
		<p>Fiende: {skurk.fiende}</p>
	</article>
{/each}
