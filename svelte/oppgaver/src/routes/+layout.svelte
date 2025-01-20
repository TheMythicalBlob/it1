<script>
    let { children } = $props();
</script>

<nav>
    <ul>
        <li><a href="/">Hjem</a></li>
        <li><a href="/dyrenett">Dyrenett</a></li>
        <li><a href="/oppg_504">5.04</a></li>
        <li><a href="/oppg_505">5.05</a></li>
        <li><a href="/oppg_506">5.06</a></li>
        <li><a href="/oppg_507">5.07</a></li>
        <li><a href="/oppg_508">5.08</a></li>
    </ul>
</nav>

<main>
    {@render children()}
</main>

<style>
    * {
        font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
            sans-serif;
    }

    nav ul {
        list-style-type: none;
        display: flex;
        flex-wrap: wrap;
        margin: 0;
        padding: 0;
        height: 3rem;
    }

    nav ul li {
        flex-grow: 1;
        height: 100%;
        flex-basis: auto;
    }

    nav ul li a {
        display: block;
        width: 100%;
        height: 100%;
        border: white 1px solid;
        padding: 0 0;
        text-decoration: none;
        color: white;
        background-color: black;
        /* Bruker flex, justify-content og align-item til å sentrere tekst på navknapper*/
        display: flex;
        align-items: center;
        justify-content: center;
    }

    nav ul li a:hover {
        background-color: darkgrey;
    }

    nav ul li a:active {
        background-color: darkgreen;
    }
</style>
