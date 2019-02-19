<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <div id="content">
      <brand-selector @onBrandClick="updateRecommendationDetails($event)"></brand-selector>
      <recommendation-details :data="recommendationDetailsData"></recommendation-details>
    </div>
  </div>
</template>

<script>
import BrandSelector from "./components/BrandSelector.vue";
import RecommendationDetails from "./components/RecommendationDetails.vue";
import axios from "axios";

export default {
  name: "recom-eval-mock",
  components: { BrandSelector, RecommendationDetails },
  data() {
    return {
      msg: "This is a small tool for the evaluation of a recommender system",
      selected_brand_id: "",
      recommendationDetailsData: []
    };
  },
  methods: {
    updateRecommendationDetails: function(brandId) {
      let generatedbrand_info = [];
      axios({
        method: "GET",
        url: "http://localhost:5000/brands/" + brandId + "/similar"
      }).then(
        result => {
          result.data.similar_brands.forEach(key => {
            axios({
              method: "GET",
              url: "http://localhost:5000/brandinfo/" + key
            }).then(
              result => {
                generatedbrand_info.push({
                  id: key,
                  logo: result.data.logo,
                  name: result.data.name
                });
              },
              error => {
                console.error(error);
              }
            );
          });
          this.recommendationDetailsData = generatedbrand_info;
        },
        error => {
          console.error(error);
        }
      );
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#content {
  display: flex;
  justify-content: center;
  flex-direction: row;
  div {
    margin: 10px;
  }
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
