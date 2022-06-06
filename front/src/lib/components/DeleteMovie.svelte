<script>
    import { API_URL } from "$lib/constants/constants.svelte";
    import Cookie from "js-cookie";

	const getMovies = async() => {
		let url = API_URL + '/movies'
		return await fetch(url)
		.then(response => response.json())
		.then(data => data)
	}
    const deleteMovie = async(movie_title) => {
        let url = API_URL + '/movies/' + movie_title
        await fetch(url, {
            method: 'DELETE',
            headers: {
                'Authorization': 'Bearer ' + Cookie.get('jwt-token'),
                'Content-type': 'application/json'
            }
        })
        movies = getMovies()
    }

	let movies = getMovies()

</script>
<div>
    <h2>Usuń film</h2>
    {#await movies}
        <span>Loading</span>
    {:then movies} 
        {#if movies}
        {#each movies as movie}
            <button on:click={() => {deleteMovie(movie.title)}}>{movie.title}</button>
        {/each}
        {:else}
            <span>Brak filmów</span>
        {/if}
    {/await}
</div>
<style>
</style>