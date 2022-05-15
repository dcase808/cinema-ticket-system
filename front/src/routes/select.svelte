<script>
	import Movie from '$lib/components/Movie.svelte'
	import { onMount } from 'svelte';

	let movies = []

	let promise
	
	onMount(async () => {
		promise = getMovies()
	})

	const getMovies = async () => {
		fetch("http://localhost:3001/movies")
		.then(response => response.json())
		.then(data => movies = data)
	}
</script>

<svelte:head>
	<title>kupa gowna froentendowa</title>
</svelte:head>

<main>
    {#each movies as movie}
        <Movie id={movie.id} title={movie.title} description={movie.description} poster={movie.poster} hours={movie.hours}/>
    {/each}
</main>
<style>
	main{
		text-align: center;
		margin: 0 auto;
		width: 900px;;
	}
</style>