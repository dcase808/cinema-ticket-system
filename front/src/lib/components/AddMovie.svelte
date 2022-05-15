<script>
    let title, desc, poster
    import { API_URL } from "$lib/constants/constants.svelte";
    import Cookie from "js-cookie";

    const addMovie = async () => {
        let url = API_URL + '/movies'
        let entry = {
            'title': title,
            'poster': poster,
            'desc': desc
        }
        let response = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + Cookie.get('jwt-token'),
                'Content-type': 'application/json'},
            body: JSON.stringify(entry)
            })
        if(response.ok)
        {
            alert('Dodano film ' + title)
            title = desc = poster = null
            
        }
    }

</script>
<div>
    <h2>Dodaj film</h2>
    <form on:submit|preventDefault={addMovie}>
        <label>
            Tytuł<br>
            <input type='text' bind:value={title} required>
        </label>
        <label>
            Opis<br>
            <textarea style='resize: none' bind:value={desc} required></textarea>
        </label>
        <label>
            Plakat<br>
            <input type='url' bind:value={poster} required>
        </label>
        <input type='submit' value='Dodaj'>
    </form>
</div>
<style>
    input, textarea 
    {
    background-color: black;
    color: white;
    width: 90%;
    }
</style>