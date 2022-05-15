<script>
	import Movie from '$lib/components/Movie.svelte'
	import {API_URL} from '$lib/constants/constants.svelte'

	const getMovies = () => {
		let url = API_URL + '/movies'
		return fetch(url)
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