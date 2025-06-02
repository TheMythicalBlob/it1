<script>
	const aktiviteter = [
		{
			navn: 'Spøkelsestur',
			bilde: '/aktiviteter/spøkelsestur.png',
			pris: 120,
			beskrivelse: 'Bli med på en spennende tur i kjellerens mørke korridorer.'
		},
		{
			navn: 'VR-opplevelse',
			bilde: '/aktiviteter/blucher.png',
			pris: 150,
			beskrivelse: 'Opplev senkningen av Blücher i VR!'
		},
		{
			navn: 'Klatring',
			bilde: '/aktiviteter/klatring.png',
			pris: 180,
			beskrivelse: 'Utendørs klatring langs festningsmurene.'
		},
		{
			navn: 'Escape room',
			bilde: '/aktiviteter/escape_room.png',
			pris: 200,
			beskrivelse: 'Klarer du å rømme fra bunkeren før tiden går ut?'
		},
		{
			navn: 'Historisk rebusløp',
			bilde: '/aktiviteter/historie_rebusløp.png',
			pris: 50,
			beskrivelse: 'Løs poster med mobilen og lær historie.'
		}
	];
</script>

<style>
	:global(body) {
		margin: 0;
		font-family: 'Segoe UI', sans-serif;
		background-color: #0e1a2b;
		color: #fff;
	}

	.hero {
		background: url('/images/spokelsestur.jpg') center/cover no-repeat;
		height: 300px;
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: center;
	}

	.hero h1 {
		background-color: rgba(0, 0, 0, 0.6);
		padding: 1rem 2rem;
		border-radius: 1rem;
		font-size: 2.5rem;
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
		gap: 1.5rem;
		padding: 2rem;
	}

	.kort {
		background: #fff;
		color: #000;
		padding: 1rem;
		border-radius: 1rem;
		box-shadow: 0 4px 8px rgba(0,0,0,0.3);
		display: flex;
		flex-direction: column;
		align-items: center;
		transition: transform 0.2s;
	}

	.kort:hover {
		transform: scale(1.02);
	}

	.kort img {
		width: 100%;
		height: 180px;
		object-fit: cover;
		border-radius: 0.5rem;
	}

	.kort h2 {
		margin: 0.5rem 0;
	}

	.kort p {
		text-align: center;
		margin: 0.5rem 0;
	}

	.kort .pris {
		font-weight: bold;
		margin: 0.5rem 0;
	}

	.kort a {
		margin-top: auto;
		background-color: #0077cc;
		color: white;
		padding: 0.5rem 1rem;
		border-radius: 0.5rem;
		text-decoration: none;
		transition: 0.2s;
	}

	.kort a:hover {
		background-color: #005fa3;
	}
</style>

<section class="hero">
	<h1>Sommeraktiviteter på Oscarsborg</h1>
</section>

<div class="grid">
	{#each aktiviteter as aktivitet}
		<div class="kort">
			<h2>{aktivitet.navn}</h2>
			<img src={aktivitet.bilde} alt={aktivitet.navn} />
			<p>{aktivitet.beskrivelse}</p>
			<p class="pris">Pris: {aktivitet.pris} kr</p>
			<a href="/registrering">Meld deg på</a>
		</div>
	{/each}
</div>