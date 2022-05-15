<script>
    import { goto } from '$app/navigation'; 
    import AddMovie from '$lib/components/AddMovie.svelte';
    import AddShow from '$lib/components/AddShow.svelte';

    import {API_URL} from '$lib/constants/constants.svelte'

    import Cookies from 'js-cookie'

    import { onMount } from 'svelte';

    let loggedIn = false

    const validateAndForward = async () => {
        let url = API_URL + '/validate'
        let response = await fetch(url, {
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token')}
        })

        if(!response.ok){
            Cookies.remove('jwt-token')
            goto('/login')
        }
        loggedIn = true
    }

    const checkIfLoggedIn = async () => {
        if(Cookies.get('jwt-token'))
        {
            validateAndForward()
        }
        else
        {
            goto('/login')
        }
    }

    onMount(() => {
        checkIfLoggedIn()
    })

    const logout = () => {
        Cookies.remove('jwt-token')
        goto('/')
    }

</script>

<main>
    {#if loggedIn}
    <AddMovie/>
    <AddShow/>
    <button on:click={logout}>Wyloguj</button>
    {/if}
</main>
<style>
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
        flex-direction: column;
        padding-top: 10px;
    }
</style>