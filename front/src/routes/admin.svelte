<script>
    import {API_URL} from '$lib/constants/constants.svelte'
    const getMovies = () => {
        let url = API_URL + '/movies'
		return fetch(url)
		.then(response => response.json())
		.then(data => data)
	}

	let movies = getMovies()
</script>

<main>
    <div id="left">
        <form>
            <label>
                Tytuł<br>
                <input type='text'>
            </label>
            <label>
                Data<br>
                <input type='date'>
            </label>
            <label>
                Opis<br>
                <textarea style='resize: none'></textarea>
            </label>
            <label>
                Plakat<br>
                <input type='text'>
            </label>
            <input type='submit' value='Dodaj'>
        </form>
    </div>
    <div id="right">
        Usuń film<br>
        {#await movies}
        <span>Loading</span>
        {:then movies}
        {#each movies as movie}
            <button>{movie.title}</button><br>
        {/each}
        {/await}

    </div>
</main>
<style>
    input, textarea {
        background-color: black;
        color: white;
        width: 90%;
    }
    #left {
        width: 100%;
    }
    #right {
        width: 100%;
    }
	main{
        text-align: center;
		margin: 0 auto;
		width: 900px;
		float: center;
        min-height: 200px;
        margin-top: 20px;
        background-color: rgb(34, 34, 34);
        color: white;
        border-radius: 2px;
        display: flex;
        padding-top: 10px;
    }
</style>