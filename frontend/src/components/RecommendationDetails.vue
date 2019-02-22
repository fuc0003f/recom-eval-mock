<template>
  <div id="recommendation-details">
    <p class="recommendation-details_headline">{{ selected_brands }}</p>

    <ul id="recommendation-list" v-if="data != null">
      <li v-for="item in data" v-bind:key="item.id" class="recommendation-list_item">
        <img :src="getImgUrl(item.logo)">
        <div class="recommendation-list_label">{{item.name}}</div>
      </li>
    </ul>
    <star-rating
      v-model="actual_rating"
      :star-size="25"
      :padding="5"
      :text-class="'rating-text'"
      active-color="#FFCB01"
      @rating-selected="setRating"
    ></star-rating>
    <p>{{ recommendation_info }}</p>
  </div>
</template>

<script>
import { getImgUrl } from "../assets/util/image";
import StarRating from "vue-star-rating";
export default {
  name: "recommendation-details",
  components: { StarRating },
  props: {
    data: Array,
    actual_rating: Number
  },
  data() {
    return {
      selected_brands: "RECOMMENDED BRANDS",
      recommendation_info:
        "Above you see a list of brands that was created by a fancy recommendation system. You can click through the brands on the left and give a rating for the quality of the recommendations."
    };
  },
  methods: {
    // set a rating for the recommendation
    setRating: function(rating) {
      this.$emit("setRating", rating);
    },
    getImgUrl
  }
};
</script>

<style lang="scss">
.vue-star-rating-rating-text {
  display: none;
}
.vue-star-rating {
  border-top: 1px solid #000;
  margin-left: 100px !important;
  margin-right: 100px !important;
  justify-content: center;
  padding-top: 5px;
}

.vue-star-rating * {
  border-top: 0px;
}

#recommendation-details {
  width: 500px !important;
  justify-content: center;
}

.recommendation-details_headline {
  font-size: 14px;
  font-weight: 700;
  line-height: 16px;
  letter-spacing: 1.1px;
  border-bottom: 1px solid #000;
  padding-bottom: 15px;
  margin-left: 100px;
  margin-right: 100px;
}

#recommendation-list {
  padding-left: 20%;
  padding-right: 20px;
  display: flex;
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
.recommendation-list_label {
  margin-top: 25px !important;
}
.recommendation-list_item {
  display: flex;
  justify-content: left;
  position: relative;
  margin-bottom: 10px;
}
</style>
