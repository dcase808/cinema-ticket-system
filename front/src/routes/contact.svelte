<script>
	let name = ''
	let email = ''
	let message = ''
</script>

<svelte:head>
	<title>Kontakt</title>
</svelte:head>

<main>
	<div id='contact'>
		<form class="form">
			<label>
				Imię
				<input type="text" bind:value={name} />
			</label>
			<label>
				E-mail
				<input type="email" bind:value={email} />
			</label>
			
			<label>
				Wiadomość
				<textarea bind:value={message} />
			</label>
			<button type="submit">Wyślij</button>
		  </form>
	</div>
</main>
<style>
	main {

		margin: 0 auto;
		width: 900px;;
	}
	#contact {
		text-align: justify;
		margin: 0 auto;
		width: 860px;;
		color: white;
		margin-top: 20px;
        background-color: rgb(34, 34, 34);
        border-radius: 2px;
		padding: 20px;
	}
	.form {
		width: auto;
	}
	input, textarea {
		width: 100%;
		background-color: black;
		color: white;
	}
	textarea {
		height: 200px;
		resize: none;
	}
	button {
		width: 100%;
	}
</style>