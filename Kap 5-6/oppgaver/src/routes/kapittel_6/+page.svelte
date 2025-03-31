<script>
	const kapittel_6 = [
		[
			{ nr: "6.0.1", navn: "For-løkke Summer" },
			{ nr: "6.0.2", navn: "For-løkke Telle antall seksere" },
			{ nr: "6.0.3", navn: "For-løkke Gå igjennom en array med verdier" },
			{ nr: "6.0.4", navn: "Each-løkke Vise en liste med verdier" },
		],[
			{ nr: "6.1.13",  navn: "Gangertabell"},
		],[
			{ nr: "6.2.2", navn: "Objekter i lister" },
			{ nr: "6.2.3", navn: "Film lister" },
			{ nr: "6.2.22", navn: "Kortstokk" },
		],[
			{ nr: "6.3.5", navn: "Land-oppgave øving" },
		],[
			{ nr: "6.4.5", navn: "Emojisøk" },
		],
	];
</script>

<main>
	<h1>Oppgaver fra kap 6</h1>

	<div class="kapittel_6">
		{#each kapittel_6 as undereksempler, under_indeks}
			<div>
				{#each undereksempler as eks, eks_indeks}
					{#if eks_indeks == 0}
						<h3>Oppgaver fra 6.{under_indeks}</h3>
					{/if}
					<a
						href="/kapittel_6/kapittel_{eks.nr.slice(
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

	.kapittel_6 {
		display: flex;
		gap: 10px;
	}
	.kapittel_6 > div,
	.oppgaver {
		flex: 0 1 250px;
		display: flex;
		flex-direction: column;
	}
	.kapittel_6 > div > h3 {
		text-align: center;
	}
	.kapittel_6 > div a,
	.oppgaver a {
		text-decoration: none;
		padding: 0.5em;
	}
	.kapittel_6 > div a:hover,
	.oppgaver a:hover {
		background-color: antiquewhite;
	}
</style>
