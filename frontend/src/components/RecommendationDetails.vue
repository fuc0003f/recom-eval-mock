<template>
  <div id="recommendation-details">
    <p>{{ selectedBrands }}</p>

    <ul id="recommendation-list" v-if="data != null">
      <li v-for="item in data" v-bind:key="item.id">
        <img :src="getImgUrl(item.logo)">
        <div>{{item.name}}</div>
      </li>
    </ul>
    <p>{{ recommendationInfo }}</p>
  </div>
</template>

<script>
import { getImgUrl } from "../assets/util/image";
export default {
  name: "recommendation-details",
  props: {
    data: Array
  },
  data() {
    return {
      selectedBrands: "These are the recommended brands",
      recommendationInfo:
        "Above you see a list of brands that was created by a fancy recommendation system. The list is ordered by the similarity of the particular brand compared to the selected one."
    };
  },
  methods: {
    getImgUrl
  }
};
</script>

<style lang="scss">
#recommendation-details {
  width: 500px !important;
}

#recommendation-list {
  display: flex;
  text-align: left;
  padding-left: 100px;
  flex-direction: column;
  height: 400px;

  img {
    width: 90px;
    height: 75px;
    float: left;
  }
  div {
    display: inline;
  }
}
</style>
