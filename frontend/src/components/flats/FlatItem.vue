<template>
 <div class="form-wrap">
   <form id="form_flat" @submit="formHandler">
<!--   <form id="form_flat" action="https://localhost:9091/flats/edit/1" method="post">-->
     <ul>
       <li>
         <div>Name</div>
         <div>Count</div>
         <div>new_count</div>
       </li>
       <li>
         <div>Day electricity</div>
         <div>{{ flat.day_el }}</div>
         <input type="hidden" :value=flat.day_el name="day_el" id="day_el" step="0.01">
         <input type="number" name="new_day_el" v-model="new_day_el" step="0.01">
       </li>
       <li>
         <div>Night electricity</div>
         <div>{{ flat.night_el }}</div>
         <input type="hidden" :value=flat.night_el name="night_el" id="night_el" step="0.01">
         <input type="number" name="new_night_el" v-model="new_night_el" id="new_night_el" step="0.01">
       </li>
       <li>
         <div>Cold water</div>
         <div>{{ flat.cold_water }}</div>
         <input type="hidden" v-model=flat.cold_water name="cold_water" id="cold_water" step="0.01">
         <input type="number" name="new_cold_water" v-model="new_cold_water" id="new_cold_water" step="0.01">
       </li>
       <li>
         <div>Hot water</div>
         <div>{{ flat.hot_water }}</div>
         <input type="hidden" :value=flat.hot_water name="hot_water" id="hot_water" step="0.01">
         <input type="number" v-model="new_hot_water" id="new_hot_water" name="new_hot_water" step="0.01">
       </li>
     </ul>
     <button type="submit">Send</button>
   </form>
 </div>
</template>

<script>
import { getService, postService } from '/src/services/fetch-service'

export default {
  name: "FlatItem",
  data() {
    return {
      flat: {},
      new_day_el: null,
      new_night_el: null,
      new_cold_water: null,
      new_hot_water: null,
    }
  },
  methods: {
    async formHandler(e) {
      e.preventDefault();
      const data = {
        new_day_el: parseFloat(this.new_day_el),
        new_night_el: parseFloat(this.new_night_el),
        new_cold_water: parseFloat(this.new_cold_water),
        new_hot_water: parseFloat(this.new_hot_water),
        day_el: this.flat.day_el,
        night_el: this.flat.night_el,
        cold_water: this.flat.cold_water,
        hot_water: this.flat.hot_water,
      }
      const url_path = `/api/v1/flats/edit/${this.$route.params.id}`;

      const result = await postService(url_path, data);
      console.log(result.status_code);
      if (result.status_code === 200) {
        await this.$router.push(`/flats/result/${this.$route.params.id}`);
      }
    },
  },
  async mounted() {
    const url_path = `/api/v1/flats/${this.$route.params.id}`;
    this.flat = await getService(url_path);
  }
}
</script>

<style scoped>
li {
  display: flex;
  width: 450px;
}

li > div {
  width: 150px;
  border: 1px solid black;
}

li:nth-child(odd) {
  background-color: #ccc;
}
</style>