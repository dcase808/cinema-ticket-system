<script>
    export let id, title, description, poster
    let date = '01.01.2023'
</script>

<div class='container'>
    <div class='poster'>
        <img src={poster} alt={title} class='posterimg'>
    </div>
    <div class='description'>
        <h3>{title} {date}</h3>
        <p>{description}</p>
    </div>
    <div id='buttons'>
        <a href='/movie-{id}'><button>Wybierz miejsca</button></a>
    </div>
</div>

<style>
    .container {
        width: auto;
        min-height: 200px;
        margin-top: 20px;
        padding: 10px;
        background-color: rgb(34, 34, 34);
        color: white;
        display: grid;
        align-items: center;
        grid-template-areas: "poster description description" "poster none buttons";
        border-radius: 2px;
    }
    .description {
        padding: 10px;
        padding-top: 0;
        margin-top: 0;
        text-align: justify;
        grid-area: description;
        min-height: 145px;
    }
    .poster {
        height: 200px;
        width: 142px;
        grid-area: poster;
    }
    .posterimg {
        height: 200px;
        width: 142px;
    }
    h3{
        text-align: left;
        padding: 0;
    }
    button {
        margin: 2px;
        height: 40px;
    }
    #buttons{
        grid-area: buttons;
        position: relative ;
    }
</style>