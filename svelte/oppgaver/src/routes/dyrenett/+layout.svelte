<script>
    let { children } = $props();
</script>

<main>
    <nav>
        <ul>
            <li><a href="/dyrenett">Ekorn</a></li>
            <li><a href="/dyrenett/pinnsvin">Pinnsvin</a></li>
            <li><a href="/dyrenett/kanin">Kanin</a></li>
        </ul>
    </nav>
    {@render children()}
</main>

<style>
    main {
        width: 600px;
        margin: 0 auto;
    }

    nav ul {
        list-style-type: none;
    }

    nav ul li {
        display: inline-block;
    }

    nav ul li a {
        display: inline-block;
        width: 100px;
        text-align: center;
        background-color: brown;
        color: white;
        padding: 10px;
        text-decoration: none;
    }

    nav ul li a:hover {
        background-color: blue;
    }

    nav ul li a:active {
        background-color: blueviolet;
    }
</style>
