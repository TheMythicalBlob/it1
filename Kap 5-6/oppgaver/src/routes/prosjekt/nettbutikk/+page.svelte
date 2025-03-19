<script>
// @ts-nocheck
	
	import varer from "./nettbutikk.json"
	
	// Legger inn antall i hvert vare-objekt
	for (let vare of varer){
		vare.antall = 0
	}
	
	// Handlekurv
	let handlekurv = []
	
	// Variabel for total pris av varer i handlekurven
	let totalPris = 0
	
	// Variabel for visning av pris
	let visMaksPris = 2600
	
	// Viser handlekurven
	let viserKurv = false
	
	// Variabel for hvilket plagg som skal vises
	let visPlagg = "alle"
	
	
	const visKurv = () => {
		console.log("vis kurv")
		viserKurv = !viserKurv
	}
	
	const tomKurv = () => {
		console.log("tøm handlekurv")
		handlekurv = []
		totalPris = 0
	}
	
	const slettVare = (indeks) => {
	const vareSomSlettes = handlekurv[indeks]
	totalPris -= vareSomSlettes.pris * vareSomSlettes.antall

	const iVarer = varer.find(v => v.navn === vareSomSlettes.navn)
	if (iVarer) {
		iVarer.antall = 0
	}
	
	handlekurv.splice(indeks, 1)
	handlekurv = [...handlekurv]
}

	
	const leggIHandlekurv = (indeks) => {
		const vare = varer[indeks]
		if (vare.antall > 0) {
			let eksisterende = handlekurv.find(v => v.navn === vare.navn)
			if (eksisterende) {
				eksisterende.antall += vare.antall
			} else {
				handlekurv = [...handlekurv, { ...vare, antall: vare.antall }]
			}
			totalPris += vare.pris * vare.antall
			varer[indeks].antall = 0
		}
}
	
	// Filtrering av varer basert på plagg og pris
	$: filtrerteVarer = varer.filter(vare => 
		(visPlagg === "alle" || vare.plagg === visPlagg) && vare.pris <= visMaksPris
	)
	</script>
	
	<link
	rel="stylesheet"
	href="https://cdnjs.cloudflare.com/ajax/libs/foundation/6.6.1/css/foundation.min.css"
/>

	<header>
		<nav>
			<select bind:value={visPlagg}>
				<option value="alle">Vis alle</option>
				<option value="skjorte">Vis Skjorter</option>
				<option value="bukse">Vis Bukser</option>
			</select>
			<button class="button success" on:click={visKurv}>Handlekurv</button>
			<button class="button warning" on:click={tomKurv}>Tøm handlekurv</button>
			<label>
				<input type="range" min="100" max="2600" step="10" bind:value={visMaksPris}>
				{visMaksPris} kr
			</label>
		</nav>
	</header>
	
	{#if viserKurv}
		<sidebar id="txtHandlekurv">
			<h3>Handlekurv</h3>
			{#each handlekurv as kurv, indeks}
				<button class="slett" on:click={() => slettVare(indeks)}>×</button>
				<article>{kurv.antall} x {kurv.navn}</article>
				<article>{kurv.pris * kurv.antall} kr</article>
			{/each}
			<article></article>
			<article><b>Total pris:</b></article>
			<article><b>{totalPris} kr</b></article>
		</sidebar>
	{:else}
		<main>
			{#each filtrerteVarer as vare, indeks}
				<article>
					<img src="/butikkbilder/{vare.bilde}" alt="{vare.navn}" />
					<h6>{vare.type} {vare.navn} <i>{vare.pris} kr</i></h6>
					<input type="number" bind:value={vare.antall} min="0" />
					<button class="button" on:click={() => leggIHandlekurv(indeks)}>Legg i Handlekurv</button>
				</article>
			{/each}
		</main>
	{/if}
	

<style>	
	header nav {
		display: grid;
		grid-template-columns: repeat(5, 1fr);
	}

	main {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		grid-gap: 10px;
	}

	article img {
		width: 100%;
	}

	@media (max-width: 1100px) {
		main {
			grid-template-columns: 1fr 1fr 1fr;
		}
	}

	@media (max-width: 900px) {
		main {
			grid-template-columns: 1fr 1fr;
		}
	}

	@media (max-width: 700px) {
		main {
			grid-template-columns: 1fr;
		}
		header nav {
			grid-template-columns: 1fr;
		}

		header nav button {
			margin: 0;
		}
	}

	/* Vil bare brukes hvis handlekurv er med */
	#txtHandlekurv {
		display: grid;
		grid-template-columns: 1fr 6fr 2fr;
		width: 400px;
	}

	.slett{
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 1.2em;
		cursor:pointer;
	}

	.slett:hover{
		color: red;
	}

	.slett:active{
		color: darkred;
	}

	#txtHandlekurv h3 {
		grid-column: span 3;
	}
</style>
