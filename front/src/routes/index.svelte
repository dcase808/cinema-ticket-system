<script>
	import Movie from '$lib/components/Movie.svelte'

	const getMovies = () => {
		return fetch("http://localhost:8000/movies")
		.then(response => response.json())
		.then(data => data)
	}

	let movies = getMovies()
</script>

<svelte:head>
	<title>strona</title>
</svelte:head>

<main>
	{#await movies}
	<span>Loading</span>
	{:then movies}
		{#each movies as movie}
			<Movie id={movie.title} title={movie.title} description={movie.desc} poster={movie.poster}/>
		{/each}
	{/await}
</main>
<style>
	main{
		text-align: center;
		margin: 0 auto;
		width: 900px;
		float: center;
	}
</style>