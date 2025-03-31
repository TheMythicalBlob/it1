<script>
	/* Brukes til å finne ut hvilken undermappe vi er i*/
	import { page } from '$app/state';
	let { children } = $props();
</script>

<!-- Navbar og style til dels hentet fra Sveltes eksempel-app -->
<header>
	<nav>
		<ul>
			<li aria-current={page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">Hovedsiden</a>
			</li>
			<li aria-current={page.url.pathname === '/kapittel_5' ? 'page' : undefined}>
				<a href="/kapittel_5">Kapittel 5</a>
			</li>
			<li aria-current={page.url.pathname === '/kapittel_6' ? 'page' : undefined}>
				<a href="/kapittel_6">Kapittel 6</a>
			</li>
			<li aria-current={page.url.pathname === '/prosjekt' ? 'page' : undefined}>
				<a href="/prosjekt">Prosjekter</a>
			</li>
		</ul>
	</nav>
</header>
<main>
	{@render children()}
</main>
<style>
	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
	}
	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0.5rem;
		font-weight: 700;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	nav a:hover {
		background-color: antiquewhite;
	}

	li[aria-current='page']{
		background-color: antiquewhite;
	}

	main {
		width: fit-content;
		max-width: var(--column-width);
		margin: 0 auto;
		padding: 1rem;
		background-color: floralwhite;
		box-shadow: 0.5rem 0.5rem 0.5rem darkgrey;
		border-radius: 0.5rem;
	}

</style>