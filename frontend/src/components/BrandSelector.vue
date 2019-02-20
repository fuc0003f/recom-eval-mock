<template>
  <div id="brand-selector">
    <div id="search-area">
      <img class="search-icon" src="../assets/images/search.png">
      <input id="search-input" v-model="search_input_value">
    </div>
    <div id="selected-area">
      <img v-if="selected_brand && selected_brand.logo" :src="getImgUrl(selected_brand.logo)">
      <p>{{selected_brand && selected_brand.name != null && selected_brand.name}}</p>
      <p
        class="choose-brand-message"
        v-if="selected_brand"
      >{{selected_brand.name == "" ? choose_brand_msg : ""}}</p>
    </div>
    <div id="brands-list-wrapper">
      <ul id="brands-list" v-if="this.brand_info">
        <li
          v-for="item in this.brand_info"
          v-bind:key="item.id"
          @click="handleBrandClickEvent(item.id)"
        >
          <img
            :class="item == null || (!item.name.includes(search_input_value) && search_input_value !== '') ? 'hidden' : ''"
            :src="getImgUrl(item.logo)"
          >
          <p
            class="brands-list_label"
            :class="item == null || (!item.name.includes(search_input_value) && search_input_value !== '') ? 'hidden' : ''"
          >{{item.name}}</p>
        </li>
      </ul>
    </div>
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
      },
      search_input_value: ""
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
              result.data &&
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
          this.selected_brand = result.data && {
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
  width: 600px;
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
.brands-list_label {
  font-size: 80%;
  text-align: center;
}
.choose-brand-message {
  margin-top: 50px;
}
input:focus {
  outline: 0px solid transparent;
}
#search-area {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.search-icon {
  width: 30px;
  height: 30px;
  padding-right: 5px;
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
