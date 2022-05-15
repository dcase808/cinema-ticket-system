<script>
    let login, password

    const submit = () => {
        console.log('we here')
    }
</script>

<main>
    <div>
        <form on:submit|preventDefault={submit}>
            <label>
                Login<br>
                <input type='text' bind:value={login}>
            </label>
            <label>
                Hasło<br>
                <input type='password' bind:value={password}>
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