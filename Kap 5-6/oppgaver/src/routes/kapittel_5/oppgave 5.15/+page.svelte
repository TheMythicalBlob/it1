<script>
   let tall1 = 0
   let tall2 = 0
   let tall3 = 0
   let tall4 = 0
   let tall5 = 0
   let tall6 = 0
   let tall7 = 0
   let tall8 = 0
   $: a = tall1 + tall2
   $: b = tall3 - tall4
   $: c = tall5 * tall6
   $: d = tall7 / tall8
</script>

<input bind:value={tall1} type="number">
<span> + </span>
<input bind:value={tall2} type="number">
<span> = </span>
<span> {a} </span>

<br>
<br>

<input bind:value={tall3} type="number">
<span> - </span>
<input bind:value={tall4} type="number">
<span> = </span>
<span> {b} </span>

<br>
<br>

<input bind:value={tall5} type="number">
<span> * </span>
<input bind:value={tall6} type="number">
<span> = </span>
<span> {c} </span>

<br>
<br>

<input bind:value={tall7} type="number">
<span> / </span>
<input bind:value={tall8} type="number">
<span> = </span>
<span> {d} </span>

<style>
   input{
      width: 80px;
   }
</style>
   