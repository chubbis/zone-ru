<template>
  <div>
    <div v-for="flat in flats" :key="flat.id">
      <router-link :to="{ name: 'flat-item', params: { id: flat.id }}">Flat {{flat.flat_number}}</router-link>
    </div>
  </div>
</template>

<script>
import {getService} from "@/services/fetch-service";

export default {
  name: "Flats",
  data() {
    return {
      flats: [],
      canGoToPage: false,
    }
  },
  async mounted() {
    const url_path = `/api/v1/flats`;
    this.flats = await getService(url_path);
  }
}
</script>

<style scoped>

</style>