<script>
    let { children } = $props();
</script>

<nav>
    <ul>
        <li><a href="/oppgave 5.13">Oppgave_5.13</a></li>
        <li><a href="/oppgave 5.14">Oppgave_5.14</a></li>
        <li><a href="/oppgave 5.15">Oppgave_5.15</a></li>
        <li><a href="/oppgave 5.16">Oppgave_5.16</a></li>
        <li><a href="/oppgave 5.21">Oppgave_5.21</a></li>
        <li><a href="/oppgave 6.01">Oppgave_6.01</a></li>
        <li><a href="/oppgave 6.02">Oppgave_6.02</a></li>
        <li><a href="/oppgave 6.03">Oppgave_6.03</a></li>
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
