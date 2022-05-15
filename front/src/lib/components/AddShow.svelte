<script>
    let title, date, time
    import { API_URL } from "$lib/constants/constants.svelte";
    import Cookie from "js-cookie";

	const getMovies = async () => {
		let url = API_URL + '/movies'
		return await fetch(url)
		.then(response => response.json())
		.then(data => data)
	}
    const addShow = async () => {
        let date_obj = new Date(Date.parse(date + ' ' + time))
        let url = API_URL + '/shows'
        let entry = {
            'title': title,
            'date': date_obj,
            'seats_taken': []
        }
        console.log(JSON.stringify(entry))
        let response = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + Cookie.get('jwt-token'),
                'Content-type': 'application/json'},
            body: JSON.stringify(entry)
            })
        if(response.ok)
        {
            alert('Dodano seans ' + title)
            title = date = time = null
        }
    }
    let movies = getMovies()

</script>
<div>
    <h2>Dodaj seans</h2>
    <form on:submit|preventDefault={addShow}>
        <label>
            Film<br>
            <select bind:value={title} required>
                {#await movies}
                    <span>Loading</span>
                {:then movies} 
                    {#each movies as movie}
                        <option>{movie.title}</option>
                    {/each}
                {/await}
            </select>
        </label>
        <label>
            Data<br>
            <input type='date' bind:value={date} required>
        </label>
        <label>
            Godzina<br>
            <input type='time' bind:value={time} required>
        </label>
        <input type='submit' value='Dodaj'>
    </form>
</div>
<style>
    input, select
    {
    background-color: black;
    color: white;
    width: 90%;
    }
</style>