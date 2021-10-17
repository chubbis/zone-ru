<template>
  <div>
    <div v-for="flat in flats" :key="flat.id">
      <router-link :to="{ name: 'flat-item', params: { id: flat.id }}">Flat {{flat.flat_number}}</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Flats",
  data() {
    return {
      flats: [],
      canGoToPage: false,
    }
  },
  mounted() {
    fetch('https://localhost:9091/api/v1/flats', {
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
        },
    })
      .then(data => data.json())
      .then(result => this.flats = result)
      .catch(err => console.log(err));
  }
}
</script>

<style scoped>

</style>