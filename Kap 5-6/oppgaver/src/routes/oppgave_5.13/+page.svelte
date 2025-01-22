<script>
       let rød = 0
       let blå = 0
       let grønn = 0
    </script>

   <label>Rødhet<input bind:value={rød} min=0 max=255 type="range"></label>
   <label>Blåhet<input bind:value={blå} min=0 max=255 type="range"></label>
   <label>Grønnhet<input bind:value={grønn} min=0 max=255 type="range"></label>

    <h1 style="color: rgb({rød}, {grønn}, {blå})">Overskrift med farge</h1>
