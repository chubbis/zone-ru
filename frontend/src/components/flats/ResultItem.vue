<template>
<div class="result-wrapper">
  <pre>{{ result.result }}</pre>
</div>
</template>

<script>
import { getService } from '/src/services/fetch-service'

export default {
  name: "ResultItem",
  data() {
    return {
      result: '',
      canGoToPage: false,
    }
  },
  async mounted() {
    const url = `https://localhost:9091/api/v1/flats/result/${this.$route.params.id}`;
    this.result = await getService(url);
  }
}
</script>

<style scoped>
.result-wrapper {
  width: fit-content;
  margin: 0 auto;
  background-color: black;
  color: white;
  text-align: left;
  padding: 10px 40px;
}
</style>