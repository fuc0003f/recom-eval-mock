<template>
  <div id="recommendation-details">
    <p>{{ selectedBrands }}</p>

    <ul id="recommendation-list" v-if="data != null">
      <li v-for="item in data" v-bind:key="item">{{ item }}</li>
    </ul>
    <div v-else-if="data.length == 0">None of the brands is selected.</div>
    <p>{{ recommendationInfo }}</p>
  </div>
</template>

<script>
export default {
  name: "recommentation-details",
  props: {
    data: Array
  },
  data() {
    return {
      selectedBrands: "These are the recommended brands",
      recommendationInfo:
        "Above you see a list of brands that was created by our fancy recommendation system. The list is ordered by the similarity of the particular brand compared to the selected one."
    };
  }
};
</script>

<style lang="scss">
#recommentation-details {
  width: 500px;
}

#recommendation-list {
  display: flex;
  flex-direction: column;
}
</style>
