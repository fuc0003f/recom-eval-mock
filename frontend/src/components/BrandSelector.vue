<template>
  <div id="brand-selector">
    <div id="search-area">
      <span class="search-icon">Suche</span>
      <div id="search-input" contenteditable="true"></div>
    </div>
    <div
      v-if="this.selected_brand != null"
      id="selected-area"
    >{{this.selected_brand.similar_brands}}</div>

    <ul id="brands-list" v-if="this.brands != null">
      <li
        v-for="item in Object.keys(this.brands)"
        v-bind:key="item"
        @click="handleBrandClickEvent(item)"
      >{{ brands[item].similar_brands }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "brand-selector",
  data() {
    return {
      msg: "This is the brand selector",
      brands: [],
      selected_brand: {}
    };
  },
  mounted() {
    axios({
      method: "GET",
      url: "http://localhost:5000/brands"
    }).then(
      result => {
        this.brands = result.data;
        this.selected_brand = this.brands[Object.keys(this.brands)[0]];
      },
      error => {
        console.error(error);
      }
    );
  },
  methods: {
    handleBrandClickEvent: function(brand_id) {
      this.selected_brand = this.brands[brand_id];
      this.$emit("onBrandClick", brand_id);
    }
  }
};
</script>

<style lang="scss">
#brand-selector {
  display: flex;
  flex-direction: column;
  width: 700px;
}
#brands-list {
  text-align: left;
}
#search-area {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
#search-input {
  border-radius: 25px;
  border: 1px solid #888;
  width: 200px;
  height: 20px;
  padding: 5px;
  margin-top: 5 !important;
  text-align: left;
  padding-left: 10px;
}
#selected-area {
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
