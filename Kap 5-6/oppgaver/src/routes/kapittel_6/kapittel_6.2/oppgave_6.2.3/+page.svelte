<script>
	let filmene = $state([
	  {tittel: "The Shining", genre: "Skrekk"},
	  {tittel: "Alien", genre: "Skrekk"},
	  {tittel: "Hot Shots", genre: "Komedie"},
	  {tittel: "Hot Shots II", genre: "Komedie"},
	  {tittel: "Aliens", genre: "Skrekk"},
	  {tittel: "Panserkrysseren Potemkin", genre: "Drama"}
	])

	  let genre = $state("Komedie")

	let filtrerte_filmer = $derived(filmene.filter(
		(element)=>{
			return element.genre === genre
		}))
  </script>

  <select bind:value={genre}>
	  <option value="Skrekk">Skrekk</option>
	  <option value="Komedie">Komedie</option>
	  <option value="Drama">Drama</option>
  </select>

  <ul>
	{#each filtrerte_filmer as film}
	  <li>{film.tittel}</li>
	{/each}
  </ul>
