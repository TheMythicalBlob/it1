<script>
    let MånedsPris = 175
    let AntallGB = [1, 5, 15]
    let DatapakkePris = [79, 149, 249]
    let brukerForbruk = 0
    let totalPris = 0

    function beregnPris() {
        let ekstraData = Math.max(0, brukerForbruk - 1)
        let prisForEkstraData = 0

        for (let i = AntallGB.length - 1; i >= 0; i--) {
            while (ekstraData >= AntallGB[i]) {
                ekstraData -= AntallGB[i]
                prisForEkstraData += DatapakkePris[i]
            }
        }

        totalPris = MånedsPris + prisForEkstraData
    }
</script>

<input type="number" bind:value={brukerForbruk} on:input={beregnPris}/>
<p>Total pris er {totalPris} kr</p>