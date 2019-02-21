<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <div id="content">
      <brand-selector @onBrandClick="updateRecommendationDetails($event)"></brand-selector>
      <recommendation-details
        :data="recommendation_details_data"
        :actual_rating="actual_rating"
        @setRating="saveRating($event)"
      ></recommendation-details>
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
      msg: "recommender evaluation mockup",
      recommendation_details_data: [],
      selected_brand: 0,
      actual_rating: 0
    };
  },
  methods: {
    // update the recommendation view because another brand was clicked
    updateRecommendationDetails: function(brandId) {
      let generatedbrand_info = [];
      this.selected_brand = brandId;
      axios({
        method: "GET",
        url: "http://localhost:5000/brands/" + brandId + "/similar"
      }).then(
        result => {
          this.actual_rating = parseInt(result.data.rating);
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
          this.recommendation_details_data = generatedbrand_info;
        },
        error => {
          console.error(error);
        }
      );
    },
    // save the rating for one recommendation
    saveRating: function(rating) {
      this.actual_rating = parseInt(rating);
      axios({
        method: "GET",
        url:
          "http://localhost:5000/saverating/" +
          this.selected_brand +
          "/" +
          this.actual_rating
      }).then(
        result => {
          console.log(
            "rating for brand: " +
              this.selected_brand +
              " updated to " +
              this.actual_rating
          );
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
$primary-color: #000;
$white: #fff;

body {
  margin: 0;
}
#app {
  font-family: "Helvetica Neue", Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $primary-color;
  margin-top: 0;
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
  background-color: $primary-color;
  color: $white;
  margin: 0px;
  font-weight: 100;
}
h1 {
  padding-top: 60px;
  padding-bottom: 30px;
}

.hidden {
  display: none;
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
