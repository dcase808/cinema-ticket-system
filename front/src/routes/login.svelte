<script>
    import { goto } from '$app/navigation';
    import {API_URL} from '$lib/constants/constants.svelte'
    import Cookies from 'js-cookie'
    
    let username, password
    let showError = false

    const validateAndForward = async () => {
        let url = API_URL + '/validate'
        let response = await fetch(url, {
            headers: {'Authorization': 'Bearer ' + Cookies.get('jwt-token')}
        })

        if(response.ok){
            goto('/admin')
        }
    }

    

    const submit = async () => {
        if(Cookies.get('jwt-token')){
            validateAndForward()
        }
        else
        {
            let data = new URLSearchParams()
            data.append('username', username)
            data.append('password', password)
            let url = API_URL + '/token'
            let response = await fetch(url, {
                method: 'POST',
                headers: {'Content-type': 'application/x-www-form-urlencoded'},
                body: data
                })
            if(response.ok)
            {
                let body = await response.json()
                showError = false
                Cookies.set('jwt-token', body.access_token, {sameSite: 'strict'})
                validateAndForward()
            }
            else
            {
                showError = true
            }
        }
    }
    if(Cookies.get('jwt-token'))
    {
        validateAndForward()
    }
</script>

<main>
    <div>
        {#if showError}
            Błędny login lub hasło
        {/if}
        <form on:submit|preventDefault={submit}>
            <label>
                Login<br>
                <input type='text' bind:value={username} required>
            </label>
            <label>
                Hasło<br>
                <input type='password' bind:value={password} required>
            </label>
            <input type='submit' value='Zaloguj'>
        </form>
    </div>
</main>
<style>
    input {
        background-color: black;
        color: white;
        width: 400px;
    }
	main {
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
        align-items: center;
        justify-content: center;
    }
</style>