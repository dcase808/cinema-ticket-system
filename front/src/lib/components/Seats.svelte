<script>
    export let id

    import {API_URL} from '$lib/constants/constants.svelte'

    let selectedSeats = new Set()

    const getShows = async () => {
        let url = API_URL + '/shows?title=' + id
        return await fetch(url)
        .then(response => response.json())
        .then(response => response)
        .catch(e => console.error(e))
    }

    const getSeats = async (id) => {
        let url = API_URL + '/seats/' + id
        return await fetch(url)
        .then(response => response.json())
        .then(response => response)
        .catch(e => console.error(e))
    }

    const selectShow = (id, date) => {
        selectedShow = id
        date = new Date(date)
        taken = getSeats(id)
        year = date.getFullYear()
        month = date.getMonth() + 1
        day = date.getDate()
        hour = date.getHours()
        minute = date.getMinutes()
    }
    
    const selectSeat = (seat) => {
        if(selectedSeats.has(seat))
        {
            selectedSeats.delete(seat)
            let temp = new Set(selectedSeats)
            selectedSeats = temp
        }
        else
        {
            selectedSeats.add(seat)
            let temp = new Set(selectedSeats)
            selectedSeats = temp
        }
    }

    let shows = getShows()

    let selectedShow

    let taken = getSeats('627f03f726dd2cd947e0163e')

    let name, email
    let year, month, day, hour, minute
</script>
{#if !selectedShow}
<div class='container'>
    <div class='text'>
        Wybierz datę seansu:<br>
    </div>
    <div class='dates'>
        {#await shows}
        <span>Loading</span>
        {:then shows}
        {#each shows as show}
            <button on:click={() => {selectShow(show.id, show.date)}}>{new Date(show.date).getFullYear()}.{new Date(show.date).getMonth() + 1}.{new Date(show.date).getDate()}<br> Godzina {new Date(show.date).getHours()}:{new Date(show.date).getMinutes()}</button>
        {/each}
        {/await}
    </div>
</div>
{/if}
{#if selectedShow}
<div class='seats'>
    <div>
        <h3>
        {year}.{month}.{day} Godzina {hour}:{minute}<button on:click={() => {selectedShow = null; selectedSeats = new Set()}}>Zmień seans</button>
        </h3>
    </div>
    <div><h2>Ekran</h2></div>
    <div class='wrapper'>
        {#await taken}
        <span>Loading</span>
        {:then taken}
        {#each {length: 200} as _, i}
            {#if taken.seats_taken.includes(i + 1)}
                <button class='seat' style='background-color: red; pointer-events: none;'>{i + 1}</button>
            {:else if selectedSeats.has(i + 1)}
                <button class='seat' on:click={() => selectSeat(i + 1)} style='background-color: green'>{i + 1}</button>
            {:else}
                <button class='seat' on:click={() => selectSeat(i + 1)}>{i + 1}</button>
            {/if}
        {/each}
        {/await}
    </div>
    <div>
        <button class='seat' style='pointer-events: none;'>999</button>Miejsce wolne
        <button class='seat' style='background-color: red; pointer-events: none;'>999</button>Miejsce zajęte
        <button class='seat' style='background-color: green; pointer-events: none;'>999</button>Wybrane miejsce<br>
    </div>
</div>
{/if}
{#if selectedSeats.size > 0}
<div class='wrap'>
    <div class='summary'>
        <div class='form'>
            <form>
                <label>
                    Imię i nazwisko<br>
                    <input type="text" bind:value={name} />
                </label>
                <label>
                    E-mail<br>
                    <input type="text" bind:value={email} />
                </label>
            </form>
        </div>

    </div>
    <div>Suma: {(selectedSeats.size * 19.99).toFixed(2)} PLN</div>
    <div><button style='width: 88%; margin-left: 50px; margin-right: 50px;'>Zapłać</button></div>
</div>

{/if}
<style>
    .dates {
        width: 100%;
    }
    .text {
        width: 100%;
    }
    .form {
        width: 100%;
        text-align: center;
        margin-left: 50px;
        margin-right: 50px;
    }
    input {
        width: 100%;
        background-color: black;
		color: white;
    }
    .wrapper {
        display: grid;
        grid-template-columns: repeat(15, 1fr);
        grid-auto-rows: auto;
    }
    .seat {
        margin: 5px;
    }
    .container {
        width: auto;
        min-height: 100px;
        margin-top: 20px;
        padding: 10px;
        background-color: rgb(34, 34, 34);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 2px;
    }
    .summary {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }
    .wrap {
        width: 90;
        min-height: 100px;
        margin-top: 20px;
        padding: 10px;
        background-color: rgb(34, 34, 34);
        color: white;
        border-radius: 2px;
    }
    .seats {
        width: auto;
        min-height: 500px;
        margin-top: 20px;
        padding: 10px;
        background-color: rgb(34, 34, 34);
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 2px;
    }
    h3{
        text-align: left;
        padding: 0;
    }
</style>