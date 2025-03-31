<script>
	const kapittel_5 = [
		[	
			{ nr: "5.1.13", navn: "Rød, Grønn og Blå farger"},
			{ nr: "5.1.14", navn: "Store bokstaver"},
			{ nr: "5.1.15", navn: "Kalkulator"},
			{ nr: "5.1.16", navn: "(tomt)"},
		],[
			{ nr: "5.2.21", navn: "ingenting"},
		]
	]
</script>

<main>
	<h1>Oppgaver fra kap 5</h1>

	<div class="kapittel_5">
		{#each kapittel_5 as undereksempler, under_indeks}
			<div>
				{#each undereksempler as eks, eks_indeks}
					{#if eks_indeks == 0}
						<h3>Oppgaver fra 5.{under_indeks+1}</h3>
					{/if}
					<a
						href="/kapittel_5/kapittel_{eks.nr.slice(
							0,
							3,
						)}/oppgave_{eks.nr}">{eks.nr} {eks.navn}</a
					>
				{/each}
			</div>
		{/each}
	</div>
</main>

<style>
	button {
		width: 100%;
	}

	h1 {
		padding: 0.5em;
	}

	h4 {
		margin: 0;
		padding: 0.5em;
	}

	#vis-oppgaver:hover {
		cursor: pointer;
		background-color: antiquewhite;
	}

	.oppgaver {
		display: flex;
		flex-direction: column;
		flex-wrap: wrap;
	}
	.kapittel_5 {
		display: flex;
		gap: 10px;
	}
	.kapittel_5 > div,
	.oppgaver {
		flex: 0 1 250px;
		display: flex;
		flex-direction: column;
	}
	.kapittel_5 > div > h3 {
		text-align: center;
	}
	.kapittel_5 > div a,
	.oppgaver a {
		text-decoration: none;
		padding: 0.5em;
	}
	.kapittel_5 > div a:hover,
	.oppgaver a:hover {
		background-color: antiquewhite;
	}
</style>
