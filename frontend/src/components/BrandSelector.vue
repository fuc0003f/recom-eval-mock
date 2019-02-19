<template>
  <div id="brand-selector">
    <div id="search-area">
      <span class="search-icon">Suche</span>
      <div id="search-input" contenteditable="true"></div>
    </div>
    <div id="selected-area">
      <img v-if="selected_brand && selected_brand.logo" :src="getImgUrl(selected_brand.logo)">
      <p>{{selected_brand.name != "" ? selected_brand.name : choose_brand_msg}}</p>
    </div>
    <ul id="brands-list" v-if="this.brand_info">
      <li
        v-for="item in this.brand_info"
        v-bind:key="item.id"
        @click="handleBrandClickEvent(item.id)"
      >
        <img v-if="item != null" :src="getImgUrl(item.logo)">
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import { getImgUrl } from "../assets/util/image";

export default {
  name: "brand-selector",
  data() {
    return {
      choose_brand_msg:
        "Please choose a brand from below to get recommendations.",
      brands: [],
      brand_info: [],
      selected_brand: {
        id: 0,
        logo: "",
        name: ""
      }
    };
  },
  mounted() {
    // receive the brands inside the brand.json
    axios({
      method: "GET",
      url: "http://localhost:5000/brands"
    }).then(
      result => {
        this.brands = result.data;
        let generatedbrand_info = [];
        Object.keys(this.brands).forEach(function(key) {
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
        this.brand_info = generatedbrand_info;
      },
      error => {
        console.error(error);
      }
    );
  },
  methods: {
    handleBrandClickEvent: function(brand_id) {
      this.selected_brand = this.getbrand_info(brand_id);
      this.$emit("onBrandClick", brand_id);
    },
    // receive the information about one brand
    getbrand_info: function(brand_id) {
      axios({
        method: "GET",
        url: "http://localhost:5000/brandinfo/" + brand_id
      }).then(
        result => {
          this.selected_brand = {
            id: brand_id,
            logo: result.data.logo,
            name: result.data.name
          };
        },
        error => {
          console.error(error);
        }
      );
    },
    getImgUrl
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
  display: inline;
  img {
    width: 180px;
    height: 150px;
    margin: -20px;
    opacity: 0.7;
  }
  img:hover {
    transform: scale(1.01);
    opacity: 1;
    cursor: pointer;
  }
  img:nth-child(3n) {
    break-after: always;
  }
}
[contenteditable]:focus {
  outline: 0px solid transparent;
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
  height: 400px;
  img {
    width: 300px;
    height: 250px;
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
