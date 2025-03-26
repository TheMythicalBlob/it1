<script>
    let pris_uten_moms = 0;
    let pris_med_moms = 0;

    function regn_moms(){
        pris_med_moms = pris_uten_moms * 1.25; 
    }
</script>

<input type="pris_med_moms" bind:value={pris_uten_moms} on:input={regn_moms} />
<p>Pris med moms: {pris_med_moms}</p>