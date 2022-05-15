<script>
	import '../app.css';
	import Header from '$lib/components/Header.svelte'
	import Menu from '$lib/components/Menu.svelte'
	import Movie from '$lib/components/Movie.svelte'
	import Footer from '$lib/components/Footer.svelte'
</script>
<Header/>
<Menu/>
<main>
	<slot/>
</main>
<Footer/>
