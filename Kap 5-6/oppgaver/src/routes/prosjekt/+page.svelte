<script>
	const prosjekter = [
		"Nettbutikk"
	]

</script>

<h1>Større prosjekter</h1>

{#each prosjekter as prosjekt}
	<a href="/prosjekt/{prosjekt.toLowerCase()}">{prosjekt}</a>
{/each}

<style>

</style>
