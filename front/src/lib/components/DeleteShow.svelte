<script>
    import { API_URL } from "$lib/constants/constants.svelte";
    import Cookie from "js-cookie";

	const getShows = async() => {
		let url = API_URL + '/shows-all'
		return await fetch(url)
		.then(response => response.json())
		.then(data => data)
	}
    const deleteShow = async(show_id) => {
        let url = API_URL + '/shows/' + show_id
        await fetch(url, {
            method: 'DELETE',
            headers: {
                'Authorization': 'Bearer ' + Cookie.get('jwt-token'),
                'Content-type': 'application/json'
            }
        })
        shows = getShows()
    }
    const getDate = (date) => {
        date = new Date(date)
        let year = date.getFullYear()
        let month = date.getMonth() + 1
        let day = date.getDate()
        let hour = date.getHours()
        let minute = date.getMinutes()
        return String(year + '.' + month + '.' + day + ' ' + hour + ':' + minute)
    }

	let shows = getShows()

</script>
<div>
    <h2>Usuń seans</h2>
    {#await shows}
        <span>Loading</span>
    {:then shows} 
        {#if shows}
        {#each shows as show}
            <button on:click={() => {deleteShow(show.id)}}>{show.title}, {getDate(show.date)}</button>
        {/each}
        {:else}
            <span>Brak filmów</span>
        {/if}
    {/await}
</div>
<style>
</style>