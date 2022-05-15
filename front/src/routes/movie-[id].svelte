<script>
	import Brief from '$lib/components/Brief.svelte'
	import Seats from '$lib/components/Seats.svelte'
	import { page } from '$app/stores';



	const fetchData = () => {
		let url = "http://localhost:8000/movies/" + $page.params.id
		console.log(url)
		return fetch(url)
		.then(response => response.json())
		.then(response => response)
		.catch(e => console.error(e))
  	}

	let movie = fetchData()
	
</script>

<svelte:head>
	<title>strona</title>
</svelte:head>

<main>
	{#await movie}
	<span>Loading</span>
	{:then movie}
    	<Brief id={movie._id} title={movie.title} description={movie.desc} poster={movie.poster}/>
		<Seats id={movie.title}/>
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