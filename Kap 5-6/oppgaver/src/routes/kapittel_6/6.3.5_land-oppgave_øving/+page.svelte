<script>
	// Importerer listen med land
	import lender_json from "./lender.json";

	// Oppretter reaktive variabler
	let lender = [...lender_json];
	const grupper = ["Norden", "Skandinavia", "EU"];
	let grupp = "Norden";
	let stigende = false;

	// Filtrerer og sorterer listen basert på valg
	$: filtrertLender = lender
		.filter(land => land.gruppemedlemskap.includes(grupp))
		.sort((a, b) => stigende 
			? a.landsnavn.localeCompare(b.landsnavn) 
			: b.landsnavn.localeCompare(a.landsnavn));
</script>

<h1>Lenders tilhørighet</h1>
<h2>Velg gruppe:</h2>
<select bind:value={grupp}>
	{#each grupper as g}
		<option value={g}>{g}</option>
	{/each}
</select>

<h2>Sorter</h2>
<button on:click={() => stigende = !stigende}>
	{stigende ? "Synkende" : "Stigende"}
</button>

{#each filtrertLender as land}
	<h3>{land.landsnavn}</h3>
	<img src="/bilder/flagg/{land.landsnavn.toLowerCase()}.png" alt="{land.landsnavn}-flagg">
	<h4>Hovedstad: {land.hovedstad}</h4>
	<h4>Medlem i:</h4>
	<ul>
		{#each land.gruppemedlemskap as gm}
			<li>{gm}</li>
		{/each}
	</ul>
{/each}

<style>
	img {
		width: 8em
	}
</style>
